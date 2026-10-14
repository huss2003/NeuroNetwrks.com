import { test, expect } from '@playwright/test';

test('security headers are served and nothing violates the CSP (3D and motion included)', async ({
  page,
}) => {
  await page.addInitScript(() =>
    Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 }),
  );
  const problems: string[] = [];
  page.on('console', (m) => ['error', 'warning'].includes(m.type()) && problems.push(m.text()));
  page.on('pageerror', (e) => problems.push(e.message));
  const res = await page.goto('/');
  const h = res!.headers();
  expect(h['content-security-policy']).toContain("default-src 'self'");
  expect(h['content-security-policy']).toMatch(/script-src 'self' 'sha256-/);
  expect(h['content-security-policy']).not.toContain("script-src 'self' 'unsafe-inline'");
  expect(h['strict-transport-security']).toContain('max-age=');
  expect(h['x-content-type-options']).toBe('nosniff');
  await page.locator('[data-ribbon]').scrollIntoViewIfNeeded();
  await expect(page.locator('[data-ribbon]')).toHaveAttribute('data-ribbon-ready', 'true', {
    timeout: 20_000,
  });
  expect(problems, problems.join('\n')).toEqual([]);
});

test('home page head: social card, manifest, feed, structured data', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('meta[property="og:image"]')).toHaveAttribute(
    'content',
    /\/og\/home\.png$/,
  );
  await expect(page.locator('meta[name="twitter:card"]')).toHaveAttribute(
    'content',
    'summary_large_image',
  );
  await expect(page.locator('link[rel="manifest"]')).toHaveCount(1);
  await expect(page.locator('link[rel="alternate"][type="application/rss+xml"]')).toHaveCount(1);
  const og = await page.locator('meta[property="og:image"]').getAttribute('content');
  const img = await page.request.get(new URL(og!).pathname);
  expect(img.status()).toBe(200);
  const graph = JSON.parse(
    (await page.locator('script[type="application/ld+json"]').first().textContent())!,
  );
  const types = graph['@graph'].flatMap((n: { '@type': string | string[] }) => [n['@type']].flat());
  expect(types).toEqual(expect.arrayContaining(['EducationalOrganization', 'WebSite', 'WebPage']));
});

test('program page structured data matches visible content and has no offers', async ({ page }) => {
  await page.goto('/programs/cybersecurity');
  const nodes = await page.$$eval('script[type="application/ld+json"]', (els) =>
    els.flatMap((e) => {
      const d = JSON.parse(e.textContent ?? '{}');
      return d['@graph'] ?? [d];
    }),
  );
  const course = nodes.find((n) => n['@type'] === 'Course');
  expect(course.name).toBe(await page.locator('h1').innerText());
  expect(course.hasCourseInstance.courseWorkload).toBe('PT624H');
  expect(JSON.stringify(nodes)).not.toContain('"offers"');
  const faq = nodes.find((n) => n['@type'] === 'FAQPage');
  const body = await page.locator('main').innerText();
  for (const q of faq.mainEntity) expect(body).toContain(q.name);
  expect(nodes.some((n) => n['@type'] === 'BreadcrumbList')).toBe(true);
});

test('robots.txt blocks everything on staging builds and sitemap lists no private pages', async ({
  request,
}) => {
  const robots = await (await request.get('/robots.txt')).text();
  expect(robots).toContain('Disallow: /');
  const sm = await (await request.get('/sitemap-0.xml')).text();
  expect(sm).not.toContain('/dev/');
  expect(sm).not.toContain('/apply/thanks');
  expect(sm).toContain('<lastmod>');
});
