"""NeuroNetworks 3D house style for Blender (bpy 5.1, headless).

Shared by every model script in tools/blender/. Gives one look across the site:
pale glass, satin metal, brand blue (#006DEE) and a little brand green (#49B716),
soft studio light, three-quarter camera, transparent background.

Usage in a model script:

    import nn_style as S
    S.start(seed=3)
    b = S.B(); b.box(...); b.obj("Name", parent=S.root("asset-name"))
    S.finish(args, name="asset-name", cam_dir=(0.55, -1, 0.62))

Blender is Z-up; the GLB export is Y-up (x, z, -y). Code on screens is abstract bars, never words.
"""
import argparse
import math
import os
import random
import sys

import bpy  # must come first: it registers bmesh and mathutils
import bmesh
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Matrix, Vector


def args(extra=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--samples", type=int, default=128)
    ap.add_argument("--res", type=int, default=2000)
    ap.add_argument("--aspect", type=float, default=1.0)
    ap.add_argument("--no-render", action="store_true")
    ap.add_argument("--no-glb", action="store_true")
    if extra:
        extra(ap)
    a = ap.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:])
    a.out = os.path.abspath(a.out)
    os.makedirs(a.out, exist_ok=True)
    return a


def start(seed=7):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    random.seed(seed)
    M.clear()
    _init_materials()


# ---------------------------------------------------------------- colour + materials
def srgb(h):
    """'#006DEE' -> linear RGB tuple."""
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c)


BLUE, GREEN, INK = srgb("#006DEE"), srgb("#49B716"), srgb("#0B1B33")
M = {}


