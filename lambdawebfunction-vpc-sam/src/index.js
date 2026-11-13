// Lambda Web Function sample app — VPC egress variant.
//
// A Web Function runs a standard HTTP server that listens on the port Lambda
// provides. This sample demonstrates PRIVATE VPC EGRESS: with a network connector
// attached (see template.yaml), outbound calls from this function are routed
// through ENIs in your VPC subnets, so it can reach private resources such as an
// internal API, database, or cache that are not exposed to the internet.
//
// Set INTERNAL_TARGET_URL (via the revision's ServiceConfig.EnvironmentVariables)
// to a private endpoint in your VPC to see the egress path working end to end.

import http from 'node:http';

// Lambda provides the exact host:port your server MUST bind to via
// AWS_LAMBDA_HTTP_ENDPOINT. You must listen on BOTH that host and that port --
// binding a different port, or only a loopback host, makes requests fail with a
// 502 (the runtime reports Application.TimeoutListenError). The fallback address
// applies only to local runs, where Lambda does not set the variable.
const [HOST, PORT] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:8080').split(':');
const APP_NAME = process.env.APP_NAME || 'lambda-web-function-vpc';
// A private URL reachable only from inside your VPC, e.g. an internal ALB or service.
const INTERNAL_TARGET_URL = process.env.INTERNAL_TARGET_URL || '';

function probeInternalTarget(url) {
  return new Promise((resolve) => {
    if (!url) {
      resolve({ configured: false, ok: false, detail: 'INTERNAL_TARGET_URL not set' });
      return;
    }
    const started = Date.now();
    // http.get throws synchronously for a bad URL (e.g. an https:// target or a
    // malformed value), which would otherwise reject this promise with no handler
    // and hang the request. Catch it so the page reports "Unreachable" instead.
    let req;
    try {
      req = http.get(url, { timeout: 2000 }, (res) => {
      // Capture a small snippet of the response body so the page can show what the
      // private target actually returned (proof of a real response, not just a status).
      let body = '';
      res.setEncoding('utf8');
      res.on('data', (chunk) => {
        if (body.length < 512) body += chunk;
      });
      res.on('end', () => {
        resolve({
          configured: true, ok: true, status: res.statusCode, ms: Date.now() - started,
          contentType: res.headers['content-type'] || '(none)',
          bytes: Number(res.headers['content-length']) || Buffer.byteLength(body),
          snippet: body.slice(0, 300).trim(),
        });
      });
      });
    } catch (err) {
      resolve({ configured: true, ok: false, detail: err.message });
      return;
    }
    req.on('timeout', () => {
      req.destroy();
      resolve({ configured: true, ok: false, detail: 'timeout (check routing / security groups)' });
    });
    req.on('error', (err) => {
      resolve({ configured: true, ok: false, detail: err.message });
    });
  });
}

