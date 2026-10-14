// The one 3D object: a glossy twisting ribbon (a stretched trefoil, flattened) with a blue-to-green
// vertex gradient. Not a brain, not a network, not particles. Imports only what it uses.
import {
  WebGLRenderer,
  Scene,
  PerspectiveCamera,
  TubeGeometry,
  Curve,
  Vector3,
  BufferAttribute,
  Mesh,
  MeshPhysicalMaterial,
  HemisphereLight,
  DirectionalLight,
  Color,
  PMREMGenerator,
  type BufferGeometry,
} from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';

class Trefoil extends Curve<Vector3> {
  constructor() {
    super();
  }
  getPoint(t: number, target = new Vector3()) {
    const a = t * Math.PI * 2;
    return target
      .set(Math.sin(a) + 2 * Math.sin(2 * a), Math.cos(a) - 2 * Math.cos(2 * a), -Math.sin(3 * a))
      .multiplyScalar(0.62);
  }
}

const cssColor = (name: string, fallback: number) => {
  const v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  return v ? new Color(v) : new Color(fallback);
};

/** Flatten a tube into a ribbon: scale each ring vertex along the curve normal and binormal. */
function ribbonGeometry(curve: Curve<Vector3>, segments: number, radial: number): BufferGeometry {
  const geo = new TubeGeometry(curve, segments, 1, radial, true);
  const frames = curve.computeFrenetFrames(segments, true);
  const pos = geo.getAttribute('position');
  const colors = new Float32Array(pos.count * 3);
  const blue = cssColor('--color-blue-600', 0x006dee);
  const green = cssColor('--color-green-600', 0x49b716);
  const c = new Color();
  const p = new Vector3();
  const v = new Vector3();
  const W = 0.5; // ribbon half width
  const T = 0.075; // ribbon half thickness
  for (let i = 0; i <= segments; i++) {
    const idx = i % segments;
    curve.getPointAt(i / segments, p);
    const n = frames.normals[idx];
    const b = frames.binormals[idx];
    // blue at the start, green half way round, back to blue: echoes the logo's two halves
    c.copy(blue).lerp(green, 0.5 - 0.5 * Math.cos((i / segments) * Math.PI * 2));
    for (let j = 0; j <= radial; j++) {
      const k = i * (radial + 1) + j;
      v.set(pos.getX(k), pos.getY(k), pos.getZ(k)).sub(p);
      const dn = v.dot(n) * W;
      const db = v.dot(b) * T;
      pos.setXYZ(
        k,
        p.x + n.x * dn + b.x * db,
        p.y + n.y * dn + b.y * db,
        p.z + n.z * dn + b.z * db,
      );
      colors.set([c.r, c.g, c.b], k * 3);
    }
  }
  geo.setAttribute('color', new BufferAttribute(colors, 3));
  geo.computeVertexNormals();
  return geo;
}

// Yield to the browser between heavy setup steps so no single task blocks input for long.
const nextFrame = () => new Promise<void>((r) => requestAnimationFrame(() => setTimeout(r, 0)));

export async function mountRibbon(host: HTMLElement) {
  const canvas = host.querySelector('canvas');
  const poster = host.querySelector<HTMLElement>('[data-ribbon-poster]');
  if (!canvas) return;

  const renderer = new WebGLRenderer({
    canvas,
    antialias: true,
    alpha: true,
    powerPreference: 'low-power',
  });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5));
  const scene = new Scene();
  const camera = new PerspectiveCamera(38, 1, 0.1, 50);
  camera.position.set(0, 0, 9.2);

  await nextFrame();
  const pmrem = new PMREMGenerator(renderer);
  const env = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environment = env;
  await nextFrame();
  scene.add(new HemisphereLight(0xffffff, cssColor('--color-blue-200', 0xb3d0ff).getHex(), 0.9));
  const key = new DirectionalLight(0xffffff, 1.4);
  key.position.set(3, 4, 5);
  scene.add(key);

  const geometry = ribbonGeometry(new Trefoil(), 320, 12);
  await nextFrame();
  const material = new MeshPhysicalMaterial({
    vertexColors: true,
    roughness: 0.28,
    metalness: 0,
    clearcoat: 1,
    clearcoatRoughness: 0.12,
    envMapIntensity: 0.9,
  });
  const mesh = new Mesh(geometry, material);
  scene.add(mesh);

  const resize = () => {
    const { clientWidth: w, clientHeight: h } = host;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  };
  resize();
  const ro = new ResizeObserver(resize);
  ro.observe(host);

  // Pointer parallax (tiny) and scroll-linked rotation.
  let px = 0;
  let py = 0;
  const onMove = (e: PointerEvent) => {
    px = (e.clientX / innerWidth - 0.5) * 2;
    py = (e.clientY / innerHeight - 0.5) * 2;
  };
  addEventListener('pointermove', onMove, { passive: true });

  let visible = true;
  let raf = 0;
  let slowFrames = 0;
  const frame = () => {
    raf = 0;
    if (!visible) return;
    const t0 = performance.now();
    const r = host.getBoundingClientRect();
    const progress =
      1 - Math.min(1, Math.max(0, (r.top + r.height / 2) / (innerHeight + r.height)));
    const t = performance.now() / 1000;
    mesh.rotation.y = progress * Math.PI * 1.2 + t * 0.08 + px * 0.12;
    mesh.rotation.x = 0.25 + py * 0.08;
    mesh.rotation.z = t * 0.03;
    renderer.render(scene, camera);
    // Adaptive guard: if frames keep costing more than 40 ms the device cannot keep up, so freeze on
    // the last frame (still a finished image) instead of fighting the main thread.
    slowFrames = performance.now() - t0 > 40 ? slowFrames + 1 : 0;
    if (slowFrames >= 4) return;
    raf = requestAnimationFrame(frame);
  };

  const io = new IntersectionObserver((entries) => {
    visible = entries.some((e) => e.isIntersecting);
    if (visible && !raf) raf = requestAnimationFrame(frame);
  });
  io.observe(host);

  // Show the canvas once the first frame is drawn, then retire the poster.
  renderer.render(scene, camera);
  host.dataset.ribbonReady = 'true';
  if (poster) poster.style.opacity = '0';

  const dispose = () => {
    cancelAnimationFrame(raf);
    io.disconnect();
    ro.disconnect();
    removeEventListener('pointermove', onMove);
    geometry.dispose();
    material.dispose();
    env.dispose();
    pmrem.dispose();
    renderer.dispose();
  };
  addEventListener('pagehide', dispose, { once: true });
  return dispose;
}
