import http from 'node:http';
import crypto from 'node:crypto';
import * as z from 'zod/v4';
import { createMcpHandler, McpServer } from '@modelcontextprotocol/server';
import {
  toNodeHandler,
  localhostHostValidation,
  localhostOriginValidation,
} from '@modelcontextprotocol/node';
import { SignatureV4 } from '@smithy/signature-v4';
import { Sha256 } from '@aws-crypto/sha256-js';
import { defaultProvider } from '@aws-sdk/credential-provider-node';

// ── Lambda Web runtime sets AWS_LAMBDA_HTTP_ENDPOINT (0.0.0.0:3000). When it is
// absent we are running locally, so bind loopback only and turn on the SDK's
// Host/Origin guards against DNS rebinding.
const ON_LAMBDA = Boolean(process.env.AWS_LAMBDA_HTTP_ENDPOINT);
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? `127.0.0.1:${process.env.PORT || 3000}`).split(':');
const PORT = Number(PORT_STR) || 3000;
const AWS_REGION = process.env.AWS_REGION || 'local';
const INSTANCE_ID = crypto.randomUUID().slice(0, 8);

// ── Backend API. On Lambda this is the CPU API's IamAuth endpoint, for example
// https://<id>.lambda-web.us-east-1.on.aws. Locally it is the CPU API on
// http://127.0.0.1:3001, and plain http requests are sent unsigned.
const BACKEND_URL = new URL(process.env.BACKEND_URL || 'http://127.0.0.1:3001');
const MAX_WORK_SECONDS = 20;

// ── SigV4 signer, created once per execution environment. Lambda Web has no
// SDK client for invoking endpoints: you sign a normal HTTPS request with the
// service name "lambda". The credentials are this function's execution role,
// which has lambda:InvokeWebFunctionEndpoint on the backend endpoint.
const signer = new SignatureV4({
  service: 'lambda',
  region: AWS_REGION,
  credentials: defaultProvider(),
  sha256: Sha256,
});

async function callBackend(path, payload, signal) {
  const url = new URL(path, BACKEND_URL);
  const body = JSON.stringify(payload);
  let headers = { 'content-type': 'application/json' };

  if (url.protocol === 'https:') {
    const signed = await signer.sign({
      method: 'POST',
      protocol: url.protocol,
      hostname: url.hostname,
      path: url.pathname,
      headers: {
        ...headers,
        host: url.hostname,
        // Lambda Web rejects requests without this header. The body is small,
        // so sign its hash rather than sending UNSIGNED-PAYLOAD.
        'x-amz-content-sha256': crypto.createHash('sha256').update(body).digest('hex'),
      },
      body,
    });
    headers = signed.headers;
  }

  return fetch(url, { method: 'POST', headers, body, signal });
}

// Yield each JSON object from a newline-delimited JSON response body.
async function* readNdjson(stream) {
  let buf = '';
  for await (const chunk of stream.pipeThrough(new TextDecoderStream())) {
    buf += chunk;
    let i;
    while ((i = buf.indexOf('\n')) >= 0) {
      const line = buf.slice(0, i).trim();
      buf = buf.slice(i + 1);
      if (line) yield JSON.parse(line);
    }
  }
  if (buf.trim()) yield JSON.parse(buf);
}

// ── MCP server factory. createMcpHandler builds a fresh McpServer per HTTP
// request, which is what makes concurrent requests in one environment safe.
function buildServer() {
  const server = new McpServer({ name: 'lambda-web-mcp-server', version: '1.0.0' });

  server.registerTool(
    'get_current_time',
    {
      description: 'Get the current date and time, optionally in a given IANA time zone (for example Europe/London).',
      inputSchema: z.object({
        timeZone: z.string().optional().describe('IANA time zone name. Defaults to UTC.'),
      }),
    },
    async ({ timeZone = 'UTC' }) => {
      const now = new Date();
      let local;
      try {
        local = new Intl.DateTimeFormat('en-GB', { timeZone, dateStyle: 'full', timeStyle: 'long' }).format(now);
      } catch {
        return { isError: true, content: [{ type: 'text', text: `Unknown time zone: ${timeZone}` }] };
      }
      const result = { iso: now.toISOString(), timeZone, local };
      return { content: [{ type: 'text', text: JSON.stringify(result) }], structuredContent: result };
    },
  );

  server.registerTool(
    'run_cpu_work',
    {
      description:
        'Run CPU-bound work (repeated SHA-256 hashing) on a backend API for a number of seconds, streaming progress every second, ' +
        'and report how many hashes were computed, the hash rate, the elapsed time and which execution environments handled it.',
      inputSchema: z.object({
        seconds: z.number().int().min(1).max(MAX_WORK_SECONDS).default(5).describe(`Seconds of CPU work to run (1-${MAX_WORK_SECONDS}).`),
      }),
    },
    async ({ seconds }, ctx) => {
      const progressToken = ctx.mcpReq._meta?.progressToken;
      const fail = (text) => ({ isError: true, content: [{ type: 'text', text }] });

      let res;
      try {
        // Passing the MCP request's abort signal means a client cancel also
        // closes the backend connection, which stops the backend's work.
        res = await callBackend('/work', { seconds }, ctx.mcpReq.signal);
      } catch (err) {
        return fail(ctx.mcpReq.signal.aborted ? 'Cancelled' : `Backend request failed: ${err.message}`);
      }
      if (!res.ok) return fail(`Backend returned ${res.status}: ${await res.text()}`);

      // Relay each backend progress line as an MCP progress notification.
      let backend;
      try {
        for await (const msg of readNdjson(res.body)) {
          if (msg.type === 'progress' && progressToken !== undefined) {
            await ctx.mcpReq.notify({
              method: 'notifications/progress',
              params: {
                progressToken,
                progress: msg.second,
                total: msg.total,
                message: `${msg.second} of ${msg.total} s: ${msg.hashes.toLocaleString('en-US')} hashes`,
              },
            });
          } else if (msg.type === 'result') {
            backend = msg;
          }
        }
      } catch (err) {
        return fail(ctx.mcpReq.signal.aborted ? 'Cancelled' : `Backend stream failed: ${err.message}`);
      }
      if (!backend) return fail('Backend ended without a result');

      const { type, instanceId, ...work } = backend;
      const result = { ...work, backendInstanceId: instanceId, mcpInstanceId: INSTANCE_ID };
      return { content: [{ type: 'text', text: JSON.stringify(result) }], structuredContent: result };
    },
  );

  return server;
}

const mcpHandler = createMcpHandler(buildServer);
const handleMcp = toNodeHandler(mcpHandler);

const validateHost = ON_LAMBDA ? () => true : localhostHostValidation();
const validateOrigin = ON_LAMBDA ? () => true : localhostOriginValidation();

// ── HTTP server ──
const server = http.createServer((req, res) => {
  const { pathname } = new URL(req.url, 'http://localhost');

  if (pathname === '/mcp') {
    if (!validateHost(req, res) || !validateOrigin(req, res)) return;
    handleMcp(req, res).catch((err) => {
      console.error('MCP request failed:', err);
      if (!res.headersSent) res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'Internal error' }));
    });
    return;
  }

  if (pathname === '/' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ name: 'lambda-web-mcp-server', mcpEndpoint: '/mcp', region: AWS_REGION, instanceId: INSTANCE_ID }));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Not found' }));
});

server.listen(PORT, HOST, () => {
  console.log(`MCP server listening on http://${HOST}:${PORT}/mcp, backend ${BACKEND_URL.origin}`);
});

process.on('SIGTERM', async () => {
  await mcpHandler.close();
  server.close(() => process.exit(0));
});
