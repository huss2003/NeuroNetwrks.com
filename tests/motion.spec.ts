import { test, expect } from '@playwright/test';

const lines = (page: import('@playwright/test').Page) => page.locator('.signature-path path');

test.describe('motion on', () => {
  test('signature line draws with scroll and nodes appear', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('html')).toHaveClass(/js-motion/);
    await expect(page.locator('.signature-path')).toHaveCount(1, { timeout: 15_000 });
    const offset = () =>
      lines(page).evaluate((p: SVGPathElement) => Number(p.style.strokeDashoffset));
    await expect.poll(offset, { timeout: 15_000 }).toBeGreaterThan(0);
    const first = await offset();
    await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
    await expect.poll(offset, { timeout: 15_000 }).toBeLessThan(first);
    await expect
      .poll(() => page.locator('.signature-path circle.on').count(), { timeout: 15_000 })
      .toBeGreaterThan(3);
  });

  test('line is rebuilt on resize and stays inside the page', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('.signature-path')).toHaveCount(1, { timeout: 15_000 });
    await page.setViewportSize({ width: 800, height: 900 });
    await expect
      .poll(async () => Number(await page.locator('.signature-path').getAttribute('width')), {
        timeout: 15_000,
      })
      .toBeLessThanOrEqual(800);
    await expect(page.locator('.signature-path')).toHaveCount(1);
    const overflow = await page.evaluate(
      () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
    );
    expect(overflow).toBeLessThanOrEqual(0);
  });

  test('headline text stays in the DOM and readable', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('h1')).toContainText(
      'AI, data and software careers, taught from zero.',
    );
  });

  test('ribbon poster shows on low-end devices', async ({ page }) => {
    await page.addInitScript(() =>
      Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 2 }),
    );
    await page.goto('/');
    await page.locator('[data-ribbon]').scrollIntoViewIfNeeded();
    await page.waitForTimeout(800);
    await expect(page.locator('[data-ribbon]')).not.toHaveAttribute('data-ribbon-ready', 'true');
    await expect(page.locator('[data-ribbon-poster]')).toBeVisible();
  });

  test('ribbon loads lazily and retires the poster when allowed', async ({ page }) => {
    await page.addInitScript(() =>
      Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 }),
    );
    const requests: string[] = [];
    page.on('request', (r) => requests.push(r.url()));
    await page.goto('/');
    expect(
      requests.some((u) => u.includes('cta-ribbon')),
      'three chunk must not load up front',
    ).toBe(false);
    await page.locator('[data-ribbon]').scrollIntoViewIfNeeded();
    await expect(page.locator('[data-ribbon]')).toHaveAttribute('data-ribbon-ready', 'true', {
      timeout: 20_000,
    });
    expect(requests.some((u) => u.includes('cta-ribbon'))).toBe(true);
  });
});

test.describe('reduced motion', () => {
  test.use({ reducedMotion: 'reduce' });
  test('no motion class, full line drawn statically, poster stays', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('html')).not.toHaveClass(/js-motion/);
    await expect(page.locator('.signature-path')).toHaveCount(1);
    await expect(page.locator('.signature-path')).toHaveAttribute('data-animated', 'false');
    const dash = await lines(page).evaluate((p: SVGPathElement) => p.style.strokeDashoffset);
    expect(dash).toBe('');
    expect(await page.locator('.signature-path circle').count()).toBe(
      await page.locator('.signature-path circle.on').count(),
    );
    await page.locator('[data-ribbon]').scrollIntoViewIfNeeded();
    await page.waitForTimeout(600);
    await expect(page.locator('[data-ribbon]')).not.toHaveAttribute('data-ribbon-ready', 'true');
    await expect(page.locator('[data-ribbon-poster]')).toBeVisible();
  });
});

test.describe('JavaScript disabled', () => {
  test.use({ javaScriptEnabled: false });
  test('everything is visible and there is no half-drawn line', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('h1')).toBeVisible();
    await expect(page.locator('.signature-path')).toHaveCount(0);
    await expect(page.locator('[data-ribbon-poster]')).toHaveCount(1);
    await expect(page.getByRole('link', { name: 'Apply' }).first()).toBeVisible();
  });
});
