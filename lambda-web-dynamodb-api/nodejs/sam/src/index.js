import http from 'http';
import express from 'express';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, GetCommand, PutCommand, UpdateCommand, ScanCommand } from '@aws-sdk/lib-dynamodb';

// The SAM template passes the table name as an environment variable.
// AWS_REGION is set by the Lambda Web Functions runtime.
const TABLE_NAME = process.env.TABLE_NAME;
const AWS_REGION = process.env.AWS_REGION || 'local';
if (!TABLE_NAME) {
  console.error('TABLE_NAME environment variable is required');
  process.exit(1);
}

// The SDK client is created once per sandbox and reused across requests.
// Credentials come from the function's execution role.
const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

const app = express();
app.use(express.json());

// Request logging: one line in, one line out, with the status and duration.
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    console.log(`${req.method} ${req.path} ${res.statusCode} ${Date.now() - start}ms`);
  });
  next();
});

app.get('/', (req, res) => {
  res.json({ message: 'Express on Lambda Web Functions', region: AWS_REGION, timestamp: new Date().toISOString() });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', region: AWS_REGION, tableName: TABLE_NAME, timestamp: new Date().toISOString() });
});

// Create an item. id and name are required; a duplicate id returns 409.
app.post('/items', async (req, res, next) => {
  try {
    const { id, name, description, metadata } = req.body ?? {};
    if (!id || !name) {
      return res.status(400).json({ error: 'id and name are required', received: { id: !!id, name: !!name } });
    }
    const now = new Date().toISOString();
    const item = {
      id,
      name,
      description: description ?? '',
      metadata: metadata ?? {},
      createdAt: now,
      updatedAt: now,
      createdInRegion: AWS_REGION,
    };
    await docClient.send(new PutCommand({
      TableName: TABLE_NAME,
      Item: item,
      ConditionExpression: 'attribute_not_exists(id)',
    }));
    res.status(201).json({ item, createdIn: AWS_REGION });
  } catch (err) {
    if (err.name === 'ConditionalCheckFailedException') {
      return res.status(409).json({ error: 'Item already exists', id: req.body.id });
    }
    next(err);
  }
});

// Read one item.
app.get('/items/:id', async (req, res, next) => {
  try {
    const result = await docClient.send(new GetCommand({ TableName: TABLE_NAME, Key: { id: req.params.id } }));
    if (!result.Item) {
      return res.status(404).json({ error: 'Item not found', id: req.params.id });
    }
    res.json({ item: result.Item, servedFrom: AWS_REGION });
  } catch (err) {
    next(err);
  }
});

// Update name, description and/or metadata of an existing item.
app.put('/items/:id', async (req, res, next) => {
  try {
    const { name, description, metadata } = req.body ?? {};
    const sets = ['updatedAt = :updatedAt', 'lastUpdatedInRegion = :region'];
    const names = {};
    const values = { ':updatedAt': new Date().toISOString(), ':region': AWS_REGION };
    if (name !== undefined) { sets.push('#name = :name'); names['#name'] = 'name'; values[':name'] = name; }
    if (description !== undefined) { sets.push('description = :description'); values[':description'] = description; }
    if (metadata !== undefined) { sets.push('metadata = :metadata'); values[':metadata'] = metadata; }

    const result = await docClient.send(new UpdateCommand({
      TableName: TABLE_NAME,
      Key: { id: req.params.id },
      UpdateExpression: `SET ${sets.join(', ')}`,
      ConditionExpression: 'attribute_exists(id)',
      ExpressionAttributeNames: Object.keys(names).length ? names : undefined,
      ExpressionAttributeValues: values,
      ReturnValues: 'ALL_NEW',
    }));
    res.json({ item: result.Attributes, updatedIn: AWS_REGION });
  } catch (err) {
    if (err.name === 'ConditionalCheckFailedException') {
      return res.status(404).json({ error: 'Item not found', id: req.params.id });
    }
    next(err);
  }
});

// List items with cursor pagination (?limit=20&lastKey=<url-encoded JSON>).
app.get('/items', async (req, res, next) => {
  try {
    const limit = Math.min(parseInt(req.query.limit, 10) || 20, 100);
    const lastKey = req.query.lastKey ? JSON.parse(req.query.lastKey) : undefined;
    const result = await docClient.send(new ScanCommand({ TableName: TABLE_NAME, Limit: limit, ExclusiveStartKey: lastKey }));
    res.json({ items: result.Items ?? [], count: result.Count ?? 0, lastKey: result.LastEvaluatedKey, servedFrom: AWS_REGION });
  } catch (err) {
    next(err);
  }
});

app.use((req, res) => {
  res.status(404).json({ error: 'Not found', path: req.path, method: req.method });
});

app.use((err, req, res, _next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

// The Lambda Web Functions runtime sets AWS_LAMBDA_HTTP_ENDPOINT (0.0.0.0:3000)
// and waits for the app to listen there. The fallback is for local development.
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? '0.0.0.0:3000').split(':');
const PORT = Number(PORT_STR) || 3000;

const server = http.createServer(app);
server.listen(PORT, HOST, () => {
  console.log(`Express API listening on ${HOST}:${PORT} (table: ${TABLE_NAME}, region: ${AWS_REGION})`);
});

process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down gracefully');
  server.close(() => process.exit(0));
});
