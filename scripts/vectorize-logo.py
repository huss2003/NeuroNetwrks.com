"""Trace docs/source/logo.jpg into layered SVGs (provisional until the owner supplies a vector logo).
Usage: python3 scripts/vectorize-logo.py  (needs: pip install potracer numpy pillow)"""
import numpy as np, potrace
from PIL import Image

img = np.asarray(Image.open('docs/source/logo.jpg').convert('RGB')).astype(int)
H, W, _ = img.shape
r, g, b = img[..., 0], img[..., 1], img[..., 2]
blue = (b > 180) & (r < 90) & (g > 70) & (g < 160)
green = (g > 140) & (r < 150) & (b < 90)
dark = (r < 80) & (g < 80) & (b < 80)

def trace(mask):
    bm = potrace.Bitmap(~mask)
    plist = bm.trace(turdsize=12, alphamax=1.0, opttolerance=0.4)
    d = []
    for c in plist:
        s = c.start_point
        d.append(f'M{s.x:.1f},{s.y:.1f}')
        for seg in c.segments:
            if seg.is_corner:
                d.append(f'L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}')
            else:
                d.append(f'C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}')
        d.append('Z')
    return ''.join(d)

def crop(mask, y0, y1, x0=0, x1=W):
    m = np.zeros_like(mask); m[y0:y1, x0:x1] = mask[y0:y1, x0:x1]; return m

parts = {
    'mark': (0, 870),
    'wordmark': (880, 1250),
    'tagline': (1250, H),
}
def svg(box, layers, title):
    x0, y0, x1, y1 = box
    paths = ''.join(f'<path fill="{c}" fill-rule="evenodd" d="{trace(m)}"/>' for c, m in layers)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {x1-x0} {y1-y0}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{paths}</svg>\n')

def bbox(*masks):
    m = np.any(masks, axis=0); ys, xs = np.where(m); return xs.min()-6, ys.min()-6, xs.max()+6, ys.max()+6

B, G, D = '#006DEE', '#49B716', '#0B1B33'
out = 'src/assets/brand/'
import os; os.makedirs(out, exist_ok=True)
mb, mg = crop(blue, 0, 870), crop(green, 0, 870)
open(out+'logo-mark.svg', 'w').write(svg(bbox(mb, mg), [(G, mg), (B, mb)], 'NeuroNetworks AI Ed mark'))
mono = crop(blue | green, 0, 870)
open(out+'logo-mark-ink.svg', 'w').write(svg(bbox(mono), [(D, mono)], 'NeuroNetworks AI Ed mark'))
wb, wg = crop(blue, 880, 1250), crop(green, 880, 1250)
open(out+'logo-wordmark.svg', 'w').write(svg(bbox(wb, wg), [(G, wg), (B, wb)], 'NeuroNetworks AI Ed'))
full_b, full_g, full_d = blue, green, crop(dark, 1250, H)
open(out+'logo-full.svg', 'w').write(svg(bbox(full_b, full_g, full_d), [(G, full_g), (B, full_b), (D, full_d)], 'NeuroNetworks AI Ed. Learn, Develop, Create'))
print('ok')
