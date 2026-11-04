"""Measure sample offset and gain between a reference and a processed file.

Usage: python align_check.py reference.wav processed.wav
Prints the lag (processed relative to reference) in samples and ms, and the
RMS gain difference. Use before blending wet/dry so the mix does not comb-filter.
"""
import sys
import numpy as np
import soundfile as sf

a, sr = sf.read(sys.argv[1], dtype="float32", always_2d=True)
b, sr2 = sf.read(sys.argv[2], dtype="float32", always_2d=True)
assert sr == sr2, "sample rates differ"
a = a.mean(axis=1)
b = b.mean(axis=1)
n = min(len(a), len(b))
a, b = a[:n], b[:n]

def lag_at(center, w):
    seg_a = a[max(0, center - w // 2): center + w // 2]
    seg_b = b[max(0, center - w // 2): center + w // 2]
    max_lag = int(0.1 * sr)
    A = np.fft.rfft(seg_a, 2 * len(seg_a))
    B = np.fft.rfft(seg_b, 2 * len(seg_b))
    xc = np.fft.irfft(B * np.conj(A))
    xc = np.concatenate([xc[-max_lag:], xc[:max_lag + 1]])
    return int(np.argmax(xc)) - max_lag


# cross-correlate a 10 s window from the middle, search +/- 100 ms
w = min(10 * sr, n // 2)
lag = lag_at(n // 2, w)
rms_a = np.sqrt(np.mean(a ** 2) + 1e-12)
rms_b = np.sqrt(np.mean(b ** 2) + 1e-12)
print(f"lag: {lag} samples ({lag / sr * 1000:.2f} ms)   length diff: {len(b) - len(a)} samples   "
      f"gain: {20 * np.log10(rms_b / rms_a):+.2f} dB")

# drift check: lag in 5 s windows across the file (only files longer than 25 s)
if n > 25 * sr:
    w5 = 5 * sr
    centers = range(w5, n - w5 // 2, w5)
    lags = [(c / sr, lag_at(c, w5)) for c in centers]
    print("lag by window (s: samples): " + "  ".join(f"{t:.0f}:{l}" for t, l in lags))
