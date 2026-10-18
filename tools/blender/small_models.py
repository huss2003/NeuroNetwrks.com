"""Smaller scene models used on project and admissions pages.

    python tools/blender/small_models.py --model project-image-classifier --out docs/3d/project-image-classifier --aspect 1.69
    python tools/blender/small_models.py --model project-rag-assistant   --out docs/3d/project-rag-assistant   --aspect 1.53
    python tools/blender/small_models.py --model admissions-steps        --out docs/3d/admissions-steps        --aspect 1.45
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args(lambda ap: ap.add_argument("--model", required=True,
                                      choices=["project-image-classifier", "project-rag-assistant", "admissions-steps"]))
S.start(seed=71)
CAM = (0.52, -1.0, 0.6)
F = S.facing(CAM)
R = S.empty(a.model)
rnd = random.Random(4)


def stand(loc):
    return Matrix.Translation(Vector(loc)) @ Matrix.Rotation(F, 4, "Z")


def post(b, x, y, h):
    b.box((0.08, 0.08, h), (x, y + 0.04, h / 2), M["metal"], bevel=0.03)
    b.box((0.5, 0.34, 0.04), (x, y + 0.04, 0.02), M["metal"], bevel=0.02)


if a.model == "project-image-classifier":
    S.platform("Base", (8.2, 2.5), loc=(0.15, 0.3, 0), parent=R)
    b = B()  # input images, slightly fanned
    for k in range(3):
        m = stand((-3.0 + k * 0.28, 0.55 - k * 0.35, 1.05 - k * 0.05))
        b.box((1.05, 0.05, 1.05), m @ Vector((0, 0, 0)), M["white"], bevel=0.06, rot=m.to_3x3().to_4x4())
        b.box((0.92, 0.012, 0.92), m @ Vector((0, -0.03, 0)), M["cellB" if k != 1 else "cellT"], bevel=0.04, rot=m.to_3x3().to_4x4(), seg=2)
        S.glyph_image(b, 0.6, m @ Matrix.Translation((0, -0.045, 0)), m="white")
    post(b, -2.72, 0.2, 0.55)
    b.obj("InputImages", parent=R)
    for i, (x, n, sz) in enumerate(((-1.1, 8, 2.0), (-0.45, 6, 1.6), (0.15, 4, 1.2)), 1):  # conv feature maps
        b = B()
        b.box((0.05, sz, sz), (0, 0, sz / 2), M["glass"], bevel=0.04)
        step = (sz - 0.2) / n
        for iy in range(n):
            for iz in range(n):
                if rnd.random() < 0.15:
                    continue
                b.box((0.03, step * 0.8, step * 0.8), (0.035, -sz / 2 + 0.1 + step * (iy + 0.5), 0.1 + step * (iz + 0.5)),
                      M[rnd.choice(("cellA", "cellB", "cellB", "cellC", "cellT"))], bevel=0.01, seg=1)
        b.obj(f"ConvLayer{i:02d}", loc=(x, 0.2, 0.25), parent=R)
    b = B()  # class scores
    m = stand((2.55, 0.3, 1.2))
    iw, ih, im = S.window(b, 1.9, 1.4, m, body="white", screen="frost", header=False)
    e = im.to_3x3().to_4x4()
    for k, (w, mm) in enumerate(((0.82, "lime"), (0.34, "blue"), (0.18, "cellB"))):
        z = ih * 0.28 - k * ih * 0.28
        b.box((iw * 0.16, 0.014, ih * 0.16), im @ Vector((-iw * 0.36, -0.006, z)), M["white"], bevel=0.03, rot=e, seg=2)
        S.glyph_image(b, ih * 0.1, im @ Matrix.Translation((-iw * 0.36, -0.016, z)), m="inkPale")
        b.box((iw * 0.62 * w, 0.016, ih * 0.1), im @ Vector((-iw * 0.22 + iw * 0.31 * w, -0.008, z)), M[mm], bevel=0.03, rot=e, seg=2)
    post(b, 2.55, 0.32, 0.5)
    b.obj("ClassScores", parent=R)
    b = B()
    for pts in ([(-2.3, 0.2, 0.9), (-1.15, 0.2, 1.1)], [(-1.05, 0.2, 1.3), (-0.5, 0.2, 1.1)], [(-0.4, 0.2, 1.0), (0.1, 0.2, 0.9)],
                [(0.2, 0.2, 0.85), (1.0, 0.25, 1.0), (1.65, 0.3, 1.15)]):
        b.tube(S.spline(pts, 16), 0.022, M["path"], sides=6)
    b.obj("DataPaths", parent=R)

elif a.model == "project-rag-assistant":
    S.platform("Base", (8.0, 2.6), loc=(0.15, 0.25, 0), parent=R)
    b = B()  # source documents
    for k in range(3):
        m = stand((-3.0 + k * 0.25, 0.5 - k * 0.3, 0.95))
        b.box((0.8, 0.04, 1.05), m @ Vector((0, 0, 0)), M["white"], bevel=0.04, rot=m.to_3x3().to_4x4())
        S.code_lines(b, 0.6, 0.8, 7, m @ Matrix.Translation((0, -0.025, 0)), mats=("inkPale", "ink", "codePale"), indent_seed=40 + k, y=0)
    post(b, -2.75, 0.2, 0.42)
    b.obj("Documents", parent=R)
    b = B()  # chunk cards
    for k in range(5):
        m = Matrix.Translation((-1.35 + (k % 3) * 0.42, -0.15 + (k // 3) * 0.55, 0.35 + (k // 3) * 0.05)) @ Matrix.Rotation(F, 4, "Z") @ Matrix.Rotation(-0.5, 4, "X")
        b.box((0.36, 0.03, 0.46), m @ Vector((0, 0, 0)), M["frost" if k % 2 else "white"], bevel=0.03, rot=m.to_3x3().to_4x4())
        S.code_lines(b, 0.26, 0.3, 3, m @ Matrix.Translation((0, -0.02, 0)), mats=("inkPale", "code"), indent_seed=50 + k, y=0)
    b.obj("Chunks", parent=R)
    b = B()  # vector index lattice
    nodes = []
    for i in range(4):
        for j in range(3):
            for k in range(3):
                p = Vector((i * 0.3, j * 0.3, 0.3 + k * 0.3)) + Vector((rnd.uniform(-0.04, 0.04), rnd.uniform(-0.04, 0.04), 0))
                nodes.append(p)
                b.sphere(0.055, p, M["lime" if (i, j, k) in ((2, 1, 1), (3, 0, 2), (1, 2, 0)) else "blue"], seg=12)
    for p in nodes:
        for q in nodes:
            if 0 < (p - q).length < 0.36 and p.x <= q.x:
                b.tube([p, q], 0.007, M["path"], sides=4)
    b.cyl(0.85, 0.06, (0.45, 0.3, 0.03), M["metal"], seg=40)
    b.obj("VectorIndex", loc=(0.0, 0.0, 0.0), parent=R)
    b = B()  # answer with citations
    m = stand((2.6, 0.3, 1.3))
    iw, ih, im = S.window(b, 1.8, 1.6, m, body="white", screen="frost")
    e = im.to_3x3().to_4x4()
    b.box((iw * 0.62, 0.016, ih * 0.14), im @ Vector((iw * 0.15, -0.008, ih * 0.32)), M["blue"], bevel=0.04, rot=e, seg=3)
    b.box((iw * 0.86, 0.016, ih * 0.36), im @ Vector((-0.01, -0.008, -ih * 0.02)), M["white"], bevel=0.04, rot=e, seg=3)
    S.code_lines(b, iw * 0.74, ih * 0.28, 4, im @ Matrix.Translation((-0.01, -0.012, -ih * 0.02)), mats=("ink", "inkPale"), indent_seed=60, y=0)
    for k in range(2):  # citation chips
        b.box((iw * 0.22, 0.018, ih * 0.08), im @ Vector((-iw * 0.3 + k * iw * 0.26, -0.012, -ih * 0.31)), M["green" if k == 0 else "cellB"], bevel=0.03, rot=e, seg=3)
    post(b, 2.6, 0.32, 0.5)
    b.obj("Answer", parent=R)
    b = B()
    for pts in ([(-2.4, 0.2, 0.7), (-1.9, 0.0, 0.6), (-1.6, -0.1, 0.5)], [(-0.6, 0.1, 0.5), (-0.3, 0.2, 0.55), (-0.05, 0.3, 0.6)],
                [(1.0, 0.3, 0.75), (1.4, 0.3, 0.85), (1.75, 0.3, 0.95)]):
        b.tube(S.spline(pts, 16), 0.022, M["path"], sides=6)
    b.obj("DataPaths", parent=R)

else:  # admissions-steps: enquire -> talk -> apply -> join, rising pads
    icons = S.empty("Steps", parent=R)
    centres = []
    for k in range(4):
        x, y, z = -2.7 + k * 1.8, 0.9 - k * 0.45, 0.25 + k * 0.42
        centres.append(Vector((x, y, z)))
        b = B()
        b.box((1.45, 1.45, z), (0, 0, z / 2), M["white"], bevel=0.1)
        b.box((1.35, 1.35, 0.05), (0, 0, z + 0.01), M["frost" if k < 3 else "green"], bevel=0.04)
        b.box((1.25, 0.04, 0.05), (0, -0.73, z - 0.08), M["rim"], bevel=0.015)
        top = Vector((0, 0, z + 0.04))
        if k == 0:  # envelope
            b.box((0.8, 0.5, 0.55), top + Vector((0, 0, 0.3)), M["blue"], bevel=0.05)
            b.prism([(-0.4, 0.27), (0.0, -0.02), (0.4, 0.27)], 0.03, M["white"], Matrix.Translation(top + Vector((0, -0.25, 0.3))))
        elif k == 1:  # chat bubble
            b.box((0.85, 0.32, 0.55), top + Vector((0, 0, 0.42)), M["blue"], bevel=0.14)
            b.prism([(-0.25, 0.0), (-0.05, 0.0), (-0.3, -0.22)], 0.3, M["blue"], Matrix.Translation(top + Vector((0, 0.15, 0.17))))
            for j in range(3):
                b.sphere(0.055, top + Vector((-0.2 + j * 0.2, -0.17, 0.42)), M["white"], seg=12)
        elif k == 2:  # application form with a tick
            m = Matrix.Translation(top + Vector((0, 0, 0.45))) @ Matrix.Rotation(F, 4, "Z")
            b.box((0.62, 0.05, 0.8), m @ Vector((0, 0, 0)), M["white"], bevel=0.04, rot=m.to_3x3().to_4x4())
            S.code_lines(b, 0.44, 0.4, 4, m @ Matrix.Translation((0, -0.03, 0.12)), mats=("inkPale", "ink"), indent_seed=80, y=0)
            S.check_mark(b, 0.3, m @ Matrix.Translation((0.05, -0.04, -0.22)), m="green", thick=0.03)
        else:  # join: a student's laptop with the lab open
            b.box((0.9, 0.6, 0.05), top + Vector((0, 0, 0.03)), M["metal"], bevel=0.03)
            lid = Matrix.Translation(top + Vector((0, 0.3, 0.05))) @ Matrix.Rotation(math.radians(-12), 4, "X")
            b.box((0.9, 0.05, 0.6), lid @ Vector((0, 0, 0.3)), M["metal"], bevel=0.03, rot=lid.to_3x3().to_4x4())
            b.box((0.8, 0.012, 0.5), lid @ Vector((0, -0.03, 0.3)), M["dark"], bevel=0.02, rot=lid.to_3x3().to_4x4(), seg=1)
            S.code_lines(b, 0.66, 0.38, 5, lid @ Matrix.Translation((0, -0.04, 0.3)), indent_seed=81, y=0, mats=("code", "codeGreen"))
        b.obj(["Enquire", "Talk", "Apply", "Join"][k], loc=(x, y, 0), parent=icons)
    b = B()
    for p, q in zip(centres, centres[1:]):
        b.tube(S.spline([p + Vector((0.6, -0.1, 0.06)), (p + q) / 2 + Vector((0, -0.3, 0.35)), q + Vector((-0.6, 0.1, 0.06))], 24), 0.026, M["path"], sides=6)
    b.obj("Path", parent=R)

S.finish(a, a.model, cam_dir=CAM, margin=0.05)
