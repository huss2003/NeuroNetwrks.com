"""NN-Bot: the small NeuroNetworks developer robot (rigged + animated) for the walking site companion.

Rigid parts parented to an armature (no skinning), clips stored as NLA tracks and exported as glTF animations:
Idle (2 s loop), Walk (1 s loop, in place), Wave, Jump, LookAround.
The robot faces -Y in Blender, which is +Z (towards the default camera) in glTF / three.js.

    python tools/blender/nn_bot.py --out docs/3d/nn-bot --aspect 1 [--sheet]
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy  # noqa: E402
import nn_style as S  # noqa: E402
from mathutils import Quaternion  # noqa: E402
from nn_style import B, M, Matrix, Vector  # noqa: E402

a = S.args(lambda ap: ap.add_argument("--sheet", action="store_true"))
S.start(seed=101)
FPS = 24
scene = bpy.context.scene
scene.render.fps = FPS

body = S.mat("BotBody", (0.9, 0.93, 0.98), rough=0.28, coat=0.8)
face = S.mat("BotFace", (0.02, 0.04, 0.1), rough=0.12, coat=1.0)
eye = S.mat("BotEye", (0.45, 0.9, 1.0), emit=(0.35, 0.85, 1.0), emit_str=3.0, rough=0.2)
joint = M["metal"]
panel = M["blue"]

# ---------------------------------------------------------------- armature (rest pose, metres-ish units)
arm_data = bpy.data.armatures.new("NNBotRig")
rig = bpy.data.objects.new("NNBot", arm_data)
scene.collection.objects.link(rig)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode="EDIT")
E = arm_data.edit_bones
SH, HIP = 0.3, 0.12  # shoulder / hip half-width


def bone(name, head, tail, parent=None):
    b = E.new(name)
    b.head, b.tail = Vector(head), Vector(tail)
    b.roll = 0
    if parent:
        b.parent = E[parent]
        b.use_connect = False
    return b


bone("root", (0, 0, 0), (0, 0.2, 0))
bone("hips", (0, 0, 0.5), (0, 0, 0.62), "root")
bone("spine", (0, 0, 0.62), (0, 0, 0.95), "hips")
bone("head", (0, 0, 0.98), (0, 0, 1.3), "spine")
for s, side in ((1, "L"), (-1, "R")):
    bone(f"upperarm.{side}", (s * SH, 0, 0.88), (s * SH, 0, 0.68), "spine")
    bone(f"forearm.{side}", (s * SH, 0, 0.68), (s * SH, 0, 0.5), f"upperarm.{side}")
    bone(f"thigh.{side}", (s * HIP, 0, 0.5), (s * HIP, 0, 0.29), "hips")
    bone(f"shin.{side}", (s * HIP, 0, 0.29), (s * HIP, 0, 0.09), f"thigh.{side}")
bpy.ops.object.mode_set(mode="OBJECT")
for pb in rig.pose.bones:
    pb.rotation_mode = "QUATERNION"

# ---------------------------------------------------------------- parts (built in world space, then bone-parented)
parts = []


def part(name, bone_name, build):
    b = B()
    build(b)
    o = b.obj(name, smooth_below=0.05)
    parts.append((o, bone_name))
    return o


def capsule(b, r, z0, z1, x, mat_, y=0.0):
    b.cyl(r, z1 - z0, (x, y, (z0 + z1) / 2), mat_, seg=24)
    b.sphere(r, (x, y, z0), mat_, seg=20)
    b.sphere(r, (x, y, z1), mat_, seg=20)


# head: rounded screen-face
def head(b):
    b.box((0.64, 0.5, 0.48), (0, 0, 1.22), body, bevel=0.16, seg=5)
    b.box((0.5, 0.03, 0.32), (0, -0.245, 1.22), face, bevel=0.09, seg=4)
    for s in (1, -1):  # ear pods
        b.cyl(0.085, 0.06, (s * 0.335, 0, 1.22), panel, rot=(0, math.pi / 2, 0), seg=24)
        b.cyl(0.05, 0.03, (s * 0.37, 0, 1.22), M["lime"] if s > 0 else M["code"], rot=(0, math.pi / 2, 0), seg=20)
    # antenna: a git branch (main stem + side branch merging back)
    stem = [Vector((0, 0.02, 1.45)), Vector((0, 0.02, 1.62))]
    b.tube(stem, 0.014, joint, sides=8)
    b.tube(S.spline([(0, 0.02, 1.49), (0.07, 0.02, 1.53), (0.08, 0.02, 1.6)], 10), 0.011, joint, sides=8)
    b.sphere(0.035, (0, 0.02, 1.64), M["lime"], seg=16)
    b.sphere(0.026, (0.08, 0.02, 1.615), panel, seg=14)


part("Head", "head", head)
part("Eyes", "head", lambda b: [b.box((0.075, 0.02, 0.12), (s * 0.11, -0.262, 1.24), eye, bevel=0.035, seg=3) for s in (1, -1)])
part("Mouth", "head", lambda b: b.box((0.09, 0.02, 0.022), (0, -0.262, 1.14), eye, bevel=0.01, seg=2))


def torso(b):
    b.box((0.5, 0.36, 0.36), (0, 0, 0.78), body, bevel=0.12, seg=4)
    b.box((0.3, 0.03, 0.18), (0, -0.18, 0.8), panel, bevel=0.05, seg=3)  # chest panel
    S.code_lines(b, 0.2, 0.1, 3, Matrix.Translation((0, -0.197, 0.8)), mats=("codePale", "white"), indent_seed=1, y=0)
    b.sphere(0.028, (0.17, -0.17, 0.92), M["lime"], seg=14)  # status light
    b.cyl(0.07, 0.06, (0, 0, 0.97), joint, seg=24)  # neck


part("Torso", "spine", torso)
part("Pelvis", "hips", lambda b: (b.box((0.38, 0.28, 0.14), (0, 0, 0.56), body, bevel=0.06, seg=3),
                                  b.box((0.4, 0.3, 0.03), (0, 0, 0.62), joint, bevel=0.012, seg=2)))
for s, side in ((1, "L"), (-1, "R")):
    x = s * SH
    part(f"UpperArm.{side}", f"upperarm.{side}", lambda b, x=x: (b.sphere(0.075, (x, 0, 0.88), joint, seg=20),
                                                               capsule(b, 0.055, 0.7, 0.86, x, body)))
    part(f"Forearm.{side}", f"forearm.{side}", lambda b, x=x: (b.sphere(0.05, (x, 0, 0.68), joint, seg=16),
                                                             capsule(b, 0.05, 0.55, 0.66, x, body),
                                                             b.box((0.1, 0.11, 0.1), (x, 0, 0.49), panel, bevel=0.045, seg=3)))
    hx = s * HIP
    part(f"Thigh.{side}", f"thigh.{side}", lambda b, hx=hx: (b.sphere(0.06, (hx, 0, 0.49), joint, seg=16),
                                                            capsule(b, 0.06, 0.31, 0.46, hx, body)))
    part(f"Shin.{side}", f"shin.{side}", lambda b, hx=hx: (b.sphere(0.05, (hx, 0, 0.29), joint, seg=16),
                                                          capsule(b, 0.055, 0.13, 0.27, hx, body),
                                                          b.box((0.17, 0.27, 0.09), (hx, -0.04, 0.045), panel, bevel=0.04, seg=3)))

bpy.context.view_layer.update()
for o, bn in parts:
    mw = o.matrix_world.copy()
    o.parent = rig
    o.parent_type = "BONE"
    o.parent_bone = bn
    bpy.context.view_layer.update()
    o.matrix_world = mw

# ---------------------------------------------------------------- animation helpers
REST = {pb.name: pb.bone.matrix_local.to_3x3() for pb in rig.pose.bones}


def q(bone_name, world_axis, deg):
    """Rotation about a world-space axis (rest orientation), expressed in the bone's local space."""
    ax = (REST[bone_name].inverted() @ Vector(world_axis)).normalized()
    return Quaternion(ax, math.radians(deg))