def mat(name, color, alpha=1.0, rough=0.3, metal=0.0, emit=None, emit_str=0.0, coat=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    b.inputs["Alpha"].default_value = alpha
    b.inputs["Coat Weight"].default_value = coat
    if emit:
        b.inputs["Emission Color"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = emit_str
    if alpha < 1:
        m.surface_render_method = "BLENDED"
        m.use_backface_culling = False
    return m


def _init_materials():
    M.update({
        "glass": mat("GlassBlue", (0.3, 0.56, 1.0), alpha=0.3, rough=0.06, coat=0.4),
        "glassEdge": mat("GlassEdge", (0.62, 0.86, 1.0), alpha=0.7, rough=0.05, emit=(0.55, 0.85, 1.0), emit_str=0.6, coat=0.6),
        "frost": mat("FrostedPanel", (0.86, 0.92, 1.0), alpha=0.75, rough=0.35, coat=0.3),
        "white": mat("SatinWhite", (0.86, 0.9, 0.96), rough=0.32, coat=0.5),
        "base": mat("PlatformFrost", (0.8, 0.88, 1.0), alpha=0.92, rough=0.3, coat=0.4),
        "rim": mat("PlatformRim", (0.55, 0.82, 1.0), alpha=0.85, emit=(0.4, 0.75, 1.0), emit_str=1.2),
        "metal": mat("SatinMetal", (0.8, 0.85, 0.92), metal=1.0, rough=0.32),
        "metalBlue": mat("SatinBlue", (0.32, 0.5, 0.82), metal=1.0, rough=0.35),
        "blue": mat("BrandBlue", BLUE, rough=0.25, coat=0.7, emit=BLUE, emit_str=0.15),
        "blueGlass": mat("BlueGlass", (0.08, 0.36, 1.0), alpha=0.7, rough=0.08, emit=(0.05, 0.3, 1.0), emit_str=0.6, coat=0.6),
        "deep": mat("DeepBlue", (0.03, 0.12, 0.42), rough=0.3, coat=0.6),
        "dark": mat("ScreenDark", (0.03, 0.06, 0.13), rough=0.35, coat=0.5),
        "green": mat("BrandGreen", GREEN, rough=0.3, coat=0.6, emit=GREEN, emit_str=0.25),
        "lime": mat("ActivationLime", (0.5, 0.88, 0.12), emit=(0.5, 0.9, 0.1), emit_str=0.5, rough=0.25, coat=0.8),
        "path": mat("DataPath", (0.45, 0.88, 1.0), alpha=0.9, emit=(0.2, 0.75, 1.0), emit_str=1.1, rough=0.2),
        "code": mat("CodeBar", (0.35, 0.65, 1.0), emit=(0.25, 0.6, 1.0), emit_str=0.9, rough=0.3),
        "codePale": mat("CodeBarPale", (0.6, 0.78, 1.0), emit=(0.5, 0.72, 1.0), emit_str=0.5, rough=0.3),
        "codeGreen": mat("CodeBarGreen", (0.45, 0.85, 0.3), emit=(0.4, 0.85, 0.2), emit_str=0.6, rough=0.3),
        "ink": mat("InkBar", (0.2, 0.3, 0.48), rough=0.4),
        "inkPale": mat("InkBarPale", (0.6, 0.68, 0.8), rough=0.4),
        "amber": mat("AlertAmber", (1.0, 0.55, 0.08), emit=(1.0, 0.5, 0.05), emit_str=0.8, rough=0.3),
        "red": mat("AlertRed", (0.85, 0.12, 0.12), emit=(0.9, 0.1, 0.1), emit_str=0.6, rough=0.3),
        "cellA": mat("CellDeep", (0.06, 0.3, 0.98), alpha=0.88, emit=(0.1, 0.35, 1.0), emit_str=0.5, rough=0.15),
        "cellB": mat("CellMid", (0.22, 0.5, 1.0), alpha=0.7, emit=(0.3, 0.6, 1.0), emit_str=0.3, rough=0.15),
        "cellC": mat("CellPale", (0.5, 0.72, 1.0), alpha=0.5, rough=0.2),
        "cellT": mat("CellTeal", (0.25, 0.78, 0.8), alpha=0.65, emit=(0.3, 0.85, 0.85), emit_str=0.3, rough=0.15),
    })


# ---------------------------------------------------------------- geometry builder
def euler(rot):
    """Euler XYZ tuple -> 4x4 matrix. A Matrix passes through (use it for compound local rotations)."""
    if isinstance(rot, Matrix):
        return rot.to_4x4()
    if not any(rot):
        return Matrix.Identity(4)
    return Matrix.Rotation(rot[2], 4, "Z") @ Matrix.Rotation(rot[1], 4, "Y") @ Matrix.Rotation(rot[0], 4, "X")


class B:
    """Accumulates primitives into one bmesh with per-face material slots."""

    def __init__(self):
        self.bm = bmesh.new()
        self.mats = []

    def _slot(self, m):
        if m not in self.mats:
            self.mats.append(m)
        return self.mats.index(m)

    def _merge(self, tmp, m, mtx):
        bmesh.ops.transform(tmp, matrix=mtx, verts=tmp.verts)
        me = bpy.data.meshes.new("tmp")
        tmp.to_mesh(me)
        tmp.free()
        n0 = len(self.bm.verts)
        self.bm.from_mesh(me)
        bpy.data.meshes.remove(me)
        self.bm.verts.ensure_lookup_table()
        idx = self._slot(m)
        for f in {f for v in self.bm.verts[n0:] for f in v.link_faces}:
            f.material_index = idx

    def box(self, size, loc, m, bevel=0.0, rot=(0, 0, 0), seg=3):
        tmp = bmesh.new()
        bmesh.ops.create_cube(tmp, size=1.0)
        bmesh.ops.scale(tmp, vec=Vector(size), verts=tmp.verts)
        if bevel > 0:
            bmesh.ops.bevel(tmp, geom=list(tmp.edges), offset=min(bevel, min(size) * 0.49), segments=seg,
                            profile=0.5, affect="EDGES", clamp_overlap=True)
        self._merge(tmp, m, Matrix.Translation(Vector(loc)) @ euler(rot))

    def cyl(self, r, depth, loc, m, rot=(0, 0, 0), seg=32, r2=None, bevel=0.0):
        tmp = bmesh.new()
        bmesh.ops.create_cone(tmp, cap_ends=True, segments=seg, radius1=r, radius2=r if r2 is None else r2, depth=depth)
        if bevel > 0:
            rim = [e for e in tmp.edges if len(e.link_faces) == 2 and abs(e.link_faces[0].normal.z) > 0.9 or
                   len(e.link_faces) == 2 and abs(e.link_faces[1].normal.z) > 0.9]
            bmesh.ops.bevel(tmp, geom=rim, offset=bevel, segments=3, profile=0.5, affect="EDGES", clamp_overlap=True)
        self._merge(tmp, m, Matrix.Translation(Vector(loc)) @ euler(rot))

    def sphere(self, r, loc, m, seg=20):
        tmp = bmesh.new()
        bmesh.ops.create_uvsphere(tmp, u_segments=seg, v_segments=seg // 2 + 2, radius=r)
        self._merge(tmp, m, Matrix.Translation(Vector(loc)))

    def cone(self, r, depth, loc, m, rot=(0, 0, 0), seg=16):
        tmp = bmesh.new()
        bmesh.ops.create_cone(tmp, cap_ends=True, segments=seg, radius1=r, radius2=0.0, depth=depth)
        self._merge(tmp, m, Matrix.Translation(Vector(loc)) @ euler(rot))

    def prism(self, pts, thick, m, mtx=None):
        """Extrude a 2D outline (x, z) in local XZ by `thick` along -Y (towards a front-facing viewer)."""
        tmp = bmesh.new()
        vs = [tmp.verts.new(Vector((p[0], 0, p[1]))) for p in pts]
        f = tmp.faces.new(vs)
        r = bmesh.ops.extrude_face_region(tmp, geom=[f])
        bmesh.ops.translate(tmp, vec=Vector((0, -thick, 0)), verts=[g for g in r["geom"] if isinstance(g, bmesh.types.BMVert)])
        bmesh.ops.recalc_face_normals(tmp, faces=tmp.faces)
        self._merge(tmp, m, mtx or Matrix.Identity(4))

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

    def obj(self, name, loc=(0, 0, 0), parent=None, rot=(0, 0, 0), smooth_below=0.02):
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
        for p in me.polygons:  # small faces belong to curved bevels: shade them smooth
            p.use_smooth = p.area < smooth_below
        return o


def empty(name, parent=None, loc=(0, 0, 0), rot=(0, 0, 0)):
    o = bpy.data.objects.new(name, None)
    o.empty_display_size = 0.3
    bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = rot
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


def ortho(ctrl, r=0.15):
    """Rounded orthogonal route through corner points (cable-tray style), as a dense polyline."""
    P = [Vector(c) for c in ctrl]
    out = [P[0]]
    for a, c, d in zip(P, P[1:], P[2:]):
        u, v = (c - a).normalized(), (d - c).normalized()
        rr = min(r, (c - a).length / 2, (d - c).length / 2)
        p0, p1 = c - u * rr, c + v * rr
        out.append(p0)
        for k in range(1, 6):
            t = k / 6
            out.append((1 - t) ** 2 * p0 + 2 * (1 - t) * t * c + t * t * p1)
        out.append(p1)
    out.append(P[-1])
    dense = []
    for a, c in zip(out, out[1:]):
        n = max(1, int((c - a).length / 0.08))
        dense += [a.lerp(c, i / n) for i in range(n)]
    return dense + [out[-1]]


# ---------------------------------------------------------------- reusable parts
def code_lines(b, w, h, rows, mtx, mats=("code", "codePale", "inkPale"), indent_seed=None, bar_h=None, y=-0.012):
    """Abstract code: rows of rounded bars with indents, lying on a screen in local XZ facing -Y."""
    rnd = random.Random(indent_seed)
    gap = h / rows
    bh = bar_h or gap * 0.42
    for r in range(rows):
        z = h / 2 - gap * (r + 0.5)
        x = -w / 2 + (rnd.choice((0, 0, 1, 1, 2)) * w * 0.07)
        for k in range(rnd.choice((1, 1, 2, 2, 3))):
            ln = w * rnd.uniform(0.12, 0.38)
            if x + ln > w / 2:
                break
            b.box((ln, 0.012, bh), mtx @ Vector((x + ln / 2, y, z)), M[rnd.choice(mats)], bevel=bh * 0.45, rot=mtx.to_3x3().to_4x4(), seg=2)
            x += ln + w * 0.03


def window(b, w, h, mtx, body="frost", screen="white", dark=False, header=True, depth=0.06, r=0.06):
    """A rounded app window: frame + inset screen + header dots. Returns (inner_w, inner_h, inner_mtx)."""
    e = mtx.to_3x3().to_4x4()
    b.box((w, depth, h), mtx @ Vector((0, 0, 0)), M[body], bevel=r, rot=e)
    hh = 0.09 * h if header else 0
    iw, ih = w * 0.92, h - hh - w * 0.08
    b.box((iw, 0.012, ih), mtx @ Vector((0, -depth / 2 - 0.004, -hh / 2)), M["dark" if dark else screen], bevel=min(r * 0.5, 0.02), rot=e, seg=2)
    if header:
        for k, mm in enumerate(("red", "amber", "green")):
            b.cyl(hh * 0.22, 0.012, mtx @ Vector((-w / 2 + w * 0.06 + k * hh * 0.6, -depth / 2 - 0.006, h / 2 - hh * 0.6)), M[mm],
                  rot=(mtx.to_3x3() @ Matrix.Rotation(math.pi / 2, 3, "X")).to_4x4(), seg=16)
    return iw, ih, mtx @ Matrix.Translation((0, -depth / 2 - 0.012, -hh / 2))


def glyph_image(b, w, mtx, m="codePale"):
    """Abstract 'image' glyph (frame, mountain, sun)."""
    e = mtx.to_3x3().to_4x4()
    t = 0.012
    for (sx, sz, x, z) in ((w, t * 2, 0, w / 2), (w, t * 2, 0, -w / 2), (t * 2, w, -w / 2, 0), (t * 2, w, w / 2, 0)):
        b.box((sx, t, sz), mtx @ Vector((x, 0, z)), M[m], rot=e)
    b.prism([(-w * 0.42, -w * 0.38), (-w * 0.05, w * 0.12), (w * 0.15, -w * 0.12), (w * 0.27, 0.0), (w * 0.42, -w * 0.38)], t, M[m], mtx)
    b.sphere(w * 0.08, mtx @ Vector((w * 0.22, 0, w * 0.24)), M[m], seg=10)


def check_mark(b, s, mtx, m="green", thick=0.04):
    """Tick glyph in the local XZ plane of `mtx`, facing -Y."""
    r3 = mtx.to_3x3()
    for (ln, x, z, ang) in ((0.42, -0.2, -0.04, 45), (0.8, 0.18, 0.11, -52)):
        rot = (r3 @ Matrix.Rotation(math.radians(ang), 3, "Y")).to_4x4()
        b.box((s * ln, thick, s * 0.13), mtx @ Vector((s * x, 0, s * z)), M[m], bevel=s * 0.05, rot=rot, seg=2)


def database(b, r, h, loc, discs=3, body="blueGlass", band="glassEdge"):
    """Stacked-disc database cylinder."""
    loc = Vector(loc)
    dh = h / discs
    for k in range(discs):
        b.cyl(r, dh * 0.86, loc + Vector((0, 0, -h / 2 + dh * (k + 0.5))), M[body], seg=40, bevel=r * 0.08)
        b.cyl(r * 1.015, dh * 0.08, loc + Vector((0, 0, -h / 2 + dh * (k + 1) - dh * 0.04)), M[band], seg=40)


def platform(name, size, loc=(0, 0, 0), parent=None, rim=True, m="base", h=0.28):
    b = B()
    sx, sy = size
    b.box((sx, sy, h), (0, 0, -h / 2), M[m], bevel=min(0.12, h * 0.45))
    if rim:
        b.box((sx - 0.2, 0.04, 0.05), (0, -sy / 2 + 0.01, -h * 0.22), M["rim"], bevel=0.015)
        b.box((0.04, sy - 0.2, 0.05), (sx / 2 - 0.01, 0, -h * 0.22), M["rim"], bevel=0.015)
    return b.obj(name, loc=loc, parent=parent)


# ---------------------------------------------------------------- scene, camera, export, render
def facing(cam_dir):
    """Z rotation that turns a -Y-facing panel towards the camera azimuth."""
    d = Vector(cam_dir).normalized()
    return math.atan2(d.x, -d.y)


def mesh_bbox_points():
    pts = []
    for o in bpy.context.scene.objects:
        if o.type == "MESH":
            pts += [o.matrix_world @ Vector(c) for c in o.bound_box]
    return pts


def fit_camera(cam_dir, aspect, margin=0.06, lens=50, target=None, shift=(0.0, 0.0)):
    """Place a camera along cam_dir so every mesh fits the frame with `margin` (fraction) on all sides."""
    scene = bpy.context.scene
    bpy.context.view_layer.update()
    pts = mesh_bbox_points()
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    tgt = Vector(target) if target else (lo + hi) / 2
    cd = bpy.data.cameras.new("CardCamera")
    cd.lens, cd.sensor_width, cd.sensor_fit = lens, 36, "HORIZONTAL" if aspect >= 1 else "VERTICAL"
    if aspect < 1:
        cd.sensor_height = 36
    cd.shift_x, cd.shift_y = shift
    cam = bpy.data.objects.new("CardCamera", cd)
    scene.collection.objects.link(cam)
    scene.camera = cam
    scene.render.resolution_x, scene.render.resolution_y = 1000, max(1, round(1000 / aspect))
    d = Vector(cam_dir).normalized()

    def fits(dist):
        cam.location = tgt + d * dist
        cam.rotation_euler = (tgt - cam.location).to_track_quat("-Z", "Y").to_euler()
        bpy.context.view_layer.update()
        for p in pts:
            v = world_to_camera_view(scene, cam, p)
            if v.z <= 0 or not (margin <= v.x <= 1 - margin and margin <= v.y <= 1 - margin):
                return False
        return True

    for _ in range(3):  # fit distance, then centre the projected bounds with lens shift, and refit
        lo_d, hi_d = 1.0, 400.0
        for _ in range(40):
            mid = (lo_d + hi_d) / 2
            lo_d, hi_d = (lo_d, mid) if fits(mid) else (mid, hi_d)
        fits(hi_d)
        vs = [world_to_camera_view(scene, cam, p) for p in pts]
        cx = (min(v.x for v in vs) + max(v.x for v in vs)) / 2 - 0.5
        cy = (min(v.y for v in vs) + max(v.y for v in vs)) / 2 - 0.5
        if aspect >= 1:
            cd.shift_x += cx
            cd.shift_y += cy / aspect
        else:
            cd.shift_x += cx * aspect
            cd.shift_y += cy
    return cam


def studio(key=1300, fill=450, rim=900, world=0.45, target=(0, 0, 1)):
    t = Vector(target)

    def area(name, loc, size, energy, color):
        l = bpy.data.lights.new(name, "AREA")
        l.size, l.energy, l.color = size, energy, color
        o = bpy.data.objects.new(name, l)
        bpy.context.scene.collection.objects.link(o)
        o.location = loc
        o.rotation_euler = (t - Vector(loc)).to_track_quat("-Z", "Y").to_euler()

    area("KeyLight", t + Vector((-6, -9, 12)), 10, key, (1.0, 0.98, 0.96))
    area("FillLight", t + Vector((12, -6, 5)), 8, fill, (0.85, 0.92, 1.0))
    area("RimLight", t + Vector((2, 10, 9)), 8, rim, (0.8, 0.9, 1.0))
    w = bpy.data.worlds.new("PaleStudio")
    w.use_nodes = True
    w.node_tree.nodes["Background"].inputs[0].default_value = (0.86, 0.91, 1.0, 1)
    w.node_tree.nodes["Background"].inputs[1].default_value = world
    bpy.context.scene.world = w


def finish(a, name, cam_dir=(0.55, -1.0, 0.62), margin=0.05, lens=50, target=None, light=None, transparent=True, exposure=0.0,
           post_shift=(0.0, 0.0), world_color=None):
    scene = bpy.context.scene
    cam = fit_camera(cam_dir, a.aspect, margin=margin, lens=lens, target=target)
    cam.data.shift_x += post_shift[0]
    cam.data.shift_y += post_shift[1]
    studio(**(light or {}))
    if world_color:
        scene.world.node_tree.nodes["Background"].inputs[0].default_value = (*world_color, 1)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(a.out, f"{name}.blend"))
    if not a.no_glb:
        bpy.ops.export_scene.gltf(filepath=os.path.join(a.out, f"{name}.glb"), export_format="GLB", export_apply=True,
                                  export_extras=True, export_cameras=True, export_lights=False, export_yup=True)
    if a.no_render:
        return
    r = scene.render
    r.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = a.samples
    scene.cycles.use_denoising = True
    scene.cycles.transparent_max_bounces = 32
    r.film_transparent = transparent
    r.resolution_x = a.res if a.aspect >= 1 else round(a.res * a.aspect)
    r.resolution_y = round(a.res / a.aspect) if a.aspect >= 1 else a.res
    r.image_settings.file_format = "PNG"
    r.image_settings.color_mode = "RGBA" if transparent else "RGB"
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = exposure
    r.filepath = os.path.join(a.out, "preview.png")
    bpy.ops.render.render(write_still=True)
    print("rendered", r.filepath)
