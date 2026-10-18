"""`software-dev-architecture`: full-stack system for the Software Development program card.

Browser + phone clients -> API gateway -> three services -> database and cache,
with a CI/CD rail along the front where containers move through build, test and deploy gates.

    python tools/blender/software_dev_architecture.py --out docs/3d/software-dev-architecture --aspect 1.7778
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args()
S.start(seed=11)
CAM = (0.52, -1.0, 0.55)
F = S.facing(CAM)
R = S.empty("software-dev-architecture")
S.platform("Base", (10.2, 5.0), loc=(0.35, 0.05, 0), parent=R)


def stand(loc):
    return Matrix.Translation(Vector(loc)) @ Matrix.Rotation(F, 4, "Z")


# ---- clients
cl = S.empty("Clients", parent=R)
b = B()
m = stand((-4.2, 0.6, 1.75))
iw, ih, im = S.window(b, 2.5, 1.75, m, body="white", screen="white")
e = m.to_euler()
b.box((iw * 0.9, 0.012, ih * 0.16), im @ Vector((0, -0.006, ih * 0.36)), M["blue"], bevel=0.03, rot=e, seg=2)  # nav/hero bar
for k in range(3):  # cards
    b.box((iw * 0.27, 0.014, ih * 0.38), im @ Vector((-iw * 0.31 + k * iw * 0.31, -0.008, -ih * 0.06)), M["frost" if k != 1 else "cellC"], bevel=0.03, rot=e, seg=2)
    b.box((iw * 0.18, 0.016, ih * 0.04), im @ Vector((-iw * 0.31 + k * iw * 0.31, -0.016, -ih * 0.02)), M["inkPale"], bevel=0.01, rot=e, seg=1)
b.box((iw * 0.22, 0.016, ih * 0.09), im @ Vector((-iw * 0.31, -0.01, -ih * 0.38)), M["green"], bevel=0.03, rot=e, seg=2)  # button
b.box((0.5, 0.36, 0.06), (-4.2, 0.6, 0.03), M["metal"], bevel=0.03)
b.box((0.09, 0.09, 0.85), (-4.2, 0.62, 0.45), M["metal"], bevel=0.03)
b.obj("BrowserClient", parent=cl)
b = B()
m = stand((-3.1, -1.2, 0.78))
b.box((0.62, 0.08, 1.2), m @ Vector((0, 0, 0)), M["white"], bevel=0.1, rot=m.to_euler())
b.box((0.54, 0.012, 1.02), m @ Vector((0, -0.046, 0.0)), M["dark"], bevel=0.05, rot=m.to_euler(), seg=2)
S.code_lines(b, 0.42, 0.8, 7, m @ Matrix.Translation((0, -0.06, 0)), indent_seed=4, y=0)
b.obj("PhoneClient", parent=cl)

# ---- API gateway
b = B()
b.box((1.0, 2.6, 1.3), (0, 0, 0.65), M["metal"], bevel=0.1)
b.box((1.04, 2.2, 0.16), (0, 0, 1.05), M["dark"], bevel=0.04)
for k in range(5):
    b.box((0.06, 0.24, 0.07), (0.52, -0.9 + k * 0.45, 1.05), M["code" if k % 2 == 0 else "lime"], bevel=0.02)
for k in range(4):  # vertical slots on the front face
    b.box((0.7, 0.05, 0.14), (0, -1.31, 0.3 + k * 0.17), M["dark"], bevel=0.02)
b.box((0.78, 0.04, 0.08), (0, -1.33, 0.95), M["blueGlass"], bevel=0.02)
b.obj("ApiGateway", loc=(-1.55, 0.1, 0.0), parent=R)

# ---- services
SV = [(1.0, -1.15), (1.15, 0.2), (1.0, 1.55)]
sv = S.empty("Services", parent=R)
for i, (x, y) in enumerate(SV, 1):
    b = B()
    b.box((1.2, 1.0, 0.9), (0, 0, 0.45), M["white"], bevel=0.1)
    b.box((1.1, 0.9, 0.08), (0, 0, 0.93), M["blue"], bevel=0.04)
    for k in range(3):  # stacked pods on top
        b.box((0.26, 0.26, 0.22), (-0.32 + k * 0.32, 0, 1.1), M["blueGlass" if k != i - 1 else "green"], bevel=0.05)
    mm = Matrix.Translation((0, -0.51, 0.45))
    b.box((0.9, 0.012, 0.56), mm @ Vector((0, -0.003, 0)), M["dark"], bevel=0.04, seg=2)
    S.code_lines(b, 0.74, 0.44, 4, mm @ Matrix.Translation((0, -0.012, 0)), indent_seed=20 + i, y=0)
    b.obj(f"Service{i:02d}", loc=(x, y, 0.0), parent=sv)

# ---- data layer
b = B()
S.database(b, 0.62, 1.5, (0, 0, 0.75), discs=3)
b.obj("Database", loc=(3.55, 0.45, 0.0), parent=R)
b = B()
S.database(b, 0.36, 0.7, (0, 0, 0.35), discs=2, body="cellT")
b.obj("Cache", loc=(3.25, -1.0, 0.0), parent=R)

# ---- request paths (cyan), routed like cable trays
P = []
gx = -1.55
P.append(S.ortho([(-3.0, 0.6, 1.2), (-2.4, 0.6, 1.2), (-2.4, 0.4, 0.95), (gx - 0.5, 0.4, 0.95)], 0.18))
P.append(S.ortho([(-2.85, -1.2, 0.5), (-2.4, -1.2, 0.5), (-2.4, -0.3, 0.6), (gx - 0.5, -0.3, 0.6)], 0.18))
for x, y in SV:
    P.append(S.ortho([(gx + 0.5, y * 0.55, 0.8), (0.0, y * 0.55, 0.8), (0.0, y, 0.6), (x - 0.6, y, 0.6)], 0.2))
for x, y in SV:
    P.append(S.ortho([(x + 0.6, y, 0.55), (2.5, y, 0.55), (2.5, 0.45 if y > -1 else -1.0, 0.55),
                      ((3.55 - 0.62) if y > -1 else (3.25 - 0.36), 0.45 if y > -1 else -1.0, 0.55)], 0.2))
b = B()
for pts in P:
    b.tube(pts, 0.02, M["path"], sides=6)
dp = b.obj("DataPaths", parent=R)

# ---- CI/CD rail along the front edge: build -> test -> deploy
ci = S.empty("CICDPipeline", parent=R)
b = B()
y0 = -2.15
b.box((8.6, 0.32, 0.06), (0.25, y0, 0.03), M["metalBlue"], bevel=0.02)
for k in range(30):
    b.box((0.04, 0.34, 0.07), (-4.0 + k * 0.29, y0, 0.04), M["metal"], bevel=0.01, seg=1)
for gxk, mname in ((-2.3, "code"), (0.2, "green"), (2.7, "lime")):  # gates
    b.box((0.08, 0.08, 0.7), (gxk, y0 - 0.22, 0.35), M["metal"], bevel=0.02)
    b.box((0.08, 0.08, 0.7), (gxk, y0 + 0.22, 0.35), M["metal"], bevel=0.02)
    b.box((0.12, 0.58, 0.1), (gxk, y0, 0.72), M[mname], bevel=0.03)
b.obj("Rail", parent=ci)
for k, x in enumerate((-3.4, -1.1, 1.4, 3.85)):
    b = B()
    b.box((0.62, 0.3, 0.3), (0, 0, 0.21), M["blue" if k < 3 else "green"], bevel=0.04)
    for r in range(5):
        b.box((0.03, 0.31, 0.26), (-0.24 + r * 0.12, 0, 0.21), M["deep" if k < 3 else "green"], bevel=0.01, seg=1)
    b.obj(f"Container{k + 1:02d}", loc=(x, y0, 0.06), parent=ci)
b = B()
b.box((1.0, 0.8, 0.1), (0, 0, 0.05), M["green"], bevel=0.05)
S.check_mark(b, 0.62, Matrix.Translation((0, 0.02, 0.1)) @ Matrix.Rotation(-math.pi / 2, 4, "X"), m="white")
b.obj("DeployTarget", loc=(4.6, y0 + 0.1, 0.0), parent=ci)

S.finish(a, "software-dev-architecture", cam_dir=CAM, margin=0.04, target=None)