def key(frame, pose):
    """pose: {bone: Quaternion or (Quaternion, loc)}; unspecified bones reset to rest."""
    for pb in rig.pose.bones:
        v = pose.get(pb.name)
        rot, loc = (v if isinstance(v, tuple) else (v, None)) if v is not None else (None, None)
        pb.rotation_quaternion = rot or Quaternion()
        pb.location = loc or Vector()
        pb.keyframe_insert("rotation_quaternion", frame=frame)
        pb.keyframe_insert("location", frame=frame)


def clip(name, frames, fn, step=2):
    act = bpy.data.actions.new(name)
    act.use_fake_user = True
    rig.animation_data_create()
    rig.animation_data.action = act
    for f in list(range(0, frames, step)) + [frames]:
        key(f, fn(f / frames))
    for fc in getattr(act, "fcurves", []):
        for kp in fc.keyframe_points:
            kp.interpolation = "BEZIER"
    track = rig.animation_data.nla_tracks.new()
    track.name = name
    track.strips.new(name, 0, act)
    rig.animation_data.action = None
    return act


X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
TAU = 2 * math.pi


def walk(t):
    p = TAU * t
    sw, kn = 26 * math.sin(p), 0
    knee_l = 45 * max(0.0, math.sin(p + 2.0)) ** 1.5
    knee_r = 45 * max(0.0, math.sin(p + 2.0 + math.pi)) ** 1.5
    bob = 0.025 * abs(math.cos(p))
    return {
        "hips": (q("hips", Z, 5 * math.sin(p)), Vector((0, bob, 0))),
        "spine": q("spine", Z, -4 * math.sin(p)) @ q("spine", X, -4),
        "head": q("head", Z, 2 * math.sin(p)) @ q("head", X, 3 * math.cos(2 * p)),
        "thigh.L": q("thigh.L", X, -sw), "thigh.R": q("thigh.R", X, sw),
        "shin.L": q("shin.L", X, knee_l), "shin.R": q("shin.R", X, knee_r),
        "upperarm.L": q("upperarm.L", X, sw * 0.8) @ q("upperarm.L", Y, -6),
        "upperarm.R": q("upperarm.R", X, -sw * 0.8) @ q("upperarm.R", Y, 6),
        "forearm.L": q("forearm.L", X, -20), "forearm.R": q("forearm.R", X, -20),
    }


