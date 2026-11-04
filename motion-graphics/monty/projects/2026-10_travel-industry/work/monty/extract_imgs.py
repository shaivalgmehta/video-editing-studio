import sys, os, pymupdf
src, out = sys.argv[1], sys.argv[2]
for n in ["Scene15.ai", "Scene_16.ai"]:
    doc = pymupdf.open(os.path.join(src, n))
    for img in doc[0].get_images(full=True):
        pix = pymupdf.Pixmap(doc, img[0])
        if pix.n - pix.alpha >= 4: pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        p = os.path.join(out, f"{n[:-3]}_x{img[0]}.png"); pix.save(p); print(p, pix.width, pix.height)
        # where is it placed
        print("  bbox", doc[0].get_image_bbox(img))
