"""Bake the TRRS cover look into cleaned guest cutouts: gentle grade (contrast 1.10, warm), soft red glow (#e3262b,
blur 28, 85%) and a thin bright rim (#ff4a55) around the silhouette, 70 px padding (none at the bottom: the body runs
off the frame). Writes <project>/assets/img/guest_r<N>_glow.png and cut_info.json (w, h, face x) for gen.py.
Usage: python bake.py --project <cover project> --cutinfo <cut_info.json> 1=<clean_r1.png> 2=<clean_r2.png> ...
"""
import argparse, json, os
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument("--project", required=True)
ap.add_argument("--cutinfo", required=True)
ap.add_argument("items", nargs="+", help="N=path/to/clean.png")
a = ap.parse_args()
P = 70
info = json.load(open(a.cutinfo)) if os.path.exists(a.cutinfo) else {}
for item in a.items:
    n, path = item.split("=", 1)
    im = Image.open(path).convert("RGBA")
    rgb, alpha = im.convert("RGB"), im.getchannel("A")
    rgb = ImageEnhance.Contrast(rgb).enhance(1.10)
    arr = np.array(rgb).astype(np.float32)
    arr[..., 0] *= 1.04; arr[..., 2] *= 0.95
    rgb = Image.fromarray((((arr / 255) ** 0.95) * 255).clip(0, 255).astype(np.uint8))
    person = Image.merge("RGBA", (*rgb.split(), alpha))
    W, H = im.size
    can = Image.new("RGBA", (W + 2 * P, H + P), (0, 0, 0, 0))
    A = Image.new("L", can.size, 0); A.paste(alpha, (P, P))
    soft = A.filter(ImageFilter.GaussianBlur(28)).point(lambda v: min(255, int(v * 0.85)))
    rim = A.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(2.5))
    glow = Image.new("RGBA", can.size, (227, 38, 43, 0)); glow.putalpha(soft)
    rimc = Image.new("RGBA", can.size, (255, 74, 85, 0)); rimc.putalpha(rim)
    can = Image.alpha_composite(Image.alpha_composite(can, glow), rimc)
    lay = Image.new("RGBA", can.size, (0, 0, 0, 0)); lay.paste(person, (P, P))
    can = Image.alpha_composite(can, lay)
    out = os.path.join(a.project, "assets", "img", f"guest_r{n}_glow.png")
    can.save(out)
    ys, xs = np.nonzero(np.array(alpha)[60:200] > 128)   # head band -> face centre x
    info[n] = dict(w=can.size[0], h=can.size[1], fx=float(xs.mean()) + P, top=P)
    print(n, out, can.size, round(info[n]["fx"]))
json.dump(info, open(a.cutinfo, "w"), indent=1)
