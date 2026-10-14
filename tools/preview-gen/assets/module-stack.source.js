// Module Stack: 36 plates (3 years x 12 monthly modules) rising in a spiral, a green bead per plate (the monthly project).
// window.ModuleStack.mount(canvas, { n, still, interactive, lit, build, accent }) -> { setProgress(p), dispose() }
import {
  WebGLRenderer, Scene, PerspectiveCamera, Group, Mesh, SphereGeometry, ExtrudeGeometry, Shape, MeshPhysicalMaterial,
  MeshBasicMaterial, Color, EdgesGeometry, LineSegments, LineBasicMaterial, CanvasTexture, DoubleSide, PMREMGenerator, DirectionalLight, PlaneGeometry, ShadowMaterial, VSMShadowMap, ACESFilmicToneMapping,
} from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';

const BLUE = 0x006dee, GREEN = 0x49b716, B100 = 0xd9e8ff, B200 = 0xb3d0ff, INK = 0x0b1b33;
const ease = (t) => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * t)); // easeOutExpo

function sector(r0, r1, a) {
  const s = new Shape();
  s.absarc(0, 0, r1, -a, a, false);
  s.absarc(0, 0, r0, a, -a, true);
  s.closePath();
  return s;
}

function mount(canvas, opts = {}) {
  const N = opts.n || 36, still = !!opts.still;
  let progress = opts.lit ?? 1, built = opts.build ?? (still ? 1 : 0);
  const renderer = new WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: still });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, still ? 1 : 1.5));
  renderer.toneMapping = ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = VSMShadowMap;
  const scene = new Scene();
  const camera = new PerspectiveCamera(26, 1, 0.1, 100);
  const pm = new PMREMGenerator(renderer);
  scene.environment = pm.fromScene(new RoomEnvironment(), 0.03).texture; scene.environmentIntensity = 1.15;
  const key = new DirectionalLight(0xffffff, 2.2); key.position.set(-4, 9, 6); key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048); key.shadow.radius = 14; key.shadow.blurSamples = 20; key.shadow.bias = -0.0005;
  Object.assign(key.shadow.camera, { left: -5, right: 5, top: 7, bottom: -3, near: 1, far: 30 });
  scene.add(key);
  const fill = new DirectionalLight(0xdbe8ff, 0.8); fill.position.set(6, 3, -2); scene.add(fill);

  const sh = document.createElement('canvas'); sh.width = sh.height = 256;
  const sc2 = sh.getContext('2d'); const gr = sc2.createRadialGradient(128, 128, 0, 128, 128, 128);
  gr.addColorStop(0, 'rgba(11,27,51,0.26)'); gr.addColorStop(0.45, 'rgba(11,27,51,0.10)'); gr.addColorStop(1, 'rgba(11,27,51,0)');
  sc2.fillStyle = gr; sc2.fillRect(0, 0, 256, 256);
  const floor = new Mesh(new PlaneGeometry(6.4, 6.4), new MeshBasicMaterial({ map: new CanvasTexture(sh), transparent: true, depthWrite: false }));
  floor.rotation.x = -Math.PI / 2; floor.position.y = -0.03; if (!opts.noFloor) scene.add(floor);
  const rim = new DirectionalLight(0xb3d0ff, 1.6); rim.position.set(5, 4, -6); scene.add(rim);

  const group = new Group(); scene.add(group);
  const geo = new ExtrudeGeometry(sector(0.95, 2.05, 0.34), { depth: 0.09, bevelEnabled: true, bevelThickness: 0.025, bevelSize: 0.025, bevelSegments: 4, curveSegments: 28 });
  geo.rotateX(-Math.PI / 2); geo.translate(0, 0.04, 0);
  const beadGeo = new SphereGeometry(0.056, 32, 20);
  const inlayGeo = new ExtrudeGeometry(sector(1.02, 1.98, 0.3), { depth: 0.012, bevelEnabled: false, curveSegments: 28 }); inlayGeo.rotateX(-Math.PI / 2); inlayGeo.translate(0, 0.04 + 0.09 + 0.05, 0);
  const edgeGeo = new EdgesGeometry(geo, 35);
  const tints = [B200, 0x6aa8f5, 0x2a82f0];
  const plates = [];
  const dy = 4.6 / N, dth = (Math.PI * 3) / N;
  for (let i = 0; i < N; i++) {
    const yr = Math.min(2, Math.floor(i / (N / 3)));
    const cap = (i + 1) % (N / 3) === 0; // capstone month closes each year
    const mat = new MeshPhysicalMaterial(cap
      ? { color: BLUE, roughness: 0.32, metalness: 0, clearcoat: 0.7, clearcoatRoughness: 0.25 }
      : { color: tints[yr], roughness: 0.18, metalness: 0, transmission: 0.55, thickness: 0.35, ior: 1.45, clearcoat: 1, clearcoatRoughness: 0.12, attenuationColor: new Color(BLUE), attenuationDistance: 2.4, transparent: false });
    const m = new Mesh(geo, mat); m.castShadow = true; m.receiveShadow = true;
    const inlay = new Mesh(inlayGeo, new MeshPhysicalMaterial({ color: cap ? 0xd9e8ff : 0xffffff, roughness: 0.55, clearcoat: 0.3 })); m.add(inlay);
    m.add(new LineSegments(edgeGeo, new LineBasicMaterial({ color: BLUE, transparent: true, opacity: cap ? 0.0 : 0.5 })));
    const bead = new Mesh(beadGeo, new MeshPhysicalMaterial({ color: 0xffffff, roughness: 0.12, clearcoat: 1, clearcoatRoughness: 0.05, emissive: GREEN, emissiveIntensity: 0 }));
    bead.position.set(2.17, 0.08, 0); m.add(bead);
    const holder = new Group(); holder.add(m); group.add(holder);
    plates.push({ holder, m, bead, i, dy, dth });
  }
  const tilt = 0.18;
  group.position.y = -0.2;

  let px = 0, py = 0, tx = 0, ty = 0, spin = 0, raf = 0, last = performance.now(), visible = true, clock = 0;
  const place = () => {
    for (const p of plates) {
      const t = Math.max(0, Math.min(1, (built * (1 + N * 0.03) * 1.0 - p.i * 0.03) / 0.9));
      const e = ease(t);
      p.holder.position.y = p.i * p.dy + (1 - e) * 3;
      p.holder.rotation.y = -(p.i * p.dth) + (1 - e) * 0.7;
      p.holder.visible = t > 0;
      const lit = p.i / N < progress;
      p.bead.material.color.setHex(lit ? GREEN : 0xffffff); p.bead.material.emissiveIntensity = lit ? 0.35 : 0;
      const sc = lit ? 1.5 : 0.9; p.bead.scale.setScalar(sc);
    }
  };
  const resize = () => { const w = canvas.clientWidth || 800, h = canvas.clientHeight || 800; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); };
  const frame = (now) => {
    const dt = Math.min(0.05, (now - last) / 1000); last = now; clock += dt;
    if (!still) {
      if (opts.build === undefined && built < 1) built = Math.min(1, built + dt / 1.9);
      spin += dt * 0.12; px += (tx - px) * 0.05; py += (ty - py) * 0.05;
    }
    place();
    group.rotation.y = (opts.yaw ?? -0.55) + spin + px * 0.1 + (opts.cam ? 0 : progress * Math.PI * 0.6);
    group.rotation.x = tilt * 0 + py * 0.05;
    const span = 4.6;
    if (opts.cam) { camera.fov = opts.cam.fov || 26; camera.updateProjectionMatrix(); camera.position.set(opts.cam.x || 0, opts.cam.y, opts.cam.z); camera.lookAt(0, opts.cam.ty, 0); } else { const D = opts.dist || 12.8; camera.position.set(0, 3.0 + progress * 0.4, D); camera.lookAt(0, span / 2 + 0.15 - (opts.dy || 0), 0); }
    renderer.render(scene, camera);
    if (!still && visible) raf = requestAnimationFrame(frame);
  };
  resize(); window.addEventListener('resize', resize);
  const onMove = (e) => { const r = canvas.getBoundingClientRect(); tx = ((e.clientX - r.left) / r.width - 0.5) * 2; ty = ((e.clientY - r.top) / r.height - 0.5) * 2; };
  if (opts.interactive !== false && !still) window.addEventListener('pointermove', onMove, { passive: true });
  if (still) frame(performance.now());
  else {
    raf = requestAnimationFrame(frame);
    if ('IntersectionObserver' in window) new IntersectionObserver((e) => { visible = e[0].isIntersecting; if (visible && !raf) { last = performance.now(); raf = requestAnimationFrame(frame); } else if (!visible) { cancelAnimationFrame(raf); raf = 0; } }).observe(canvas);
  }
  return { setProgress(p) { progress = Math.max(0, Math.min(1, p)); }, dispose() { cancelAnimationFrame(raf); window.removeEventListener('resize', resize); window.removeEventListener('pointermove', onMove); renderer.dispose(); } };
}
window.ModuleStack = { mount };
window.NeuralLoom = { mount: (c, o = {}) => mount(c, { ...o, n: o.variant && o.variant !== 'hero' ? 12 : 36 }) };
