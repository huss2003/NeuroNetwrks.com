// Post-build: put sha256 hashes of the site's own inline scripts into the Content-Security-Policy in
// dist/client/_headers, so the policy needs no 'unsafe-inline' for scripts. JSON-LD blocks are data,
// not executable, and are skipped. Fails if a page carries an inline event handler.
import { createHash } from 'node:crypto';
import { readdirSync, readFileSync, writeFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const dir = 'dist/client';
const hashes = new Set();
const problems = [];

function walk(d) {
  for (const n of readdirSync(d)) {
    const p = join(d, n);
    if (statSync(p).isDirectory()) walk(p);
    else if (n.endsWith('.html')) scan(p);
  }
}
function scan(file) {
  const html = readFileSync(file, 'utf8');
  for (const m of html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)) {
    const attrs = m[1];
    if (/type="application\/ld\+json"/.test(attrs) || /\ssrc=/.test(attrs)) continue;
    hashes.add(`'sha256-${createHash('sha256').update(m[2]).digest('base64')}'`);
  }
  if (/\son(click|load|error|submit|mouseover)=/.test(html))
    problems.push(`${file}: inline event handler`);
}
walk(dir);

const headersPath = join(dir, '_headers');
const out = readFileSync(headersPath, 'utf8').replace('__SCRIPT_HASHES__', [...hashes].join(' '));
if (out.includes('__SCRIPT_HASHES__')) problems.push('token not replaced');
writeFileSync(headersPath, out);
console.log(`CSP: ${hashes.size} inline script hash(es) written to ${headersPath}`);
if (problems.length) {
  console.error(problems.join('\n'));
  process.exit(1);
}
