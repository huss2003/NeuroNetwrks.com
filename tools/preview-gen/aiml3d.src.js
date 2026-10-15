/* Live 3D model for the AI/ML Engineering program card.
   Source of tools/preview-gen/assets/aiml3d.js (bundle: see docs/3d/ai-ml-training-pipeline/README.md).
   Loaded by site.js with dynamic import() only when the card nears the viewport on capable desktops.
   The model and object names come from tools/blender/ai_ml_pipeline.py. */
import {
  WebGLRenderer, Scene, PerspectiveCamera, PMREMGenerator, NeutralToneMapping, SRGBColorSpace,
  HemisphereLight, DirectionalLight, Mesh, SphereGeometry, MeshBasicMaterial, AdditiveBlending, Vector3, Color, MathUtils,
} from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { MeshoptDecoder } from 'three/examples/jsm/libs/meshopt_decoder.module.js';

const ease = (t) => 1 - Math.pow(1 - t, 3);

export async function mount(box) {
  const card = box.closest('.pt') || box;
  const renderer = new WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 1.75));
  renderer.outputColorSpace = SRGBColorSpace;
  renderer.toneMapping = NeutralToneMapping;
  renderer.toneMappingExposure = 0.95;
  renderer.setClearColor(0x000000, 0);
  const cv = renderer.domElement;
  cv.setAttribute('aria-hidden', 'true');
  cv.className = 'pt-3d-cv';

  const scene = new Scene();
  const pm = new PMREMGenerator(renderer);
  scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.5;
  scene.add(new HemisphereLight(0xeaf3ff, 0x9fb8e0, 0.55));
  const key = new DirectionalLight(0xffffff, 1.3); key.position.set(-6, 12, 9); scene.add(key);
  const fill = new DirectionalLight(0xd8e8ff, 0.6); fill.position.set(12, 5, 6); scene.add(fill);

  const gltf = await new GLTFLoader().setMeshoptDecoder(MeshoptDecoder).loadAsync(box.dataset.glb);
  const root = gltf.scene.getObjectByName('ai-ml-training-pipeline') || gltf.scene;
  scene.add(gltf.scene);

  // Camera: reuse the Blender framing so the live model matches the static poster.
  const src = gltf.cameras[0];
  const camera = new PerspectiveCamera(src ? src.fov : 22, 16 / 9, 0.5, 200);
  if (src) { src.updateWorldMatrix(true, false); src.matrixWorld.decompose(camera.position, camera.quaternion, new Vector3()); }
  else { camera.position.set(12, 15, 22); camera.lookAt(0, 1.5, 0); }

  // Glass reads better with depth writes only on the denser parts.
  gltf.scene.traverse((o) => {
    if (!o.isMesh) return;
    for (const m of [].concat(o.material)) {
      if (m.transparent) { m.depthWrite = m.opacity > 0.75; m.side = 2; }
      if (m.metalness > 0.5) { m.metalness = 0.7; m.envMapIntensity = 2; } else m.envMapIntensity = 0.7; // satin metal stays light without a studio HDR
    }
  });

  const get = (n) => gltf.scene.getObjectByName(n);
  // 1. Assembly: components settle into place once.
  const parts = [];
  const add = (o, d, off, s) => { if (!o) return; parts.push({ o, d, p: o.position.clone(), off: new Vector3(...off), s: o.scale.clone(), s0: s }); };
  get('InputData')?.children.forEach((c, i) => add(c, i * 40, [-0.7, 0.15, 0], 0.7));
  add(get('ProcessorCore'), 120, [0, -0.35, 0], 0.92);
  ['FeatureLayer01', 'FeatureLayer02', 'FeatureLayer03', 'FeatureLayer04'].forEach((n, i) => add(get(n), 220 + i * 70, [0, 0.55, 0], 0.94));
  add(get('ActivationNodes'), 480, [0, 0.55, 0], 1);
  add(get('TrainedModel'), 420, [0.5, 0, 0], 0.85);
  const ASSEMBLE = 820;

  // 2. Data flow: a few slow pulses along the main paths.
  const dp = get('DataPaths');
  const raw = dp && dp.userData.paths ? JSON.parse(dp.userData.paths) : [];
  const main = raw.slice(0, dp ? dp.userData.mainPathCount || 3 : 0);
  const paths = [...main, raw[main.length], raw[main.length + 2]].filter(Boolean).map((pts) => {
    const v = pts.map((p) => new Vector3(...p)); const len = [0];
    for (let i = 1; i < v.length; i++) len.push(len[i - 1] + v[i].distanceTo(v[i - 1]));
    return { v, len, total: len[len.length - 1] };
  });
  const pulseGeo = new SphereGeometry(0.06, 12, 8), haloGeo = new SphereGeometry(0.16, 12, 8);
  const pulses = paths.map((path, i) => {
    const m = new Mesh(pulseGeo, new MeshBasicMaterial({ color: 0xe6fbff }));
    m.add(new Mesh(haloGeo, new MeshBasicMaterial({ color: 0x5cc8ff, transparent: true, opacity: 0.35, blending: AdditiveBlending, depthWrite: false })));
    root.add(m);
    return { m, path, period: 5200 + i * 650, phase: i * 1300 };
  });
  const at = (path, d, out) => {
    let i = 1; while (i < path.len.length - 1 && path.len[i] < d) i++;
    const k = (d - path.len[i - 1]) / Math.max(path.len[i] - path.len[i - 1], 1e-6);
    return out.copy(path.v[i - 1]).lerp(path.v[i], MathUtils.clamp(k, 0, 1));
  };

  // 3. Hover: lime nodes brighten, the model turns at most 2.5 degrees.
  const nodes = get('ActivationNodes');
  const limeMats = []; nodes?.traverse((o) => { if (o.isMesh) limeMats.push(...[].concat(o.material)); });
  const limeBase = limeMats.map((m) => m.emissiveIntensity || 1);
  const limeColor = new Color(0x9be15d);
  limeMats.forEach((m) => { if (m.emissive.getHex() === 0) m.emissive.copy(limeColor); });
  let hover = 0, hoverT = 0, px = 0, py = 0, rx = 0, ry = 0;
  card.addEventListener('pointerenter', () => { hoverT = 1; });
  card.addEventListener('pointerleave', () => { hoverT = 0; px = py = 0; });
  card.addEventListener('pointermove', (e) => { const r = box.getBoundingClientRect(); px = MathUtils.clamp((e.clientX - r.left) / r.width - 0.5, -0.5, 0.5); py = MathUtils.clamp((e.clientY - r.top) / r.height - 0.5, -0.5, 0.5); });
  const MAXR = MathUtils.degToRad(2.5);

  // 4. Charts: the training curves draw in, the prediction bars rise and settle.
  const curves = ['TrainingCurveA', 'TrainingCurveB'].map(get).filter(Boolean).map((o) => ({ g: o.geometry, n: o.geometry.index ? o.geometry.index.count : o.geometry.attributes.position.count }));
  const bars = [1, 2, 3, 4, 5].map((i) => get('PredictionBar0' + i)).filter(Boolean);
  const barY = bars.map((o) => o.scale.y); // meshopt quantization stores a scale on each node; animate relative to it

  // Size + visibility handling
  box.appendChild(cv);
  const size = () => { const w = box.clientWidth, h = box.clientHeight; if (!w || !h) return; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); };
  size();
  new ResizeObserver(size).observe(box);
  let visible = true, raf = 0, t0 = 0, last = 0, first = true;
  const tmp = new Vector3();

  function frame(now) {
    raf = 0;
    if (!t0) t0 = now;
    const t = now - t0, dt = Math.min(64, now - (last || now)); last = now;
    for (const p of parts) {
      const k = ease(MathUtils.clamp((t - p.d) / (ASSEMBLE - Math.min(p.d, 500)), 0, 1));
      p.o.position.copy(p.off).multiplyScalar(1 - k).add(p.p);
      p.o.scale.copy(p.s).multiplyScalar(p.s0 + (1 - p.s0) * k);
    }
    const flowOn = MathUtils.clamp((t - 900) / 600, 0, 1);
    for (const q of pulses) {
      const u = ((t + q.phase) % q.period) / q.period;
      at(q.path, u * q.path.total, tmp); q.m.position.copy(tmp);
      const fade = Math.sin(Math.PI * u) * flowOn; q.m.scale.setScalar(0.4 + 0.6 * fade); q.m.visible = fade > 0.02;
    }
    hover += (hoverT - hover) * Math.min(1, dt / 180);
    limeMats.forEach((m, i) => { m.emissiveIntensity = limeBase[i] * (1 + 3.2 * hover) + 0.25 * Math.sin(t / 900 + i) * hover; });
    rx += (py * MAXR * hover - rx) * Math.min(1, dt / 220);
    ry += (px * MAXR * 2 * hover - ry) * Math.min(1, dt / 220);
    root.rotation.set(rx, MathUtils.clamp(ry, -MAXR, MAXR), 0);
    const cyc = (t % 7000) / 7000, draw = ease(MathUtils.clamp(cyc / 0.4, 0, 1)) * (cyc > 0.94 ? (1 - cyc) / 0.06 : 1);
    curves.forEach((c, i) => c.g.setDrawRange(0, Math.floor(c.n * MathUtils.clamp(draw - i * 0.06, 0.02, 1) / 3) * 3));
    bars.forEach((b, i) => { b.scale.y = barY[i] * (0.86 + 0.14 * (0.5 + 0.5 * Math.sin(t / 1400 + i * 1.3))); });
    renderer.render(scene, camera);
    if (first) { first = false; box.classList.add('is-live'); }
    if (visible && !document.hidden) raf = requestAnimationFrame(frame);
  }
  const start = () => { if (!raf && visible && !document.hidden) { last = 0; raf = requestAnimationFrame(frame); } };
  new IntersectionObserver((es) => { visible = es[0].isIntersecting; if (visible) start(); else if (raf) { cancelAnimationFrame(raf); raf = 0; } }).observe(box);
  document.addEventListener('visibilitychange', start);
  start();
}
