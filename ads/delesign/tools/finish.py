"""Stages 5-6 pipeline for a Delesign ad: mix, exports, SRT, thumbnail, QA numbers.

Usage: python finish.py <render.mp4> [music.mp3] [--thumb-at 1.93] [--name 2A] [--version N]
                        [--hf <hyperframes dir>] [--project <job dir>]
  --project  job folder with work/ and output/final/ (default: current folder)
  --hf       the ad's HyperFrames project (default: <project>/work/hyperframes/<name>); reads index.html
             (end-card start) and assets/captions_groups.json (SRT)
  music      default: _shared/music/mixkit/mixkit_749.mp3 (house bed)
  --version  optional; appends _v<N> to every output name (workspace naming rule)
Reads the HyperFrames render (voice + clicks), ducks the music bed under speech with a swell
on the end card, two-pass loudnorm to -14 LUFS / -1.5 dBTP, muxes, then writes to <project>/output/final/:
  <name>_9x16.mp4, <name>_4x5.mp4, <name>.srt, <name>_thumb.jpg  (stems/premix in <project>/work/mix/)
and prints the QA measurements.
"""
import argparse, sys, json, re, subprocess
from pathlib import Path
from _paths import MUSIC_749, project_dir

_ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
_ap.add_argument("render")
_ap.add_argument("music", nargs="?")
_ap.add_argument("--thumb-at", type=float, default=1.93)
_ap.add_argument("--name", default="2A")
_ap.add_argument("--version", type=int)
_ap.add_argument("--hf")
_ap.add_argument("--project")
_a = _ap.parse_args()
P = project_dir(_a.project)
RENDER = Path(_a.render)
MUSIC = Path(_a.music) if _a.music else MUSIC_749
THUMB_AT = _a.thumb_at
NAME = _a.name
V = f"_v{_a.version}" if _a.version is not None else ""
PROJ = Path(_a.hf) if _a.hf else P / "work" / "hyperframes" / NAME
MIX = P / "work" / "mix"; OUT = P / "output" / "final"; MIX.mkdir(parents=True, exist_ok=True); OUT.mkdir(parents=True, exist_ok=True)

def run(args, capture=True):
    r = subprocess.run(args, capture_output=capture, text=True)
    if r.returncode and capture:
        print(r.stderr[-800:]); raise SystemExit(f"failed: {args[0]}")
    return r

def probe(path, entries):
    return run(["ffprobe", "-v", "error", "-show_entries", entries, "-of", "default=nw=1", str(path)]).stdout

dur = float(re.search(r"duration=([\d.]+)", probe(RENDER, "format=duration")).group(1))
# end card starts where the A-roll ends: read it from the project root
idx = (PROJ / "index.html").read_text(encoding="utf-8")
end_start = float(re.search(r'id="endcard"[^>]*data-start="([\d.]+)"', idx, re.S).group(1))
print(f"render {dur:.3f}s, end card at {end_start}s")

