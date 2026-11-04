import sys, glob, os, pymupdf
d = sys.argv[1]
for f in sorted(os.path.join(d, n) for n in os.listdir(d) if n.endswith(".ai")):
    try:
        doc = pymupdf.open(f)
        p = doc[0]
        imgs = p.get_images(full=True)
        print(os.path.basename(f), "pages", len(doc), "size", p.rect, "images", [(i[0], i[2], i[3]) for i in imgs][:6], "textlen", len(p.get_text()))
    except Exception as e:
        print(os.path.basename(f), "ERR", e)
