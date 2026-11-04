"""Who is speaking, second by second: pitch (f0) + level map of one stretch of audio.

Usage:
  python pitch_map.py <media> <start_s> <end_s> [--step 0.05] [--split 150] [--fmin 60] [--fmax 400]

Reads any file ffmpeg can open (mp4, wav...), takes <start_s>..<end_s>, downmixes to
16 kHz mono and runs librosa pYIN. Prints one cell per --step seconds:
    t:f0/dB[tag]
f0 is the median voiced pitch in Hz (0 = unvoiced or silent), dB is the peak RMS level.
With --split HZ each voiced cell gets tag L (below HZ) or H (above HZ), e.g. a male host
~90-130 Hz vs a female guest ~180-260 Hz -> --split 150. Measure each speaker on a clean
stretch first; the split is per show, not universal.

Unvoiced sounds (/s/, /t/, /f/, breaths) have NO pitch: a word can run on past the last
voiced cell. Check word ends with a spectrogram (see SKILL.md), not with this map.
Default f0 = fast numpy autocorrelation (seconds); --pyin uses librosa pYIN (more robust, can take minutes).
Runs with system python (numpy; librosa only for --pyin).
"""
import argparse
import subprocess
import sys

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("media")
ap.add_argument("start", type=float)
ap.add_argument("end", type=float)
ap.add_argument("--step", type=float, default=0.05)
ap.add_argument("--split", type=float, default=0.0)
ap.add_argument("--fmin", type=float, default=60.0)
ap.add_argument("--fmax", type=float, default=400.0)
ap.add_argument("--pyin", action="store_true", help="librosa pYIN instead of the fast autocorrelation")
a = ap.parse_args()

SR = 16000
dur = a.end - a.start
raw = subprocess.run(
    ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{a.start:.3f}", "-t", f"{dur:.3f}",
     "-i", a.media, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
    capture_output=True, check=True).stdout
x = np.frombuffer(raw, dtype=np.float32)
if len(x) < SR * 0.1:
    sys.exit("no audio in that range")

HOP = 160  # 10 ms
if a.pyin:
    import librosa  # slow to import (numba); first call can take minutes under load
    f0, _, _ = librosa.pyin(x, fmin=a.fmin, fmax=a.fmax, sr=SR, frame_length=1024, hop_length=HOP)
else:
    # normalised autocorrelation, 40 ms window every 10 ms; voiced if peak >= 0.45 and level > -50 dB
    W = 640
    lo, hi = int(SR / a.fmax), int(SR / a.fmin)
    f0 = np.full(max(0, (len(x) - W) // HOP + 1), np.nan)
    for i in range(len(f0)):
        fr = x[i * HOP:i * HOP + W]
        fr = fr - fr.mean()
        e = np.dot(fr, fr)
        if e <= 0 or 10 * np.log10(e / W + 1e-12) < -50:
            continue
        ac = np.correlate(fr, fr, "full")[W - 1:W + hi + 1] / e
        lag = lo + int(np.argmax(ac[lo:hi + 1]))
        if ac[lag] >= 0.45:
            f0[i] = SR / lag
n = len(x) // HOP
rms = np.sqrt(np.array([np.mean(x[i * HOP:(i + 1) * HOP] ** 2) for i in range(n)]) + 1e-12)
db = 20 * np.log10(rms + 1e-9)

per = max(1, int(round(a.step * SR / HOP)))
cells = []
for k in range(0, min(len(f0), n), per):
    seg = f0[k:k + per]
    seg = seg[~np.isnan(seg)]
    v = int(np.median(seg)) if len(seg) >= max(1, per // 3) else 0
    d = int(round(db[k:k + per].max()))
    tag = ""
    if a.split and v:
        tag = "L" if v < a.split else "H"
    cells.append(f"{a.start + k * HOP / SR:.2f}:{v}/{d}{tag}")

for i in range(0, len(cells), 10):
    print("  ".join(cells[i:i + 10]))

vs = f0[~np.isnan(f0)]
if len(vs):
    print(f"\nvoiced frames {len(vs)}/{len(f0)}; f0 p10/p50/p90 = "
          f"{np.percentile(vs, 10):.0f}/{np.percentile(vs, 50):.0f}/{np.percentile(vs, 90):.0f} Hz")
