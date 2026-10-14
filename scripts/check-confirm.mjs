// Fails the production build if any unresolved {{CONFIRM placeholder reaches dist/.
// Staging (PUBLIC_ENV != production) only warns, so work in progress can still build.
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join, extname } from 'node:path';

const TEXT = new Set(['.html', '.xml', '.txt', '.json', '.js', '.css', '.svg']);
const hits = [];

function walk(dir) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p);
    else if (TEXT.has(extname(p)) && readFileSync(p, 'utf8').includes('{{CONFIRM')) hits.push(p);
  }
}

try {
  walk('dist');
} catch {
  console.error('dist/ not found. Run the build first.');
  process.exit(1);
}

if (hits.length) {
  const strict = process.env.PUBLIC_ENV === 'production';
  console.error(`${strict ? 'ERROR' : 'WARNING'}: {{CONFIRM found in ${hits.length} file(s):`);
  hits.forEach((h) => console.error('  ' + h));
  process.exit(strict ? 1 : 0);
}
console.log('No {{CONFIRM placeholders in dist/.');
