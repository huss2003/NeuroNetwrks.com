import gsap from 'gsap';
import { SplitText } from 'gsap/SplitText';

gsap.registerPlugin(SplitText);

/** One-time line reveal on the hero headline. The text is already in the HTML and painted (LCP);
 *  this runs after first paint and re-splits on resize. */
export async function initHeroReveal() {
  const el = document.querySelector<HTMLElement>('[data-hero-title]');
  if (!el) return;
  await document.fonts.ready;
  const mm = gsap.matchMedia();
  mm.add('(prefers-reduced-motion: no-preference)', () => {
    let played = false;
    SplitText.create(el, {
      type: 'lines',
      mask: 'lines',
      autoSplit: true,
      onSplit(self) {
        if (played) return; // do not replay on resize
        played = true;
        return gsap.from(self.lines, {
          yPercent: 100,
          duration: 0.9,
          ease: 'expo.out',
          stagger: 0.08,
        });
      },
    });
  });
}
