"""Build the `ai-ml-training-pipeline` 3D asset for the AI/ML Engineering program card.

Run headless with the Blender Python module (pip install bpy==5.1.2):

    python tools/blender/ai_ml_pipeline.py --out docs/3d/ai-ml-training-pipeline [--samples 128] [--res 2400]

Writes <out>/ai-ml-training-pipeline.blend, .glb and preview.png (transparent).
Every component is a separate, stably named object so the website can animate it.
Blender is Z-up; the glTF export converts to Y-up (x, z, -y).
"""
import argparse
import json
import math
import os
import random
import sys

import bpy  # must come first: it registers bmesh and mathutils
import bmesh
from mathutils import Matrix, Vector

ap = argparse.ArgumentParser()
ap.add_argument("--out", required=True)
ap.add_argument("--samples", type=int, default=128)
ap.add_argument("--res", type=int, default=2400)
ap.add_argument("--no-render", action="store_true")
args = ap.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:])
OUT = os.path.abspath(args.out)
os.makedirs(OUT, exist_ok=True)
random.seed(7)

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

# Camera azimuth: panels that should face the viewer are turned by this angle around Z.
CAM_DIR = Vector((0.52, -1.0, 0.66)).normalized()
FACE = math.atan2(CAM_DIR.x, -CAM_DIR.y)


