// Tells Bing and Yandex which URLs exist (IndexNow). Google does not use it. Run after a production deploy:
//   node scripts/indexnow.mjs            sends every URL in the sitemap
//   node scripts/indexnow.mjs --dry-run  prints what would be sent
// The key file is public by design (public/76bace88968609c5db0f4efe9261d74d.txt).
import { readFileSync, readdirSync } from 'node:fs';

const key = '76bace88968609c5db0f4efe9261d74d';
const host = 'neuronetwrks.com';
const dry = process.argv.includes('--dry-run');
const sitemapDir = 'dist/client';

const urls = readdirSync(sitemapDir)
  .filter((f) => /^sitemap-\d+\.xml$/.test(f))
  .flatMap((f) =>
    [...readFileSync(`${sitemapDir}/${f}`, 'utf8').matchAll(/<loc>([^<]+)<\/loc>/g)].map(
      (m) => m[1],
    ),
  );

if (!urls.length) {
  console.error('No sitemap URLs found. Build first.');
  process.exit(1);
}
const body = { host, key, keyLocation: `https://${host}/${key}.txt`, urlList: urls };
if (dry) {
  console.log(JSON.stringify(body, null, 2));
  process.exit(0);
}
const res = await fetch('https://api.indexnow.org/indexnow', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: JSON.stringify(body),
});
console.log(`IndexNow: HTTP ${res.status} for ${urls.length} URL(s)`);
process.exit(res.ok || res.status === 202 ? 0 : 1);
