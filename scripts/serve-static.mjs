// Tiny static server for dist/client, used by e2e and audits (astro preview needs workerd network access).
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { URL } from 'node:url';

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
      res.writeHead(200, { 'Content-Type': types[extname(f)] ?? 'application/octet-stream' });
      return res.end(body);
    } catch {
      /* try next */
    }
  }
  res.writeHead(404);
  res.end('Not found');
}).listen(port, () => console.log(`Serving ${root} on http://localhost:${port}`));
