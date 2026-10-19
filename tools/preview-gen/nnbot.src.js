/* NN-Bot: the walking site companion. Source of tools/preview-gen/assets/nnbot.js (bundled with aiml3d.js; shared three chunk).
   site.js imports this on idle, only on capable desktops/tablets without reduced motion, and only if the visitor hasn't hidden it.
   Model + clips (Idle, Walk, Wave, Jump, LookAround) come from tools/blender/nn_bot.py. */
import {
  WebGLRenderer, Scene, PerspectiveCamera, PMREMGenerator, NeutralToneMapping, SRGBColorSpace, HemisphereLight, DirectionalLight,
  AnimationMixer, LoopOnce, LoopRepeat, Mesh, PlaneGeometry, MeshBasicMaterial, CanvasTexture, Vector3, MathUtils, Quaternion, Euler,
} from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { MeshoptDecoder } from 'three/examples/jsm/libs/meshopt_decoder.module.js';

const STRIP = 210;        // px height of the walking strip
const BOT_PX = 150;       // on-screen robot height in px
const BOT_H = 1.68;       // robot height in model units (feet to antenna tip)
const SPEED = 0.7;        // model units per second; matches the 1 s walk cycle's stride, so feet don't slide
const store = { get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }, set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private mode */ } } };

export async function mount({ glb, links }) {
  const root = document.createElement('div');
  root.className = 'nnbot';
  root.innerHTML = `<canvas class="nnbot-cv" aria-hidden="true"></canvas>
<button type="button" class="nnbot-hit" aria-label="NN-Bot, the Neuronetworks robot. Press to say hello." aria-expanded="false" aria-controls="nnbot-bubble"></button>
<div class="nnbot-bubble" id="nnbot-bubble" role="dialog" aria-label="NN-Bot" hidden><p>Hi! I'm NN-Bot. Where to next?</p>
<a href="${links.programs}">Explore programs</a><a href="${links.talk}">Talk to us</a></div>
<button type="button" class="nnbot-hide" aria-label="Hide the robot">×</button>`;
  document.body.appendChild(root);
  const cv = root.querySelector('.nnbot-cv'), hit = root.querySelector('.nnbot-hit'), bubble = root.querySelector('.nnbot-bubble'), hideBtn = root.querySelector('.nnbot-hide');

  const renderer = new WebGLRenderer({ canvas: cv, antialias: true, alpha: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 1.5));
  renderer.outputColorSpace = SRGBColorSpace;
  renderer.toneMapping = NeutralToneMapping;
  renderer.setClearColor(0x000000, 0);
  const scene = new Scene();
  scene.environment = new PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.6;
  scene.add(new HemisphereLight(0xf0f6ff, 0xa9bfe6, 0.9));
  const key = new DirectionalLight(0xffffff, 1.5); key.position.set(-3, 6, 5); scene.add(key);

  const camera = new PerspectiveCamera(20, 1, 0.1, 100);
  const visH = BOT_H * STRIP / BOT_PX;                       // world units visible vertically
  const dist = visH / 2 / Math.tan(MathUtils.degToRad(10));
  camera.position.set(0, visH / 2 - 0.05, dist);
  camera.lookAt(0, visH / 2 - 0.05, 0);
  let halfW = 4;
  const size = () => { const w = innerWidth; renderer.setSize(w, STRIP, false); cv.style.width = w + 'px'; cv.style.height = STRIP + 'px'; camera.aspect = w / STRIP; camera.updateProjectionMatrix(); halfW = visH * camera.aspect / 2; };
  size(); addEventListener('resize', size);
  const pxPerUnit = () => STRIP / visH;

  const gltf = await new GLTFLoader().setMeshoptDecoder(MeshoptDecoder).loadAsync(glb);
  const bot = gltf.scene;
  scene.add(bot);
  const shadowTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const g = c.getContext('2d'); const r = g.createRadialGradient(32, 32, 2, 32, 32, 32); r.addColorStop(0, 'rgba(10,40,100,.35)'); r.addColorStop(1, 'rgba(10,40,100,0)'); g.fillStyle = r; g.fillRect(0, 0, 64, 64); return new CanvasTexture(c); })();
  const shadow = new Mesh(new PlaneGeometry(0.9, 0.5), new MeshBasicMaterial({ map: shadowTex, transparent: true, depthWrite: false }));
  shadow.rotation.x = -Math.PI / 2; shadow.position.y = 0.005; scene.add(shadow);

  const mixer = new AnimationMixer(bot);
  const A = {}; gltf.animations.forEach((c) => { A[c.name] = mixer.clipAction(c); });
  ['Wave', 'Jump', 'LookAround'].forEach((n) => { if (A[n]) { A[n].setLoop(LoopOnce, 1); A[n].clampWhenFinished = false; } });
  let current = null;
  const play = (name, fade = 0.25) => {
    const next = A[name]; if (!next || next === current) return;
    next.reset().setEffectiveWeight(1).play();
    if (current) current.crossFadeTo(next, fade, false);
    current = next;
  };
  play('Idle');
  const head = bot.getObjectByName('head'), eyes = bot.getObjectByName('Eyes');
  const eyesY = eyes ? eyes.scale.y : 1;

  // ---- behaviour state
  const s = { x: (Math.random() * 0.6 - 0.3) * halfW, target: 0, mode: 'idle', until: performance.now() + 1500, face: 0, yaw: 0, spin: 0, spinV: 0, tilt: 0, busy: false, lookX: 0, lookY: 0, hover: false, blinkAt: performance.now() + 2500 };
  const avoid = () => { const c = document.querySelector('.consent:not([hidden])'); if (!c || c.offsetParent === null) return null; const r = c.getBoundingClientRect(); return [(r.left - innerWidth / 2) / pxPerUnit() - 0.6, (r.right - innerWidth / 2) / pxPerUnit() + 0.6]; };
  const pickTarget = () => {
    const m = 0.8; let t;
    for (let i = 0; i < 8; i++) { t = (Math.random() * 2 - 1) * (halfW - m); const z = avoid(); if (!z || t < z[0] || t > z[1]) break; }
    return t;
  };
  const finished = new Set();
  mixer.addEventListener('finished', (e) => { finished.add(e.action.getClip().name); });

  function setMode(mode, ms) { s.mode = mode; s.until = performance.now() + (ms || 0); }
  function stopAndFace() { setMode('attend', 0); s.face = 0; play('Idle', 0.2); }
  function wave() {
    stopAndFace(); s.busy = true; finished.delete('Wave'); play('Wave', 0.15);
    bubble.hidden = false; hit.setAttribute('aria-expanded', 'true');
  }
  function jump() { stopAndFace(); s.busy = true; finished.delete('Jump'); play('Jump', 0.08); }
  function closeBubble() { bubble.hidden = true; hit.setAttribute('aria-expanded', 'false'); setMode('idle', 1200); }

  // ---- interaction (only the robot's hit area takes pointer events)
  let clickT = 0, drag = null;
  hit.addEventListener('pointerdown', (e) => { drag = { x: e.clientX, y: e.clientY, moved: 0, t: performance.now() }; hit.setPointerCapture(e.pointerId); });
  hit.addEventListener('pointermove', (e) => {
    const r = hit.getBoundingClientRect();
    s.lookX = MathUtils.clamp((e.clientX - (r.left + r.width / 2)) / 200, -1, 1); s.lookY = MathUtils.clamp((e.clientY - r.top) / 200 - 0.3, -1, 1);
    if (!drag) return;
    const dx = e.clientX - drag.x, dy = e.clientY - drag.y; drag.moved += Math.abs(dx) + Math.abs(dy);
    s.spinV = dx * 0.012; s.spin += dx * 0.012; s.tilt = MathUtils.clamp(s.tilt + dy * 0.004, -0.25, 0.25);
    drag.x = e.clientX; drag.y = e.clientY;
    if (drag.moved > 6 && s.mode === 'walk') { setMode('held', 0); play('Idle', 0.2); }
  });
  hit.addEventListener('pointerup', () => {
    const d = drag; drag = null; if (!d) return;
    if (d.moved > 6) { setMode('idle', 1800); return; }
    const now = performance.now();
    if (now - clickT < 320) { clearTimeout(hit._t); clickT = 0; jump(); return; }
    clickT = now; hit._t = setTimeout(() => { bubble.hidden ? wave() : closeBubble(); }, 260);
  });
  hit.addEventListener('pointerenter', () => { s.hover = true; hideBtn.classList.add('on'); });
  hit.addEventListener('pointerleave', () => { s.hover = false; setTimeout(() => { if (!s.hover && !hideBtn.matches(':hover,:focus')) hideBtn.classList.remove('on'); }, 900); });
  hit.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); bubble.hidden ? wave() : closeBubble(); if (!bubble.hidden) setTimeout(() => bubble.querySelector('a').focus(), 50); } });
  hit.addEventListener('focus', () => hideBtn.classList.add('on'));
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && !bubble.hidden) { closeBubble(); hit.focus(); } });
  document.addEventListener('pointerdown', (e) => { if (!bubble.hidden && !root.contains(e.target)) closeBubble(); });
  hideBtn.addEventListener('click', () => { store.set('nnbot', 'off'); root.remove(); running = false; document.dispatchEvent(new CustomEvent('nnbot:hidden')); });

  // ---- loop (~30 fps, paused when the tab is hidden)
  let last = performance.now(), acc = 0, running = true;
  const q = new Quaternion(), eul = new Euler(), proj = new Vector3();
  function frame(now) {
    if (!running) return;
    requestAnimationFrame(frame);
    if (document.hidden) { last = now; return; }
    acc += now - last; last = now;
    if (acc < 33) return;
    const dt = Math.min(acc, 100) / 1000; acc = 0;

    // state machine
    if (s.mode === 'idle' && now > s.until) {
      if (Math.random() < 0.3) { setMode('look', 2600); finished.delete('LookAround'); play('LookAround', 0.3); }
      else { s.target = pickTarget(); setMode('walk'); play('Walk', 0.25); }
    } else if (s.mode === 'look' && (finished.has('LookAround') || now > s.until)) { play('Idle'); setMode('idle', 1500 + Math.random() * 3000); }
    else if (s.mode === 'walk') {
      const dir = Math.sign(s.target - s.x);
      s.face = dir > 0 ? Math.PI / 2 : -Math.PI / 2;
      const turned = Math.abs(s.yaw - s.face) < 0.35;
      if (turned) s.x += dir * SPEED * dt;
      const z = avoid(); if (z && s.x > z[0] && s.x < z[1] && Math.sign(s.target - s.x) === dir && s.target > z[0] && s.target < z[1]) s.target = pickTarget();
      if (Math.abs(s.target - s.x) < 0.05 || Math.abs(s.x) > halfW - 0.4) { s.x = MathUtils.clamp(s.x, -halfW + 0.4, halfW - 0.4); s.face = 0; play('Idle', 0.3); setMode('idle', 2000 + Math.random() * 4000); }
    } else if (s.mode === 'attend' && s.busy && (finished.has('Wave') || finished.has('Jump'))) { s.busy = false; play('Idle', 0.25); if (bubble.hidden) setMode('idle', 1500); }
    else if (s.mode === 'held' && !drag) setMode('idle', 1500);

    // turning + drag spin with inertia (spin decays back to the walking direction)
    s.yaw += (s.face - s.yaw) * Math.min(1, dt * 6);
    if (!drag) { s.spin += s.spinV; s.spinV *= 0.9; s.spin *= 0.94; s.tilt *= 0.92; }
    bot.position.set(s.x, 0, 0); shadow.position.x = s.x;
    bot.rotation.set(s.tilt, s.yaw + s.spin, 0);

    mixer.update(dt);
    // head follows the pointer while hovered (additive on top of the clip)
    if (head && (s.hover || s.mode === 'attend')) {
      eul.set(-s.lookY * 0.25, s.lookX * 0.5, 0); q.setFromEuler(eul); head.quaternion.multiply(q);
    }
    // blink
    if (eyes) { if (now > s.blinkAt) { eyes.scale.y = eyesY * 0.12; if (now > s.blinkAt + 110) { eyes.scale.y = eyesY; s.blinkAt = now + 2500 + Math.random() * 3500; } } }

    renderer.render(scene, camera);
    // keep the hit area and bubble on the robot
    proj.set(s.x, BOT_H / 2, 0).project(camera);
    const cx = (proj.x + 1) / 2 * innerWidth, bw = 0.62 * pxPerUnit(), bh = BOT_H * pxPerUnit();
    hit.style.transform = `translate(${cx - bw / 2}px, ${STRIP - bh - 8}px)`; hit.style.width = bw + 'px'; hit.style.height = bh + 'px';
    hideBtn.style.transform = `translate(${cx + bw / 2 - 4}px, ${STRIP - bh - 6}px)`;
    if (!bubble.hidden) { const w = bubble.offsetWidth; bubble.style.transform = `translate(${MathUtils.clamp(cx - w / 2, 8, innerWidth - w - 8)}px, ${STRIP - bh - bubble.offsetHeight - 14}px)`; }
  }
  requestAnimationFrame(frame);
  root.classList.add('is-live');
}