# ---------------------------------------------------------------- materials
def mat(name, color, alpha=1.0, rough=0.3, metal=0.0, emit=None, emit_str=0.0, coat=0.0, trans=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    b.inputs["Alpha"].default_value = alpha
    b.inputs["Coat Weight"].default_value = coat
    b.inputs["Transmission Weight"].default_value = trans
    if emit:
        b.inputs["Emission Color"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = emit_str
    if alpha < 1:
        m.surface_render_method = "BLENDED"
        m.use_backface_culling = False
    return m


M = {
    "glass": mat("GlassBlue", (0.3, 0.56, 1.0), alpha=0.3, rough=0.06, coat=0.4),
    "glassEdge": mat("GlassEdge", (0.62, 0.86, 1.0), alpha=0.7, rough=0.05, emit=(0.55, 0.85, 1.0), emit_str=0.6, coat=0.6),
    "cube": mat("CubeBlue", (0.08, 0.36, 1.0), alpha=0.7, rough=0.08, emit=(0.05, 0.3, 1.0), emit_str=0.6, coat=0.6),
    "glyph": mat("GlyphLight", (0.75, 0.9, 1.0), emit=(0.65, 0.88, 1.0), emit_str=1.4, rough=0.2),
    "frost": mat("FrostedPanel", (0.86, 0.92, 1.0), alpha=0.7, rough=0.35, coat=0.3),
    "base": mat("PlatformFrost", (0.8, 0.88, 1.0), alpha=0.92, rough=0.3, coat=0.4),
    "rim": mat("PlatformRim", (0.55, 0.82, 1.0), alpha=0.85, emit=(0.4, 0.75, 1.0), emit_str=1.2),
    "metal": mat("SatinMetal", (0.8, 0.85, 0.92), metal=1.0, rough=0.32),
    "metalBlue": mat("SatinBlue", (0.32, 0.5, 0.82), metal=1.0, rough=0.35),
    "dark": mat("CoreDark", (0.04, 0.07, 0.14), rough=0.4),
    "coreGlow": mat("CoreGlow", (0.3, 0.65, 1.0), alpha=0.9, emit=(0.3, 0.7, 1.0), emit_str=2.2, rough=0.1, coat=1.0),
    "grid": mat("CoreGrid", (0.2, 0.55, 1.0), emit=(0.15, 0.5, 1.0), emit_str=1.0),
    "path": mat("DataPath", (0.45, 0.88, 1.0), alpha=0.9, emit=(0.2, 0.75, 1.0), emit_str=1.1, rough=0.2),
    "lime": mat("ActivationLime", (0.5, 0.88, 0.12), emit=(0.5, 0.9, 0.1), emit_str=0.5, rough=0.25, coat=0.8),
    "cellA": mat("CellDeep", (0.06, 0.3, 0.98), alpha=0.88, emit=(0.1, 0.35, 1.0), emit_str=0.5, rough=0.15),
    "cellB": mat("CellMid", (0.22, 0.5, 1.0), alpha=0.7, emit=(0.3, 0.6, 1.0), emit_str=0.3, rough=0.15),
    "cellC": mat("CellPale", (0.5, 0.72, 1.0), alpha=0.5, rough=0.2),
    "cellT": mat("CellTeal", (0.25, 0.78, 0.8), alpha=0.65, emit=(0.3, 0.85, 0.85), emit_str=0.3, rough=0.15),
    "modelCore": mat("ModelCore", (0.05, 0.32, 1.0), alpha=0.9, emit=(0.15, 0.45, 1.0), emit_str=0.9, rough=0.1, coat=1.0),
    "chartBlue": mat("ChartBlue", (0.1, 0.42, 0.95), emit=(0.1, 0.42, 0.95), emit_str=0.4, rough=0.3),
    "chartLime": mat("ChartLime", (0.6, 0.88, 0.25), emit=(0.6, 0.9, 0.2), emit_str=0.4, rough=0.3),
    "chartAxis": mat("ChartAxis", (0.55, 0.68, 0.85), rough=0.4),
}


# ---------------------------------------------------------------- geometry builder
class B:
    """Accumulates primitives into one bmesh with per-face material slots."""

    def __init__(self):
        self.bm = bmesh.new()
        self.mats = []

    def _slot(self, m):
        if m not in self.mats:
            self.mats.append(m)
        return self.mats.index(m)

    def _finish(self, geom_verts, m, mtx):
        bmesh.ops.transform(self.bm, matrix=mtx, verts=geom_verts)
        idx = self._slot(m)
        faces = {f for v in geom_verts for f in v.link_faces}
        for f in faces:
            f.material_index = idx
            f.smooth = True

    def box(self, size, loc, m, bevel=0.0, rot=(0, 0, 0), seg=3):
        tmp = bmesh.new()
        bmesh.ops.create_cube(tmp, size=1.0)
        bmesh.ops.scale(tmp, vec=Vector(size), verts=tmp.verts)
        if bevel > 0:
            bmesh.ops.bevel(tmp, geom=list(tmp.edges), offset=min(bevel, min(size) * 0.49), segments=seg,
                            profile=0.5, affect="EDGES", clamp_overlap=True)
        self._merge(tmp, m, Matrix.Translation(loc) @ euler(rot))

    def sphere(self, r, loc, m, seg=16):
        tmp = bmesh.new()
        bmesh.ops.create_uvsphere(tmp, u_segments=seg, v_segments=seg // 2 + 2, radius=r)
        self._merge(tmp, m, Matrix.Translation(loc))

    def cone(self, r, depth, loc, m, rot=(0, 0, 0), seg=16):
        tmp = bmesh.new()
        bmesh.ops.create_cone(tmp, cap_ends=True, segments=seg, radius1=r, radius2=0.0, depth=depth)
        self._merge(tmp, m, Matrix.Translation(loc) @ euler(rot))

    def tri(self, pts, thick, m, mtx):
        tmp = bmesh.new()
        vs = [tmp.verts.new(Vector(p)) for p in pts]
        f = tmp.faces.new(vs)
        r = bmesh.ops.extrude_face_region(tmp, geom=[f])
        bmesh.ops.translate(tmp, vec=Vector((0, 0, thick)), verts=[g for g in r["geom"] if isinstance(g, bmesh.types.BMVert)])
        bmesh.ops.recalc_face_normals(tmp, faces=tmp.faces)
        self._merge(tmp, m, mtx)

    def tube(self, pts, r, m, sides=8):
        """Sweep a circle along a polyline. Faces are emitted in path order (for draw-range reveals)."""
        tmp = bmesh.new()
        rings = []
        for i, p in enumerate(pts):
            t = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
            up = Vector((0, 0, 1)) if abs(t.z) < 0.9 else Vector((1, 0, 0))
            n = t.cross(up).normalized()
            bn = t.cross(n).normalized()
            rings.append([tmp.verts.new(p + (n * math.cos(a) + bn * math.sin(a)) * r)
                          for a in (2 * math.pi * k / sides for k in range(sides))])
        for a, b in zip(rings, rings[1:]):
            for k in range(sides):
                tmp.faces.new((a[k], a[(k + 1) % sides], b[(k + 1) % sides], b[k]))
        tmp.faces.new(list(reversed(rings[0])))
        tmp.faces.new(rings[-1])
        self._merge(tmp, m, Matrix.Identity(4))

    def _merge(self, tmp, m, mtx):
        bmesh.ops.transform(tmp, matrix=mtx, verts=tmp.verts)
        me = bpy.data.meshes.new("tmp")
        tmp.to_mesh(me)
        tmp.free()
        n0 = len(self.bm.verts)
        self.bm.from_mesh(me)
        bpy.data.meshes.remove(me)
        self.bm.verts.ensure_lookup_table()
        new = self.bm.verts[n0:]
        idx = self._slot(m)
        for f in {f for v in new for f in v.link_faces}:
            f.material_index = idx
            f.smooth = True

    def obj(self, name, loc=(0, 0, 0), parent=None, rot=(0, 0, 0)):
        me = bpy.data.meshes.new(name)
        self.bm.normal_update()
        self.bm.to_mesh(me)
        self.bm.free()
        for m in self.mats:
            me.materials.append(m)
        o = bpy.data.objects.new(name, me)
        bpy.context.collection.objects.link(o)
        o.location = loc
        o.rotation_euler = rot
        if parent:
            o.parent = parent
        # auto-smooth substitute: flat shade large flat faces, smooth curved ones
        for p in me.polygons:
            p.use_smooth = p.area < 0.02
        return o


def euler(rot):
    return Matrix.Rotation(rot[0], 4, "X") @ Matrix.Rotation(rot[1], 4, "Y") @ Matrix.Rotation(rot[2], 4, "Z") \
        if any(rot) else Matrix.Identity(4)


def empty(name, parent=None, loc=(0, 0, 0)):
    o = bpy.data.objects.new(name, None)
    o.empty_display_size = 0.3
    bpy.context.collection.objects.link(o)
    o.location = loc
    if parent:
        o.parent = parent
    return o


def spline(ctrl, n=48):
    """Catmull-Rom through control points, returned as Vectors."""
    P = [Vector(c) for c in ctrl]
    P = [P[0] * 2 - P[1]] + P + [P[-1] * 2 - P[-2]]
    out = []
    segs = len(P) - 3
    for s in range(segs):
        p0, p1, p2, p3 = P[s:s + 4]
        steps = max(4, n // segs)
        for i in range(steps):
            t = i / steps
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(P[-2].copy())
    return out


def glyph(b, w, mtx):
    """Abstract 'image' glyph (frame, mountain, sun) lying in local XZ, facing -Y."""
    t = 0.012
    for (sx, sz, x, z) in ((w, t * 2, 0, w / 2), (w, t * 2, 0, -w / 2), (t * 2, w, -w / 2, 0), (t * 2, w, w / 2, 0)):
        b.box((sx, t, sz), (mtx @ Vector((x, 0, z))), M["glyph"], rot=mtx.to_euler())
    b.tri([(-w * 0.42, 0, -w * 0.38), (-w * 0.05, 0, w * 0.12), (w * 0.15, 0, -w * 0.12), (w * 0.27, 0, 0.0),
           (w * 0.42, 0, -w * 0.38)], -t, M["glyph"], mtx)
    b.sphere(w * 0.08, mtx @ Vector((w * 0.22, 0, w * 0.24)), M["glyph"], seg=10)


root = empty("ai-ml-training-pipeline")

# ---------------------------------------------------------------- platform
b = B()
b.box((11.8, 5.0, 0.28), (0.55, 0.0, -0.14), M["base"], bevel=0.12)
b.box((11.6, 0.04, 0.05), (0.55, -2.49, -0.06), M["rim"], bevel=0.015)
b.box((0.04, 4.8, 0.05), (6.44, 0.0, -0.06), M["rim"], bevel=0.015)
b.obj("Base", parent=root)

# ---------------------------------------------------------------- input data
inp = empty("InputData", parent=root)
cubes = [((-6.7, -0.6, 2.6), 0.55, False), ((-5.7, 0.5, 3.15), 0.45, False), ((-5.9, -1.5, 1.6), 0.8, True),
         ((-7.3, 0.9, 1.45), 0.72, True), ((-4.75, -0.35, 1.05), 0.5, False), ((-6.4, 1.7, 2.35), 0.4, False)]
face = euler((0, 0, FACE))
input_pts = []
for i, (loc, s, g) in enumerate(cubes, 1):
    b = B()
    b.box((s, s, s), (0, 0, 0), M["cube"], bevel=s * 0.12)
    b.box((s * 0.78, s * 0.78, s * 0.78), (0, 0, 0), M["cellA"], bevel=s * 0.1)
    if g:
        glyph(b, s * 0.62, Matrix.Translation((0, -s * 0.51, 0)))
    o = b.obj(f"InputCube{i:02d}", loc=loc, parent=inp, rot=(0, 0, FACE * 0.6))
    input_pts.append(Vector(loc))
tiles = [((-4.55, 1.05, 2.75), 0.5), ((-5.15, -1.1, 3.25), 0.42), ((-7.75, -0.5, 3.0), 0.36)]
for i, (loc, s) in enumerate(tiles, 1):
    b = B()
    b.box((s, 0.05, s), (0, 0, 0), M["glass"], bevel=0.02)
    glyph(b, s * 0.7, Matrix.Translation((0, -0.03, 0)))
    b.obj(f"InputTile{i:02d}", loc=loc, parent=inp, rot=(0, 0, FACE))
    input_pts.append(Vector(loc))
# tall glass intake panel with image tiles
b = B()
b.box((0.12, 3.7, 3.7), (0, 0, 0), M["glass"], bevel=0.1)
b.box((0.03, 3.5, 0.03), (0.07, 0, 1.78), M["glassEdge"])
for k, (y, z) in enumerate(((-0.9, 0.9), (0.6, 0.2), (-0.2, -0.9))):
    b.box((0.04, 0.62, 0.62), (0.09, y, z), M["cellB"], bevel=0.04)
    glyph(b, 0.42, Matrix.Translation((0.12, y, z)) @ Matrix.Rotation(math.pi / 2, 4, "Z"))
b.obj("InputPanel", loc=(-3.85, 0.0, 1.95), parent=inp)

# ---------------------------------------------------------------- processor
PX, PS = -1.6, Vector((2.5, 2.1, 1.7))
b = B()
b.box(PS, (0, 0, 0), M["metal"], bevel=0.1)
b.box((2.2, 1.8, 0.06), (0, 0, PS.z / 2 + 0.01), M["dark"], bevel=0.02)
for ix in range(14):
    for iy in range(11):
        if random.random() < 0.82:
            b.box((0.1, 0.1, 0.012), (-1.0 + ix * 0.154, -0.78 + iy * 0.156, PS.z / 2 + 0.045), M["grid"])
for k in range(11):  # cooling fins on the viewer side
    b.box((0.07, 0.16, 1.3), (-1.0 + k * 0.2, -PS.y / 2 - 0.07, -0.05), M["metal"], bevel=0.02)
b.box((2.1, 0.05, 1.36), (0, -PS.y / 2 - 0.01, -0.05), M["dark"])
for k in range(6):  # memory-like modules behind the fins
    b.box((0.18, 0.04, 1.0), (-0.9 + k * 0.36, -PS.y / 2 - 0.035, -0.05), M["metalBlue"])
b.box((0.3, 2.2, 1.8), (PS.x / 2 + 0.1, 0, 0), M["metal"], bevel=0.08)
b.box((0.12, 1.8, 1.4), (PS.x / 2 + 0.27, 0, 0), M["coreGlow"], bevel=0.05)
b.box((0.04, 1.86, 0.04), (PS.x / 2 + 0.3, 0, 0.72), M["glassEdge"])
b.box((0.3, 2.2, 1.8), (-PS.x / 2 - 0.1, 0, 0), M["metal"], bevel=0.08)
b.obj("ProcessorCore", loc=(PX, 0.0, PS.z / 2 + 0.05), parent=root)
PROC_IN = PX - PS.x / 2 - 0.25
PROC_OUT = PX + PS.x / 2 + 0.35

# ---------------------------------------------------------------- feature layers
LX = [0.65, 1.35, 2.05, 2.75]
LSIZE = [(3.8, 3.5), (3.6, 3.3), (3.4, 3.1), (3.2, 2.9)]
CELLMIX = [("cellA", 0.3), ("cellB", 0.32), ("cellC", 0.25), ("cellT", 0.13)]
for i, (x, (w, h)) in enumerate(zip(LX, LSIZE), 1):
    b = B()
    b.box((0.05, w, h), (0, 0, h / 2), M["glass"], bevel=0.04)
    b.box((0.06, w - 0.05, 0.035), (0, 0, h - 0.02), M["glassEdge"])
    b.box((0.06, 0.035, h - 0.05), (0, -w / 2 + 0.02, h / 2), M["glassEdge"])
    ny, nz = int(w / 0.27), int(h / 0.27)
    teal_bias = 0.25 if i in (2, 3) else 0.0
    for iy in range(ny):
        for iz in range(nz):
            if random.random() < 0.18:
                continue
            r = random.random()
            acc, key = 0, "cellA"
            for k, p in CELLMIX:
                p = p + (teal_bias if k == "cellT" else 0)
                acc += p
                if r < acc / (1 + teal_bias):
                    key = k
                    break
            y = -w / 2 + 0.2 + iy * (w - 0.4) / max(ny - 1, 1)
            z = 0.2 + iz * (h - 0.4) / max(nz - 1, 1)
            b.box((0.03, 0.2, 0.2), (0.035, y, z), M[key], bevel=0.015, seg=1)
    b.obj(f"FeatureLayer{i:02d}", loc=(x, 0.0, 0.02), parent=root)

# ---------------------------------------------------------------- activation nodes
NODES = [(LX[0] + 0.07, -1.2, 2.7), (LX[0] + 0.07, 0.5, 1.15), (LX[1] + 0.07, -0.35, 2.95), (LX[1] + 0.07, 1.0, 0.55),
         (LX[2] + 0.07, -1.25, 1.45), (LX[2] + 0.07, 0.35, 2.35), (LX[3] + 0.07, -0.55, 0.85)]
b = B()
for p in NODES:
    b.sphere(0.12, Vector(p) + Vector((0, 0, 0.02)), M["lime"], seg=18)
b.obj("ActivationNodes", parent=root)

# ---------------------------------------------------------------- trained model
TM = Vector((5.0, -0.15, 0.85))
b = B()
b.box((1.5, 1.5, 1.5), (0, 0, 0), M["glass"], bevel=0.14)
for (sx, sy, x, y) in ((1.2, 0.03, 0, -0.69), (1.2, 0.03, 0, 0.69), (0.03, 1.2, -0.69, 0), (0.03, 1.2, 0.69, 0)):
    b.box((sx, sy, 0.03), (x, y, 0.745), M["glassEdge"])  # polished top edges
tm = b.obj("TrainedModel", loc=TM + Vector((0, 0, 0.02)), parent=root)
b = B()
for ix in (-1, 0, 1):
    for iy in (-1, 0, 1):
        for iz in (-1, 0, 1):
            k = "modelCore" if (ix + iy + iz) % 2 == 0 else "cellB"
            b.box((0.34, 0.34, 0.34), (ix * 0.38, iy * 0.38, iz * 0.38), M[k], bevel=0.04, seg=2)
b.obj("TrainedModelCore", parent=tm)

# ---------------------------------------------------------------- charts (face the camera, no text)
tc = B()
W, H = 2.1, 1.55
tc.box((W, 0.06, H), (0, 0, 0), M["frost"], bevel=0.08)
tc.box((0.02, 0.02, H * 0.7), (-W * 0.38, -0.04, 0.0), M["chartAxis"])
tc.box((W * 0.78, 0.02, 0.02), (0.0, -0.04, -H * 0.35), M["chartAxis"])
for k, mname in enumerate(("chartBlue", "chartLime")):
    tc.box((0.08, 0.02, 0.08), (-W * 0.3 + k * 0.5, -0.04, -H * 0.43), M[mname])
tch = tc.obj("TrainingChart", loc=(3.55, 2.1, 4.35), parent=root, rot=(0, 0, FACE))


def curve_pts(f, x0, x1, n=40):
    return [Vector((x0 + (x1 - x0) * i / n, -0.05, f(i / n))) for i in range(n + 1)]


for name, f, mname in (("TrainingCurveA", lambda t: -0.32 + 0.82 * math.exp(-4.2 * t), "chartBlue"),
                       ("TrainingCurveB", lambda t: -0.27 + 0.62 * math.exp(-3.0 * t) + 0.03 * math.sin(t * 18), "chartLime")):
    b = B()
    b.tube(curve_pts(f, -W * 0.36, W * 0.38), 0.022, M[mname], sides=6)
    b.obj(name, parent=tch)

pc = B()
pc.box((1.25, 0.06, 1.45), (0, 0, 0), M["frost"], bevel=0.08)
pc.box((0.95, 0.02, 0.02), (0, -0.04, -0.5), M["chartAxis"])
pch = pc.obj("PredictionChart", loc=(6.45, 1.2, 1.85), parent=root, rot=(0, 0, FACE))
for k, (h, mname) in enumerate(((0.38, "chartBlue"), (0.55, "chartLime"), (0.48, "chartBlue"), (0.85, "chartBlue"), (0.66, "chartLime"))):
    b = B()
    b.box((0.13, 0.04, h), (0, 0, h / 2), M[mname], bevel=0.015, seg=1)
    b.obj(f"PredictionBar{k + 1:02d}", loc=(-0.38 + k * 0.19, -0.05, -0.49), parent=pch)

# ---------------------------------------------------------------- data paths
paths = []
targets = [(-0.5, 2.3), (0.2, 2.0), (-0.6, 1.4), (0.6, 1.2), (0.0, 0.8), (-0.3, 1.8), (0.5, 2.2), (-0.7, 0.9), (0.3, 1.6)]
for p, (ty, tz) in zip(input_pts, targets):
    end = Vector((PROC_IN, ty, tz))
    mid = Vector((-3.85, p.y * 0.5 + ty * 0.5, (p.z + tz) / 2 + 0.25))
    paths.append(spline([p, (p + mid) / 2 + Vector((0, 0, 0.15)), mid, end], 40))
for k, (y0, z0) in enumerate(((-0.45, 1.3), (0.2, 0.9), (0.45, 1.55))):
    ctrl = [Vector((PROC_OUT, y0, z0))]
    for j, x in enumerate(LX):
        n = [q for q in NODES if abs(q[0] - x - 0.07) < 0.01]
        q = Vector(n[(k + j) % len(n)])
        ctrl.append(Vector((x + 0.07, q.y * 0.55 + y0 * 0.45, q.z * 0.55 + z0 * 0.45)))
    ctrl += [Vector((3.9, -0.15 + (k - 1) * 0.2, 0.9 + (k - 1) * 0.12)), TM + Vector((-0.78, (k - 1) * 0.25, (k - 1) * 0.2))]
    paths.append(spline(ctrl, 60))
paths.append(spline([TM + Vector((0.6, 0.6, 0.3)), Vector((5.95, 1.0, 1.6)), Vector((6.3, 1.25, 1.75))], 24))
b = B()
for pts in paths:
    b.tube(pts, 0.016, M["path"], sides=6)
for a, c in zip(NODES, NODES[2:]):  # faint links between activation nodes in neighbouring layers
    b.tube(spline([a, (Vector(a) + Vector(c)) / 2 + Vector((0, 0, 0.12)), c], 16), 0.008, M["path"], sides=5)
b.cone(0.11, 0.26, Vector((4.05, -0.15, 0.9)), M["path"], rot=(0, math.pi / 2, 0))
dp = b.obj("DataPaths", parent=root)
dp["paths"] = json.dumps([[[round(v.x, 3), round(v.z, 3), round(-v.y, 3)] for v in pts[::2] + [pts[-1]]] for pts in paths[len(input_pts):]
                          ] + [[[round(v.x, 3), round(v.z, 3), round(-v.y, 3)] for v in pts[::2] + [pts[-1]]] for pts in paths[:len(input_pts)]])
dp["mainPathCount"] = len(paths) - len(input_pts)

# ---------------------------------------------------------------- camera + lights
cam_data = bpy.data.cameras.new("CardCamera")
cam_data.lens = 50
cam_data.sensor_width = 36
cam = bpy.data.objects.new("CardCamera", cam_data)
bpy.context.collection.objects.link(cam)
target = Vector((0.05, 0.1, 1.55))
cam.location = target + CAM_DIR * 25.5
cam.rotation_euler = (target - cam.location).to_track_quat("-Z", "Y").to_euler()
scene.camera = cam


def area(name, loc, size, energy, color=(1, 1, 1)):
    l = bpy.data.lights.new(name, "AREA")
    l.size = size
    l.energy = energy
    l.color = color
    o = bpy.data.objects.new(name, l)
    bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = (target - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    return o


area("KeyLight", (-6, -9, 12), 10, 1300, (1.0, 0.98, 0.96))
area("FillLight", (12, -6, 5), 8, 450, (0.85, 0.92, 1.0))
area("RimLight", (2, 10, 9), 8, 900, (0.8, 0.9, 1.0))

world = bpy.data.worlds.new("PaleStudio")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.86, 0.91, 1.0, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.45
scene.world = world

# ---------------------------------------------------------------- save + export
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "ai-ml-training-pipeline.blend"))
bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, "ai-ml-training-pipeline.glb"), export_format="GLB",
                          export_apply=True, export_extras=True, export_cameras=True, export_lights=False,
                          export_yup=True, use_selection=False)

if not args.no_render:
    r = scene.render
    r.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = args.samples
    scene.cycles.use_denoising = True
    scene.cycles.transparent_max_bounces = 32
    r.film_transparent = True
    r.resolution_x = args.res
    r.resolution_y = round(args.res * 9 / 16)
    r.image_settings.file_format = "PNG"
    r.image_settings.color_mode = "RGBA"
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    r.filepath = os.path.join(OUT, "preview.png")
    bpy.ops.render.render(write_still=True)
print("done", OUT)
