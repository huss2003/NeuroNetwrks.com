// Decides whether the 3D ribbon may load, and loads it lazily when the closing CTA is one viewport away.
// Otherwise the committed poster image stays, and the page looks finished with the poster alone.
interface NavigatorExtras extends Navigator {
  connection?: { saveData?: boolean };
  deviceMemory?: number;
}

export function canRun3D(): boolean {
  const nav = navigator as NavigatorExtras;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return false;
  if (nav.connection?.saveData) return false;
  if ((nav.hardwareConcurrency ?? 8) <= 4) return false;
  if (nav.deviceMemory !== undefined && nav.deviceMemory <= 4) return false;
  try {
    const c = document.createElement('canvas');
    if (!(c.getContext('webgl2') || c.getContext('webgl'))) return false;
  } catch {
    return false;
  }
  return true;
}

export function initRibbonLazy() {
  const host = document.querySelector<HTMLElement>('[data-ribbon]');
  if (!host || !canRun3D()) return;
  const io = new IntersectionObserver(
    (entries) => {
      if (!entries.some((e) => e.isIntersecting)) return;
      io.disconnect();
      import('./cta-ribbon')
        .then((m) => m.mountRibbon(host))
        .catch(() => {
          /* chunk or WebGL failure: the poster stays */
        });
    },
    { rootMargin: '100% 0px' },
  );
  io.observe(host);
}
