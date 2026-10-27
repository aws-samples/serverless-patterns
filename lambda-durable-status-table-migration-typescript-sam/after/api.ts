/**
 * AFTER - job API backed by durable executions.
 *
 * POST /v2/jobs       -> start a durable execution named by job_id, store its ARN
 * GET  /v2/jobs/{id}  -> job_id -> execution ARN -> GetDurableExecution
 *
 * The table shrinks to one job: map a public job_id to an execution ARN.
 * Status, step progress, retries and results now live in the durable runtime.
 *
 * Cutover: a GET for a job created by the OLD API (a row with no execution
 * ARN) still answers from the row. Point clients at /v2 and the old poller
 * keeps draining old rows until they are gone.
 */

import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { GetDurableExecutionCommand, InvokeCommand, LambdaClient } from '@aws-sdk/client-lambda';
import { DynamoDBDocumentClient, GetCommand, PutCommand } from '@aws-sdk/lib-dynamodb';
import type { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import { randomUUID } from 'node:crypto';

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
    return response(500, { error: 'target is not a durable function', job_id: jobId });
  }

  const now = Math.floor(Date.now() / 1000);
  await ddb.send(
    new PutCommand({
      TableName: table,
      Item: { job_id: jobId, execution_arn: executionArn, created_at: now, expires_at: now + TTL_SECONDS },
    }),
  );
  return response(202, { job_id: jobId, status: 'RUNNING' });
}

async function getJob(event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> {
  const jobId = event.pathParameters?.job_id;
  const item = (await ddb.send(new GetCommand({ TableName: table, Key: { job_id: jobId } }))).Item;
  if (!item) return response(404, { error: 'job not found', job_id: jobId });

  const executionArn = item.execution_arn as string | undefined;
  if (!executionArn) {
    // Legacy row from the status-table version: still in flight on the old poller.
    const body: Body = { job_id: jobId, status: item.status ?? 'UNKNOWN', step: item.step ?? null, legacy: true };
    if ('result' in item) body.result = item.result;
    if ('error' in item) body.error = item.error;
    return response(200, body);
  }

  const execution = await lambda.send(new GetDurableExecutionCommand({ DurableExecutionArn: executionArn }));
  const status = execution.Status ?? 'UNKNOWN';
  const body: Body = { job_id: jobId, status: STATUS_MAP[status] ?? status };
  if (execution.Result) body.result = JSON.parse(execution.Result);
  if (execution.Error) body.error = execution.Error.ErrorMessage ?? JSON.stringify(execution.Error);
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
