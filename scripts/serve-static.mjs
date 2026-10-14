// Tiny static server for dist/client, used by e2e and audits (astro preview needs workerd network access).
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { URL } from 'node:url';
import { Buffer } from 'node:buffer';
import { brotliCompressSync } from 'node:zlib';

const root = 'dist/client';
const port = Number(process.argv[2] ?? 4321);
const types = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.txt': 'text/plain',
  '.xml': 'application/xml',
  '.svg': 'image/svg+xml',
  '.json': 'application/json',
};

createServer(async (req, res) => {
  const path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(
    /^(\.\.[/\\])+/,
    '',
  );
  const candidates = [join(root, path), join(root, path, 'index.html'), join(root, path + '.html')];
  for (const f of candidates) {
    try {
      const body = await readFile(f);
      const type = types[extname(f)] ?? 'application/octet-stream';
      // Mimic Cloudflare: compress text types so lab numbers match production transfer sizes.
      const compress =
        /text|xml|json|javascript|svg/.test(type) &&
        /br/.test(req.headers['accept-encoding'] ?? '');
      res.writeHead(200, {
        'Content-Type': type,
        ...(compress ? { 'Content-Encoding': 'br' } : {}),
      });
      return res.end(compress ? brotliCompressSync(body) : body);
    } catch {
      /* try next */
    }
  }
  const nf = await readFile(join(root, '404.html')).catch(() => Buffer.from('Not found'));
  res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(nf);
}).listen(port, () => console.log(`Serving ${root} on http://localhost:${port}`));