# 1. voice + clicks stem
stem = MIX / "stem_voice_sfx.wav"
run(["ffmpeg", "-y", "-v", "error", "-i", str(RENDER), "-vn", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s24le", str(stem)])
# 2. bed: in at 8 s, -26 dB, fade in, +6 dB swell on the end card, fade out on the last bar; ducked under speech
graph = (f"[1:a]atrim=start=8:end={8 + dur},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
         f"volume=-26dB,afade=t=in:st=0:d=1.5,"
         f"volume='if(gte(t,{end_start}),1+min(1,(t-{end_start})/0.8),1)':eval=frame,"
         f"afade=t=out:st={dur - 1.4}:d=1.4[m];"
         "[0:a]asplit=2[v][key];"
         "[m][key]sidechaincompress=threshold=0.03:ratio=5:attack=15:release=450:makeup=1:level_sc=1[md];"
         "[v][md]amix=inputs=2:normalize=0:duration=first[mix]")
premix = MIX / "premix.wav"
run(["ffmpeg", "-y", "-v", "error", "-i", str(stem), "-i", str(MUSIC), "-filter_complex", graph, "-map", "[mix]", "-c:a", "pcm_s24le", str(premix)])
# 3. two-pass loudnorm
p1 = run(["ffmpeg", "-hide_banner", "-i", str(premix), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"]).stderr
j = json.loads(p1[p1.rfind("{"):p1.rfind("}") + 1])
ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
      f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
final = MIX / "2A_mix_final.wav"
run(["ffmpeg", "-y", "-v", "error", "-i", str(premix), "-af", ln + ",aresample=48000", "-ar", "48000", "-c:a", "pcm_s24le", str(final)])
mixed = RENDER.with_name(RENDER.stem + "_mixed.mp4")
run(["ffmpeg", "-y", "-v", "error", "-i", str(RENDER), "-i", str(final), "-map", "0:v", "-c:v", "copy", "-map", "1:a", "-c:a", "aac", "-b:a", "320k", "-movflags", "+faststart", str(mixed)])

# 4. exports
enc = ["-c:v", "libx264", "-profile:v", "high", "-level", "4.1", "-preset", "slow", "-pix_fmt", "yuv420p", "-r", "30", "-g", "60",
       "-c:a", "aac", "-ar", "48000", "-b:a", "320k", "-movflags", "+faststart"]
run(["ffmpeg", "-y", "-v", "error", "-i", str(mixed), "-b:v", "14M", "-maxrate", "16M", "-bufsize", "28M", *enc, str(OUT / f"{NAME}_9x16{V}.mp4")])
run(["ffmpeg", "-y", "-v", "error", "-i", str(mixed), "-vf", "crop=1080:1350:0:120", "-b:v", "12M", "-maxrate", "14M", "-bufsize", "24M", *enc, str(OUT / f"{NAME}_4x5{V}.mp4")])
run(["ffmpeg", "-y", "-v", "error", "-ss", str(THUMB_AT), "-i", str(mixed), "-frames:v", "1", "-q:v", "2", str(OUT / f"{NAME}_thumb{V}.jpg")])

# 5. SRT from the caption groups
g = json.load(open(PROJ / "assets" / "captions_groups.json", encoding="utf-8"))
def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
(OUT / f"{NAME}{V}.srt").write_text("\n".join(f"{i}\n{ts(x['start'])} --> {ts(x['visEnd'])}\n{' '.join(w['text'] for w in x['words'])}\n"
                                      for i, x in enumerate(g, 1)), encoding="utf-8")
full = " ".join(" ".join(w["text"] for w in x["words"]) for x in g)

# 6. QA numbers
lo = run(["ffmpeg", "-hide_banner", "-i", str(OUT / f"{NAME}_9x16{V}.mp4"), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
I = re.findall(r"I:\s+(-?[\d.]+) LUFS", lo)[-1]; TP = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", lo)[-1]; LRA = re.findall(r"LRA:\s+([\d.]+)", lo)[-1]
sil = run(["ffmpeg", "-hide_banner", "-i", str(stem), "-af", "silencedetect=n=-40dB:d=0.4", "-f", "null", "-"]).stderr
gaps = [(float(a), float(b)) for a, b in zip(re.findall(r"silence_start: ([\d.]+)", sil), re.findall(r"silence_end: ([\d.]+)", sil))]
still = run(["ffmpeg", "-hide_banner", "-i", str(OUT / f"{NAME}_9x16{V}.mp4"), "-vf", f"trim={dur-1.0}:{dur},setpts=PTS-STARTPTS,scale=120:-2,signalstats,metadata=print:key=lavfi.signalstats.YDIF:file=-", "-f", "null", "-"]).stdout
ydif = [float(x) for x in re.findall(r"YDIF=([\d.]+)", still)]
v = probe(OUT / f"{NAME}_9x16{V}.mp4", "stream=codec_name,profile,width,height,r_frame_rate,bit_rate:format=duration")
print("9x16:", " ".join(v.split()))
print(f"loudness: I={I} LUFS  LRA={LRA}  TP={TP} dBTP")
print("voice-stem gaps >0.4s:", [(round(a, 2), round(b - a, 2)) for a, b in gaps])
print(f"end card last second: mean frame diff {sum(ydif)/max(1,len(ydif)):.3f} over {len(ydif)} frames")
print(f"srt: {len(g)} cues; 'Delesign' x{full.count('Delesign')}; flags:", [w for w in ('organised', 'colour', 'Delisign', 'DDSign') if w in full] or "none")
print("thumb at", THUMB_AT)
