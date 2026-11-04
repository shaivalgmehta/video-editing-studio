"""Stage 3 rough cut for Ad 2B: A-roll only, no graphics. LEGACY: kept for reference; new ads use build_cut.py.

Usage: python build_cut_2B.py [--dry] [--project <job dir>]   (project defaults to the current folder)

Builds the segment list from measured speech onsets/offsets (silencedetect at
-40 dB on the clean audio) and the brief's pacing rules, writes the EDL, then
runs ffmpeg once to produce:
  <project>/work/cut/2B_aroll_v1.mov      1080x1920 30fps H.264 CRF 16 + 24-bit PCM (locked master)
  <project>/work/cut/2B_aroll_v1.wav      the cut voice track on its own (for Stage 5)
  <project>/work/cut/2B_aroll_v1_540p.mp4 540x960 proxy for Checkpoint 2

Picture: raw camera file (auto-rotated to portrait), conformed to 30 fps, scaled
to 1080x1920. Punch-ins alternate 100% / 115% per segment, anchored to the top
of the frame and centered horizontally (face sits in the top 40% of frame).
Audio: <project>/work/audio_clean/take2B_CLEAN_A3.wav, same timeline as the picture
(both streams start at 0, cleanup chain is sample-aligned). 10 ms crossfade at
every cut, with the segment edges extended 5 ms each side so the total audio
length still equals the picture length.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from _paths import project_dir

_ap = argparse.ArgumentParser(description="Legacy per-ad cut (2B_aroll_v1). Prefer build_cut.py + a cut config.")
_ap.add_argument("--dry", action="store_true", help="write and print the EDL only, no render")
_ap.add_argument("--project", help="job folder with input/ work/ output/ (default: current folder)")
_args = _ap.parse_args()
P = project_dir(_args.project)
SRC_V = P / "input" / "VID20261022173605.mp4"
SRC_A = P / "work" / "audio_clean" / "take2B_CLEAN_A3.wav"
OUT = P / "work" / "cut"
EDL = P / "work" / "edl"
OUT.mkdir(parents=True, exist_ok=True)
EDL.mkdir(parents=True, exist_ok=True)
FPS = 30
XF = 0.010  # audio crossfade

# Speech runs in the source, from silencedetect (-40 dB, 0.2 s) on the clean
# audio, labeled with the line they carry. onset = silence_end, offset = silence_start.
# gap_after: target gap (s) to the next run. None = keep the natural gap (it is
# already <= 0.25 s). Comments give the rule applied.
RUNS = [
    # label,                                   onset,   offset,  gap_after, note   (cut v1 of ad 2B)
    ("L1  Did you know the pilot and co-pilot... on the plane?", 5.779, 8.786, 0.17, "cold open after the walk-in"),
    ("L2  If one gets food poisoning... land the plane.", 9.614, 12.253, 0.45, "DELIBERATE BEAT before 'Most outsourced design services'"),
    ("L3  Most outsourced design services don't have a co-pilot.", 13.114, 15.596, 0.22, ""),
    ("L4a The first job looks fine,",               16.182, 17.298, 0.22, "mid-sentence 0.35 trimmed"),
    ("L4b and then the monthly work piles up.",     17.647, 18.817, 0.20, ""),
    ("L5  Your designer is out on leave and you're chasing every project.", 19.477, 21.849, 0.30, "turn to the questions"),
    ("L6  So here's what I'd ask any design partner.", 22.561, 24.487, 0.20, ""),
    ("Q1n 1.",                                      25.366, 25.666, None, "natural 0.23 kept"),
    ("Q1  How do you track priorities?",            25.898, 26.954, 0.15, "list"),
    ("Q2n 2.",                                      27.493, 27.823, None, "natural 0.29 kept"),
    ("Q2  Where do the briefs live?",               28.108, 29.028, 0.15, "list"),
    ("Q3n 3.",                                      29.573, 29.916, 0.20, ""),
    ("Q3  How do I see what's being worked on?",    30.290, 31.603, 0.15, "list"),
    ("Q4n 4.",                                      32.389, 32.802, None, "natural 0.25 kept"),
    ("Q4  What happens when the designers are unavailable?", 33.056, 34.869, 0.35, "PAUSE + punch-in before 'At Delesign'"),
    ("L7a At Delesign we use a dedicated designer", 35.742, 37.616, None, "natural 0.21 kept"),
    ("L7b with a backup",                           37.826, 38.382, None, "natural 0.29 kept"),
    ("L7c and a shared way to manage requests.",    38.671, 40.257, 0.25, ""),
    ("L8  Don't take my word for it.",              41.101, 42.037, None, "natural 0.23 kept"),
    ("L9a Ask to see a real request,",              42.271, 43.759, None, "natural 0.27 kept"),
    ("L9b a real progress update,",                 44.031, 45.132, 0.25, "0.30 trimmed"),
    ("L9c and how a project gets handed over.",     45.436, 46.862, 0.30, "FLUB 'Ask every design partner who uses it.' (47.69-49.75) removed"),
    ("L10 Ask every design partner who their co-pilot is.", 50.169, 52.320, 0.20, ""),
    ("L11 Ours is already on your account.",        53.056, 54.215, 0.30, "FLUB 'If you run an agency and need a reliable' (54.93-57.03) removed; cut inside speech at 57.03"),
    ("L12a If you run an agency and need a reliable design partner,", 57.03, 59.493, 0.25, "0.40 trimmed"),
    ("L12b book a call.",                           59.889, 60.343, None, "last line"),
]

HEAD = 0.05   # air before the very first word (1.5 frames); v2 adds PREROLL before it
PREROLL_IN = 3.3  # 2B: cold open on Shaival walking in and sitting down (first word at 5.78 s)
TAIL = 0.35   # air after the last word, before the end card


def q(t):
    """Quantize to the frame grid."""
    return round(round(t * FPS) / FPS, 4)


# Build segments: each run becomes [in, out] in source time. The kept gap is
# split 60% after the word (natural decay) / 40% before the next word.
segs = []
for i, (label, on, off, gap, note) in enumerate(RUNS):
    nxt_on = RUNS[i + 1][1] if i + 1 < len(RUNS) else None
    seg_in = PREROLL_IN if i == 0 else None
    seg_out = off + TAIL if nxt_on is None else None
    segs.append({"label": label, "onset": on, "offset": off, "in": seg_in, "out": seg_out,
                 "gap": gap, "note": note})

for i in range(len(segs) - 1):
    a, b = segs[i], segs[i + 1]
    natural = b["onset"] - a["offset"]
    gap = a["gap"] if a["gap"] is not None else natural
    if gap >= natural:  # never add air, only remove
        a["out"] = a["offset"]
        b["in"] = b["onset"] - 0.0  # cut point sits exactly at the next onset
        a["out"] = a["offset"] + natural  # == b.onset, i.e. no cut at all
        a["cut"] = False
    else:
        after, before = 0.6 * gap, 0.4 * gap
        if "split" in a["note"]:  # explicit "split X after / Y before" in the note
            parts = a["note"].split("split ")[1].split()
            after, before = float(parts[0]), float(parts[3])
        a["out"] = a["offset"] + after
        b["in"] = b["onset"] - before
        a["cut"] = True
segs[-1]["cut"] = False

# Merge runs that have no cut between them (natural gap kept).
merged = []
for s in segs:
    if merged and not merged[-1]["cut"]:
        m = merged[-1]
        m["out"] = s["out"]
        m["label"] += " + " + s["label"].split(" ", 1)[1]
        m["offset"] = s["offset"]
        m["cut"] = s["cut"]
        m["gap"] = s["gap"]
        m["note"] = (m["note"] + "; " + s["note"]).strip("; ")
    else:
        merged.append(dict(s))

for s in merged:
    s["in"] = q(s["in"])
    s["out"] = q(s["out"])

# Alternate punch-in scale per segment.
for i, s in enumerate(merged):
    s["scale"] = 1.0 if i % 2 == 0 else 1.15
    s["dur"] = round(s["out"] - s["in"], 4)
    s["tl_in"] = round(sum(x["dur"] for x in merged[:i]), 4)

total = round(sum(s["dur"] for s in merged), 3)

# EDL files
with open(EDL / "2B_aroll_v1.json", "w") as f:
    json.dump({"source": SRC_V.name, "audio": SRC_A.name, "fps": FPS, "total": total, "segments": merged}, f, indent=1)

lines = ["# EDL: 2B cut v1 (A-roll only): walk-in pre-roll, two flubbed restarts removed", "",
         f"Source: `input/{SRC_V.name}` (picture) + `work/audio_clean/{SRC_A.name}` (voice). {FPS} fps. "
         f"Total {total:.2f}s. {len(merged)} segments, {len(merged)-1} cuts, 10 ms audio crossfade on every cut.", "",
         "| # | Timeline in | Src in | Src out | Dur | Scale | Gap kept after | Line | Note |",
         "|---|---|---|---|---|---|---|---|---|"]
for i, s in enumerate(merged):
    nxt = merged[i + 1] if i + 1 < len(merged) else None
    gap_kept = f"{(s['out'] - s['offset']) + (nxt['onset'] - nxt['in']):.2f}s" if nxt else "end"
    lines.append(f"| {i+1} | {s['tl_in']:.2f} | {s['in']:.3f} | {s['out']:.3f} | {s['dur']:.2f} | "
                 f"{int(round(s['scale']*100))}% | {gap_kept} | {s['label']} | {s['note']} |")
(EDL / "2B_aroll_v1.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))

if _args.dry:
    sys.exit(0)

# ffmpeg graph
n = len(merged)
vf = [f"[0:v]fps={FPS},scale=1080:1920:flags=lanczos,setsar=1,split={n}" + "".join(f"[v{i}]" for i in range(n))]
af = [f"[1:a]aformat=sample_fmts=fltp:channel_layouts=mono,asplit={n}" + "".join(f"[a{i}]" for i in range(n))]
for i, s in enumerate(merged):
    punch = ""
    if s["scale"] != 1.0:
        w = int(round(1080 * s["scale"] / 2) * 2)
        h = int(round(1920 * s["scale"] / 2) * 2)
        punch = f",scale={w}:{h}:flags=lanczos,crop=1080:1920:{(w-1080)//2}:0"
    vf.append(f"[v{i}]trim=start={s['in']}:end={s['out']},setpts=PTS-STARTPTS{punch}[pv{i}]")
    a_in = s["in"] - (XF / 2 if i > 0 else 0)
    a_out = s["out"] + (XF / 2 if i < n - 1 else 0)
    af.append(f"[a{i}]atrim=start={a_in:.4f}:end={a_out:.4f},asetpts=PTS-STARTPTS[pa{i}]")
vf.append("".join(f"[pv{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vout]")
prev = "pa0"
for i in range(1, n):
    lab = "aout" if i == n - 1 else f"x{i}"
    af.append(f"[{prev}][pa{i}]acrossfade=d={XF}:c1=tri:c2=tri[{lab}]")
    prev = lab
if n == 1:
    af.append("[pa0]anull[aout]")
graph = ";".join(vf + af)
(OUT / "2B_aroll_v1_filtergraph.txt").write_text(graph, encoding="utf-8")

cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-stats",
       "-i", str(SRC_V), "-i", str(SRC_A),
       "-/filter_complex", str(OUT / "2B_aroll_v1_filtergraph.txt"),
       "-map", "[vout]", "-map", "[aout]",
       "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS),
       "-c:a", "pcm_s24le", str(OUT / "2B_aroll_v1.mov")]
print("\nrunning ffmpeg...")
subprocess.run(cmd, check=True)
subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(OUT / "2B_aroll_v1.mov"),
                "-vn", "-c:a", "pcm_s24le", str(OUT / "2B_aroll_v1.wav")], check=True)
subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(OUT / "2B_aroll_v1.mov"),
                "-vf", "scale=540:960", "-c:v", "libx264", "-preset", "fast", "-crf", "23", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(OUT / "2B_aroll_v1_540p.mp4")], check=True)
print("done. total", total)
