"""Snap ASR word times onto the measured speech regions of a WAV.

Parakeet word starts run 0.15-0.45 s early (and ends late) against the audio envelope on these takes.
For each speech region (between silences at -45 dB / 0.1 s) the words that fall in it are linearly
re-mapped so the first word starts at the region start and the last word ends at the region end.

Usage: python align_words.py <words.json> <cut.wav> <out.json>
"""
import json, re, subprocess, sys

words_in, wav, out_path = sys.argv[1:4]

def regions(path):
    s = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "silencedetect=n=-45dB:d=0.1", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", s)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", s)]
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", s)
    dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    reg, prev = [], 0.0
    for a, b in zip(st, en):
        if a - prev > 0.05:
            reg.append((prev, a))
        prev = b
    if dur - prev > 0.05:
        reg.append((prev, dur))
    return reg

w = json.load(open(words_in, encoding="utf-8"))
w = w if isinstance(w, list) else w.get("words", w)
reg = regions(wav)

def dist(i, m):
    a, b = reg[i]
    return 0 if a <= m <= b else min(abs(m - a), abs(m - b))

# assign by word start (+0.25 s, since the starts run early); ends are inflated so they are not used
assign = [min(range(len(reg)), key=lambda i, m=x["start"] + 0.25: dist(i, m)) for x in w]
out, notes = [], []
for i in sorted(set(assign)):
    idx = [k for k, a in enumerate(assign) if a == i]
    a, b = reg[i]
    s0, e0 = w[idx[0]]["start"], w[idx[-1]]["end"]
    sc = (b - a) / (e0 - s0) if e0 > s0 else 1.0
    for k in idx:
        out.append({"text": w[k]["text"], "start": round(a + (w[k]["start"] - s0) * sc, 3),
                    "end": round(a + (w[k]["end"] - s0) * sc, 3)})
    notes.append(f"{a:.2f}:{a - s0:+.2f}/{sc:.2f}")
json.dump(out, open(out_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"{len(w)} words, {len(reg)} speech regions; region start: shift/scale -> " + " ".join(notes))
print(" ".join(f"{x['text']}@{x['start']:.2f}" for x in out))
