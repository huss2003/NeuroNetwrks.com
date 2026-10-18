"""`build-path-staircase`: the brand staircase as three engineered tiers (Learn, Develop, Create).

Learn   - a terminal and stacked code blocks.
Develop - an IDE (editor + terminal panes), connected API modules, a test rail with passing checks.
Create  - a deployed app window on a server, with a live indicator.
A cyan pipeline climbs the glass steps with lime checkpoints at each tier.

    python tools/blender/build_path_staircase.py --out docs/3d/build-path-staircase --aspect 1
    python tools/blender/build_path_staircase.py --out docs/3d/cta-night-build --aspect 1.7921 --night
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args(lambda ap: ap.add_argument("--night", action="store_true"))
S.start(seed=61)
if a.night:  # same model, dark presentation: deeper bodies, stronger glow
    for k, col in (("white", (0.16, 0.24, 0.42)), ("frost", (0.2, 0.3, 0.52)), ("base", (0.1, 0.16, 0.32))):
        M[k].node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*col, 1)
    for k, st in (("path", 3.2), ("code", 2.2), ("codePale", 1.4), ("lime", 1.6), ("glassEdge", 1.8), ("rim", 2.4), ("blue", 0.8)):
        M[k].node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = st
NAME = "cta-night-build" if a.night else "build-path-staircase"
CAM = (0.95, -1.0, 0.72)
F = S.facing(CAM)
R = S.empty(NAME)


def stand(loc, extra=0.0):
    return Matrix.Translation(Vector(loc)) @ Matrix.Rotation(F + extra, 4, "Z")


TIERS = [  # (name, centre xy, size xy, top z)
    ("TierLearn", (-1.45, -2.55), (3.2, 2.5), 0.55),
    ("TierDevelop", (0.0, 0.25), (3.3, 2.6), 1.95),
    ("TierCreate", (1.45, 3.05), (3.0, 2.5), 3.35),
]
for name, (x, y), (sx, sy), top in TIERS:
    b = B()
    b.box((sx, sy, top), (0, 0, top / 2), M["white"], bevel=0.12)
    b.box((sx - 0.12, sy - 0.12, 0.05), (0, 0, top + 0.01), M["frost"], bevel=0.04)
    b.box((sx - 0.25, 0.04, 0.05), (0, -sy / 2 - 0.005, top - 0.12), M["rim"], bevel=0.015)
    b.box((0.04, sy - 0.25, 0.05), (sx / 2 + 0.005, 0, top - 0.12), M["rim"], bevel=0.015)
    b.obj(name, loc=(x, y, 0), parent=R)

# glass steps between tiers
st = S.empty("Steps", parent=R)
for i in range(2):
    (_, (x0, y0), (sx0, sy0), z0), (_, (x1, y1), (sx1, sy1), z1) = TIERS[i], TIERS[i + 1]
    p0 = Vector((x0 + 0.75, y0 + sy0 / 2 - 0.15, z0))
    p1 = Vector((x1 - 0.55, y1 - sy1 / 2 + 0.15, z1))
    n = 5
    b = B()
    for k in range(n):
        t = (k + 0.5) / n
        p = p0.lerp(p1, t)
        h = (z1 - z0) / n
        b.box((1.1, 0.62, 0.14), (p.x, p.y, z0 + h * (k + 1) - 0.07), M["glass"], bevel=0.05)
        b.box((1.12, 0.64, 0.03), (p.x, p.y, z0 + h * (k + 1) - 0.005), M["glassEdge"], bevel=0.01, seg=1)
    b.obj(f"Steps{i + 1:02d}", parent=st)

# ---- Learn: terminal + code blocks
(x, y), z = TIERS[0][1], TIERS[0][3]
b = B()
m = stand((x - 0.55, y + 0.25, z + 0.95))
iw, ih, im = S.window(b, 1.7, 1.2, m, body="white", dark=True)
S.code_lines(b, iw * 0.85, ih * 0.8, 6, im @ Matrix.Translation((0, 0, 0)), indent_seed=1, y=-0.004, mats=("code", "codeGreen", "codePale"))
b.box((0.09, 0.09, 0.32), (x - 0.55, y + 0.3, z + 0.16), M["metal"], bevel=0.03)
b.box((0.5, 0.34, 0.04), (x - 0.55, y + 0.3, z + 0.02), M["metal"], bevel=0.02)
b.obj("LearnTerminal", parent=R)
b = B()
for k, (dx, dy, dz, mm) in enumerate(((0.85, -0.6, 0, "blue"), (1.22, -0.6, 0, "blueGlass"), (1.03, -0.6, 0.36, "green"), (0.85, -0.23, 0, "cellB"))):
    b.box((0.34, 0.34, 0.34), (x + dx, y + dy, z + 0.17 + dz), M[mm], bevel=0.06)
    b.box((0.2, 0.012, 0.04), (x + dx - 0.02, y + dy - 0.176, z + 0.2 + dz), M["white"], bevel=0.015, seg=1)
    b.box((0.12, 0.012, 0.04), (x + dx - 0.06, y + dy - 0.176, z + 0.11 + dz), M["white"], bevel=0.015, seg=1)
b.obj("CodeBlocks", parent=R)

# ---- Develop: IDE + API modules + test rail
(x, y), z = TIERS[1][1], TIERS[1][3]
b = B()
m = stand((x - 0.55, y + 0.2, z + 1.0))
iw, ih, im = S.window(b, 2.2, 1.35, m, body="white", screen="white")
e = im.to_3x3().to_4x4()
b.box((iw * 0.16, 0.012, ih * 0.92), im @ Vector((-iw * 0.42, -0.004, 0)), M["frost"], bevel=0.02, rot=e, seg=1)  # file tree
S.code_lines(b, iw * 0.12, ih * 0.8, 7, im @ Matrix.Translation((-iw * 0.42, 0, 0)), indent_seed=2, y=-0.008, mats=("inkPale",))
S.code_lines(b, iw * 0.62, ih * 0.5, 5, im @ Matrix.Translation((iw * 0.08, 0, ih * 0.2)), indent_seed=5, y=-0.006, mats=("code", "ink", "inkPale"))
b.box((iw * 0.74, 0.012, ih * 0.3), im @ Vector((iw * 0.08, -0.004, -ih * 0.31)), M["dark"], bevel=0.02, rot=e, seg=1)  # terminal pane
S.code_lines(b, iw * 0.64, ih * 0.22, 3, im @ Matrix.Translation((iw * 0.08, 0, -ih * 0.31)), indent_seed=6, y=-0.01, mats=("codeGreen", "codePale"))
b.box((0.09, 0.09, 0.32), (x - 0.55, y + 0.25, z + 0.16), M["metal"], bevel=0.03)
b.box((0.55, 0.36, 0.04), (x - 0.55, y + 0.25, z + 0.02), M["metal"], bevel=0.02)
b.obj("DevelopIDE", parent=R)
b = B()
mods = [Vector((x + 1.05, y - 0.15, z + 0.2)), Vector((x + 1.05, y - 0.85, z + 0.2)), Vector((x + 0.45, y - 0.95, z + 0.2))]
for k, p in enumerate(mods):
    b.box((0.4, 0.4, 0.34), p, M["blue" if k != 1 else "metalBlue"], bevel=0.07)
    b.cyl(0.07, 0.04, p + Vector((0, 0, 0.18)), M["lime" if k == 0 else "code"], seg=16)
for p, q in zip(mods, mods[1:]):
    b.tube([p + Vector((0, 0, 0.05)), q + Vector((0, 0, 0.05))], 0.03, M["path"], sides=6)
b.obj("ApiModules", parent=R)
b = B()
for k in range(4):
    px, py = x - 1.35 + k * 0.42, y - 0.95
    b.box((0.34, 0.34, 0.06), (px, py, z + 0.03), M["green" if k < 3 else "frost"], bevel=0.03)
    if k < 3:
        S.check_mark(b, 0.22, Matrix.Translation((px, py, z + 0.075)) @ Matrix.Rotation(-math.pi / 2, 4, "X"), m="white", thick=0.03)
b.obj("TestRail", parent=R)

# ---- Create: server + deployed app + live light
(x, y), z = TIERS[2][1], TIERS[2][3]
b = B()
b.box((0.95, 0.8, 0.9), (x + 0.85, y - 0.45, z + 0.45), M["metal"], bevel=0.08)
for u in range(3):
    b.box((0.8, 0.04, 0.18), (x + 0.85, y - 0.86, z + 0.2 + u * 0.25), M["dark"], bevel=0.02, seg=1)
    b.sphere(0.03, (x + 0.58, y - 0.89, z + 0.2 + u * 0.25), M["lime"], seg=10)
b.obj("Server", parent=R)
b = B()
m = stand((x - 0.45, y + 0.15, z + 1.15))
iw, ih, im = S.window(b, 1.9, 1.4, m, body="white", screen="white")
e = im.to_3x3().to_4x4()
b.box((iw * 0.92, 0.012, ih * 0.14), im @ Vector((0, -0.004, ih * 0.38)), M["blue"], bevel=0.03, rot=e, seg=2)
b.box((iw * 0.5, 0.014, ih * 0.36), im @ Vector((-iw * 0.2, -0.006, ih * 0.04)), M["cellB"], bevel=0.03, rot=e, seg=2)
S.glyph_image(b, ih * 0.22, im @ Matrix.Translation((-iw * 0.2, -0.014, ih * 0.04)), m="white")
b.box((iw * 0.34, 0.014, ih * 0.08), im @ Vector((iw * 0.26, -0.006, ih * 0.16)), M["ink"], bevel=0.02, rot=e, seg=1)
b.box((iw * 0.3, 0.014, ih * 0.06), im @ Vector((iw * 0.24, -0.006, ih * 0.04)), M["inkPale"], bevel=0.02, rot=e, seg=1)
b.box((iw * 0.2, 0.016, ih * 0.1), im @ Vector((iw * 0.19, -0.008, -ih * 0.1)), M["green"], bevel=0.03, rot=e, seg=2)
for k in range(3):
    b.box((iw * 0.27, 0.014, ih * 0.2), im @ Vector((-iw * 0.31 + k * iw * 0.31, -0.006, -ih * 0.35)), M["frost"], bevel=0.03, rot=e, seg=2)
b.box((0.09, 0.09, 0.42), (x - 0.45, y + 0.2, z + 0.21), M["metal"], bevel=0.03)
b.box((0.55, 0.36, 0.04), (x - 0.45, y + 0.2, z + 0.02), M["metal"], bevel=0.02)
b.sphere(0.11, im @ Vector((iw * 0.5 + 0.02, -0.06, ih * 0.5 + 0.02)), M["lime"], seg=18)
b.obj("DeployedApp", parent=R)

# ---- pipeline up the steps, checkpoints at each tier
ctrl = [Vector((TIERS[0][1][0] + 1.37, TIERS[0][1][1] + 0.2, TIERS[0][3] + 0.12))]
for i in range(2):
    (_, (x0, y0), (sx0, sy0), z0), (_, (x1, y1), (sx1, sy1), z1) = TIERS[i], TIERS[i + 1]
    p0 = Vector((x0 + 0.75 + 0.62, y0 + sy0 / 2 - 0.15, z0 + 0.12))
    p1 = Vector((x1 - 0.55 + 0.62, y1 - sy1 / 2 + 0.15, z1 + 0.12))
    ctrl += [p0, p0.lerp(p1, 0.5) + Vector((0, 0, 0.12)), p1]
ctrl.append(Vector((TIERS[2][1][0] + 0.07, TIERS[2][1][1] - 0.1, TIERS[2][3] + 0.12)))
pts = S.spline(ctrl, 120)
b = B()
b.tube(pts, 0.03, M["path"], sides=8)
b.obj("Pipeline", parent=R)
b = B()
for _, (x, y), _, z in TIERS:
    b.sphere(0.1, (x + 1.37 if z < 1 else x + 0.07, y + 0.2 if z < 1 else y - 0.1, z + 0.14), M["lime"], seg=18)
b.obj("Checkpoints", parent=R)

if a.night:
    S.finish(a, NAME, cam_dir=CAM, margin=0.14, transparent=False, post_shift=(-0.16, 0.0), world_color=(0.006, 0.014, 0.05),
             light=dict(key=500, fill=250, rim=900, world=0.6))
else:
    S.finish(a, NAME, cam_dir=CAM, margin=0.04)
