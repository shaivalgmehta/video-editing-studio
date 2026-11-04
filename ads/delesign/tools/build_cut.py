"""Config-driven A-roll cut (house pacing rules). Replaces the per-ad copies of build_rough_cut.py.

Usage: python build_cut.py <config.json> [--dry] [--project <job dir>]   (project defaults to the current folder)
Config (paths relative to the project; legacy "raw/..." is read as "input/..."):
{
  "name": "2B_aroll_v1",
  "video": "input/VID....mp4",
  "audio": "work/audio_clean/2B_CLEAN_A3.wav",
  "preroll_in": 3.3,            # source time where the cut opens (walk-in); first run's onset follows
  "tail": 0.35,
  "runs": [                     # one row per speech run, in source time
    ["L1 label", 5.779, 8.786, 0.17, "note"],       # [label, onset, offset, gap_after or null, note]
    ...
  ]
}
Rules: a null gap keeps the natural pause (no cut); a gap is split 60% after the word / 40% before the next
unless the note contains "split X after / Y before"; punch-ins alternate 100% / 115% per segment, anchored to
the top of frame; 10 ms audio crossfade per cut; everything quantized to the 30 fps grid.
Outputs: work/cut/<name>.mov (H.264 CRF16 + 24-bit PCM), <name>.wav, <name>_540p.mp4, work/edl/<name>.md/.json
"""
import argparse, json, subprocess, sys
from pathlib import Path
from _paths import project_dir, resolve_in_project

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("config", help="cut config JSON (relative to cwd or to the project)")
ap.add_argument("--dry", action="store_true", help="write and print the EDL only, no render")
ap.add_argument("--project", help="job folder with input/ work/ output/ (default: current folder)")
args = ap.parse_args()

P = project_dir(args.project)
cfg_path = Path(args.config)
if not cfg_path.exists() and (P / args.config).exists():
    cfg_path = P / args.config
cfg = json.load(open(cfg_path, encoding="utf-8"))
NAME = cfg["name"]; SRC_V = resolve_in_project(P, cfg["video"]); SRC_A = resolve_in_project(P, cfg["audio"])
PREROLL_IN = float(cfg.get("preroll_in", 0)); TAIL = float(cfg.get("tail", 0.35)); HEAD = 0.05
OUT = P / "work" / "cut"; EDL = P / "work" / "edl"; OUT.mkdir(parents=True, exist_ok=True); EDL.mkdir(parents=True, exist_ok=True)
FPS = 30; XF = 0.010
RUNS = [tuple(r) for r in cfg["runs"]]

def q(t): return round(round(t * FPS) / FPS, 4)

segs = []
for i, (label, on, off, gap, note) in enumerate(RUNS):
    segs.append({"label": label, "onset": on, "offset": off, "gap": gap, "note": note or "",
                 "in": (PREROLL_IN if PREROLL_IN else on - HEAD) if i == 0 else None,
                 "out": off + TAIL if i == len(RUNS) - 1 else None})
for i in range(len(segs) - 1):
    a, b = segs[i], segs[i + 1]
    natural = b["onset"] - a["offset"]
    gap = a["gap"] if a["gap"] is not None else natural
    if gap >= natural:
        a["out"] = a["offset"] + natural; b["in"] = b["onset"]; a["cut"] = False
    else:
        after, before = 0.6 * gap, 0.4 * gap
        if "split" in a["note"]:
            parts = a["note"].split("split ")[1].split(); after, before = float(parts[0]), float(parts[3])
        a["out"] = a["offset"] + after; b["in"] = b["onset"] - before; a["cut"] = True
segs[-1]["cut"] = False
merged = []
for s in segs:
    if merged and not merged[-1]["cut"]:
        m = merged[-1]; m["out"] = s["out"]; m["label"] += " + " + s["label"]; m["offset"] = s["offset"]
        m["cut"] = s["cut"]; m["gap"] = s["gap"]; m["note"] = (m["note"] + "; " + s["note"]).strip("; ")
    else:
        merged.append(dict(s))