// Renders a self-contained styled HTML page (inline CSS, no dependencies) showing
// the VPC-egress probe result.
function renderPage({ appName, probe, host, port }) {
  // Derive a human status + accent color from the probe result.
  let statusText, statusDetail, accent, badgeBg, badgeFg, badgeText;
  if (!probe.configured) {
    statusText = 'Not configured';
    statusDetail = 'Set INTERNAL_TARGET_URL to probe a private endpoint in your VPC';
    accent = '#8a6b05'; badgeBg = '#fff4ce'; badgeFg = '#8a6b05';
    badgeText = 'Set INTERNAL_TARGET_URL to test VPC egress';
  } else if (probe.ok) {
    statusText = 'Reachable';
    statusDetail = `HTTP ${probe.status} in ${probe.ms} ms via VPC egress`;
    accent = '#1b7e3f'; badgeBg = '#e8f5e9'; badgeFg = '#1b7e3f';
    badgeText = '\u26A1 Private resource reached through your VPC';
  } else {
    statusText = 'Unreachable';
    statusDetail = probe.detail || 'request failed';
    accent = '#d13212'; badgeBg = '#fdecea'; badgeFg = '#b02a0d';
    badgeText = 'Check subnet routing and security group rules';
  }

  // Escape untrusted response text before embedding it in the page.
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  // On a reachable target, show WHAT it returned: content-type, size, and a body
  // snippet. This block is empty for the other two states.
  let responseBlock = '';
  if (probe.ok) {
    const snippet = probe.snippet ? esc(probe.snippet) : '(empty response body)';
    responseBlock = `
      <div class="resp">
        <div class="resp__head">Response from private target</div>
        <dl class="resp__meta">
          <dt>Status</dt><dd>HTTP ${probe.status}</dd>
          <dt>Latency</dt><dd>${probe.ms} ms</dd>
          <dt>Content-Type</dt><dd>${esc(probe.contentType)}</dd>
          <dt>Size</dt><dd>${probe.bytes} bytes</dd>
        </dl>
        <pre class="resp__body">${snippet}</pre>
      </div>`;
  }
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lambda Web Function + VPC egress</title>
<style>
  :root { color-scheme: light dark; }
  * { box-sizing: border-box; }
  body {
    margin: 0; min-height: 100vh; display: flex; align-items: center; justify-content: center;
    font-family: "Amazon Ember", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: linear-gradient(135deg, #232f3e 0%, #0f1b2d 100%); color: #0f141a; padding: 40px;
  }
  .card {
    width: 100%; max-width: 900px; background: #ffffff; border-radius: 20px;
    box-shadow: 0 24px 72px rgba(0,0,0,.35); overflow: hidden;
  }
  .card__header { padding: 48px 56px; background: linear-gradient(135deg, #ff9900 0%, #ec7211 100%); color: #1a1109; }
  .card__header h1 { margin: 0; font-size: 40px; line-height: 1.15; }
  .card__header p { margin: 14px 0 0; font-size: 19px; opacity: .9; }
  .card__body { padding: 48px 56px 56px; }
  .stat {
    display: flex; align-items: baseline; gap: 20px; padding: 36px 40px; border-radius: 16px;
    background: #f1f6fb; border: 1px solid #e3edf6; margin-bottom: 28px;
  }
  .stat__num { font-size: 56px; font-weight: 700; color: ${accent}; line-height: 1; white-space: nowrap; }
  .stat__label { font-size: 20px; color: #44515e; line-height: 1.35; }
  .meta { display: grid; grid-template-columns: auto 1fr; gap: 12px 28px; font-size: 18px; color: #44515e; }
  .meta dt { font-weight: 600; color: #232f3e; }
  .meta dd { margin: 0; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
  .resp { margin: 28px 0; padding: 28px 32px; border-radius: 16px; background: #f6fbf7; border: 1px solid #cfe9d8; }
  .resp__head { font-size: 18px; font-weight: 700; color: #1b7e3f; margin-bottom: 18px; }
  .resp__meta { display: grid; grid-template-columns: auto 1fr; gap: 10px 28px; font-size: 17px; color: #44515e; margin: 0 0 20px; }
  .resp__meta dt { font-weight: 600; color: #232f3e; }
  .resp__meta dd { margin: 0; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
  .resp__body {
    margin: 0; padding: 18px 20px; border-radius: 10px; background: #0f1b2d; color: #e8f0f8;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 15px; line-height: 1.5;
    white-space: pre-wrap; word-break: break-word; max-height: 220px; overflow: auto;
  }
  .badge { display: inline-block; margin-top: 32px; padding: 10px 20px; border-radius: 999px;
    background: ${badgeBg}; color: ${badgeFg}; font-size: 17px; font-weight: 600; }
</style>
</head>
<body>
  <div class="card">
    <div class="card__header">
      <h1>Hello from AWS&nbsp;!</h1>
      <p>AWS Lambda Web Function with private VPC egress via a network connector</p>
    </div>
    <div class="card__body">
      <div class="stat">
        <span class="stat__num">${statusText}</span>
        <span class="stat__label">internal target<br>${statusDetail}</span>
      </div>
      ${responseBlock}
      <dl class="meta">
        <dt>App</dt><dd>${appName}</dd>
        <dt>Egress</dt><dd>VPC network connector (ENIs in your subnets)</dd>
        <dt>Listening on</dt><dd>${host}:${port}</dd>
      </dl>
      <span class="badge">${badgeText}</span>
    </div>
  </div>
</body>
</html>`;
}

const server = http.createServer(async (req, res) => {
  const probe = await probeInternalTarget(INTERNAL_TARGET_URL);
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(renderPage({ appName: APP_NAME, probe, host: HOST, port: PORT }));
});

server.listen(PORT, HOST, () => {
  console.log(`[${APP_NAME}] Web Function HTTP server listening on ${HOST}:${PORT}`);
});
