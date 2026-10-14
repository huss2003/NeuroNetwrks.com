// The signature moment: one continuous line, blue at the top to green at the bottom, running down the
// left gutter and through every [data-path-anchor], drawn as the reader scrolls. Nodes appear as the
// line reaches them. Reduced motion draws the finished line statically; no JS shows no line.
const SVG_NS = 'http://www.w3.org/2000/svg';
const SEED = 20261013;

// Small seeded PRNG so the hand-drawn irregularity is stable between loads and resizes.
function mulberry32(a: number) {
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const el = <K extends keyof SVGElementTagNameMap>(tag: K, attrs: Record<string, string> = {}) => {
  const n = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
  return n;
};

interface Point {
  x: number;
  y: number;
}

function buildPath(points: Point[], straight: boolean, rand: () => number) {
  let d = `M${points[0].x.toFixed(1)},${points[0].y.toFixed(1)}`;
  for (let i = 1; i < points.length; i++) {
    const a = points[i - 1];
    const b = points[i];
    if (straight) {
      d += ` L${b.x.toFixed(1)},${b.y.toFixed(1)}`;
      continue;
    }
    const dy = b.y - a.y;
    const sway = (rand() - 0.5) * 36; // gentle S-curve, never geometric
    d += ` C${(a.x + sway).toFixed(1)},${(a.y + dy * 0.4).toFixed(1)} ${(b.x - sway).toFixed(1)},${(b.y - dy * 0.4).toFixed(1)} ${b.x.toFixed(1)},${b.y.toFixed(1)}`;
  }
  return d;
}

type Teardown = () => void;

// Size of the layout the current line was drawn for. The observer compares against this, not against
// a value read later, so a resize that lands while drawing is never missed.
let drawn = { w: 0, h: 0 };

async function draw(main: HTMLElement, animate: boolean): Promise<Teardown> {
  const anchors = [...document.querySelectorAll<HTMLElement>('[data-path-anchor]')];
  const mainTop = main.getBoundingClientRect().top + scrollY;
  const mainBox = main.getBoundingClientRect();
  const straight = innerWidth < 768;

  // The line lives in the left gutter. Content padding is 16 px on phones, wider above.
  const container = document.querySelector('.container-page');
  const left = container
    ? container.getBoundingClientRect().left + parseFloat(getComputedStyle(container).paddingLeft)
    : 16;
  const x = Math.max(8, Math.min(left - 22, 120));

  const ys = anchors
    .map((a) => a.getBoundingClientRect().top + scrollY - mainTop)
    .sort((a, b) => a - b);
  if (ys.length < 2) return () => {};
  const rand = mulberry32(SEED);
  const points: Point[] = ys.map((y, i) => ({
    x: x + (straight || i === 0 ? 0 : (rand() - 0.5) * 10),
    y,
  }));

  const height = main.scrollHeight;
  drawn = { w: main.clientWidth, h: height };
  const svg = el('svg', {
    class: 'signature-path',
    'aria-hidden': 'true',
    focusable: 'false',
    width: String(mainBox.width),
    height: String(height),
    viewBox: `0 0 ${mainBox.width} ${height}`,
    'data-animated': String(animate),
  });
  const grad = el('linearGradient', {
    id: 'sig-grad',
    gradientUnits: 'userSpaceOnUse',
    x1: '0',
    y1: String(ys[0]),
    x2: '0',
    y2: String(ys[ys.length - 1]),
  });
  const s1 = el('stop', { offset: '0' });
  s1.style.stopColor = 'var(--color-blue-600)';
  const s2 = el('stop', { offset: '1' });
  s2.style.stopColor = 'var(--color-green-600)';
  grad.append(s1, s2);
  const defs = el('defs');
  defs.append(grad);
  svg.append(defs);

  const path = el('path', { d: buildPath(points, straight, rand) });
  const nodes = points.map((p) => el('circle', { cx: String(p.x), cy: String(p.y), r: '6' }));
  svg.append(path, ...nodes);
  main.append(svg);

  const total = path.getTotalLength();
  // Lookup of path length at each y, so scroll position maps to a drawn length.
  const lut: { y: number; len: number }[] = [];
  const N = 240;
  for (let i = 0; i <= N; i++) {
    const len = (total * i) / N;
    lut.push({ y: path.getPointAtLength(len).y, len });
  }
  const lenAtY = (y: number) => {
    if (y <= lut[0].y) return 0;
    if (y >= lut[N].y) return total;
    let lo = 0;
    let hi = N;
    while (hi - lo > 1) {
      const mid = (lo + hi) >> 1;
      if (lut[mid].y < y) lo = mid;
      else hi = mid;
    }
    const a = lut[lo];
    const b = lut[hi];
    return a.len + ((y - a.y) / (b.y - a.y || 1)) * (b.len - a.len);
  };

  if (!animate) {
    nodes.forEach((n) => n.classList.add('on'));
    return () => svg.remove();
  }

  const { default: gsap } = await import('gsap');
  const { ScrollTrigger } = await import('gsap/ScrollTrigger');
  gsap.registerPlugin(ScrollTrigger);

  path.style.strokeDasharray = String(total);
  path.style.strokeDashoffset = String(total);
  const state = { len: 0 };
  const render = () => {
    path.style.strokeDashoffset = String(total - state.len);
    nodes.forEach((n, i) => n.classList.toggle('on', state.len >= lenAtY(points[i].y) - 1));
  };
  render();

  const st = ScrollTrigger.create({
    trigger: main,
    start: 'top bottom',
    end: 'bottom top',
    onUpdate: () => {
      // The tip of the line trails the reader's eye line, about two thirds down the viewport.
      const tipY = scrollY - mainTop + innerHeight * 0.66;
      gsap.to(state, {
        len: lenAtY(tipY),
        duration: 0.6,
        ease: 'power2.out',
        overwrite: true,
        onUpdate: render,
      });
    },
  });
  st.update();

  return () => {
    st.kill();
    gsap.killTweensOf(state);
    svg.remove();
  };
}

export async function initSignaturePath(animate: boolean) {
  const main = document.querySelector<HTMLElement>('main');
  if (!main) return;
  let teardown: Teardown = () => {};
  let building = false;
  let queued = false;

  const rebuild = async () => {
    if (building) {
      queued = true;
      return;
    }
    building = true;
    teardown();
    try {
      teardown = await draw(main, animate);
    } finally {
      building = false;
      if (queued) {
        queued = false;
        void rebuild();
      }
    }
  };

  await document.fonts.ready;
  await rebuild();

  let timer: number | undefined;
  const ro = new ResizeObserver(() => {
    // Ignore our own svg and sub-pixel noise; rebuild only on real layout change.
    const w = main.clientWidth;
    const h = main.scrollHeight;
    if (Math.abs(w - drawn.w) < 2 && Math.abs(h - drawn.h) < 4) return;
    clearTimeout(timer);
    timer = window.setTimeout(rebuild, 160);
  });
  ro.observe(main);
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) ro.disconnect();
    else ro.observe(main);
  });
}
