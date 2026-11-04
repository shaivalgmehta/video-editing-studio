"""Stage 3 rough cut for Ad 2A: A-roll only, no graphics. LEGACY: kept for reference; new ads use build_cut.py.

Usage: python build_rough_cut.py [--dry] [--project <job dir>]   (project defaults to the current folder)

Builds the segment list from measured speech onsets/offsets (silencedetect at
-40 dB on the clean audio) and the brief's pacing rules, writes the EDL, then
runs ffmpeg once to produce:
  <project>/work/cut/2A_aroll_v2.mov      1080x1920 30fps H.264 CRF 16 + 24-bit PCM (locked master)
  <project>/work/cut/2A_aroll_v2.wav      the cut voice track on its own (for Stage 5)
  <project>/work/cut/2A_aroll_v2_540p.mp4 540x960 proxy for Checkpoint 2

Picture: raw camera file (auto-rotated to portrait), conformed to 30 fps, scaled
to 1080x1920. Punch-ins alternate 100% / 115% per segment, anchored to the top
of the frame and centered horizontally (face sits in the top 40% of frame).
Audio: <project>/work/audio_clean/take01_CLEAN_A3.wav, same timeline as the picture
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

_ap = argparse.ArgumentParser(description="Legacy per-ad cut (2A_aroll_v2). Prefer build_cut.py + a cut config.")
_ap.add_argument("--dry", action="store_true", help="write and print the EDL only, no render")
_ap.add_argument("--project", help="job folder with input/ work/ output/ (default: current folder)")
_args = _ap.parse_args()
P = project_dir(_args.project)
SRC_V = P / "input" / "VID20261022172544.mp4"
SRC_A = P / "work" / "audio_clean" / "take01_CLEAN_A3.wav"
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
    # label,                                  onset,   offset,  gap_after, note
    ("L1  Did you know... all year round/long", 5.799, 8.929, 0.17, "cold open, start on 'Did'"),
    ("L2  By the time they finish...",          9.476, 11.452, 0.45, "DELIBERATE BEAT before 'Agency design work'"),
    ("L3  Agency design work is the same.",     12.295, 13.682, 0.17, ""),
    ("L4  Landing pages, ads, social... clients", 14.028, 16.983, 0.17, ""),
    ("L5a and next month",                      17.453, 18.141, None, "natural 0.29 mid-sentence, kept"),
    ("L5b they all need more.",                 18.433, 19.109, 0.15, "list: tight before 'You can hire'"),
    ("L6  You can hire another designer.",      19.991, 21.061, 0.17, ""),
    ("L7  That might be right... $85,000 a year.", 21.568, 24.461, 0.15, "list: tight before 'You could find'"),
    ("L8a You could find freelancers and keep chasing them on deadlines", 25.327, 27.806, 0.15, "v2: 'and have the uncertainty of their availability' (28.21-30.67) removed per CD; list: tight before 'You could keep'"),
    ("L9a You could keep giving it to your existing designer", 31.654, 33.394, 0.22, "mid-sentence 0.34 trimmed"),
    ("L9b until the deadline becomes a negotiation.", 33.734, 35.545, 0.33, "PAUSE before 'Or you could use Delesign' + punch-in; split 0.12 after / 0.21 before so the cut lands before his blink"),
    ("L10 Or you could use Delesign.",          36.643, 37.704, 0.20, ""),
    ("L11 Delesign gives agencies ongoing design support,", 38.571, 40.905, None, "natural 0.23, list rhythm"),
    ("L12 a dedicated designer learns the brands,", 41.137, 42.979, 0.20, "list rhythm"),
    ("L13 requests stay organized,",            43.470, 44.940, None, "natural 0.29 kept: a cut here would land on a blink"),
    ("L14 and there's a/then the process for continuity... unavailable.", 45.228, 47.729, 0.25, "into B-roll"),
    ("L15a The moment that bridge is finished,", 48.877, 50.385, 0.22, "mid-sentence 0.30 trimmed"),
    ("L15b it needs another coat.",             50.686, 51.526, 0.17, ""),
    ("L16 So does your client work, every month.", 52.044, 53.563, 0.20, ""),
    ("L17a If your agency has monthly creatives,", 54.612, 56.165, 0.22, "0.71 trimmed"),
    ("L17b speak to us to get a reliable designer.", 56.875, 58.477, None, "last line"),
]

HEAD = 0.05   # air before the very first word (1.5 frames); v2 adds PREROLL before it
PREROLL_IN = 3.9  # v2: cold open on Shaival walking in and sitting down (3.9 s to the first word at 5.8 s)
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
with open(EDL / "2A_aroll_v2.json", "w") as f:
    json.dump({"source": SRC_V.name, "audio": SRC_A.name, "fps": FPS, "total": total, "segments": merged}, f, indent=1)

lines = ["# EDL: 2A cut v2 (A-roll only): sit-down pre-roll, 'uncertainty' sentence removed", "",
         f"Source: `input/{SRC_V.name}` (picture) + `work/audio_clean/{SRC_A.name}` (voice). {FPS} fps. "
         f"Total {total:.2f}s. {len(merged)} segments, {len(merged)-1} cuts, 10 ms audio crossfade on every cut.", "",
         "| # | Timeline in | Src in | Src out | Dur | Scale | Gap kept after | Line | Note |",
         "|---|---|---|---|---|---|---|---|---|"]
for i, s in enumerate(merged):
    nxt = merged[i + 1] if i + 1 < len(merged) else None
    gap_kept = f"{(s['out'] - s['offset']) + (nxt['onset'] - nxt['in']):.2f}s" if nxt else "end"
    lines.append(f"| {i+1} | {s['tl_in']:.2f} | {s['in']:.3f} | {s['out']:.3f} | {s['dur']:.2f} | "
                 f"{int(round(s['scale']*100))}% | {gap_kept} | {s['label']} | {s['note']} |")
(EDL / "2A_aroll_v2.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
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
(OUT / "2A_aroll_v2_filtergraph.txt").write_text(graph, encoding="utf-8")

cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-stats",
       "-i", str(SRC_V), "-i", str(SRC_A),
       "-/filter_complex", str(OUT / "2A_aroll_v2_filtergraph.txt"),
       "-map", "[vout]", "-map", "[aout]",
       "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS),
       "-c:a", "pcm_s24le", str(OUT / "2A_aroll_v2.mov")]
print("\nrunning ffmpeg...")
subprocess.run(cmd, check=True)
subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(OUT / "2A_aroll_v2.mov"),
                "-vn", "-c:a", "pcm_s24le", str(OUT / "2A_aroll_v2.wav")], check=True)
subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(OUT / "2A_aroll_v2.mov"),
                "-vf", "scale=540:960", "-c:v", "libx264", "-preset", "fast", "-crf", "23", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(OUT / "2A_aroll_v2_540p.mp4")], check=True)
print("done. total", total)
