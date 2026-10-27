/**
 * BEFORE - job API backed by a status table.
 *
 * POST /v1/jobs       -> write {job_id, status=PENDING, payload} to the table
 * GET  /v1/jobs/{id}  -> read the row and return its status
 *
 * The table is the only source of truth about where a job is.
 * A separate poller (worker.ts) moves rows through PENDING -> RUNNING -> DONE.
 */

import { ConditionalCheckFailedException, DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, GetCommand, PutCommand } from '@aws-sdk/lib-dynamodb';
import type { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import { randomUUID } from 'node:crypto';

const table = process.env.JOBS_TABLE!;
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}), {
  marshallOptions: { removeUndefinedValues: true },
});

const TTL_SECONDS = 3 * 24 * 60 * 60;

type Body = Record<string, unknown>;

function response(statusCode: number, body: Body): APIGatewayProxyResult {
  return {
    statusCode,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  };
}

function parseBody(event: APIGatewayProxyEvent): Body | undefined {
  try {
    return JSON.parse(event.body || '{}');
  } catch {
    return undefined;
  }
}

async function createJob(event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> {
  const payload = parseBody(event);
  if (!payload) return response(400, { error: 'body must be JSON' });
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
    const body: Body = { job_id: jobId, status: existing.status, step: existing.step ?? null };
    for (const k of ['result', 'error']) if (k in existing) body[k] = existing[k];
    return response(200, body);
  }

  return response(202, { job_id: jobId, status: 'PENDING' });
}

async function getJob(event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> {
  const jobId = event.pathParameters?.job_id;
  const item = (await ddb.send(new GetCommand({ TableName: table, Key: { job_id: jobId } }))).Item;
  if (!item) return response(404, { error: 'job not found', job_id: jobId });

  const body: Body = { job_id: jobId, status: item.status, step: item.step ?? null };
  if ('result' in item) body.result = item.result;
  if ('error' in item) body.error = item.error;
  return response(200, body);
}

export const handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
  let result: APIGatewayProxyResult;
  if (event.httpMethod === 'POST') result = await createJob(event);
  else if (event.httpMethod === 'GET') result = await getJob(event);
  else result = response(405, { error: 'method not allowed' });
  console.info(`${event.httpMethod} ${event.path} -> ${result.statusCode}`);
  return result;
};
