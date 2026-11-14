/**
 * BEFORE - Express job API backed by a status table.
 *
 * POST /v1/jobs       -> write {job_id, status=PENDING, payload} to the table
 * GET  /v1/jobs/{id}  -> read the row and return its status
 *
 * This is the web app a team already has: an Express service whose only
 * record of a job is a row in a "jobs" table. A separate poller (worker.ts)
 * moves rows through PENDING -> RUNNING -> DONE. serverless-http adapts the
 * Express app to the API Gateway proxy event, so the same app runs on Lambda
 * unchanged.
 */

import { ConditionalCheckFailedException, DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, GetCommand, PutCommand } from '@aws-sdk/lib-dynamodb';
import express, { type Request, type Response } from 'express';
import { randomUUID } from 'node:crypto';
import serverless from 'serverless-http';

const table = process.env.JOBS_TABLE!;
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}), {
  marshallOptions: { removeUndefinedValues: true },
});

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

// Log every request the way the old handler did.
app.use((req, res, next) => {
  res.on('finish', () => console.info(`${req.method} ${req.path} -> ${res.statusCode}`));
  next();
});

app.post('/v1/jobs', async (req: Request, res: Response) => {
  const payload = req.body as Body;
  const jobId = (payload.job_id as string | undefined) || randomUUID();
  const now = Math.floor(Date.now() / 1000);

  // Conditional put so a client retry with the same job_id does not reset a job.
  try {
    await ddb.send(
      new PutCommand({
        TableName: table,
        Item: {
          job_id: jobId,
          status: 'PENDING',
          step: null,
          payload,
          created_at: now,
          updated_at: now,
          expires_at: now + TTL_SECONDS,
        },
        ConditionExpression: 'attribute_not_exists(job_id)',
      }),
    );
  } catch (err) {
    if (!(err instanceof ConditionalCheckFailedException)) throw err;
    // Already exists: report where it really is, not a fresh PENDING.
    const existing = (await ddb.send(new GetCommand({ TableName: table, Key: { job_id: jobId } }))).Item ?? {};
    res.status(200).json(rowToBody(jobId, existing));
    return;
  }

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

// Lambda entry point.
export const handler = serverless(app);
