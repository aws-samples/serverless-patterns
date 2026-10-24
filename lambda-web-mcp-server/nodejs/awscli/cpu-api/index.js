import http from 'node:http';
import crypto from 'node:crypto';

// ── A plain HTTP API with no MCP in it: this stands in for a service you
// already run. Its endpoint uses IamAuth, so Lambda Web only forwards requests
// signed by a principal with lambda:InvokeWebFunctionEndpoint. The code itself
// does no authentication, and Lambda Web removes the Authorization header
// after validating the signature.

// The Lambda Web runtime sets AWS_LAMBDA_HTTP_ENDPOINT. Locally, bind loopback.
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? `127.0.0.1:${process.env.PORT || 3001}`).split(':');
const PORT = Number(PORT_STR) || 3001;
const AWS_REGION = process.env.AWS_REGION || 'local';

// Stable for the life of this execution environment.
const INSTANCE_ID = crypto.randomUUID().slice(0, 8);

const MAX_WORK_SECONDS = 20;
const SLICE_MS = 50;

function sendJson(res, status, body) {
  res.writeHead(status, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(body));
}

async function readJson(req) {
  let body = '';
  for await (const chunk of req) {
    body += chunk;
    if (body.length > 10_000) throw new Error('Body too large');
  }
  return body ? JSON.parse(body) : {};
}

// POST /work {"seconds": 5}
// Streams newline-delimited JSON: one progress line per second of work, then
// one result line.
async function handleWork(req, res) {
  let seconds;
  try {
    ({ seconds } = await readJson(req));
  } catch {
    return sendJson(res, 400, { error: 'Body must be JSON' });
  }
  if (!Number.isInteger(seconds) || seconds < 1 || seconds > MAX_WORK_SECONDS) {
    return sendJson(res, 400, { error: `seconds must be an integer from 1 to ${MAX_WORK_SECONDS}` });
  }

  // Stop working if the caller goes away (for example, the MCP client cancels).
  let closed = false;
  res.on('close', () => { closed = true; });

  res.writeHead(200, { 'Content-Type': 'application/x-ndjson', 'Cache-Control': 'no-cache' });

  const targetMs = seconds * 1000;
  const startedAt = Date.now();
  let workMs = 0;
  let hashes = 0;
  let reported = 0;
  let buf = crypto.randomBytes(1024);

  while (workMs < targetMs && !closed) {
    // Hash for one short slice, then yield so this environment keeps serving
    // its other concurrent requests and the progress lines go out on time.
    const sliceStart = performance.now();
    while (performance.now() - sliceStart < SLICE_MS) {
      for (let i = 0; i < 200; i++) buf = crypto.createHash('sha256').update(buf).digest();
      hashes += 200;
    }
    workMs += performance.now() - sliceStart;
    await new Promise((resolve) => setImmediate(resolve));

    const done = Math.min(seconds, Math.floor(workMs / 1000));
    if (done > reported) {
      reported = done;
      res.write(JSON.stringify({ type: 'progress', second: done, total: seconds, hashes }) + '\n');
    }
  }
  if (closed) return;

  res.end(JSON.stringify({
    type: 'result',
    requestedSeconds: seconds,
    hashes,
    hashesPerSecond: Math.round(hashes / (workMs / 1000)),
    elapsedMs: Date.now() - startedAt,
    region: AWS_REGION,
    instanceId: INSTANCE_ID,
  }) + '\n');
}

const server = http.createServer((req, res) => {
  const { pathname } = new URL(req.url, 'http://localhost');

  if (pathname === '/work' && req.method === 'POST') {
    handleWork(req, res).catch((err) => {
      console.error('Work request failed:', err);
      if (!res.headersSent) sendJson(res, 500, { error: 'Internal error' });
      else res.end();
    });
    return;
  }
  if (pathname === '/' && req.method === 'GET') {
    return sendJson(res, 200, { name: 'lambda-web-cpu-api', region: AWS_REGION, instanceId: INSTANCE_ID });
  }
  sendJson(res, 404, { error: 'Not found' });
});

server.listen(PORT, HOST, () => {
  console.log(`CPU API listening on http://${HOST}:${PORT} (region: ${AWS_REGION})`);
});

process.on('SIGTERM', () => server.close(() => process.exit(0)));
