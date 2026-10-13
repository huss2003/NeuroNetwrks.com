// Fails the build if an unresolved {{CONFIRM placeholder reaches dist/.
// Also writes noindex headers for every non-production build.
import { readdirSync, readFileSync, writeFileSync, existsSync, statSync } from 'node:fs';
import { join } from 'node:path';

const walk = (dir) =>
  readdirSync(dir).flatMap((f) => {
    const p = join(dir, f);
    return statSync(p).isDirectory() ? walk(p) : [p];
  });

if (!existsSync('dist')) {
  console.error('dist/ not found');
  process.exit(1);
}
const textExt = /\.(html|xml|txt|json|js|css|svg|md)$/;
const bad = walk('dist').filter(
  (f) => textExt.test(f) && readFileSync(f, 'utf8').includes('{{CONFIRM'),
);
if (bad.length) {
  console.error('Unresolved {{CONFIRM placeholders in:\n' + bad.join('\n'));
  process.exit(1);
}
if (process.env.PUBLIC_ENV !== 'production') {
  const hdr = join('dist', 'client', '_headers');
  const prev = existsSync(hdr) ? readFileSync(hdr, 'utf8') : '';
  writeFileSync(hdr, '/*\n  X-Robots-Tag: noindex, nofollow\n\n' + prev);
  console.log('Non-production build: noindex headers written.');
}
console.log('CONFIRM check passed.');
