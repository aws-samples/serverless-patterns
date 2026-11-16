import http from 'http';
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// ── Lambda Web runtime sets AWS_LAMBDA_HTTP_ENDPOINT (0.0.0.0:3000); PORT is a local-dev fallback ──
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? `0.0.0.0:${process.env.PORT || 3000}`).split(':');
const PORT = Number(PORT_STR) || 3000;
const AWS_REGION = process.env.AWS_REGION || 'local';

// ── Metrics state ──
const startTime = Date.now();
// Per-process id: unique to THIS execution environment. It changes whenever the
// platform recycles the environment (new process) — a truthful "which instance
// am I on" signal for the demo, without depending on an undocumented env var.
const INSTANCE_ID = crypto.randomUUID().slice(0, 8);
let totalRequests = 0;
let peakConnections = 0;
const clients = new Set();

// Baseline for computing per-interval CPU (process.cpuUsage returns cumulative µs).
let lastCpu = process.cpuUsage();   // { user, system } in microseconds
let lastCpuAt = Date.now();

// ── REAL metrics generator ──
// Every value here is measured from this Node process, no synthetic data. The
// point of the demo is the CONTRAST: the environment is alive for the full
// wall-clock uptime, but it only consumes a tiny amount of CPU. Cross-check the
// cpuMs figures against the platform's `invokeSummary` logs — same story.
function generateMetrics() {
  const now = Date.now();
  const uptimeSeconds = Math.floor((now - startTime) / 1000);

  // Cumulative CPU consumed by this process since it started (seconds).
  const cpuNow = process.cpuUsage(); // cumulative µs
  const cpuSecondsTotal = (cpuNow.user + cpuNow.system) / 1e6;

  // CPU used in just the last interval (µs -> ms), and as a % of wall-clock.
  const intervalUs = (cpuNow.user + cpuNow.system) - (lastCpu.user + lastCpu.system);
  const intervalMs = intervalUs / 1000;
  const wallMs = now - lastCpuAt;
  const cpuPercent = wallMs > 0 ? Math.min(100, (intervalMs / wallMs) * 100) : 0;
  lastCpu = cpuNow;
  lastCpuAt = now;

  const mem = process.memoryUsage();

  return {
    timestamp: new Date(now).toISOString(),
    region: AWS_REGION,
    instanceId: INSTANCE_ID,
    uptime: uptimeSeconds,
    activeConnections: clients.size,
    peakConnections,
    totalRequests,
    // ── real measurements ──
    cpuSecondsTotal: Number(cpuSecondsTotal.toFixed(3)), // climbs slowly
    cpuMsInterval: Number(intervalMs.toFixed(1)),        // per-2s CPU, wiggles
    cpuPercent: Number(cpuPercent.toFixed(2)),           // active CPU % this interval
    rssMB: Number((mem.rss / 1048576).toFixed(1)),       // resident memory
    heapMB: Number((mem.heapUsed / 1048576).toFixed(1)),
  };
}

// ── Broadcast to all SSE clients ──
function broadcast(data) {
  const payload = `data: ${JSON.stringify(data)}\n\n`;
  for (const client of clients) {
    try {
      client.write(payload);
    } catch {
      clients.delete(client);
    }
  }
}

// Push metrics every 2 seconds
const metricsInterval = setInterval(() => {
  if (clients.size > 0) {
    broadcast(generateMetrics());
  }
}, 2000);

// ── Static file serving ──
const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
};

function serveStatic(res, filePath) {
  const ext = path.extname(filePath);
  const mime = MIME_TYPES[ext] || 'application/octet-stream';

  try {
    const content = fs.readFileSync(filePath);
    res.writeHead(200, { 'Content-Type': mime });
    res.end(content);
  } catch {
    res.writeHead(404, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Not found' }));
  }
}

// ── HTTP Server ──
const server = http.createServer((req, res) => {
  totalRequests++;
  const url = new URL(req.url, `http://${HOST}:${PORT}`);

  // ── SSE endpoint ──
  if (url.pathname === '/api/events' && req.method === 'GET') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': '*',
    });

    clients.add(res);
    peakConnections = Math.max(peakConnections, clients.size);

    // Send initial snapshot immediately
    const initial = generateMetrics();
    res.write(`data: ${JSON.stringify(initial)}\n\n`);

    req.on('close', () => {
      clients.delete(res);
    });

    return;
  }

  // ── Real CPU work (for the demo) ──
  // Does genuine work — repeated SHA-256 hashing for ~`ms` milliseconds — so the
  // CPU line MOVES because actual work happened, not because of synthetic data.
  // Trigger it from the UI ("Generate load") or curl: GET /api/work?ms=1500
  if (url.pathname === '/api/work' && req.method === 'GET') {
    const ms = Math.min(5000, Math.max(50, Number(url.searchParams.get('ms')) || 1000));
    const started = Date.now();
    let iterations = 0;
    let buf = crypto.randomBytes(1024);
    // Busy-hash until the time budget elapses. This is real CPU on the event loop.
    while (Date.now() - started < ms) {
      for (let i = 0; i < 500; i++) {
        buf = crypto.createHash('sha256').update(buf).digest();
        iterations++;
      }
    }
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ranMs: Date.now() - started, iterations, instanceId: INSTANCE_ID, region: AWS_REGION }));
    return;
  }

  // ── Ping: tiny response for client-measured round-trip latency ──
  // The browser times a request here to show network latency to the serving
  // region. When deployed MultiRegion, a nearer region shows lower latency.
  if (url.pathname === '/api/ping' && req.method === 'GET') {
    res.writeHead(200, {
      'Content-Type': 'application/json',
      'Cache-Control': 'no-store',
      'Access-Control-Allow-Origin': '*',
    });
    res.end(JSON.stringify({ region: AWS_REGION, instanceId: INSTANCE_ID, t: Date.now() }));
    return;
  }

  // ── Status endpoint ──
  if (url.pathname === '/api/status' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(generateMetrics()));
    return;
  }

  // ── Static files ──
  let filePath = url.pathname === '/'
    ? path.join(__dirname, 'public', 'index.html')
    : path.join(__dirname, 'public', url.pathname);

  serveStatic(res, filePath);
});

server.listen(PORT, HOST, () => {
  console.log(`SSE Dashboard listening on ${HOST}:${PORT}`);
  console.log(`Region: ${AWS_REGION}`);
});

// ── Graceful shutdown ──
process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down...');
  clearInterval(metricsInterval);

  // Close all SSE connections
  for (const client of clients) {
    try { client.end(); } catch {}
  }
  clients.clear();

  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});
