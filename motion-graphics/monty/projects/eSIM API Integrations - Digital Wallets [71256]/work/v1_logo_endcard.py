"""v4 = v1 with the Monty eSIM logo in place of the "Monty eSIM" eyebrow on the end card.

v1's source was overwritten by the v2/v3 passes, so this patches the archived v1 render:
the eyebrow sits on a flat gradient, so each frame's text rows are refilled by interpolating
between clean columns either side, then the logo is laid in with v1's eyebrow entrance (fade + 16 px rise).
Everything outside that box, and the audio, is v1 untouched.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).parent
SRC = HERE.parent / "output/archive/Monty_eSIM_API_Digital_Wallets_16x9_v1.mp4"
OUT = Path(sys.argv[1])
LOGO = HERE / "hyperframes/monty_wallets/assets/img/montyesim_logo.png"

W, H, FPS = 1920, 1080, 30
T_IN, T_DUR, RISE = 35.72, 0.4, 16   # v1 eyebrow: first faint at 35.733 (frame 1072), settles by ~36.1
X0, X1 = 846, 1074                   # refill columns (text spans 855-1063)
LOGO_W, CY = 236, 290                # logo width, resting centre (text centre was 292)

logo = Image.open(LOGO).convert("RGBA")
logo = logo.resize((LOGO_W, round(LOGO_W * logo.height / logo.width)), Image.LANCZOS)
lw, lh = logo.size
la = np.asarray(logo, dtype=np.float32) / 255.0
lx = 960 - lw // 2


def refill(f, y0, y1):
    l = f[y0:y1, X0 - 1:X0].astype(np.float32)
    r = f[y0:y1, X1:X1 + 1].astype(np.float32)
    k = np.linspace(0, 1, X1 - X0, dtype=np.float32)[None, :, None]
    f[y0:y1, X0:X1] = np.rint(l * (1 - k) + r * k).astype(np.uint8)


def ease(p):  # power2.out
    p = min(max(p, 0.0), 1.0)
    return 1 - (1 - p) ** 2


dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(SRC), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                       stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                        "-r", str(FPS), "-i", "-", "-i", str(SRC), "-map", "0:v", "-map", "1:a",
                        "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p",
                        "-c:a", "copy", "-movflags", "+faststart", str(OUT)], stdin=subprocess.PIPE)
n = 0
while True:
    buf = dec.stdout.read(W * H * 3)
    if len(buf) < W * H * 3:
        break
    t = n / FPS
    if t >= T_IN:
        f = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
        # the outgoing scene's text clears this band at ~35.8; refill only below it until then
        refill(f, 288 if t < 35.8 else 268, 330)
        e = ease((t - T_IN) / T_DUR)
        y = round(CY - lh / 2 + RISE * (1 - e))
        a = la[..., 3:] * e
        reg = f[y:y + lh, lx:lx + lw].astype(np.float32) / 255.0
        f[y:y + lh, lx:lx + lw] = np.rint((la[..., :3] * a + reg * (1 - a)) * 255).astype(np.uint8)
        buf = f.tobytes()
    enc.stdin.write(buf)
    n += 1
enc.stdin.close()
enc.wait()
dec.wait()
print(f"{n} frames -> {OUT}")
