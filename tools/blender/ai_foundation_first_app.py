"""`ai-foundation-first-app`: a student's first AI application.

Python notebook -> prompt -> model core <- documents -> vector index (RAG) ; model -> chat app deployed on a cloud pad.
Compact footprint so it works as a wide card (16:9), the square hero (1:1) and the programs banner (~1.45).

    python tools/blender/ai_foundation_first_app.py --out docs/3d/ai-foundation-first-app --aspect 1.7778
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args()
S.start(seed=51)
CAM = (0.55, -1.0, 0.6)
F = S.facing(CAM)
R = S.empty("ai-foundation-first-app")
S.platform("Base", (7.6, 4.9), loc=(0.0, 0.1, 0), parent=R)
rnd = random.Random(2)


def stand(loc):
    return Matrix.Translation(Vector(loc)) @ Matrix.Rotation(F, 4, "Z")


# ---- notebook (learn Python, data, first model)
b = B()
m = stand((-2.2, 1.1, 1.55))
iw, ih, im = S.window(b, 2.2, 1.7, m, body="white", screen="white")
e = im.to_3x3().to_4x4()
for k in range(3):  # three cells: code, code, output
    cz = ih * 0.33 - k * ih * 0.33
    b.box((0.05, 0.012, ih * 0.24), im @ Vector((-iw * 0.45, -0.006, cz)), M["blue" if k < 2 else "green"], rot=e)
    if k < 2:
        S.code_lines(b, iw * 0.8, ih * 0.24, 3, im @ Matrix.Translation((iw * 0.04, 0, cz)), indent_seed=10 + k, y=-0.006,
                     mats=("code", "ink", "inkPale"))
    else:
        for j, h in enumerate((0.3, 0.55, 0.42, 0.8, 0.65, 0.9)):
            hh = h * ih * 0.24
            b.box((iw * 0.07, 0.02, hh), im @ Vector((-iw * 0.3 + j * iw * 0.11, -0.012, cz - ih * 0.12 + hh / 2)), M["blue" if j != 5 else "lime"], bevel=0.01, rot=e, seg=1)
b.box((0.1, 0.1, 0.62), (-2.2, 1.15, 0.31), M["metal"], bevel=0.03)
b.box((0.6, 0.4, 0.05), (-2.2, 1.15, 0.025), M["metal"], bevel=0.02)
b.obj("Notebook", parent=R)

# ---- documents + vector index (RAG)
b = B()
for k in range(3):
    mm = Matrix.Translation((k * 0.32, k * 0.12, 0.5 + k * 0.03)) @ Matrix.Rotation(F - 0.15 + k * 0.1, 4, "Z") @ Matrix.Rotation(-0.25, 4, "X")
    b.box((0.7, 0.04, 0.9), mm @ Vector((0, 0, 0)), M["white"], bevel=0.03, rot=mm.to_3x3().to_4x4())
    S.code_lines(b, 0.52, 0.6, 6, mm @ Matrix.Translation((0, -0.025, -0.05)), mats=("inkPale", "ink", "codePale"), indent_seed=30 + k, y=0)
b.box((1.3, 0.55, 0.06), (0.3, 0.1, 0.03), M["metal"], bevel=0.02)
b.obj("Documents", loc=(-2.75, -1.05, 0.0), parent=R)
b = B()
nodes = []
for i in range(3):
    for j in range(3):
        for k in range(2):
            p = Vector((i * 0.32, j * 0.32, 0.25 + k * 0.32)) + Vector((rnd.uniform(-0.05, 0.05), rnd.uniform(-0.05, 0.05), 0))
            nodes.append(p)
            b.sphere(0.06, p, M["lime" if (i, j, k) in ((1, 1, 1), (2, 0, 0)) else "blue"], seg=12)
for p in nodes:
    for q in nodes:
        if 0 < (p - q).length < 0.4 and p.x <= q.x:
            b.tube([p, q], 0.008, M["path"], sides=4)
b.obj("VectorIndex", loc=(-1.25, -1.2, 0.0), parent=R)

# ---- model core with a prompt card
b = B()
b.box((1.25, 1.25, 1.25), (0, 0, 0.72), M["glass"], bevel=0.14)
for i in (-1, 0, 1):
    for j in (-1, 0, 1):
        for k in (-1, 0, 1):
            b.box((0.28, 0.28, 0.28), (i * 0.32, j * 0.32, 0.72 + k * 0.32), M["blueGlass" if (i + j + k) % 2 == 0 else "cellB"], bevel=0.04, seg=2)
b.cyl(0.62, 0.08, (0, 0, 0.04), M["metal"], seg=40)
b.obj("ModelCore", loc=(0.35, 0.35, 0.0), parent=R)
b = B()
m = stand((0.3, -1.05, 0.55))
iw, ih, im = S.window(b, 1.2, 0.5, m, body="white", screen="white", header=False, depth=0.05)
e = im.to_3x3().to_4x4()
b.box((iw * 0.55, 0.012, ih * 0.22), im @ Vector((-iw * 0.18, -0.006, 0)), M["ink"], bevel=0.02, rot=e, seg=1)
b.box((0.025, 0.014, ih * 0.4), im @ Vector((iw * 0.13, -0.008, 0)), M["blue"], rot=e)  # caret
b.box((ih * 0.5, 0.016, ih * 0.5), im @ Vector((iw * 0.38, -0.01, 0)), M["blue"], bevel=0.04, rot=e, seg=2)  # send button
b.box((0.4, 0.3, 0.05), (0.3, -1.02, 0.025), M["metal"], bevel=0.02)
b.box((0.07, 0.07, 0.3), (0.3, -1.02, 0.15), M["metal"], bevel=0.02)
b.obj("PromptCard", parent=R)

# ---- chat app on a cloud pad
b = B()
b.box((1.9, 1.5, 0.16), (0, 0, 0.08), M["white"], bevel=0.07)
for (x, y, r) in ((-0.45, 0.25, 0.42), (0.1, 0.35, 0.5), (0.55, 0.2, 0.36)):
    b.sphere(r, (x, y, 0.16), M["frost"], seg=24)
b.obj("CloudPad", loc=(2.45, 0.35, 0.0), parent=R)
b = B()
m = stand((2.45, 0.2, 1.62))
iw, ih, im = S.window(b, 1.45, 1.75, m, body="white", screen="frost")
e = im.to_3x3().to_4x4()
for k, (side, w, mm) in enumerate(((-1, 0.6, "white"), (1, 0.5, "blue"), (-1, 0.7, "white"), (1, 0.38, "blue"))):
    bw, bh = iw * w, ih * 0.15
    x = side * (iw / 2 - bw / 2 - iw * 0.06)
    z = ih * 0.33 - k * ih * 0.21
    b.box((bw, 0.016, bh), im @ Vector((x, -0.008, z)), M[mm], bevel=bh * 0.4, rot=e, seg=3)
b.box((iw * 0.9, 0.016, ih * 0.1), im @ Vector((0, -0.008, -ih * 0.43)), M["white"], bevel=0.03, rot=e, seg=2)
b.sphere(0.05, im @ Vector((iw * 0.36, -0.03, -ih * 0.43)), M["green"], seg=12)
b.box((0.09, 0.09, 0.62), (2.45, 0.25, 0.45), M["metal"], bevel=0.03)
b.obj("ChatApp", parent=R)

# ---- paths
P = [S.spline([(-1.3, 1.0, 0.9), (-0.6, 0.8, 0.85), (-0.3, 0.55, 0.8)], 24),
     S.spline([(-2.1, -1.0, 0.35), (-1.6, -1.15, 0.4), (-1.3, -1.15, 0.45)], 16),
     S.spline([(-0.6, -0.9, 0.6), (-0.4, -0.4, 0.65), (-0.25, 0.1, 0.7)], 16),
     S.spline([(0.3, -0.75, 0.55), (0.32, -0.45, 0.6), (0.33, -0.3, 0.62)], 10),
     S.spline([(1.0, 0.35, 0.95), (1.4, 0.3, 1.0), (1.75, 0.25, 1.05)], 16)]
b = B()
for pts in P:
    b.tube(pts, 0.022, M["path"], sides=6)
b.obj("DataPaths", parent=R)

S.finish(a, "ai-foundation-first-app", cam_dir=CAM, margin=0.04)
