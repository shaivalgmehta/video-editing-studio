"""Verify a cut: re-transcribe the FINAL voice track and diff it against words.json.

Usage:
  python verify_words.py <final_voice.wav> <words.json> [--model small.en] [--tol 0.25]

words.json may be [{"w","s","e"}] or [{"text","start","end"}] (or {"words": [...]}).
Prints:
  - every text difference (missing / extra / changed words) with times,
  - words whose start differs from the ASR by more than --tol seconds,
  - words.json entries that sit in silence (< -45 dB peak over the word).
Exit code 1 if any word is missing/changed or sits in silence.

faster-whisper is given the WAV PATH (it resamples itself). Never pass a numpy array:
an array is assumed to be 16 kHz, so a 48 kHz array transcribes as garbage, slowly.
Run ONE whisper job at a time on this machine. ASR mishears are expected
(names, "wanna", unstressed "and"): judge each diff, decide with a second model
(medium.en) or the source's own captions, and note the call in the EDL.
Runs with system python (faster-whisper 1.2, soundfile, numpy).
"""
import argparse
import difflib
import json
import re
import sys

import numpy as np
import soundfile as sf

ap = argparse.ArgumentParser()
ap.add_argument("wav")
ap.add_argument("words")
ap.add_argument("--model", default="small.en")
ap.add_argument("--tol", type=float, default=0.25)
a = ap.parse_args()


def norm(t):
    return re.sub(r"[^a-z0-9']", "", t.lower().replace("’", "'"))


ref = json.load(open(a.words, encoding="utf-8"))
ref = ref["words"] if isinstance(ref, dict) else ref
ref = [{"w": r.get("w", r.get("text", "")), "s": float(r.get("s", r.get("start", 0))),
        "e": float(r.get("e", r.get("end", 0)))} for r in ref]

from faster_whisper import WhisperModel  # noqa: E402

model = WhisperModel(a.model, device="cpu", compute_type="int8")
segs, info = model.transcribe(a.wav, language="en", word_timestamps=True, beam_size=5,
                              vad_filter=False, condition_on_previous_text=False)
hyp = [{"w": w.word.strip(), "s": w.start, "e": w.end} for s in segs for w in (s.words or [])]

R = [norm(r["w"]) for r in ref]
H = [norm(h["w"]) for h in hyp]
bad = 0
print(f"words.json {len(ref)} words | ASR ({a.model}) {len(hyp)} words | audio {info.duration:.2f}s\n")
print("== text differences")
sm = difflib.SequenceMatcher(a=R, b=H, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal":
        continue
    rt = " ".join(r["w"] for r in ref[i1:i2]) or "-"
    ht = " ".join(h["w"] for h in hyp[j1:j2]) or "-"
    t = ref[i1]["s"] if i1 < len(ref) else (hyp[j1]["s"] if j1 < len(hyp) else 0)
    print(f"  {t:7.2f}s  {op:8s} words.json: {rt!r:40s} ASR: {ht!r}")
    if op in ("delete", "replace"):
        bad += 1

print(f"\n== start offsets > {a.tol}s (matched words)")
offs = []
for blk in sm.get_matching_blocks():
    for k in range(blk.size):
        r, h = ref[blk.a + k], hyp[blk.b + k]
        d = h["s"] - r["s"]
        offs.append(d)
        if abs(d) > a.tol:
            print(f"  {r['w']!r:16s} words.json {r['s']:.2f}  ASR {h['s']:.2f}  ({d:+.2f})")
if offs:
    print(f"  matched {len(offs)}/{len(ref)}; mean |offset| {np.mean(np.abs(offs)):.3f}s")

print("\n== words in silence (< -45 dB)")
x, sr = sf.read(a.wav, dtype="float32", always_2d=True)
x = x.mean(axis=1)
silent = 0
for r in ref:
    seg = x[int(r["s"] * sr):max(int(r["e"] * sr), int(r["s"] * sr) + 1)]
    if len(seg) == 0:
        print(f"  {r['w']!r} at {r['s']:.2f} is past the end of the audio")
        silent += 1
        continue
    hop = max(1, sr // 100)
    m = len(seg) // hop
    peak = (20 * np.log10(np.sqrt(np.mean(seg[:m * hop].reshape(m, hop) ** 2, axis=1)).max() + 1e-9)
            if m else -120)
    if peak < -45:
        print(f"  {r['w']!r} {r['s']:.2f}-{r['e']:.2f} peak {peak:.1f} dB")
        silent += 1
print(f"  {silent} flagged")

print("\nASR text:\n" + " ".join(h["w"] for h in hyp))
sys.exit(1 if (bad or silent) else 0)
