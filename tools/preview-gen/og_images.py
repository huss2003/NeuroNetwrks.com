# Per-page share images (1200x630) for programs and guides. exec'd from build.py (shares its namespace).
from PIL import Image as _Img, ImageDraw as _Draw, ImageFont as _Font

def _og_font(size, weight):
    f = _Font.truetype(os.path.join(HERE, "og-font.ttf"), size)  # Plus Jakarta Sans (site font), converted from f-jakarta.woff2
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    return f

def og_image(route, title):
    """Draw the share image for a program or guide page and return its URL, or None for other pages."""
    if not (route.startswith("/programs/") or (route.startswith("/guides/") and route != "/guides")):
        return None
    name = route.strip("/").replace("/", "-")
    path = os.path.join(OUT, "assets", "og", name + ".png")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    W, H = 1200, 630
    im = _Img.new("RGB", (W, H), "white"); d = _Draw.Draw(im)
    logo = _Img.open(os.path.join(HERE, "assets", "logo-512.png")).convert("RGBA").resize((76, 76), _Img.LANCZOS)
    im.paste(logo, (72, 64), logo)
    d.text((166, 84), "NeuroNetworks AI Ed", font=_og_font(34, 700), fill="#0B1B33")
    words, lines, size = title.split(), [], 72
    while True:  # wrap to at most 4 lines, shrinking the type if needed
        f = _og_font(size, 800); lines, cur = [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) <= W - 144: cur = t
            else: lines.append(cur); cur = w
        lines.append(cur)
        if len(lines) <= 4 or size <= 44: break
        size -= 6
    y = 210 if len(lines) <= 2 else 190
    for ln in lines[:4]:
        d.text((72, y), ln, font=f, fill="#006DEE"); y += int(size * 1.18)
    d.rectangle((72, 540, 132, 546), fill="#49B716")
    d.text((72, 562), "neuronetwrks.com  ·  Learn · Develop · Create", font=_og_font(26, 500), fill="#3D4B63")
    im.save(path, "PNG", optimize=True)
    return f"{SITE}/assets/og/{name}.png"
