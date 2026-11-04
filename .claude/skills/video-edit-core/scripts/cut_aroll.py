"""Cut A-roll picture + voice from one source, frame-locked, from a segment list.

Usage:
  python cut_aroll.py <source.mp4> <segs.json> <out_dir> [--fps 30] [--fade-ms 12] [--lufs -16]
                      [--chain "<ffmpeg -af chain>"] [--audio-only | --video-only] [--crf 16]

segs.json: [[src_in, src_out, "label"], ...] in source seconds (pick in/out points INSIDE silences
or closures; see SKILL.md). Each segment length is snapped to whole frames, so picture and
audio stay locked and every join lands on a frame boundary.

Writes to <out_dir>:
  aroll.mp4          full source frame, <fps> CFR, H.264 high crf 16, yuv420p, no audio,
                     no chapters/data streams (HyperFrames-ready)
  voice.wav          48 kHz 24-bit mono, exactly frames/fps seconds, cleaned with --chain,
                     gain-matched to --lufs integrated, limited (~ -2 dBTP)
  segs_snapped.json  src/reel times and frame counts per segment (paste into EDL.md)

Audio joins: --fade-ms fade-out/fade-in on each side (no overlap, so length is exact).
Default chain (clean podcast / camera audio): highpass 80 Hz, gentle de-ess, 2.5:1 compression.
For noisy/echoey audio run DeepFilterNet + the studio chain on the source region first
(references/audio.md), then pass --audio-src <clean.wav> --audio-offset <its source start>
--chain anull so the cleaned audio is only cut, fade-joined and level-matched. Runs with system python (numpy, soundfile).
"""
import argparse
import json
import os
import re
import subprocess

import numpy as np
import soundfile as sf

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("segs")
ap.add_argument("out")
ap.add_argument("--fps", type=float, default=30)
ap.add_argument("--fade-ms", type=float, default=12)
ap.add_argument("--lufs", type=float, default=-16.0)
ap.add_argument("--crf", type=int, default=16)
ap.add_argument("--chain", default="highpass=f=80,deesser=i=0.25,acompressor=threshold=-24dB:ratio=2.5:attack=8:release=120")
ap.add_argument("--audio-src", help="take audio from this (e.g. DeepFilterNet-cleaned) WAV instead of <source>")
ap.add_argument("--audio-offset", type=float, default=0.0, help="source time of the --audio-src WAV's first sample")
ap.add_argument("--audio-only", action="store_true")
ap.add_argument("--video-only", action="store_true")
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
FPS, SR = a.fps, 48000

segs, t = [], 0.0
for s_in, s_out, *lab in json.load(open(a.segs, encoding="utf-8")):
    n = int(round((s_out - s_in) * FPS))
    segs.append(dict(src_in=round(s_in, 3), src_out=round(s_in + n / FPS, 3), label=(lab or [""])[0],
                     reel_in=round(t, 3), reel_out=round(t + n / FPS, 3), frames=n))
    t += n / FPS
frames = sum(s["frames"] for s in segs)
DUR = frames / FPS
json.dump(segs, open(os.path.join(a.out, "segs_snapped.json"), "w"), indent=1)


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def meter(path):
    m = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", m)[-1])
    pk = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", m)
    return i, (float(pk[-1]) if pk else None)


if not a.video_only:
    F = int(a.fade_ms / 1000 * SR)
    parts = []
    for s in segs:
        L = int(round(s["frames"] / FPS * SR))
        raw = subprocess.run(  # bytes, so not run() (text mode)
            ["ffmpeg", "-v", "error", "-ss", f"{s['src_in'] - (a.audio_offset if a.audio_src else 0):.4f}",
             "-i", a.audio_src or a.src, "-t", f"{L / SR + 0.05:.4f}",
             "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], check=True, capture_output=True).stdout
        p = np.frombuffer(raw, dtype=np.float32)[:L].copy()
        p = np.pad(p, (0, L - len(p)))
        if F:
            p[:F] *= np.linspace(0, 1, F)
            p[-F:] *= np.linspace(1, 0, F)
        parts.append(p)
    y = np.concatenate(parts)
    N = int(round(DUR * SR))
    y = np.pad(y, (0, max(0, N - len(y))))[:N]
    tmp_raw = os.path.join(a.out, "_voice_cut_raw.wav")
    tmp_cmp = os.path.join(a.out, "_voice_cut_chain.wav")
    sf.write(tmp_raw, y, SR, subtype="FLOAT")
    run(["ffmpeg", "-v", "error", "-y", "-i", tmp_raw, "-af", a.chain, "-c:a", "pcm_f32le", tmp_cmp])
    out_wav = os.path.join(a.out, "voice.wav")
    g = a.lufs - meter(tmp_cmp)[0]
    for _ in range(3):  # gain -> limiter changes loudness slightly; iterate to within 0.2 LU
        run(["ffmpeg", "-v", "error", "-y", "-i", tmp_cmp, "-af",
             f"volume={g:.2f}dB,alimiter=limit=0.79:attack=3:release=50:level=false,"
             "afade=t=in:d=0.01,areverse,afade=t=in:d=0.03,areverse",
             "-ar", str(SR), "-ac", "1", "-c:a", "pcm_s24le", out_wav])
        I, pk = meter(out_wav)
        if abs(I - a.lufs) < 0.2:
            break
        g += a.lufs - I
    os.remove(tmp_raw)
    os.remove(tmp_cmp)
    print(f"voice.wav {sf.info(out_wav).frames} samples (expected {N}), {I:.1f} LUFS, true peak {pk} dBTP")

if not a.audio_only:
    ins, fc = [], []
    for i, s in enumerate(segs):
        # fast seek to 2 s before, then frame-accurate trim; fps= converts 29.97 -> CFR target
        ins += ["-ss", f"{max(0, s['src_in'] - 2):.3f}", "-t", f"{s['frames'] / FPS + 3:.3f}", "-i", a.src]
        pre = s["src_in"] - max(0, s["src_in"] - 2)
        fc.append(f"[{i}:v]trim=start={pre:.4f}:duration={s['frames'] / FPS + 0.5:.4f},setpts=PTS-STARTPTS,"
                  f"fps={FPS:g},trim=end_frame={s['frames']},setpts=PTS-STARTPTS[v{i}]")
    fc.append("".join(f"[v{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=0,format=yuv420p[out]")
    fc_path = os.path.join(a.out, "_fc.txt")
    open(fc_path, "w").write(";\n".join(fc))
    out_mp4 = os.path.join(a.out, "aroll.mp4")
    run(["ffmpeg", "-v", "error", "-y", *ins, "-/filter_complex", fc_path, "-map", "[out]", "-map_chapters", "-1",
         "-dn", "-an", "-fps_mode", "cfr", "-c:v", "libx264", "-preset", "slow", "-crf", str(a.crf),
         "-profile:v", "high", "-frames:v", str(frames), out_mp4])
    os.remove(fc_path)
    print(run(["ffprobe", "-v", "error", "-count_frames", "-show_entries",
               "stream=nb_read_frames,r_frame_rate:format=duration", "-of", "compact", out_mp4]).stdout.strip())

for s in segs:
    print(f"{s['label']:6s} src {s['src_in']:9.3f}-{s['src_out']:9.3f}  reel {s['reel_in']:7.3f}-{s['reel_out']:7.3f}  ({s['frames']} f)")
print(f"total {frames} frames = {DUR:.3f} s")
