"""`laptop-lab`: house-style laptop whose screen shows the practice lab
(instructions | code editor | output + passing tests). Renders 24 lid frames for the scroll animation.

    python tools/blender/laptop_lab.py --out docs/3d/laptop-lab --aspect 1.2955 --res 640 --frames 24
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy  # noqa: E402
import nn_style as S  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args(lambda ap: ap.add_argument("--frames", type=int, default=24))
S.start(seed=91)
CAM = (0.38, -1.0, 0.5)
R = S.empty("laptop-lab")

W, D, T = 3.2, 2.2, 0.12
b = B()
b.box((W, D, T), (0, 0, T / 2), M["metal"], bevel=0.06)
b.box((W * 0.86, D * 0.42, 0.012), (0, 0.2, T + 0.004), M["dark"], bevel=0.02, seg=1)  # keyboard well
for r in range(4):
    for c in range(12):
        b.box((0.18, 0.15, 0.02), (-W * 0.39 + c * 0.226, 0.48 - r * 0.2, T + 0.014), M["metal"], bevel=0.02, seg=1)
b.box((0.9, 0.55, 0.008), (0, -0.62, T + 0.003), M["metal"], bevel=0.02, seg=1)  # trackpad
b.obj("Base", parent=R)

hinge = S.empty("Lid", parent=R, loc=(0, D / 2 - 0.04, T))
b = B()
H = 2.05
b.box((W, 0.08, H), (0, 0, H / 2), M["metal"], bevel=0.06)
im = Matrix.Translation((0, -0.045, H / 2 + 0.02))
iw, ih = W - 0.18, H - 0.2
b.box((iw, 0.012, ih), im @ Vector((0, 0, 0)), M["white"], bevel=0.03, seg=2)
# app header
b.box((iw, 0.014, ih * 0.08), im @ Vector((0, -0.004, ih * 0.46)), M["frost"], seg=1)
b.box((iw * 0.12, 0.016, ih * 0.04), im @ Vector((-iw * 0.42, -0.008, ih * 0.46)), M["blue"], bevel=0.01, seg=1)
# left: instructions
b.box((iw * 0.24, 0.014, ih * 0.82), im @ Vector((-iw * 0.37, -0.004, -ih * 0.05)), M["frost"], bevel=0.02, seg=1)
S.code_lines(b, iw * 0.2, ih * 0.6, 8, im @ Matrix.Translation((-iw * 0.37, 0, 0.0)), mats=("ink", "inkPale", "inkPale"), indent_seed=3, y=-0.01)
# centre: editor
b.box((iw * 0.44, 0.014, ih * 0.82), im @ Vector((-iw * 0.01, -0.004, -ih * 0.05)), M["dark"], bevel=0.02, seg=1)
S.code_lines(b, iw * 0.38, ih * 0.7, 11, im @ Matrix.Translation((-iw * 0.01, 0, -ih * 0.05)), mats=("code", "codeGreen", "codePale"), indent_seed=4, y=-0.012)
# right: output + tests
b.box((iw * 0.24, 0.014, ih * 0.4), im @ Vector((iw * 0.36, -0.004, ih * 0.16)), M["deep"], bevel=0.02, seg=1)
S.code_lines(b, iw * 0.2, ih * 0.3, 5, im @ Matrix.Translation((iw * 0.36, 0, ih * 0.16)), mats=("codePale", "codeGreen"), indent_seed=5, y=-0.012)
for k in range(3):
    z = -ih * 0.12 - k * ih * 0.1
    b.box((iw * 0.24, 0.014, ih * 0.075), im @ Vector((iw * 0.36, -0.004, z)), M["frost"], bevel=0.02, seg=1)
    b.sphere(ih * 0.025, im @ Vector((iw * 0.27, -0.02, z)), M["green"], seg=10)
    b.box((iw * 0.13, 0.016, ih * 0.025), im @ Vector((iw * 0.38, -0.008, z)), M["inkPale"], seg=1)
b.box((iw * 0.24, 0.016, ih * 0.05), im @ Vector((iw * 0.36, -0.006, -ih * 0.44)), M["green"], bevel=0.02, seg=1)  # all tests pass
lid = b.obj("Screen", parent=hinge)

OPEN = math.radians(-12)  # leaning back a little past vertical
hinge.rotation_euler = (OPEN, 0, 0)
S.finish(a, "laptop-lab", cam_dir=CAM, margin=0.06, target=(0, 0.2, 0.9))

if not a.no_render and a.frames:
    scene = bpy.context.scene
    fd = os.path.join(a.out, "frames")
    os.makedirs(fd, exist_ok=True)
    for k in range(a.frames):  # frame 0 closed, last frame open (matches site.js lap-NN order)
        t = k / (a.frames - 1)
        e = 1 - (1 - t) ** 2
        hinge.rotation_euler = (math.radians(90) + (OPEN - math.radians(90)) * e, 0, 0)
        scene.render.filepath = os.path.join(fd, f"lap-{k:02d}.png")
        bpy.ops.render.render(write_still=True)
