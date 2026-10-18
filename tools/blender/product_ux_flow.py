"""`product-ux-flow`: wireframe -> mid-fidelity -> polished prototype (laptop + phone),
joined by a user-flow path, with a component-library stack.

    python tools/blender/product_ux_flow.py --out docs/3d/product-ux-flow --aspect 1.7778
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args()
S.start(seed=31)
CAM = (0.52, -1.0, 0.55)
F = S.facing(CAM)
R = S.empty("product-ux-flow")
S.platform("Base", (9.6, 3.9), loc=(0.15, 0.05, 0), parent=R)


def stand(loc):
    return Matrix.Translation(Vector(loc)) @ Matrix.Rotation(F, 4, "Z")


def pedestal(b, x, y):
    b.box((1.9, 1.2, 0.18), (x, y, 0.09), M["white"], bevel=0.06)


def screen_layout(b, iw, ih, im, stage):
    """Same page at three fidelities. stage 0 = outlines, 1 = grey blocks, 2 = branded."""
    e = im.to_3x3().to_4x4()

    def blk(w, h, x, z, kind, mm_hi):
        if stage == 0:  # outline only: four thin bars
            t = 0.014
            for (sx, sz, dx, dz) in ((w, t, 0, h / 2), (w, t, 0, -h / 2), (t, h, -w / 2, 0), (t, h, w / 2, 0)):
                b.box((sx, 0.01, sz), im @ Vector((x + dx, -0.006, z + dz)), M["inkPale"], rot=e)
            if kind == "img":
                for sgn in (1, -1):
                    rot = (im.to_3x3() @ Matrix.Rotation(sgn * math.atan2(h, w), 3, "Y")).to_4x4()
                    b.box((math.hypot(w, h) * 0.98, 0.008, 0.01), im @ Vector((x, -0.006, z)), M["inkPale"], rot=rot)
        else:
            mm = "inkPale" if stage == 1 else mm_hi
            b.box((w, 0.014, h), im @ Vector((x, -0.008, z)), M[mm], bevel=min(w, h) * 0.12, rot=e, seg=2)

    blk(iw * 0.9, ih * 0.1, 0, ih * 0.4, "bar", "blue")
    blk(iw * 0.5, ih * 0.38, -iw * 0.18, ih * 0.08, "img", "cellB")
    blk(iw * 0.32, ih * 0.07, iw * 0.27, ih * 0.2, "txt", "ink")
    blk(iw * 0.32, ih * 0.07, iw * 0.27, ih * 0.06, "txt", "inkPale")
    blk(iw * 0.2, ih * 0.09, iw * 0.21, -ih * 0.08, "btn", "green")
    for k in range(3):
        blk(iw * 0.27, ih * 0.22, -iw * 0.31 + k * iw * 0.31, -ih * 0.34, "card", "frost" if k != 1 else "cellC")


screens = S.empty("Screens", parent=R)
for i, (x, y, stage, name) in enumerate(((-3.3, 0.75, 0, "Wireframe"), (-0.5, 0.5, 1, "MidFidelity"), (2.3, 0.25, 2, "Prototype"))):
    b = B()
    pedestal(b, x, y)
    m = stand((x, y, 1.25))
    iw, ih, im = S.window(b, 2.1, 1.5, m, body="white" if stage else "frost", screen="white", header=stage == 2)
    screen_layout(b, iw, ih, im, stage)
    b.box((0.08, 0.08, 0.35), (x, y + 0.05, 0.36), M["metal"], bevel=0.03)
    b.obj(name, parent=screens)

# phone prototype in front of the final screen
b = B()
m = stand((3.7, -0.85, 0.75))
e = m.to_3x3().to_4x4()
b.box((0.62, 0.08, 1.2), m @ Vector((0, 0, 0)), M["white"], bevel=0.1, rot=e)
iw, ih = 0.54, 1.02
im = m @ Matrix.Translation((0, -0.05, 0))
b.box((iw, 0.012, ih), im @ Vector((0, 0, 0)), M["white"], bevel=0.05, rot=e, seg=2)
b.box((iw * 0.86, 0.014, ih * 0.08), im @ Vector((0, -0.006, ih * 0.4)), M["blue"], bevel=0.02, rot=e, seg=2)
b.box((iw * 0.86, 0.014, ih * 0.34), im @ Vector((0, -0.006, ih * 0.12)), M["cellB"], bevel=0.03, rot=e, seg=2)
for k in range(3):
    b.box((iw * 0.86, 0.014, ih * 0.08), im @ Vector((0, -0.006, -ih * 0.12 - k * ih * 0.11)), M["inkPale"], bevel=0.02, rot=e, seg=2)
b.box((iw * 0.5, 0.016, ih * 0.08), im @ Vector((0, -0.01, -ih * 0.42)), M["green"], bevel=0.03, rot=e, seg=2)
b.box((0.5, 0.36, 0.05), (3.7, -0.82, 0.025), M["metal"], bevel=0.02)
b.obj("PhonePrototype", parent=R)

# cursor over the prototype's button
b = B()
pts = [(0, 0), (0, -0.42), (0.1, -0.31), (0.19, -0.48), (0.25, -0.45), (0.16, -0.29), (0.3, -0.28)]
b.prism([(x * 1.4, z * 1.4) for x, z in pts], 0.06, M["deep"], Matrix.Translation((0, 0, 0)))
b.obj("Cursor", parent=R, loc=Vector((2.3, 0.25, 1.25)) + Matrix.Rotation(F, 3, "Z") @ Vector((0.42, -0.35, -0.02)), rot=(0, 0, F))

# component library: stacked tiles (button, toggle, card, input)
b = B()
lib = [("blue", 0.9, 0.34), ("frost", 0.9, 0.5), ("white", 0.9, 0.3), ("green", 0.9, 0.24)]
z = 0.0
for k, (mm, w, h) in enumerate(lib):
    b.box((w, 0.7, 0.1), (0, 0, z + 0.05), M["glass"], bevel=0.04)
    b.box((w * 0.7, 0.4, 0.06), (0, 0, z + 0.12), M[mm], bevel=0.04)
    z += 0.24
b.box((0.36, 0.18, 0.06), (0.15, -0.12, z + 0.02), M["green"], bevel=0.05)  # toggle on top
b.sphere(0.07, (0.27, -0.12, z + 0.08), M["white"], seg=14)
b.obj("ComponentLibrary", loc=(-1.9, -1.1, 0.0), parent=R)

# user-flow path with arrowheads
b = B()
for (x0, y0), (x1, y1) in (((-3.3, 0.75), (-0.5, 0.5)), ((-0.5, 0.5), (2.3, 0.25))):
    p0 = Vector((x0 + 1.05, y0 - 0.3, 0.3))
    p1 = Vector((x1 - 1.05, y1 - 0.3, 0.3))
    pts = S.spline([p0, (p0 + p1) / 2 + Vector((0, -0.35, 0.55)), p1], 30)
    for k in range(0, len(pts) - 2, 3):  # dashed
        b.tube(pts[k:k + 2], 0.024, M["path"], sides=6)
    d = (pts[-1] - pts[-3]).normalized()
    b.cone(0.07, 0.18, pts[-1], M["path"], rot=d.to_track_quat("Z", "Y").to_matrix().to_4x4())
b.obj("UserFlow", parent=R)

S.finish(a, "product-ux-flow", cam_dir=CAM, margin=0.04)
