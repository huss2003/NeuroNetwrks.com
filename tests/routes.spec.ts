import { test, expect } from '@playwright/test';

const routes = [
  '/',
  '/programs',
  '/programs/ai-foundation',
  '/programs/ai-ml-engineering',
  '/programs/software-development',
  '/programs/product-ux-ai-design',
  '/programs/data-science-ai',
  '/programs/cybersecurity',
  '/for/students',
  '/for/parents',
  '/for/schools',
  '/for/professionals',
  '/about',
  '/admissions',
  '/apply',
  '/contact',
  '/resources',
  '/resources/category/guides',
  '/privacy',
  '/terms',
];

for (const route of routes) {
  test(`${route} meets the page rules`, async ({ page }) => {
    await page.goto(route);
    await expect(page.locator('html')).toHaveAttribute('lang', 'en-IN');
    await expect(page.locator('h1')).toHaveCount(1);
    await expect(page.locator('main')).toHaveCount(1);
    await expect(page.locator('header').first()).toBeVisible();

    const title = await page.title();
    expect(title.length, `title length: ${title}`).toBeLessThanOrEqual(60);
    const desc = await page.locator('meta[name="description"]').getAttribute('content');
    expect(desc && desc.length).toBeGreaterThan(0);
    expect(desc!.length, `description length: ${desc}`).toBeLessThanOrEqual(155);
    await expect(page.locator('link[rel="canonical"]')).toHaveCount(1);

    // Heading levels never skip
    const levels = await page.$$eval('h1,h2,h3,h4,h5,h6', (els) =>
      els.map((e) => Number(e.tagName[1])),
    );
    levels.forEach((l, i) => {
      if (i > 0)
        expect(
          l - levels[i - 1],
          `heading order on ${route}: ${levels.join(',')}`,
        ).toBeLessThanOrEqual(1);
    });

    // JSON-LD parses
    const blocks = await page.$$eval('script[type="application/ld+json"]', (els) =>
      els.map((e) => e.textContent ?? ''),
    );
    expect(blocks.length).toBeGreaterThan(0);
    blocks.forEach((b) => expect(() => JSON.parse(b)).not.toThrow());

    // No horizontal scroll
    const overflow = await page.evaluate(
      () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
    );
    expect(overflow, 'horizontal overflow in px').toBeLessThanOrEqual(0);

    // Images have alt text
    expect(await page.$$eval('img:not([alt])', (els) => els.length)).toBe(0);
  });
}

test('404 page renders', async ({ page }) => {
  const res = await page.goto('/this-does-not-exist');
  expect(res?.status()).toBe(404);
  await expect(page.locator('h1')).toHaveCount(1);
});
