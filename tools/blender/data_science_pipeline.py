"""`data-science-pipeline`: raw data -> ETL -> warehouse -> notebook analysis -> dashboard.

    python tools/blender/data_science_pipeline.py --out docs/3d/data-science-pipeline --aspect 1.7778
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args()
S.start(seed=21)
CAM = (0.52, -1.0, 0.55)
F = S.facing(CAM)
R = S.empty("data-science-pipeline")
S.platform("Base", (10.2, 3.9), loc=(0.3, 0.25, 0), parent=R)
rnd = random.Random(5)


def stand(loc, extra=0.0):
    return Matrix.Translation(Vector(loc)) @ Matrix.Rotation(F + extra, 4, "Z")


# ---- raw data: an untidy pile of mixed records
b = B()
for k in range(14):
    s = rnd.uniform(0.22, 0.42)
    loc = (-3.95 + rnd.uniform(-0.55, 0.55), rnd.uniform(-0.9, 1.2), s / 2 + (0.3 if k > 9 else 0))
    b.box((s, s, s), loc, M[rnd.choice(("cellB", "cellC", "blueGlass", "cellT"))], bevel=s * 0.15,
          rot=(0, 0, rnd.uniform(-0.6, 0.6)))
b.obj("RawData", parent=R)

# ---- ETL: conveyor through a cleaning gate; records come out aligned
etl = S.empty("ETL", parent=R)
b = B()
b.box((3.2, 0.7, 0.08), (0, 0, 0.12), M["metalBlue"], bevel=0.03)
for k in range(14):
    b.cyl(0.05, 0.72, (-1.5 + k * 0.23, 0, 0.12), M["metal"], rot=(math.pi / 2, 0, 0), seg=12)
for x in (-1.55, 1.55):
    b.box((0.1, 0.1, 0.12), (x, -0.3, 0.06), M["metal"])
    b.box((0.1, 0.1, 0.12), (x, 0.3, 0.06), M["metal"])
b.box((0.16, 0.9, 1.25), (0.0, 0, 0.75), M["frost"], bevel=0.05)  # gate frame
b.box((0.18, 0.7, 0.7), (0.0, 0, 0.58), M["dark"], bevel=0.03)
for k in range(5):
    b.box((0.2, 0.62, 0.03), (0.0, 0, 0.32 + k * 0.12), M["code"], bevel=0.01, seg=1)
b.box((0.2, 0.5, 0.08), (0.0, 0, 1.25), M["green"], bevel=0.03)
b.obj("CleaningGate", loc=(-1.75, -0.15, 0), parent=etl)
b = B()
for k in range(3):  # messy in
    b.box((0.24, 0.24, 0.24), (-3.05 + k * 0.33, -0.15 + rnd.uniform(-0.12, 0.12), 0.34), M["cellC"], bevel=0.04, rot=(0, 0, rnd.uniform(-0.5, 0.5)))
for k in range(4):  # tidy out
    b.box((0.26, 0.26, 0.26), (-1.25 + k * 0.33, -0.15, 0.35), M["blue"], bevel=0.04)
b.obj("Records", parent=etl)

# ---- warehouse
b = B()
S.database(b, 0.6, 1.5, (0, 0, 0.75), discs=3)
b.obj("Warehouse01", loc=(0.55, 0.85, 0), parent=R)
b = B()
S.database(b, 0.48, 1.05, (0, 0, 0.53), discs=2, body="cellT")
b.obj("Warehouse02", loc=(0.75, -0.75, 0), parent=R)

# ---- notebook with a scatter plot and regression line
b = B()
m = stand((2.85, 0.75, 1.55))
iw, ih, im = S.window(b, 2.3, 1.9, m, body="white", screen="white")
e = m.to_3x3().to_4x4()
S.code_lines(b, iw * 0.86, ih * 0.22, 3, im @ Matrix.Translation((0, 0, ih * 0.36)), indent_seed=8, y=-0.004)
ox, oz, pw, ph = -iw * 0.38, -ih * 0.42, iw * 0.78, ih * 0.5
b.box((pw, 0.01, 0.015), im @ Vector((ox + pw / 2, -0.008, oz)), M["inkPale"], rot=e)
b.box((0.015, 0.01, ph), im @ Vector((ox, -0.008, oz + ph / 2)), M["inkPale"], rot=e)
for k in range(26):
    t = rnd.random()
    z = 0.12 + 0.72 * t + rnd.gauss(0, 0.09)
    b.sphere(0.028, im @ Vector((ox + 0.06 + t * (pw - 0.12), -0.02, oz + max(0.05, min(0.95, z)) * ph)), M["blue" if k % 4 else "lime"], seg=10)
line = [im @ Vector((ox + 0.04 + t * (pw - 0.08), -0.03, oz + (0.12 + 0.72 * t) * ph)) for t in (0, 1)]
b.tube(line, 0.012, M["green"], sides=6)
b.box((0.1, 0.1, 0.6), (2.85, 0.8, 0.3), M["metal"], bevel=0.03)
b.box((0.6, 0.4, 0.05), (2.85, 0.8, 0.025), M["metal"], bevel=0.02)
b.obj("Notebook", parent=R)

# ---- dashboard: KPI tiles, bars, donut
b = B()
m = stand((4.55, -0.35, 1.15))
iw, ih, im = S.window(b, 1.7, 1.45, m, body="white", screen="frost", header=False)
e = m.to_3x3().to_4x4()
for k in range(3):
    b.box((iw * 0.28, 0.014, ih * 0.18), im @ Vector((-iw * 0.32 + k * iw * 0.32, -0.006, ih * 0.36)), M["white"], bevel=0.02, rot=e, seg=2)
    b.box((iw * 0.14, 0.016, ih * 0.05), im @ Vector((-iw * 0.36 + k * iw * 0.32, -0.012, ih * 0.38)), M["blue" if k != 2 else "green"], bevel=0.01, rot=e, seg=1)
for k, h in enumerate((0.3, 0.5, 0.42, 0.66, 0.55)):
    hh = h * ih * 0.62
    b.box((iw * 0.07, 0.03, hh), im @ Vector((-iw * 0.4 + k * iw * 0.1, -0.02, -ih * 0.42 + hh / 2)), M["blue" if k != 3 else "lime"], bevel=0.012, rot=e, seg=1)
c = im @ Vector((iw * 0.26, -0.02, -ih * 0.14))
for k, (a0, a1, mm) in enumerate(((0, 200, "blue"), (205, 300, "cellT"), (305, 355, "lime"))):
    pts = [c + (m.to_3x3() @ Vector((math.cos(math.radians(t)) * 0.24, 0, math.sin(math.radians(t)) * 0.24))) for t in range(a0, a1 + 1, 8)]
    b.tube(pts, 0.045, M[mm], sides=8)
b.box((0.1, 0.1, 0.42), (4.55, -0.3, 0.21), M["metal"], bevel=0.03)
b.box((0.5, 0.36, 0.05), (4.55, -0.3, 0.025), M["metal"], bevel=0.02)
b.obj("Dashboard", parent=R)

# ---- data paths
P = [S.ortho([(-3.6, -0.15, 0.35), (-3.3, -0.15, 0.35)], 0.1),
     S.ortho([(-0.15, -0.15, 0.4), (0.0, -0.15, 0.4), (0.0, 0.85, 0.4), (-0.05, 0.85, 0.4)], 0.15),
     S.ortho([(-0.1, -0.15, 0.4), (0.3, -0.75, 0.4)], 0.1),
     S.spline([(1.15, 0.85, 1.0), (1.6, 0.85, 1.1), (1.85, 0.75, 1.2)], 20),
     S.spline([(1.2, -0.75, 0.6), (2.6, -0.6, 0.55), (3.7, -0.4, 0.6)], 30)]
b = B()
for pts in P:
    b.tube(pts, 0.02, M["path"], sides=6)
b.obj("DataPaths", parent=R)

S.finish(a, "data-science-pipeline", cam_dir=CAM, margin=0.04)
