"""DeepFilterNet (DeepFilterNet3) speech enhancement.

Usage: python run_dfn.py input.wav output.wav [atten_lim_db]
Runs at 48 kHz natively. Output is 48 kHz 24-bit mono.
atten_lim_db (optional) caps how much noise is removed, e.g. 20 for a lighter touch.
"""
import sys
import numpy as np
import soundfile as sf
import torch
from df.enhance import enhance, init_df

PF = "--pf" in sys.argv
args = [a for a in sys.argv[1:] if a != "--pf"]
src, dst = args[0], args[1]
atten = float(args[2]) if len(args) > 2 else None

model, df_state, _ = init_df(log_level="WARNING", post_filter=PF)
sr = df_state.sr()

x, in_sr = sf.read(src, dtype="float32", always_2d=True)
x = x.mean(axis=1)
if in_sr != sr:
    import torchaudio
    x = torchaudio.functional.resample(torch.from_numpy(x), in_sr, sr).numpy()

audio = torch.from_numpy(x).unsqueeze(0)
with torch.no_grad():
    out = enhance(model, df_state, audio, atten_lim_db=atten)
y = out.squeeze(0).cpu().numpy()
y = np.clip(y, -1.0, 1.0)
sf.write(dst, y, sr, subtype="PCM_24")
print(f"wrote {dst}: {len(y)/sr:.2f}s @ {sr} Hz, atten_lim_db={atten}")
