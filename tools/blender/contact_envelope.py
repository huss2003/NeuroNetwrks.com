"""Contact page hero object: an envelope with a letter and a green reply badge.

    python tools/blender/contact_envelope.py --out docs/3d/contact-envelope --aspect 0.95
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args()
S.start(seed=19)
CAM = (0.42, -1.0, 0.38)
M["shell"] = S.mat("EnvelopeShell", S.srgb("#9DBDF2"), rough=0.22, coat=0.9)
M["flap"] = S.mat("EnvelopeFlap", S.srgb("#B7CFF7"), rough=0.2, coat=0.9)
M["paper"] = S.mat("Letter", (0.93, 0.95, 0.99), rough=0.35, coat=0.4)
R = S.empty("ContactEnvelope", rot=(math.radians(-6), 0, S.facing(CAM) + math.radians(-14)))

W, H, D = 2.4, 1.6, 0.34
b = B()
b.box((W, D, H), (0, 0, 0), M["shell"], bevel=0.12, seg=5)  # body
b.box((W - 0.4, 0.07, 1.5), (0, 0.02, 0.62), M["paper"], bevel=0.04)  # letter, top edge shows above the body
for i, (w, x) in enumerate([(1.1, -0.25), (0.75, -0.43), (0.95, -0.33)]):  # lines of text on the letter
    b.box((w, 0.02, 0.07), (x, -0.025, 1.24 - i * 0.16), M["codePale" if i else "code"], bevel=0.02)
front = -D / 2
b.prism([(-W / 2 + 0.1, -H / 2 + 0.1), (W / 2 - 0.1, -H / 2 + 0.1), (0, 0.06)], 0.03, M["flap"],
        Matrix.Translation(Vector((0, front, 0))))  # lower fold
b.prism([(-W / 2 + 0.06, H / 2 - 0.06), (W / 2 - 0.06, H / 2 - 0.06), (0, -0.16)], 0.07, M["flap"],
        Matrix.Translation(Vector((0, front - 0.03, 0))))  # top flap
b.obj("Envelope", parent=R, smooth_below=0.03)

g = B()  # reply badge: green disc with a white tick, pinned to the top-right corner
badge = Matrix.Translation(Vector((W / 2 - 0.12, front - 0.16, H / 2 - 0.02))) @ Matrix.Rotation(math.radians(90), 4, "X")
g.cyl(0.36, 0.14, badge @ Vector((0, 0, 0)), M["green"], rot=(math.radians(90), 0, 0), seg=48, bevel=0.04)
S.check_mark(g, 0.34, Matrix.Translation(Vector((W / 2 - 0.12, front - 0.24, H / 2 - 0.04))), m="white", thick=0.06)
g.obj("ReplyBadge", parent=R)

S.finish(a, "contact-envelope", cam_dir=CAM, margin=0.06, lens=60, light={"key": 1500, "fill": 600, "rim": 1000, "world": 0.6})
