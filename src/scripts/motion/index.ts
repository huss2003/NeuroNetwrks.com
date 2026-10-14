// Single entry for all motion. Loaded once from Base.astro. Nothing else may import gsap, lenis or three.
// Content is complete without any of this: the `js-motion` class (set by an inline snippet in <head>
// only when reduced motion is NOT requested) is the gate for every hidden-until-animated style.
const root = document.documentElement;
const animate = root.classList.contains('js-motion');

async function boot() {
  // Signature line: animated when motion is allowed, drawn fully and statically otherwise.
  if (document.querySelector('[data-path-anchor]')) {
    const { initSignaturePath } = await import('./signature-path');
    void initSignaturePath(animate);
  }
  if (!animate) return;

  const path = location.pathname;
  const longForm = path.startsWith('/apply') || path.startsWith('/contact');
  if (!longForm && matchMedia('(pointer: fine)').matches) {
    const { initSmoothScroll } = await import('./lenis-gsap');
    void initSmoothScroll();
  }
  if (document.querySelector('[data-hero-title]')) {
    const { initHeroReveal } = await import('./hero-reveal');
    void initHeroReveal();
  }
  if (document.querySelector('[data-magnetic]') && matchMedia('(pointer: fine)').matches) {
    const { initMagnetic } = await import('./magnetic');
    void initMagnetic();
  }
  if (document.querySelector('[data-ribbon]')) {
    const { initRibbonLazy } = await import('./ribbon-loader');
    initRibbonLazy();
  }
}

// Start after first paint so nothing here can delay LCP.
const start = () => requestAnimationFrame(() => setTimeout(boot, 0));
if (document.readyState === 'complete') start();
else addEventListener('load', start, { once: true });
