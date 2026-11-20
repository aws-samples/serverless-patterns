/**
 * Exercise both Express apps through the Lambda handler (serverless-http) with
 * API Gateway proxy events, no AWS account needed. The AWS SDK clients are
 * mocked so the tests cover the HTTP layer: status codes, idempotent starts,
 * the legacy-row branch, and the one durable-specific trap (a duplicate start
 * must not overwrite the stored execution ARN).
 */

import { ConditionalCheckFailedException } from '@aws-sdk/client-dynamodb';
import { GetDurableExecutionCommand, InvokeCommand, LambdaClient } from '@aws-sdk/client-lambda';
import { DynamoDBDocumentClient, GetCommand, PutCommand } from '@aws-sdk/lib-dynamodb';
import { mockClient } from 'aws-sdk-client-mock';

process.env.JOBS_TABLE = 'jobs';
process.env.JOB_FUNCTION = 'arn:fn:live';

const { handler: before } = await import('../before/api');
const { handler: after } = await import('../after/api');

type Row = Record<string, unknown>;
const ddb = mockClient(DynamoDBDocumentClient);
const lambda = mockClient(LambdaClient);

/** In-memory table with the conditional-put semantics the code relies on. */
let rows: Record<string, Row>;
/** Invoke returns an ARN stamped with the CURRENT version, like the real API. */
let version: number;

function event(method: string, path: string, body?: string, contentType = 'application/json') {
  return {
    httpMethod: method,
    path,
    resource: path,
    pathParameters: null,
    headers: { 'content-type': contentType },
    multiValueHeaders: {},
    queryStringParameters: null,
    multiValueQueryStringParameters: null,
    body: body ?? null,
    isBase64Encoded: false,
    requestContext: { stage: 'prod', requestId: 'r', identity: { sourceIp: '127.0.0.1' }, path: `/prod${path}`, httpMethod: method },
  };
}

async function call(fn: typeof before, method: string, path: string, body?: string, contentType?: string) {
  const res = (await fn(event(method, path, body, contentType) as never, {} as never)) as { statusCode: number; body: string };
  return [res.statusCode, res.body ? JSON.parse(res.body) : undefined] as const;
}

beforeEach(() => {
  rows = {};
  version = 1;
  ddb.reset();
  lambda.reset();
  ddb.on(PutCommand).callsFake(({ Item, ConditionExpression }) => {
    if (ConditionExpression && Item.job_id in rows) {
      throw new ConditionalCheckFailedException({ message: 'exists', $metadata: {} });
    }
    rows[Item.job_id] = { ...Item };
    return {};
  });
  ddb.on(GetCommand).callsFake(({ Key }) => ({ Item: rows[Key.job_id] }));
  lambda.on(InvokeCommand).callsFake(({ DurableExecutionName }) => ({
    DurableExecutionArn: `arn:fn:${version}/durable-execution/${DurableExecutionName}`,
  }));
  lambda.on(GetDurableExecutionCommand).callsFake(({ DurableExecutionArn }) => {
    // Only the version the execution was created under resolves, like the real service.
    if (!DurableExecutionArn.startsWith('arn:fn:1/')) throw new Error('Durable Execution does not exist');
    return { Status: 'SUCCEEDED', Result: '{"ok":1}' };
  });
});

describe('before: Express + status table', () => {
  it('creates, reports duplicates truthfully, reads, and rejects bad input', async () => {
    expect(await call(before, 'POST', '/v1/jobs', '{"job_id":"j1","input":"x"}')).toEqual([202, { job_id: 'j1', status: 'PENDING' }]);
    const [dupStatus, dup] = await call(before, 'POST', '/v1/jobs', '{"job_id":"j1"}');
    expect([dupStatus, dup.status]).toEqual([200, 'PENDING']);
    expect((await call(before, 'GET', '/v1/jobs/j1'))[0]).toBe(200);
    expect((await call(before, 'GET', '/v1/jobs/nope'))[0]).toBe(404);
    expect((await call(before, 'POST', '/v1/jobs', '{nope'))[0]).toBe(400);
  });

  it('parses JSON even when the client forgets the Content-Type header', async () => {
    const [status, body] = await call(before, 'POST', '/v1/jobs', '{"job_id":"j9"}', 'application/x-www-form-urlencoded');
    expect([status, body.job_id]).toEqual([202, 'j9']);
  });
});

describe('after: Express + durable function', () => {
  it('starts an execution, stores its ARN, and maps status words', async () => {
    expect(await call(after, 'POST', '/v2/jobs', '{"job_id":"j2","input":"x"}')).toEqual([202, { job_id: 'j2', status: 'RUNNING' }]);
    expect(rows.j2.execution_arn).toBe('arn:fn:1/durable-execution/j2');
    expect(await call(after, 'GET', '/v2/jobs/j2')).toEqual([200, { job_id: 'j2', status: 'DONE', result: { ok: 1 } }]);
    expect((await call(after, 'GET', '/v2/jobs/nope'))[0]).toBe(404);
    expect((await call(after, 'POST', '/v2/jobs', '{nope'))[0]).toBe(400);
  });

  it('keeps the original ARN when a duplicate start arrives after a redeploy', async () => {
    await call(after, 'POST', '/v2/jobs', '{"job_id":"j3","input":"x"}');
    version = 2; // the redeploy moved the alias
    const [status, body] = await call(after, 'POST', '/v2/jobs', '{"job_id":"j3","input":"x"}');
    expect([status, body.status]).toEqual([200, 'DONE']);
    expect(rows.j3.execution_arn).toBe('arn:fn:1/durable-execution/j3');
    expect((await call(after, 'GET', '/v2/jobs/j3'))[0]).toBe(200);
  });

  it('serves a legacy row that has no execution ARN', async () => {
    rows.old = { job_id: 'old', status: 'RUNNING', step: 'transform' };
    expect(await call(after, 'GET', '/v2/jobs/old')).toEqual([200, { job_id: 'old', status: 'RUNNING', step: 'transform', legacy: true }]);
  });
});
