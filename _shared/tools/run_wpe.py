"""Single-channel WPE de-reverberation (nara_wpe), offline, 48 kHz in/out.

Usage: python run_wpe.py input.wav output.wav [taps] [delay] [iterations]
Defaults: taps=10 delay=3 iterations=5 on a 1024-point STFT (hop 256).
Removes late reverberation only; direct sound and early reflections are kept,
so it never sounds gated. Output is 24-bit mono.
"""
import sys
import numpy as np
import soundfile as sf
from nara_wpe.wpe import wpe
from nara_wpe.utils import stft, istft

src, dst = sys.argv[1], sys.argv[2]
taps = int(sys.argv[3]) if len(sys.argv) > 3 else 10
delay = int(sys.argv[4]) if len(sys.argv) > 4 else 3
iters = int(sys.argv[5]) if len(sys.argv) > 5 else 5

x, sr = sf.read(src, dtype="float64", always_2d=True)
x = x.mean(axis=1)[None, :]            # (channels=1, samples)

size, shift = 1024, 256
Y = stft(x, size=size, shift=shift)    # (D, T, F)
Y = Y.transpose(2, 0, 1)               # (F, D, T)
Z = wpe(Y, taps=taps, delay=delay, iterations=iters, statistics_mode="full")
z = istft(Z.transpose(1, 2, 0), size=size, shift=shift)[0]
z = z[: x.shape[1]]
peak = np.max(np.abs(z)) + 1e-9
if peak > 0.99:
    z = z / peak * 0.99
sf.write(dst, z.astype(np.float32), sr, subtype="PCM_24")
print(f"wrote {dst}: {len(z)/sr:.2f}s, taps={taps} delay={delay} iters={iters}")
