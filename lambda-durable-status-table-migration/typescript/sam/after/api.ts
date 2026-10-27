/**
 * AFTER - the same Express job API, backed by durable executions.
 *
 * POST /v2/jobs       -> start a durable execution named by job_id, store its ARN
 * GET  /v2/jobs/{id}  -> job_id -> execution ARN -> GetDurableExecution
 *
 * The web app is unchanged in shape: same framework, same routes, same public
 * job_id. What changed is behind it. The table shrinks to one job: map a
 * public job_id to an execution ARN. Status, step progress, retries and
 * results now live in the durable runtime.
 *
 * Cutover: a GET for a job created by the OLD API (a row with no execution
 * ARN) still answers from the row. Point clients at /v2 and the old poller
 * keeps draining old rows until they are gone.
 */

import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { GetDurableExecutionCommand, InvokeCommand, LambdaClient } from '@aws-sdk/client-lambda';
import { DynamoDBDocumentClient, GetCommand, PutCommand } from '@aws-sdk/lib-dynamodb';
import express, { type Request, type Response } from 'express';
import { randomUUID } from 'node:crypto';
import serverless from 'serverless-http';

const table = process.env.JOBS_TABLE!;
const JOB_FUNCTION = process.env.JOB_FUNCTION!; // qualified alias ARN
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}));
const lambda = new LambdaClient({});

const TTL_SECONDS = 3 * 24 * 60 * 60;

// Durable execution status -> the status words the old API returned,
// so clients polling GET /jobs/{id} need no change.
const STATUS_MAP: Record<string, string> = {
  RUNNING: 'RUNNING',
  SUCCEEDED: 'DONE',
  FAILED: 'FAILED',
  TIMED_OUT: 'FAILED',
  STOPPED: 'FAILED',
};

type Body = Record<string, unknown>;

const app = express();
app.use(express.json());

// Log every request the way the old handler did.
app.use((req, res, next) => {
  res.on('finish', () => console.info(`${req.method} ${req.path} -> ${res.statusCode}`));
  next();
});

app.post('/v2/jobs', async (req: Request, res: Response) => {
  const payload = req.body as Body;
  const jobId = (payload.job_id as string | undefined) || randomUUID();

  // DurableExecutionName makes the start idempotent: a retry with the same
  // job_id returns the existing execution instead of creating a second one.
  const invoke = await lambda.send(
    new InvokeCommand({
      FunctionName: JOB_FUNCTION,
      InvocationType: 'Event',
      DurableExecutionName: jobId,
      Payload: JSON.stringify({ job_id: jobId, payload }),
    }),
  );
  const executionArn = invoke.DurableExecutionArn;
  if (!executionArn) {
    // Only a durable function returns this. A missing ARN means JOB_FUNCTION
    // points at a function without DurableConfig.
    res.status(500).json({ error: 'target is not a durable function', job_id: jobId });
    return;
  }

  const now = Math.floor(Date.now() / 1000);
  await ddb.send(
    new PutCommand({
      TableName: table,
      Item: { job_id: jobId, execution_arn: executionArn, created_at: now, expires_at: now + TTL_SECONDS },
    }),
  );
  res.status(202).json({ job_id: jobId, status: 'RUNNING' });
});

app.get('/v2/jobs/:job_id', async (req: Request, res: Response) => {
  const jobId = String(req.params.job_id);
  const item = (await ddb.send(new GetCommand({ TableName: table, Key: { job_id: jobId } }))).Item;
  if (!item) {
    res.status(404).json({ error: 'job not found', job_id: jobId });
    return;
  }

  const executionArn = item.execution_arn as string | undefined;
  if (!executionArn) {
    // Legacy row from the status-table version: still in flight on the old poller.
    const body: Body = { job_id: jobId, status: item.status ?? 'UNKNOWN', step: item.step ?? null, legacy: true };
    if ('result' in item) body.result = item.result;
    if ('error' in item) body.error = item.error;
    res.status(200).json(body);
    return;
  }

  const execution = await lambda.send(new GetDurableExecutionCommand({ DurableExecutionArn: executionArn }));
  const status = execution.Status ?? 'UNKNOWN';
  const body: Body = { job_id: jobId, status: STATUS_MAP[status] ?? status };
  if (execution.Result) body.result = JSON.parse(execution.Result);
  if (execution.Error) body.error = execution.Error.ErrorMessage ?? JSON.stringify(execution.Error);
  res.status(200).json(body);
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