for i, s in enumerate(merged):
    s["in"], s["out"] = q(s["in"]), q(s["out"]); s["scale"] = 1.0 if i % 2 == 0 else 1.15
    s["dur"] = round(s["out"] - s["in"], 4); s["tl_in"] = round(sum(x["dur"] for x in merged[:i]), 4)
total = round(sum(s["dur"] for s in merged), 3)
json.dump({"source": SRC_V.name, "audio": SRC_A.name, "fps": FPS, "total": total, "segments": merged}, open(EDL / f"{NAME}.json", "w"), indent=1)
lines = [f"# EDL: {NAME}", "", f"Source `{cfg['video']}` + `{cfg['audio']}`. {FPS} fps. Total {total:.2f}s. {len(merged)} segments, {len(merged)-1} cuts.", "",
         "| # | Timeline in | Src in | Src out | Dur | Scale | Gap kept after | Line | Note |", "|---|---|---|---|---|---|---|---|---|"]
for i, s in enumerate(merged):
    nxt = merged[i + 1] if i + 1 < len(merged) else None
    gk = f"{(s['out'] - s['offset']) + (nxt['onset'] - nxt['in']):.2f}s" if nxt else "end"
    lines.append(f"| {i+1} | {s['tl_in']:.2f} | {s['in']:.3f} | {s['out']:.3f} | {s['dur']:.2f} | {int(round(s['scale']*100))}% | {gk} | {s['label']} | {s['note']} |")
(EDL / f"{NAME}.md").write_text("\n".join(lines) + "\n", encoding="utf-8"); print("\n".join(lines))
if args.dry: sys.exit(0)

n = len(merged)
vf = [f"[0:v]fps={FPS},scale=1080:1920:flags=lanczos,setsar=1,split={n}" + "".join(f"[v{i}]" for i in range(n))]
af = [f"[1:a]aformat=sample_fmts=fltp:channel_layouts=mono,asplit={n}" + "".join(f"[a{i}]" for i in range(n))]
for i, s in enumerate(merged):
    punch = ""
    if s["scale"] != 1.0:
        w = int(round(1080 * s["scale"] / 2) * 2); h = int(round(1920 * s["scale"] / 2) * 2)
        punch = f",scale={w}:{h}:flags=lanczos,crop=1080:1920:{(w-1080)//2}:0"
    vf.append(f"[v{i}]trim=start={s['in']}:end={s['out']},setpts=PTS-STARTPTS{punch}[pv{i}]")
    a_in = s["in"] - (XF / 2 if i > 0 else 0); a_out = s["out"] + (XF / 2 if i < n - 1 else 0)
    af.append(f"[a{i}]atrim=start={a_in:.4f}:end={a_out:.4f},asetpts=PTS-STARTPTS[pa{i}]")
vf.append("".join(f"[pv{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vout]")
prev = "pa0"
for i in range(1, n):
    lab = "aout" if i == n - 1 else f"x{i}"; af.append(f"[{prev}][pa{i}]acrossfade=d={XF}:c1=tri:c2=tri[{lab}]"); prev = lab
if n == 1: af.append("[pa0]anull[aout]")
(OUT / f"{NAME}_filtergraph.txt").write_text(";".join(vf + af), encoding="utf-8")
subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(SRC_V), "-i", str(SRC_A), "-/filter_complex", str(OUT / f"{NAME}_filtergraph.txt"),
                "-map", "[vout]", "-map", "[aout]", "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "pcm_s24le", str(OUT / f"{NAME}.mov")], check=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(OUT / f"{NAME}.mov"), "-vn", "-c:a", "pcm_s24le", str(OUT / f"{NAME}.wav")], check=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(OUT / f"{NAME}.mov"), "-vf", "scale=540:960", "-c:v", "libx264", "-preset", "fast", "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(OUT / f"{NAME}_540p.mp4")], check=True)
print("done. total", total)
