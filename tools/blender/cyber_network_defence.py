"""`cyber-network-defence`: endpoints -> firewall (allowed packets pass, suspicious ones stop)
-> segmented internal network (app rack | data zone) watched by a SOC terminal.

    python tools/blender/cyber_network_defence.py --out docs/3d/cyber-network-defence --aspect 1.7778
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args()
S.start(seed=41)
CAM = (0.52, -1.0, 0.55)
F = S.facing(CAM)
R = S.empty("cyber-network-defence")
S.platform("Base", (10.2, 4.4), loc=(0.2, 0.1, 0), parent=R)
rnd = random.Random(9)


def stand(loc):
    return Matrix.Translation(Vector(loc)) @ Matrix.Rotation(F, 4, "Z")


# ---- endpoints (outside the perimeter)
ep = S.empty("Endpoints", parent=R)
b = B()  # laptop
b.box((0.95, 0.65, 0.05), (0, 0, 0.03), M["metal"], bevel=0.03)
b.box((0.8, 0.45, 0.012), (0, 0.02, 0.06), M["dark"], bevel=0.02, seg=1)
lid = Matrix.Translation((0, 0.32, 0.05)) @ Matrix.Rotation(math.radians(-15), 4, "X")
b.box((0.95, 0.05, 0.62), lid @ Vector((0, 0, 0.31)), M["metal"], bevel=0.03, rot=lid.to_3x3().to_4x4())
b.box((0.84, 0.012, 0.52), lid @ Vector((0, -0.03, 0.31)), M["dark"], bevel=0.02, rot=lid.to_3x3().to_4x4(), seg=1)
S.code_lines(b, 0.7, 0.42, 5, lid @ Matrix.Translation((0, -0.04, 0.31)), indent_seed=3, y=0)
b.obj("Laptop", loc=(-4.2, 0.9, 0.0), rot=(0, 0, 0.35), parent=ep)
b = B()  # phone
m = stand((0, 0, 0.5))
b.box((0.42, 0.06, 0.8), m @ Vector((0, 0, 0)), M["white"], bevel=0.07, rot=m.to_3x3().to_4x4())
b.box((0.36, 0.012, 0.68), m @ Vector((0, -0.035, 0)), M["dark"], bevel=0.04, rot=m.to_3x3().to_4x4(), seg=1)
b.box((0.36, 0.25, 0.04), (0, 0.02, 0.02), M["metal"], bevel=0.02)
b.obj("Phone", loc=(-4.35, -0.75, 0.0), parent=ep)
b = B()  # IoT camera
b.cyl(0.2, 0.08, (0, 0, 0.04), M["metal"], seg=24)
b.box((0.08, 0.08, 0.4), (0, 0, 0.24), M["metal"], bevel=0.03)
b.box((0.42, 0.26, 0.24), (0, 0, 0.52), M["white"], bevel=0.08)
b.cyl(0.08, 0.06, (0, -0.15, 0.52), M["dark"], rot=(math.pi / 2, 0, 0), seg=20)
b.obj("Camera", loc=(-3.35, 0.0, 0.0), parent=ep)

# ---- firewall: glass-brick wall with two inspection portals
FX = -1.7
b = B()
for row in range(3):
    for col in range(8):
        y = -1.75 + col * 0.5 + (0.25 if row % 2 else 0)
        if (abs(y + 0.35) < 0.3 or abs(y - 0.95) < 0.3) and row < 2:
            continue  # inspection portals
        if y > 1.85:
            continue
        b.box((0.3, 0.46, 0.34), (0, y, 0.2 + row * 0.37), M["white" if (row + col) % 3 else "blueGlass"], bevel=0.05)
b.box((0.36, 3.7, 0.05), (0, 0.05, 1.17), M["path"], bevel=0.02)  # scanning band
for y in (-0.35, 0.95):  # portal frames glow
    b.box((0.34, 0.06, 0.74), (0, y - 0.3, 0.38), M["glassEdge"])
    b.box((0.34, 0.06, 0.74), (0, y + 0.3, 0.38), M["glassEdge"])
b.obj("Firewall", loc=(FX, 0.0, 0.0), parent=R)

# packets: allowed (blue) pass the portals, flagged (amber) are held at the wall
pk = S.empty("Packets", parent=R)
b = B()
for k, (x, y) in enumerate(((-3.0, -0.35), (-2.45, -0.35), (-1.0, -0.35), (-2.7, 0.95), (-0.95, 0.95))):
    b.box((0.2, 0.2, 0.2), (x, y, 0.32), M["blue"], bevel=0.04)
b.obj("AllowedPackets", parent=pk)
b = B()
for (x, y, z) in ((FX - 0.45, -1.3, 0.12), (FX - 0.45, -1.3, 0.34), (FX - 0.45, -1.05, 0.12), (FX - 0.45, 0.35, 0.12)):
    b.box((0.2, 0.2, 0.2), (x, y, z), M["amber"], bevel=0.04)  # held outside the wall
b.box((0.6, 0.85, 0.04), (FX - 0.45, -1.15, 0.02), M["amber"], bevel=0.02)  # quarantine pad
b.obj("BlockedPackets", parent=pk)

# ---- internal network: app zone + data zone, separated by a glass partition
b = B()
b.box((2.4, 3.6, 0.12), (0.55, 0.1, 0.06), M["white"], bevel=0.05)
b.box((2.1, 3.6, 0.12), (3.45, 0.1, 0.06), M["white"], bevel=0.05)
b.box((0.08, 3.4, 1.2), (2.05, 0.1, 0.72), M["glass"], bevel=0.03)
b.box((0.1, 0.5, 0.06), (2.05, 0.3, 1.33), M["green"], bevel=0.02)
b.obj("Segments", parent=R)
b = B()  # server rack
b.box((1.0, 1.0, 2.0), (0, 0, 1.12), M["metal"], bevel=0.08)
for u in range(7):
    b.box((0.86, 0.04, 0.22), (0, -0.5, 0.3 + u * 0.26), M["dark"], bevel=0.02, seg=1)
    for k in range(3):
        b.sphere(0.022, (-0.33 + k * 0.07, -0.53, 0.3 + u * 0.26), M["lime" if (u + k) % 4 == 0 else "code"], seg=8)
    for k in range(4):
        b.box((0.06, 0.02, 0.12), (0.06 + k * 0.08, -0.53, 0.3 + u * 0.26), M["inkPale"], seg=1)
b.obj("ServerRack", loc=(0.55, 0.65, 0.12), parent=R)
b = B()
S.database(b, 0.5, 1.2, (0, 0, 0.6), discs=3)
b.obj("DataStore", loc=(3.3, 0.75, 0.12), parent=R)
b = B()  # key vault
b.box((0.6, 0.6, 0.6), (0, 0, 0.3), M["deep"], bevel=0.08)
b.cyl(0.16, 0.06, (0, -0.31, 0.32), M["metal"], rot=(math.pi / 2, 0, 0), seg=24)
for k in range(4):
    b.box((0.04, 0.03, 0.12), Vector((0, -0.34, 0.32)) + Vector((math.cos(k * math.pi / 2) * 0.09, 0, math.sin(k * math.pi / 2) * 0.09)), M["lime"], seg=1)
b.obj("KeyVault", loc=(4.05, -0.45, 0.12), parent=R)

# ---- SOC terminal: event timeline with one alert
b = B()
m = stand((2.65, -1.35, 0.95))
iw, ih, im = S.window(b, 1.6, 1.1, m, body="white", dark=True)
e = im.to_3x3().to_4x4()
for k in range(6):
    w = iw * rnd.uniform(0.25, 0.7)
    mm = "amber" if k == 2 else ("code" if k % 2 else "codePale")
    b.box((w, 0.012, ih * 0.07), im @ Vector((-iw * 0.42 + w / 2, -0.006, ih * 0.36 - k * ih * 0.13)), M[mm], bevel=0.02, rot=e, seg=1)
b.box((0.08, 0.08, 0.36), (2.65, -1.32, 0.18), M["metal"], bevel=0.03)
b.box((0.5, 0.34, 0.05), (2.65, -1.32, 0.025), M["metal"], bevel=0.02)
b.obj("SocTerminal", parent=R)

# ---- traffic paths
P = [S.ortho([(-3.85, 0.9, 0.3), (-3.3, 0.9, 0.3), (-3.3, 0.95, 0.32), (FX - 0.2, 0.95, 0.32)], 0.15),
     S.ortho([(-4.15, -0.75, 0.3), (-3.3, -0.75, 0.3), (-3.3, -0.35, 0.32), (FX - 0.2, -0.35, 0.32)], 0.15),
     S.ortho([(FX + 0.2, -0.35, 0.32), (-0.3, -0.35, 0.32), (-0.3, 0.65, 0.5), (0.05, 0.65, 0.5)], 0.15),
     S.ortho([(FX + 0.2, 0.95, 0.32), (-0.3, 0.95, 0.32), (-0.3, 0.75, 0.5), (0.05, 0.75, 0.5)], 0.15),
     S.ortho([(1.05, 0.5, 0.7), (2.05, 0.3, 0.7), (2.8, 0.6, 0.7)], 0.2),
     S.spline([(1.0, 0.2, 0.4), (1.8, -0.7, 0.5), (2.2, -1.1, 0.6)], 20)]
b = B()
for pts in P:
    b.tube(pts, 0.02, M["path"], sides=6)
b.obj("DataPaths", parent=R)

S.finish(a, "cyber-network-defence", cam_dir=CAM, margin=0.04)
