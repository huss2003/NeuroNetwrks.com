import gsap from 'gsap';

const MAX = 8; // px pull

export function initMagnetic() {
  const mm = gsap.matchMedia();
  mm.add(
    '(prefers-reduced-motion: no-preference) and (pointer: fine) and (min-width: 1024px)',
    () => {
      const cleanups: (() => void)[] = [];
      document.querySelectorAll<HTMLElement>('[data-magnetic]').forEach((el) => {
        const x = gsap.quickTo(el, 'x', { duration: 0.35, ease: 'power3.out' });
        const y = gsap.quickTo(el, 'y', { duration: 0.35, ease: 'power3.out' });
        const move = (e: PointerEvent) => {
          const r = el.getBoundingClientRect();
          const dx = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
          const dy = (e.clientY - (r.top + r.height / 2)) / (r.height / 2);
          x(gsap.utils.clamp(-1, 1, dx) * MAX);
          y(gsap.utils.clamp(-1, 1, dy) * MAX);
        };
        const leave = () => {
          x(0);
          y(0);
        };
        el.addEventListener('pointermove', move);
        el.addEventListener('pointerleave', leave);
        cleanups.push(() => {
          el.removeEventListener('pointermove', move);
          el.removeEventListener('pointerleave', leave);
          gsap.set(el, { clearProps: 'transform' });
        });
      });
      return () => cleanups.forEach((c) => c());
    },
  );
}
