"""One-shot ingest for a new Delesign ad: probe, clean audio (house chain), transcribe, silence map.

Usage: python new_ad.py <ad_name> <raw_video_path> [--project <job dir>]   (project defaults to the current folder)
<raw_video_path> may be relative to the current folder or to <project>/input/.
Writes (inside the project):
  work/audio_raw/<ad>_raw.wav, work/audio_clean/<ad>_A_dfn.wav, work/audio_clean/<ad>_CLEAN_A3.wav
  work/transcripts/<ad>_CLEAN_A3_parakeet_words.json, work/transcripts/<ad>_CLEAN_A3_fw.json (cross-check)
  work/edl/<ad>_ingest.md  (probe, words with times, silence list, a draft RUNS table to paste into a cut config)
Uses the DeepFilterNet venv _shared/tools/venvs/dfn and _shared/tools/run_dfn.py / transcribe_fw.py from the workspace root.
"""
import argparse, sys, json, re, subprocess, shutil, os
from pathlib import Path
from _paths import DFN_PY, RUN_DFN, TRANSCRIBE_FW, project_dir

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("ad", help="ad name, e.g. 2E")
ap.add_argument("raw", help="camera file (relative to cwd or to <project>/input/)")
ap.add_argument("--project", help="job folder with input/ work/ output/ (default: current folder)")
a = ap.parse_args()

P = project_dir(a.project)
AD = a.ad
RAW = Path(a.raw)
if not RAW.exists() and (P / "input" / a.raw).exists():
    RAW = P / "input" / a.raw
if not RAW.exists():
    raise SystemExit(f"raw file not found: {a.raw}")
WORK = P / "work"
A_RAW = WORK / "audio_raw" / f"{AD}_raw.wav"
A_DFN = WORK / "audio_clean" / f"{AD}_A_dfn.wav"
A_CLEAN = WORK / "audio_clean" / f"{AD}_CLEAN_A3.wav"
TR = WORK / "transcripts"
for d in (A_RAW.parent, A_CLEAN.parent, TR, WORK / "edl"):
    d.mkdir(parents=True, exist_ok=True)
# House "studio" chain, approved on 2B v2 (the gentler 2A chain is in the skill file if ever wanted back)
POLISH = ("agate=threshold=0.01:ratio=2.5:attack=10:release=220:knee=6,highpass=f=90,equalizer=f=280:t=q:w=1.2:g=-4,"
          "equalizer=f=3500:t=q:w=1:g=3,highshelf=f=9000:g=2,deesser=i=0.55:m=0.5:f=0.5,"
          "acompressor=threshold=-20dB:ratio=4:attack=8:release=120:makeup=2.5")

def run(args, **kw):
    r = subprocess.run(args, capture_output=True, text=True, **kw)
    if r.returncode and "ffprobe" not in args[0]:
        print(r.stderr[-600:]); raise SystemExit(f"failed: {args[:2]}")
    return r

probe = run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_name,width,height,r_frame_rate,channels:stream_side_data=rotation:format=duration", "-of", "default=nw=1", str(RAW)]).stdout
print(probe.replace("\n", " "))
run(["ffmpeg", "-y", "-v", "error", "-i", str(RAW), "-vn", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s24le", str(A_RAW)])
run([str(DFN_PY), str(RUN_DFN), str(A_RAW), str(A_DFN), "--pf"])
run(["ffmpeg", "-y", "-v", "error", "-i", str(A_DFN), "-af", POLISH, "-c:a", "pcm_s24le", str(A_CLEAN)])
print("clean audio:", A_CLEAN.name)

# Parakeet (writes transcript.json beside its input)
tmp = TR / f"_{AD}"; tmp.mkdir(parents=True, exist_ok=True); shutil.copy(A_CLEAN, tmp / "in.wav")
subprocess.run("npx -y hyperframes transcribe " + str(tmp / "in.wav") + " --engine parakeet --json", shell=True, capture_output=True, text=True, env={**os.environ, "CI": "1"})
words_p = TR / f"{AD}_CLEAN_A3_parakeet_words.json"; shutil.copy(tmp / "transcript.json", words_p)
w = json.load(open(words_p, encoding="utf-8")); w = w if isinstance(w, list) else w.get("words", w)
# faster-whisper cross-check (text only)
fw = run([sys.executable, str(TRANSCRIBE_FW), str(A_CLEAN), str(TR / f"{AD}_CLEAN_A3_fw.json"), "small.en"]).stdout.strip().splitlines()
fw_text = fw[-1] if fw else ""

sil = run(["ffmpeg", "-hide_banner", "-i", str(A_CLEAN), "-af", "silencedetect=n=-40dB:d=0.2", "-f", "null", "-"]).stderr
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", sil)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", sil)]
gaps = list(zip(starts, ends))
# speech runs = between silences
runs = []
for i in range(len(gaps) - 1):
    on, off = gaps[i][1], gaps[i + 1][0]
    text = " ".join(x["text"] for x in w if x["start"] >= on - 0.15 and x["start"] < off)
    runs.append((on, off, text))

lines = [f"# Ingest: ad {AD}", "", f"Source `{RAW.name}`: {probe.replace(chr(10), ' ')}", "",
         "## Parakeet words", "", " ".join(f"{x['text']}@{x['start']:.2f}" for x in w), "",
         "## faster-whisper cross-check", "", fw_text, "",
         "## Speech runs (onset, offset from silencedetect -40 dB / 0.2 s) — draft RUNS for the cut config", "",
         "| # | onset | offset | natural gap after | words |", "|---|---|---|---|---|"]
for i, (on, off, text) in enumerate(runs, 1):
    nxt = runs[i][0] if i < len(runs) else None
    lines.append(f"| {i} | {on:.3f} | {off:.3f} | {'' if nxt is None else f'{nxt - off:.2f}s'} | {text} |")
out = WORK / "edl" / f"{AD}_ingest.md"
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"{len(w)} words, {len(runs)} runs -> {out}")
