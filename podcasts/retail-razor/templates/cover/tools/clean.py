"""Clean a `npx hyperframes remove-background` cutout of the guest for a TRRS cover.

Keeps the largest connected subject, erodes + softens the alpha edge, darkens edge pixels (despill of a white backdrop),
crops to the subject. Check the result by eye: backdrop fragments touching the head (S6E15 R4/R5) must be erased by hand,
and once hand-fixed, do NOT re-run this on that file.
Usage: python clean.py <in_cut.png> <out_clean.png>
"""
import sys
import cv2
import numpy as np
from PIL import Image, ImageChops, ImageFilter

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
a = im.getchannel("A")
a2 = ImageChops.darker(a, a.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.2)))
arr = np.array(im).astype(np.float32)
al = np.array(a2).astype(np.float32) / 255
_, lab, st, _ = cv2.connectedComponentsWithStats((al > 0.05).astype(np.uint8), 8)
big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
al *= cv2.dilate((lab == big).astype(np.uint8), np.ones((3, 3), np.uint8))
arr[..., :3][al < 0.98] *= 0.55
arr[..., 3] = al * 255
out = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
out = out.crop(out.getbbox())
out.save(dst)
print(dst, out.size)