def idle(t):
    p = TAU * t
    return {
        "hips": (Quaternion(), Vector((0, 0.008 * math.sin(p), 0))),
        "spine": q("spine", X, 1.8 * math.sin(p)),
        "head": q("head", Z, 4 * math.sin(p)) @ q("head", Y, 3 * math.sin(p + 1)),
        "upperarm.L": q("upperarm.L", Y, -5 - 2 * math.sin(p)), "upperarm.R": q("upperarm.R", Y, 5 + 2 * math.sin(p)),
        "forearm.L": q("forearm.L", X, -12), "forearm.R": q("forearm.R", X, -12),
    }


def wave(t):
    up = min(1.0, t / 0.18) if t < 0.82 else max(0.0, (1 - t) / 0.18)
    up = up * up * (3 - 2 * up)
    w = math.sin(TAU * 3 * min(1.0, max(0.0, (t - 0.15) / 0.65))) * up
    return {
        "upperarm.R": q("upperarm.R", Y, 150 * up) @ q("upperarm.R", X, -10 * up),
        "forearm.R": q("forearm.R", Y, 25 * w) @ q("forearm.R", X, -20 * up),
        "head": q("head", Y, -8 * up) @ q("head", X, -4 * up),
        "spine": q("spine", Y, 4 * up),
        "upperarm.L": q("upperarm.L", Y, -6),
    }


def jump(t):
    def s(a0, a1):  # smooth 0..1 between t=a0..a1
        k = min(1.0, max(0.0, (t - a0) / (a1 - a0)))
        return k * k * (3 - 2 * k)
    crouch = s(0.0, 0.22) - s(0.22, 0.34) + s(0.78, 0.88) - s(0.88, 1.0)
    air = s(0.28, 0.5) - s(0.55, 0.8)
    return {
        "hips": (Quaternion(), Vector((0, -0.09 * crouch + 0.42 * air, 0))),
        "thigh.L": q("thigh.L", X, -38 * crouch - 20 * air), "thigh.R": q("thigh.R", X, -38 * crouch - 20 * air),
        "shin.L": q("shin.L", X, 70 * crouch + 35 * air), "shin.R": q("shin.R", X, 70 * crouch + 35 * air),
        "spine": q("spine", X, 10 * crouch),
        "upperarm.L": q("upperarm.L", Y, -140 * air - 10 * crouch), "upperarm.R": q("upperarm.R", Y, 140 * air + 10 * crouch),
        "head": q("head", X, -10 * air + 6 * crouch),
    }


def look(t):
    k = math.sin(TAU * t)
    return {
        "head": q("head", Z, 38 * k) @ q("head", X, -5 * abs(k)),
        "spine": q("spine", Z, 8 * k),
        "upperarm.L": q("upperarm.L", Y, -5), "upperarm.R": q("upperarm.R", Y, 5),
    }


clip("Idle", 48, idle, step=4)
clip("Walk", 24, walk, step=2)
clip("Wave", 40, wave, step=2)
clip("Jump", 22, jump, step=1)
clip("LookAround", 58, look, step=4)

# ---------------------------------------------------------------- export (GLB with all clips), preview renders
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(a.out, "nn-bot.blend"))
bpy.ops.export_scene.gltf(filepath=os.path.join(a.out, "nn-bot.glb"), export_format="GLB", export_apply=False,
                          export_animations=True, export_animation_mode="NLA_TRACKS", export_force_sampling=True,
                          export_frame_step=1, export_cameras=False, export_lights=False, export_yup=True)

if not a.no_render:
    # preview: mid-wave, 3/4 view
    for t in rig.animation_data.nla_tracks:
        t.mute = t.name != "Wave"
    scene.frame_set(18)
    S.finish(a, "nn-bot-preview", cam_dir=(0.45, -1.0, 0.32), margin=0.08)
    if a.sheet:  # turntable (idle) + walk strip for review
        cam = scene.camera
        tgt = Vector((0, 0, 0.8))
        dist = (cam.location - tgt).length
        out = []
        for t in rig.animation_data.nla_tracks:
            t.mute = t.name != "Walk"
        for k, ang in enumerate((0, 90, 180, 270)):
            d = Matrix.Rotation(math.radians(ang), 3, "Z") @ Vector((0.45, -1.0, 0.32)).normalized()
            cam.location = tgt + d * dist
            cam.rotation_euler = (tgt - cam.location).to_track_quat("-Z", "Y").to_euler()
            cam.data.shift_x = cam.data.shift_y = 0
            scene.frame_set(k * 6)
            scene.render.filepath = os.path.join(a.out, f"turn-{k}.png")
            bpy.ops.render.render(write_still=True)
