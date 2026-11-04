"""Envelope-based lag check: robust to vocoder phase regeneration.

Usage: python align_env.py reference.wav processed.wav
Builds 1 ms RMS envelopes of both files and cross-correlates them in 5 s
windows. Reports lag (processed relative to reference) in ms per window.
"""
import sys
import numpy as np
import soundfile as sf

a, sr = sf.read(sys.argv[1], dtype="float32", always_2d=True)
b, sr2 = sf.read(sys.argv[2], dtype="float32", always_2d=True)
assert sr == sr2
a = a.mean(axis=1)
b = b.mean(axis=1)
n = min(len(a), len(b))
a, b = a[:n], b[:n]

hop = sr // 1000  # 1 ms
frames = n // hop
ea = np.sqrt(np.mean(a[:frames * hop].reshape(frames, hop) ** 2, axis=1))
eb = np.sqrt(np.mean(b[:frames * hop].reshape(frames, hop) ** 2, axis=1))
ea = np.log(ea + 1e-6)
eb = np.log(eb + 1e-6)


def lag_ms(x, y, max_lag=100):
    x = x - x.mean()
    y = y - y.mean()
    X = np.fft.rfft(x, 2 * len(x))
    Y = np.fft.rfft(y, 2 * len(y))
    xc = np.fft.irfft(Y * np.conj(X))
    xc = np.concatenate([xc[-max_lag:], xc[:max_lag + 1]])
    return int(np.argmax(xc)) - max_lag


w = 5000
out = []
for c in range(w, frames - w // 2, w):
    out.append((c / 1000, lag_ms(ea[c - w // 2:c + w // 2], eb[c - w // 2:c + w // 2])))
print("envelope lag by window (s: ms): " + "  ".join(f"{t:.0f}:{l:+d}" for t, l in out))
print(f"whole-file envelope lag: {lag_ms(ea, eb):+d} ms")
