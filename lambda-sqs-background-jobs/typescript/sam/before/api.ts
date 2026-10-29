/**
 * BEFORE - an Express job API whose work runs IN THE WEB PROCESS.
 *
 * POST /v1/jobs       -> write {job_id, status=PENDING} and start the steps
 *                        on the same process (fire-and-forget), return 202
 * GET  /v1/jobs/{id}  -> read the row and return its status
 *
 * This is the shape a team already has: one Express service that both takes
 * the request AND does the work. The jobs table is the only record of
 * progress. It runs locally as a normal Express server; on Lambda,
 * serverless-http adapts the app to the API Gateway proxy event unchanged.
 *
 * Why this hurts: the work is tied to the web process. A deploy, scale-in, or
 * crash kills every in-flight job, and the row is stuck at RUNNING forever. On
 * Lambda it is worse - the environment can be frozen the moment the handler
 * returns, so the fire-and-forget work may not run at all. Compare with
 * after/api.ts, where the POST returns after an SQS send and the work runs in
 * its own Lambda.
 */

import { ConditionalCheckFailedException, DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, GetCommand, PutCommand, UpdateCommand } from '@aws-sdk/lib-dynamodb';
import express, { type Request, type Response } from 'express';
import { randomUUID } from 'node:crypto';
import serverless from 'serverless-http';
import { fetchSource, publishResult, transform, TransientError, type JobPayload } from './steps';

const table = process.env.JOBS_TABLE!;
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}), {
  marshallOptions: { removeUndefinedValues: true },
});

const TTL_SECONDS = 3 * 24 * 60 * 60;
const MAX_ATTEMPTS = 3;

type Body = Record<string, unknown>;

const now = (): number => Math.floor(Date.now() / 1000);

function rowToBody(jobId: string, item: Body): Body {
  const body: Body = { job_id: jobId, status: item.status, step: item.step ?? null };
  for (const k of ['result', 'error']) if (k in item) body[k] = item[k];
  return body;
}

/**
 * SET the given fields (and REMOVE the named ones) on an EXISTING row. Every
 * name is aliased: status, step, error and result are DynamoDB reserved words,
 * and a bare name in an UpdateExpression fails. attribute_exists(job_id) stops
 * an update from phantom-creating a row (with no expires_at) after the row's
 * TTL has removed it.
 */
async function update(jobId: string, fields: Body, remove: string[] = []): Promise<void> {
  const keys = Object.keys(fields);
  const names: Record<string, string> = Object.fromEntries(keys.map((k, i) => [`#f${i}`, k]));
  const values: Body = Object.fromEntries(keys.map((k, i) => [`:v${i}`, fields[k]]));
  let expression = 'SET ' + keys.map((_, i) => `#f${i} = :v${i}`).join(', ');
  if (remove.length) {
    remove.forEach((k, i) => (names[`#r${i}`] = k));
    expression += ' REMOVE ' + remove.map((_, i) => `#r${i}`).join(', ');
  }
  await ddb.send(
    new UpdateCommand({
      TableName: table,
      Key: { job_id: jobId },
      UpdateExpression: expression,
      ConditionExpression: 'attribute_exists(job_id)',
      ExpressionAttributeNames: names,
      ExpressionAttributeValues: values,
    }),
  );
}

/**
 * Run the three steps in this process. A crash or deploy mid-run leaves the
 * row at RUNNING with no one to resume it: the cost this pattern removes.
 */
async function runJob(jobId: string, payload: JobPayload): Promise<void> {
  for (let attempt = 1; ; attempt += 1) {
    try {
      await update(jobId, { status: 'RUNNING', step: 'fetch_source', updated_at: now() });
      const source = await fetchSource(jobId, payload);
      await update(jobId, { step: 'transform', updated_at: now() });
      const result = await transform(jobId, source, attempt);
      await update(jobId, { step: 'publish_result', updated_at: now() });
      const published = await publishResult(jobId, result);
      // Clear any error from a prior failed attempt so DONE never reads as
      // DONE-with-error.
      await update(jobId, { status: 'DONE', result: published, updated_at: now() }, ['error']);
      console.info(`job ${jobId} DONE`);
      return;
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err);
      if (err instanceof ConditionalCheckFailedException) {
        // The row is gone (TTL expired); there is nothing to update.
        console.error(`job ${jobId} has no row, dropping`);
        return;
      }
      // Retry only the transient class, by hand, in this process.
      if (err instanceof TransientError && attempt < MAX_ATTEMPTS) {
        console.warn(`job ${jobId} attempt ${attempt} failed, retrying: ${message}`);
        await new Promise((r) => setTimeout(r, 500 * attempt));
        continue;
      }
      await update(jobId, { status: 'FAILED', error: message, updated_at: now() });
      console.error(`job ${jobId} FAILED: ${message}`);
      return;
    }
  }
}

const app = express();
// Parse the body as JSON whatever the Content-Type says (curl -d sends a form
// type), and bound it: API Gateway caps payloads anyway, but say so here.
app.use(express.json({ type: () => true, limit: '1mb' }));

app.use((req, res, next) => {
  res.on('finish', () => console.info(`${req.method} ${req.path} -> ${res.statusCode}`));
  next();
});

app.post('/v1/jobs', async (req: Request, res: Response) => {
  const payload = req.body as Body;
  if (payload === null || typeof payload !== 'object' || Array.isArray(payload) || Object.keys(payload).length === 0) {
    res.status(400).json({ error: 'body must be a non-empty JSON object' });
    return;
  }
  const jobId = (payload.job_id as string | undefined) || randomUUID();
  const ts = now();

  // Conditional put so a client retry with the same job_id does not reset a job.
  try {
    await ddb.send(
      new PutCommand({
        TableName: table,
        Item: { job_id: jobId, status: 'PENDING', step: null, created_at: ts, updated_at: ts, expires_at: ts + TTL_SECONDS },
        ConditionExpression: 'attribute_not_exists(job_id)',
      }),
    );
  } catch (err) {
    if (!(err instanceof ConditionalCheckFailedException)) throw err;
    const existing = (await ddb.send(new GetCommand({ TableName: table, Key: { job_id: jobId } }))).Item ?? {};
    res.status(200).json(rowToBody(jobId, existing));
    return;
  }

  // Do the work right here, in the web process. Not awaited: the HTTP response
  // returns while the job runs on.
  void runJob(jobId, payload as JobPayload);
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
