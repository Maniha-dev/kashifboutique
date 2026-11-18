"""Builds index.html (one self-contained file) from template.html + images.
Usage:  python3 build.py        (needs only Python 3)
- frames/   : scroll-animation frames, played in filename order
- products/ : pNN_cK_a.webp = product NN, colour K, main photo
              pNN_cK_b.webp = same product/colour, hover photo
To use your own photos, replace files with the same names (webp, jpg or png
all work if you keep the matching extension in EXT below)."""
import base64, glob, json, mimetypes, os
here = os.path.dirname(os.path.abspath(__file__))
def uri(path):
    mime = mimetypes.guess_type(path)[0] or "image/webp"
    return "data:%s;base64,%s" % (mime, base64.b64encode(open(path, "rb").read()).decode())
frames = [uri(p) for p in sorted(glob.glob(os.path.join(here, "frames", "frame_*.*")))]
im = []
for n in range(1, 13):
    prod = []
    for k in range(1, 4):
        prod.append([uri(glob.glob(os.path.join(here, "products", "p%02d_c%d_%s.*" % (n, k, s)))[0]) for s in "ab"])
    im.append(prod)
html = open(os.path.join(here, "template.html"), encoding="utf-8").read()
html = html.replace("/*FRAMES*/", json.dumps(frames)).replace("/*IMGS*/", json.dumps(im))
out = os.path.join(here, "..", "index.html")
open(out, "w", encoding="utf-8").write(html)
print("Built", os.path.abspath(out), round(len(html) / 1e6, 2), "MB")
