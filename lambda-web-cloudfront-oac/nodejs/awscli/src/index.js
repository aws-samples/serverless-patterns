import http from 'node:http';
import crypto from 'node:crypto';

// The Lambda Web runtime sets AWS_LAMBDA_HTTP_ENDPOINT (0.0.0.0:3000). When it is
// absent we are running locally, so bind loopback only.
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? `127.0.0.1:${process.env.PORT || 3000}`).split(':');
const PORT = Number(PORT_STR) || 3000;
const AWS_REGION = process.env.AWS_REGION || 'local';

// Stable for the life of this execution environment.
const INSTANCE_ID = crypto.randomUUID().slice(0, 8);

const CLOUDFRONT_HEADERS = [
  'cloudfront-viewer-country',
  'cloudfront-viewer-city',
  'cloudfront-is-mobile-viewer',
  'cloudfront-is-desktop-viewer',
  'cloudfront-forwarded-proto',
  'via',
  'x-amz-cf-id',
];

function sendJson(res, status, body, headers = {}) {
  res.writeHead(status, { 'Content-Type': 'application/json', ...headers });
  res.end(JSON.stringify(body, null, 2));
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host ?? 'localhost'}`);

  // Cached at the edge for 60 seconds. Repeat requests within that window are
  // served by CloudFront without reaching this function.
  if (url.pathname === '/' || url.pathname === '/cached') {
    return sendJson(res, 200, {
      message: 'Served by a Lambda Web Function behind CloudFront',
      generatedAt: new Date().toISOString(),
      region: AWS_REGION,
      instanceId: INSTANCE_ID,
    }, { 'Cache-Control': 'public, max-age=60' });
  }

  // Never cached: shows what reaches the origin on every request.
  if (url.pathname === '/whoami') {
    const cloudfront = Object.fromEntries(
      CLOUDFRONT_HEADERS.filter((h) => h in req.headers).map((h) => [h, req.headers[h]]),
    );
    return sendJson(res, 200, {
      generatedAt: new Date().toISOString(),
      region: AWS_REGION,
      instanceId: INSTANCE_ID,
      // Lambda validated CloudFront's SigV4 signature before this request
      // reached the app and removed the Authorization header, so the app never
      // sees CloudFront's credentials and has no auth code of its own.
      viaCloudFront: 'x-amz-cf-id' in req.headers,
      authorizationHeaderPresent: 'authorization' in req.headers,
      cloudfront,
    }, { 'Cache-Control': 'no-store' });
  }

  sendJson(res, 404, { error: 'Not found' });
});

server.listen(PORT, HOST, () => {
  console.log(`Listening on http://${HOST}:${PORT} (region: ${AWS_REGION})`);
});

process.on('SIGTERM', () => server.close(() => process.exit(0)));
