import { test, expect } from '@playwright/test';

test('home renders with one h1 and en-IN', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en-IN');
  await expect(page.locator('h1')).toHaveCount(1);
});
