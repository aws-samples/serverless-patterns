// Lambda Web Function sample app.
//
// Unlike a classic Lambda event handler (which exports a `handler` and returns a
// { statusCode, body } object), a Web Function runs a standard HTTP server that
// listens on the port Lambda provides. You can drop in Express, Fastify, or Hono
// here with no adapters; this sample uses Node's built-in `http` module so the
// pattern deploys with no dependencies to install.
//
// This sample also demonstrates the headline Web Functions differentiator:
// a single warm execution environment serves MANY concurrent requests. We track
// the number of in-flight requests this environment is handling and return it in
// the response, so you can observe multi-concurrency directly (e.g. with a quick
// `ab`/`hey`/`curl` burst against the CloudFront domain).

import http from 'node:http';

// Lambda provides the exact host:port your server MUST bind to via
// AWS_LAMBDA_HTTP_ENDPOINT. You must listen on BOTH that host and that port --
// binding a different port, or only a loopback host, makes requests fail with a
// 502 (the runtime reports Application.TimeoutListenError). The fallback address
// applies only to local runs, where Lambda does not set the variable.
const [HOST, PORT] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:8080').split(':');

// Environment variables supplied via the revision's ServiceConfig.EnvironmentVariables.
const APP_NAME = process.env.APP_NAME || 'lambda-web-function';
const LOG_LEVEL = process.env.LOG_LEVEL || 'info';

// Number of requests currently being handled by THIS execution environment.
let inFlight = 0;
let peakInFlight = 0;

// Renders a small, self-contained styled HTML page (inline CSS, no dependencies,
// so the pattern still deploys with nothing to install). Shows the live and peak
// concurrent-request counts so the multi-concurrency behavior is visible in a browser.
function renderPage({ inFlight, peakInFlight, appName, host, port }) {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lambda Web Function + CloudFront OAC</title>
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
  .stat__num { font-size: 84px; font-weight: 700; color: #ec7211; line-height: 1; }
  .stat__label { font-size: 20px; color: #44515e; line-height: 1.35; }
  .stat__peak { margin-left: auto; font-size: 18px; color: #67748a; white-space: nowrap; }
  .meta { display: grid; grid-template-columns: auto 1fr; gap: 12px 28px; font-size: 18px; color: #44515e; }
  .meta dt { font-weight: 600; color: #232f3e; }
  .meta dd { margin: 0; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
  .badge { display: inline-block; margin-top: 32px; padding: 10px 20px; border-radius: 999px;
    background: #e8f5e9; color: #1b7e3f; font-size: 17px; font-weight: 600; }
</style>
</head>
<body>
  <div class="card">
    <div class="card__header">
      <h1>Hello from AWS&nbsp;!</h1>
      <p>Amazon CloudFront &rarr; Lambda Web Function, secured with Origin Access Control (OAC)</p>
    </div>
    <div class="card__body">
      <div class="stat">
        <span class="stat__num">${inFlight}</span>
        <span class="stat__label">concurrent request${inFlight === 1 ? '' : 's'}<br>in this execution environment</span>
        <span class="stat__peak">peak observed: ${peakInFlight}</span>
      </div>
      <dl class="meta">
        <dt>App</dt><dd>${appName}</dd>
        <dt>Served via</dt><dd>CloudFront + OAC (SigV4)</dd>
        <dt>Listening on</dt><dd>${host}:${port}</dd>
      </dl>
      <span class="badge">&#9889; One warm environment, many concurrent requests</span>
    </div>
  </div>
</body>
</html>`;
}

const server = http.createServer(async (req, res) => {
  inFlight += 1;
  peakInFlight = Math.max(peakInFlight, inFlight);
  try {
    // Simulate a short I/O wait (e.g. a DB or downstream call). Because the
    // environment handles requests concurrently, overlapping requests push
    // `inFlight` above 1 -- which you would never see on a one-request-per-
    // environment event function.
    await new Promise((resolve) => setTimeout(resolve, 200));

    if (LOG_LEVEL === 'debug') {
      console.log(`[${APP_NAME}] handled ${req.method} ${req.url} | inFlight=${inFlight} peak=${peakInFlight}`);
    }

    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(renderPage({ inFlight, peakInFlight, appName: APP_NAME, host: HOST, port: PORT }));
  } finally {
    inFlight -= 1;
  }
});

server.listen(PORT, HOST, () => {
  console.log(`[${APP_NAME}] Web Function HTTP server listening on ${HOST}:${PORT} (log level: ${LOG_LEVEL})`);
});
