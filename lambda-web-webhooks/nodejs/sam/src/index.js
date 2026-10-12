import http from 'http';
import express from 'express';
import crypto from 'crypto';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand, GetCommand, ScanCommand } from '@aws-sdk/lib-dynamodb';
import { verifiers, generateSignature } from './lib/verify.js';

// ── Config ──
// The Lambda Web Functions runtime sets AWS_LAMBDA_HTTP_ENDPOINT (0.0.0.0:3000);
// the fallback is for local development.
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? '0.0.0.0:3000').split(':');
const PORT = Number(PORT_STR) || 3000;
const AWS_REGION = process.env.AWS_REGION || 'local';
const TABLE_NAME = process.env.TABLE_NAME; // set by the SAM template
const EVENT_TTL_DAYS = Number(process.env.EVENT_TTL_DAYS || 30);
const ENABLE_TEST_ENDPOINT = process.env.ENABLE_TEST_ENDPOINT === 'true';
if (!TABLE_NAME) {
  console.error('TABLE_NAME environment variable is required');
  process.exit(1);
}

// One shared secret per provider, injected by the template. In production
// load them from AWS Secrets Manager or SSM Parameter Store at startup.
const SECRETS = {
  stripe: process.env.STRIPE_WEBHOOK_SECRET,
  github: process.env.GITHUB_WEBHOOK_SECRET,
  generic: process.env.GENERIC_WEBHOOK_SECRET,
};

// ── DynamoDB (one client per sandbox, reused across requests) ──
const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

// ── Express app ──
const app = express();

// Signatures are computed over the exact bytes the provider sent, so the
// webhook route must see the raw body. Other routes use JSON parsing.
app.use('/webhooks', express.raw({ type: '*/*', limit: '1mb' }));
app.use(express.json());

let totalEvents = 0;

// ── Webhook receiver ──
app.post('/webhooks/:provider', async (req, res) => {
  const { provider } = req.params;
  const verifier = verifiers[provider];
  if (!verifier) {
    return res.status(400).json({ error: `Unknown provider: ${provider}`, supported: Object.keys(verifiers) });
  }
  const secret = SECRETS[provider];
  if (!secret) {
    return res.status(500).json({ error: `No secret configured for ${provider}` });
  }

  const rawBody = Buffer.isBuffer(req.body) ? req.body.toString('utf8') : '';

  // 1. Verify the HMAC signature (timing-safe) before touching the payload.
  const result = verifier(rawBody, req.headers, secret);
  if (!result.valid) {
    return res.status(401).json({ error: 'Invalid signature', provider, detail: result.error || 'Signature mismatch' });
  }

  // 2. Parse the payload.
  let payload;
  try {
    payload = JSON.parse(rawBody);
  } catch {
    return res.status(400).json({ error: 'Invalid JSON payload' });
  }

  // 3. Derive a stable event id per provider so retries are recognised.
  const providerEventId =
    (provider === 'github' && req.headers['x-github-delivery']) || payload.id || crypto.randomUUID();
  const eventType = payload.type || payload.action || (provider === 'github' && req.headers['x-github-event']) || 'unknown';

  const event = {
    eventId: `${provider}:${providerEventId}`,
    provider,
    eventType,
    payload,
    receivedAt: new Date().toISOString(),
    region: AWS_REGION,
    // DynamoDB TTL (epoch seconds): events expire automatically.
    ttl: Math.floor(Date.now() / 1000) + EVENT_TTL_DAYS * 86400,
  };

  // 4. Store once. attribute_not_exists makes redelivery idempotent.
  try {
    await docClient.send(new PutCommand({
      TableName: TABLE_NAME,
      Item: event,
      ConditionExpression: 'attribute_not_exists(eventId)',
    }));
    totalEvents++;
    res.status(200).json({ success: true, eventId: event.eventId, provider, eventType, receivedAt: event.receivedAt });
  } catch (err) {
    if (err.name === 'ConditionalCheckFailedException') {
      // Already processed: acknowledge with 200 so the provider stops retrying.
      return res.status(200).json({ success: true, eventId: event.eventId, duplicate: true, message: 'Event already processed' });
    }
    console.error('Error storing event:', err);
    res.status(500).json({ error: 'Failed to store event' });
  }
});

// ── Read back stored events ──
app.get('/events', async (req, res) => {
  const limit = Math.min(parseInt(req.query.limit || '20', 10), 100);
  try {
    const { Items, LastEvaluatedKey } = await docClient.send(new ScanCommand({ TableName: TABLE_NAME, Limit: limit }));
    res.json({ count: Items.length, events: Items, lastKey: LastEvaluatedKey || null });
  } catch (err) {
    console.error('Error listing events:', err);
    res.status(500).json({ error: 'Failed to list events' });
  }
});

app.get('/events/:eventId', async (req, res) => {
  try {
    const { Item } = await docClient.send(new GetCommand({ TableName: TABLE_NAME, Key: { eventId: req.params.eventId } }));
    if (!Item) return res.status(404).json({ error: 'Event not found' });
    res.json(Item);
  } catch (err) {
    console.error('Error getting event:', err);
    res.status(500).json({ error: 'Failed to get event' });
  }
});

// ── Test helper: build a correctly signed request for a provider ──
// Enabled only when ENABLE_TEST_ENDPOINT=true. It signs with the real
// secret, so it must be off wherever real webhooks are accepted.
if (ENABLE_TEST_ENDPOINT) {
  app.post('/test/fire', (req, res) => {
    const { provider = 'generic', eventType = 'test.event' } = req.body || {};
    const secret = SECRETS[provider];
    if (!secret) return res.status(400).json({ error: `Unknown provider: ${provider}`, supported: Object.keys(verifiers) });

    const payload = JSON.stringify({
      id: crypto.randomUUID(),
      type: eventType,
      data: { message: 'This is a test webhook', timestamp: new Date().toISOString() },
    });
    const sig = generateSignature(provider, payload, secret);
    res.json({
      instruction: `POST /webhooks/${provider}`,
      headers: { 'Content-Type': 'application/json', [sig.header]: sig.value },
      body: JSON.parse(payload),
    });
  });
}

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    providers: Object.keys(SECRETS).filter((p) => SECRETS[p]),
    testEndpoint: ENABLE_TEST_ENDPOINT,
    totalEventsProcessed: totalEvents,
    region: AWS_REGION,
    tableName: TABLE_NAME,
    timestamp: new Date().toISOString(),
  });
});

app.use((req, res) => {
  res.status(404).json({ error: 'Not found', path: req.path, endpoints: ['POST /webhooks/:provider', 'GET /events', 'GET /events/:eventId', 'GET /health'] });
});

// ── Start server ──
const server = http.createServer(app);
server.listen(PORT, HOST, () => {
  console.log(`Webhook ingestion listening on ${HOST}:${PORT} (table: ${TABLE_NAME}, region: ${AWS_REGION})`);
});

process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down gracefully');
  server.close(() => process.exit(0));
});
