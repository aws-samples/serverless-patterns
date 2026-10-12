import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// The Lambda Web Functions runtime sets AWS_LAMBDA_HTTP_ENDPOINT (0.0.0.0:3000)
// and waits for the app to listen there. The fallback is for local development.
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? '0.0.0.0:3000').split(':');
const PORT = Number(PORT_STR) || 3000;
const AWS_REGION = process.env.AWS_REGION || 'local';

// ── Metrics state (per sandbox: every sandbox keeps its own counters and clients) ──
const startTime = Date.now();
let totalRequests = 0;
let peakConnections = 0;
const clients = new Set();

// ── Synthetic metrics generator ──
function generateMetrics() {
  const uptimeSeconds = Math.floor((Date.now() - startTime) / 1000);
  const t = uptimeSeconds / 10;

  return {
    timestamp: new Date().toISOString(),
    region: AWS_REGION,
    uptime: uptimeSeconds,
    activeConnections: clients.size,
    peakConnections,
    totalRequests,
    // Synthetic workload metrics (sine waves with noise)
    cpuPercent: Math.max(0, Math.min(100, 40 + 30 * Math.sin(t) + (Math.random() - 0.5) * 20)),
    memoryMB: Math.max(50, Math.min(512, 180 + 60 * Math.sin(t * 0.7) + (Math.random() - 0.5) * 30)),
    requestsPerSec: Math.max(0, Math.floor(120 + 80 * Math.sin(t * 1.3) + (Math.random() - 0.5) * 40)),
    errorRate: Math.max(0, Math.min(5, 0.5 + 0.4 * Math.sin(t * 2.1) + Math.random() * 0.5)),
    p99Latency: Math.max(5, Math.floor(45 + 25 * Math.sin(t * 0.9) + (Math.random() - 0.5) * 15)),
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

const PUBLIC_DIR = path.join(__dirname, 'public');

function serveStatic(res, filePath) {
  // Never serve anything outside public/ (blocks ../ traversal).
  if (!filePath.startsWith(PUBLIC_DIR + path.sep)) {
    res.writeHead(404, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Not found' }));
    return;
  }
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

  // ── SSE endpoint: the response stays open and receives a broadcast every 2 s ──
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

  // ── POST custom metric injection ──
  if (url.pathname === '/api/metrics' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const custom = JSON.parse(body);
        broadcast({ ...generateMetrics(), custom });
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, broadcastTo: clients.size }));
      } catch {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON' }));
      }
    });
    return;
  }

  // ── Status endpoint ──
  if (url.pathname === '/api/status' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(generateMetrics()));
    return;
  }

  // ── Static files ──
  const filePath = url.pathname === '/'
    ? path.join(PUBLIC_DIR, 'index.html')
    : path.resolve(PUBLIC_DIR, '.' + path.posix.normalize(url.pathname));

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
