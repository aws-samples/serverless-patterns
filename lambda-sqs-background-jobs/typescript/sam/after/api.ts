/**
 * AFTER - the same Express job API, with the work moved to SQS + Lambda.
 *
 * POST /v1/jobs       -> write {job_id, status=PENDING}, send one SQS message,
 *                        return. The web process does NOT run the steps.
 * GET  /v1/jobs/{id}  -> read the row and return its status (unchanged)
 *
 * The API is unchanged in shape: same framework, same routes, same public
 * job_id, same status words. What changed is behind it. The POST now returns
 * after a single SQS SendMessage; a separate Lambda consumer (worker.ts) runs
 * the identical step code and writes progress back to the same table.
 *
 * Why this is better: the work no longer rides the web process. A deploy or
 * scale-in cannot strand a job - unacked SQS messages are redelivered, and a
 * poison message lands in a dead-letter queue instead of looping forever. The
 * API and the worker scale independently.
 *
 * Cutover: this reuses the SAME table and the SAME /v1 routes, so clients need
 * no change. Point all traffic at this version and old in-flight jobs finish
 * on the old box until the table is empty.
 */

import { Logger } from '@aws-lambda-powertools/logger';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { Tracer } from '@aws-lambda-powertools/tracer';
import { ConditionalCheckFailedException, DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DeleteCommand, DynamoDBDocumentClient, GetCommand, PutCommand } from '@aws-sdk/lib-dynamodb';
import { SendMessageCommand, SQSClient } from '@aws-sdk/client-sqs';
import type { APIGatewayProxyEvent, Context } from 'aws-lambda';
import express, { type Request, type Response } from 'express';
import { randomUUID } from 'node:crypto';
import serverless from 'serverless-http';

// Powertools: JSON logs with the Lambda context, X-Ray subsegments for every
// SDK call, and EMF metrics. Service name and namespace come from the
// POWERTOOLS_* env vars in template.yaml.
const logger = new Logger();
const tracer = new Tracer();
const metrics = new Metrics();

const table = process.env.JOBS_TABLE!;
const queueUrl = process.env.JOBS_QUEUE_URL!;
// SDK timeouts well inside the 10s function timeout, so a slow dependency
// surfaces as an SDK error (and a JSON 500) rather than a Lambda timeout.
// Two attempts at (2s connect + 5s request) worst case still fits.
const sdk = { maxAttempts: 2, requestHandler: { connectionTimeout: 2_000, requestTimeout: 5_000 } };
const ddb = DynamoDBDocumentClient.from(tracer.captureAWSv3Client(new DynamoDBClient(sdk)), {
  marshallOptions: { removeUndefinedValues: true },
});
const sqs = tracer.captureAWSv3Client(new SQSClient(sdk));

const TTL_SECONDS = 3 * 24 * 60 * 60;

type Body = Record<string, unknown>;

function rowToBody(jobId: string, item: Body): Body {
  const body: Body = { job_id: jobId, status: item.status, step: item.step ?? null };
  for (const k of ['result', 'error']) if (k in item) body[k] = item[k];
  return body;
}

const app = express();
// Parse the body as JSON whatever the Content-Type says (curl -d sends a form
// type), and bound it: API Gateway caps payloads anyway, but say so here.
app.use(express.json({ type: () => true, limit: '1mb' }));

app.use((req, res, next) => {
  res.on('finish', () => logger.info('request', { method: req.method, path: req.path, status: res.statusCode }));
  next();
});

app.post('/v1/jobs', async (req: Request, res: Response) => {
  const payload = req.body as Body;
  // express.json() yields {} for an empty body and an array for a JSON array.
  // Require a non-empty JSON object so an empty POST is not silently enqueued
  // under a random id.
  if (payload === null || typeof payload !== 'object' || Array.isArray(payload) || Object.keys(payload).length === 0) {
    res.status(400).json({ error: 'body must be a non-empty JSON object' });
    return;
  }
  const jobId = (payload.job_id as string | undefined) || randomUUID();
  const now = Math.floor(Date.now() / 1000);

  // Conditional put so a client retry with the same job_id does not reset a
  // job or enqueue it twice.
  try {
    await ddb.send(
      new PutCommand({
        TableName: table,
        Item: {
          job_id: jobId,
          status: 'PENDING',
          step: null,
          source: 'sqs',
          created_at: now,
          updated_at: now,
          expires_at: now + TTL_SECONDS,
        },
        ConditionExpression: 'attribute_not_exists(job_id)',
      }),
    );
  } catch (err) {
    if (!(err instanceof ConditionalCheckFailedException)) throw err;
    const existing = (await ddb.send(new GetCommand({ TableName: table, Key: { job_id: jobId } }))).Item ?? {};
    res.status(200).json(rowToBody(jobId, existing));
    return;
  }

  // Hand the job off. The row is already PENDING, so a GET works immediately
  // even if the worker has not picked the message up yet.
  try {
    await sqs.send(new SendMessageCommand({ QueueUrl: queueUrl, MessageBody: JSON.stringify({ job_id: jobId, payload }) }));
  } catch (err) {
    // The row and the message are two writes, not one transaction. If the
    // send fails, remove the PENDING row we just wrote (only if it is still
    // the row we wrote) so the client's retry can create and enqueue it again
    // instead of hitting the duplicate branch above with a job no worker will
    // ever see.
    logger.error('enqueue failed, rolling back row', { jobId, error: err instanceof Error ? err.message : String(err) });
    await ddb.send(
      new DeleteCommand({
        TableName: table,
        Key: { job_id: jobId },
        ConditionExpression: '#s = :p',
        ExpressionAttributeNames: { '#s': 'status' },
        ExpressionAttributeValues: { ':p': 'PENDING' },
      }),
    );
    res.status(503).json({ error: 'could not enqueue job, retry', job_id: jobId });
    return;
  }
  metrics.addMetric('JobsEnqueued', MetricUnit.Count, 1);
  res.status(202).json({ job_id: jobId, status: 'PENDING' });
});

app.get('/v1/jobs/:job_id', async (req: Request, res: Response) => {
  const jobId = String(req.params.job_id);
  const item = (await ddb.send(new GetCommand({ TableName: table, Key: { job_id: jobId } }))).Item;
  if (!item) {
    res.status(404).json({ error: 'job not found', job_id: jobId });
    return;
  }
  res.status(200).json(rowToBody(jobId, item));
});

// express.json() rejects a malformed body with a 400 that is HTML by default.
app.use((err: Error & { type?: string }, _req: Request, res: Response, next: express.NextFunction) => {
  if (err.type === 'entity.parse.failed') {
    res.status(400).json({ error: 'body must be JSON' });
    return;
  }
  next(err);
});

// Anything else (an SDK error, a bug) becomes a logged JSON 500 instead of
// Express's default HTML page. Express 5 routes a rejected async handler here.
app.use((err: Error, req: Request, res: Response, _next: express.NextFunction) => {
  logger.error('unhandled error', { method: req.method, path: req.path, error: err.message });
  res.status(500).json({ error: 'internal error' });
});

// Lambda entry point: attach the invocation context to every log line, run the
// request through Express, then flush any metrics the request recorded.
const serverlessHandler = serverless(app);
export const handler = async (event: APIGatewayProxyEvent, context: Context) => {
  logger.addContext(context);
  metrics.captureColdStartMetric();
  try {
    return await serverlessHandler(event, context);
  } finally {
    if (metrics.hasStoredMetrics()) metrics.publishStoredMetrics();
  }
};
