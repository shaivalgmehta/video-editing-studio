"""resemble-enhance: denoise + enhance (CPU).

Usage: python run_resemble.py input.wav output.wav [lambd] [nfe] [tau]
  lambd  denoise strength inside enhance, 0..1 (default 0.9)
  nfe    diffusion steps (default 32; higher = slower, slightly cleaner)
  tau    prior temperature, 0..1 (default 0.5; lower = more faithful to the input, less invention)
Model output is 44.1 kHz. This script resamples back to 48 kHz and writes 24-bit mono.
First run downloads the model weights from Hugging Face.
"""
import sys
import pathlib
if sys.platform == "win32":
    # The published checkpoint pickles PosixPath objects; alias so torch.load works on Windows.
    pathlib.PosixPath = pathlib.WindowsPath
import numpy as np
import soundfile as sf
import torch
import torchaudio
from resemble_enhance.enhancer.inference import enhance

src, dst = sys.argv[1], sys.argv[2]
lambd = float(sys.argv[3]) if len(sys.argv) > 3 else 0.9
nfe = int(sys.argv[4]) if len(sys.argv) > 4 else 32
tau = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5

torch.set_num_threads(max(1, torch.get_num_threads()))
x, sr = sf.read(src, dtype="float32", always_2d=True)
dwav = torch.from_numpy(x.mean(axis=1))

with torch.no_grad():
    wav, out_sr = enhance(dwav, sr, "cpu", nfe=nfe, solver="midpoint", lambd=lambd, tau=tau)

wav = wav.cpu()
if out_sr != 48000:
    wav = torchaudio.functional.resample(wav, out_sr, 48000, lowpass_filter_width=64,
                                         rolloff=0.9475937167399596, resampling_method="sinc_interp_kaiser")
y = np.clip(wav.numpy(), -1.0, 1.0)
sf.write(dst, y, 48000, subtype="PCM_24")
print(f"wrote {dst}: {len(y)/48000:.2f}s, lambd={lambd}, nfe={nfe}, tau={tau}, model sr={out_sr}")
