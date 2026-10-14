// Budget check on the built output. Entry JS = what the home page loads on its own (gzip),
// the lazy 3D chunk must stay under 200 KB gzip. Run after `astro build`.
import { readdirSync, readFileSync } from 'node:fs';
import { gzipSync } from 'node:zlib';
import { join } from 'node:path';

const dir = 'dist/client/_astro';
const gz = (f) => gzipSync(readFileSync(join(dir, f)), { level: 9 }).length;
const js = readdirSync(dir).filter((f) => f.endsWith('.js'));
const ribbon = js.filter((f) => f.startsWith('cta-ribbon'));
const entry = js.filter((f) => !ribbon.includes(f));

const kb = (n) => (n / 1024).toFixed(1);
const entryTotal = entry.reduce((s, f) => s + gz(f), 0);
const ribbonTotal = ribbon.reduce((s, f) => s + gz(f), 0);
console.log(`Entry JS (gzip, upper bound: all non-3D chunks): ${kb(entryTotal)} KB (budget 100)`);
console.log(`3D chunk (gzip): ${kb(ribbonTotal)} KB (budget 200)`);

let bad = false;
if (entryTotal > 100 * 1024) {
  console.error('Entry JS over budget');
  bad = true;
}
if (ribbonTotal > 200 * 1024) {
  console.error('3D chunk over budget');
  bad = true;
}
process.exit(bad ? 1 : 0);
