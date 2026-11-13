// Lambda Web Function app for lambda-web-weighted-rollout.
// Change RELEASE (and ACCENT) before `./deploy.sh canary 10` to see the new release
// take a share of the traffic.
import http from 'node:http';
import { createHash, randomUUID } from 'node:crypto';

const RELEASE = 'v4';
const ACCENT = '#2563eb';

// The runtime sets AWS_LAMBDA_HTTP_ENDPOINT to host:port. Locally, fall back to 127.0.0.1:3000.
const endpoint = process.env.AWS_LAMBDA_HTTP_ENDPOINT || '127.0.0.1:3000';
const sep = endpoint.lastIndexOf(':');
const HOST = endpoint.slice(0, sep);
const PORT = Number(endpoint.slice(sep + 1));

// Set per revision in template.yaml. A revision can't know its current traffic weight
// (weights change without a new revision), so the page shows only what is fixed at
// creation: the slot, the release, and when this slot's code was deployed.
const SLOT = process.env.REVISION_SLOT || 'local';
const CODE_VERSION = process.env.CODE_VERSION_ID || 'local';
const DEPLOYED_AT = process.env.DEPLOYED_AT || 'unknown';
const ENVIRONMENT_ID = randomUUID().slice(0, 8);
const SLOT_COLOR = { blue: '#1d4ed8', green: '#15803d' }[SLOT] || '#6b7280';

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

function deployedLabel() {
  const d = new Date(DEPLOYED_AT);
  if (Number.isNaN(d.getTime())) return 'unknown';
  return d.toISOString().replace('T', ' ').replace(/:\d\d\.\d+Z$|:\d\dZ$/, ' UTC');
}

// Samples /version from the browser so the page shows the real split right now.
// cache: 'no-store' and a unique query string make every call reach the endpoint.
const SAMPLE_SCRIPT = `
const btn = document.getElementById('sample');
const out = document.getElementById('result');
btn.addEventListener('click', async () => {
  btn.disabled = true;
  const counts = { blue: 0, green: 0 };
  let failed = 0;
  for (let i = 0; i < 20; i++) {
    out.textContent = 'Sampling... ' + (i + 1) + ' of 20';
    try {
      const r = await fetch('/version?n=' + Date.now() + '-' + i, { cache: 'no-store' });
      const v = await r.json();
      counts[v.slot] = (counts[v.slot] || 0) + 1;
    } catch (e) { failed++; }
  }
  const bar = (n) => '\\u2588'.repeat(n);
  out.innerHTML = '<span class="b">blue ' + bar(counts.blue) + ' ' + counts.blue + '</span>'
    + '<span class="g">green ' + bar(counts.green) + ' ' + counts.green + '</span>'
    + (failed ? '<span class="f">' + failed + ' failed</span>' : '');
  btn.disabled = false;
});`;

function page() {
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Weighted rollout: ${esc(SLOT)} ${esc(RELEASE)}</title>
<style>
  body { margin:0; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background:#0f172a; color:#e2e8f0; }
  main { max-width: 760px; margin: 48px auto; padding: 0 20px; }
  .card { background:#111827; border-radius:16px; overflow:hidden; box-shadow: 0 10px 30px rgba(0,0,0,.4); }
  header { background:${SLOT_COLOR}; padding:28px 32px; }
  header h1 { margin:0; font-size:40px; }
  header p { margin:6px 0 0; font-size:18px; opacity:.9; }
  .body { padding:24px 32px; font-size:18px; line-height:1.5; }
  .release { display:inline-block; padding:4px 14px; border-radius:999px; background:${ACCENT}; color:#fff; font-weight:600; }
  .muted { color:#94a3b8; }
  button { font-size:17px; padding:10px 18px; border:0; border-radius:10px; background:#f8fafc; color:#0f172a; font-weight:600; cursor:pointer; }
  button:disabled { opacity:.6; cursor:wait; }
  #result { margin-top:14px; min-height:28px; font-family: ui-monospace, Menlo, monospace; font-size:16px; }
  #result span { display:block; }
  .b { color:#60a5fa; } .g { color:#4ade80; } .f { color:#f87171; }
  code { font-size:15px; background:#1f2937; padding:2px 6px; border-radius:6px; }
</style></head>
<body><main><div class="card">
  <header><h1>Served by: ${esc(SLOT)}</h1><p>AWS Lambda Web Function behind Amazon CloudFront</p></header>
  <div class="body">
    <p><span class="release">${esc(RELEASE)}</span> &nbsp;<span class="muted">deployed ${esc(deployedLabel())}</span></p>
    <p>Refresh to see which revision serves each request. During a canary, requests are split between blue and green.</p>
    <p><button id="sample" type="button">Sample 20 requests</button></p>
    <div id="result" class="muted">Shows how the endpoint is splitting traffic right now.</div>
    <p class="muted">Current weights and next steps: <code>./deploy.sh status</code></p>
  </div>
</div></main>
<script>${SAMPLE_SCRIPT}</script>
</body></html>`;
}

// The CSP allows only this page's own inline script, by hash.
const SCRIPT_HASH = createHash('sha256').update(SAMPLE_SCRIPT).digest('base64');
const CSP = `default-src 'none'; style-src 'unsafe-inline'; script-src 'sha256-${SCRIPT_HASH}'; connect-src 'self'`;

const server = http.createServer((req, res) => {
  const path = (req.url || '/').split('?')[0];
  let status = 200;
  const headers = { 'cache-control': 'no-store', 'x-revision-slot': SLOT, 'x-release': RELEASE, 'x-content-type-options': 'nosniff' };
  if (path === '/health') {
    res.writeHead(200, { ...headers, 'content-type': 'text/plain' }).end('ok');
  } else if (path === '/version') {
    res.writeHead(200, { ...headers, 'content-type': 'application/json' })
      .end(JSON.stringify({ slot: SLOT, release: RELEASE, deployedAt: DEPLOYED_AT, codeVersion: CODE_VERSION, environment: ENVIRONMENT_ID }));
  } else if (path === '/') {
    res.writeHead(200, { ...headers, 'content-type': 'text/html; charset=utf-8', 'content-security-policy': CSP }).end(page());
  } else {
    status = 404;
    res.writeHead(404, { ...headers, 'content-type': 'text/plain' }).end('not found');
  }
  // One structured line per request, so you can compare the canary with the live slot in logs.
  console.log(JSON.stringify({ slot: SLOT, release: RELEASE, codeVersion: CODE_VERSION, path, status }));
});

server.listen(PORT, HOST, () => console.log(`Listening on ${HOST}:${PORT} (slot ${SLOT}, release ${RELEASE})`));
process.on('SIGTERM', () => server.close(() => process.exit(0)));
