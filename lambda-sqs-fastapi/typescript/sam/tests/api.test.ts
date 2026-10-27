/**
 * Exercise both Express apps through the Lambda handler (serverless-http) with
 * API Gateway proxy events, and the worker with SQS events, no AWS account
 * needed. The AWS SDK clients are mocked so the tests cover the HTTP + queue
 * layer: status codes, idempotent enqueue, bad input, and the worker's job
 * lifecycle including the flaky redelivery and a malformed message in a batch.
 */

import { ConditionalCheckFailedException } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, GetCommand, PutCommand, UpdateCommand } from '@aws-sdk/lib-dynamodb';
import { SendMessageCommand, SQSClient } from '@aws-sdk/client-sqs';
import { mockClient } from 'aws-sdk-client-mock';
import type { SQSEvent } from 'aws-lambda';

process.env.JOBS_TABLE = 'jobs';
process.env.JOBS_QUEUE_URL = 'https://sqs.local/jobs';

const { handler: before } = await import('../before/api');
const { handler: after } = await import('../after/api');
const { handler: worker } = await import('../after/worker');

type Row = Record<string, unknown>;
const ddb = mockClient(DynamoDBDocumentClient);
const sqs = mockClient(SQSClient);

let rows: Record<string, Row>;
let sent: { QueueUrl?: string; MessageBody?: string }[];

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

function sqsEvent(records: { messageId: string; body: string; receive?: number }[]): SQSEvent {
  return {
    Records: records.map((r) => ({
      messageId: r.messageId,
      receiptHandle: 'rh',
      body: r.body,
      attributes: { ApproximateReceiveCount: String(r.receive ?? 1) },
      messageAttributes: {},
      md5OfBody: '',
      eventSource: 'aws:sqs',
      eventSourceARN: 'arn:aws:sqs:us-east-1:0:jobs',
      awsRegion: 'us-east-1',
    })) as SQSEvent['Records'],
  };
}

const flush = () => new Promise((r) => setTimeout(r, 50));

beforeEach(() => {
  rows = {};
  sent = [];
  ddb.reset();
  sqs.reset();
  ddb.on(PutCommand).callsFake(({ Item, ConditionExpression }) => {
    if (ConditionExpression && Item.job_id in rows) {
      throw new ConditionalCheckFailedException({ message: 'exists', $metadata: {} });
    }
    rows[Item.job_id] = { ...Item };
    return {};
  });
  ddb.on(GetCommand).callsFake(({ Key }) => ({ Item: rows[Key.job_id] }));
  ddb.on(UpdateCommand).callsFake(({ Key, UpdateExpression, ExpressionAttributeNames, ExpressionAttributeValues }) => {
    const row = (rows[Key.job_id] ??= { job_id: Key.job_id });
    const [setPart, removePart] = String(UpdateExpression).split(' REMOVE ');
    for (const assign of setPart.replace('SET ', '').split(',')) {
      const [nameAlias, valAlias] = assign.trim().split(' = ');
      row[ExpressionAttributeNames![nameAlias]] = ExpressionAttributeValues![valAlias];
    }
    if (removePart) for (const alias of removePart.split(',')) delete row[ExpressionAttributeNames![alias.trim()]];
    return {};
  });
  sqs.on(SendMessageCommand).callsFake((input) => {
    sent.push(input);
    return { MessageId: 'm' };
  });
});

describe('before: Express + in-process worker', () => {
  it('creates, reports duplicates truthfully, reads, and rejects bad input', async () => {
    expect(await call(before, 'POST', '/v1/jobs', '{"job_id":"j1","input":"x"}')).toEqual([202, { job_id: 'j1', status: 'PENDING' }]);
    // Duplicate POST returns the EXISTING row (not a reset). The in-process job
    // starts asynchronously, so by now the row may already read RUNNING/DONE -
    // the point is it is never reset back to a fresh PENDING.
    const [dupStatus, dup] = await call(before, 'POST', '/v1/jobs', '{"job_id":"j1"}');
    expect(dupStatus).toBe(200);
    expect(['PENDING', 'RUNNING', 'DONE']).toContain(dup.status);
    expect((await call(before, 'GET', '/v1/jobs/nope'))[0]).toBe(404);
    expect((await call(before, 'POST', '/v1/jobs', '{nope'))[0]).toBe(400);
  });
});

describe('after: Express + SQS enqueue', () => {
  it('enqueues once, returns PENDING, and reads status', async () => {
    expect(await call(after, 'POST', '/v1/jobs', '{"job_id":"j2","input":"x"}')).toEqual([202, { job_id: 'j2', status: 'PENDING' }]);
    expect(sent).toHaveLength(1);
    expect(JSON.parse(sent[0].MessageBody!).job_id).toBe('j2');
    expect((await call(after, 'GET', '/v1/jobs/j2'))[0]).toBe(200);
  });

  it('does not enqueue a duplicate POST again', async () => {
    await call(after, 'POST', '/v1/jobs', '{"job_id":"dup","input":"x"}');
    const [status] = await call(after, 'POST', '/v1/jobs', '{"job_id":"dup","input":"x"}');
    expect(status).toBe(200);
    expect(sent).toHaveLength(1);
  });

  it('returns 400 on bad JSON and 404 on an unknown job', async () => {
    expect((await call(after, 'POST', '/v1/jobs', '{nope'))[0]).toBe(400);
    expect((await call(after, 'GET', '/v1/jobs/missing'))[0]).toBe(404);
  });

  it('parses JSON even when the client forgets the Content-Type header', async () => {
    const [status, body] = await call(after, 'POST', '/v1/jobs', '{"job_id":"j9"}', 'application/x-www-form-urlencoded');
    expect([status, body.job_id]).toEqual([202, 'j9']);
  });
});

describe('after: SQS worker', () => {
  it('runs a job to DONE with no error key', async () => {
    rows.w1 = { job_id: 'w1', status: 'PENDING' };
    const out = await worker(sqsEvent([{ messageId: 'm-w1', body: JSON.stringify({ job_id: 'w1', payload: { input: 'hello' } }) }]));
    expect(out).toEqual({ batchItemFailures: [] });
    expect(rows.w1.status).toBe('DONE');
    expect('error' in rows.w1).toBe(false);
  });

  it('redelivers a flaky job without leaking a stale error, then completes', async () => {
    rows.w2 = { job_id: 'w2', status: 'PENDING' };
    const body = JSON.stringify({ job_id: 'w2', payload: { input: 'flaky thing' } });
    const out1 = await worker(sqsEvent([{ messageId: 'm-w2', body, receive: 1 }]));
    expect(out1).toEqual({ batchItemFailures: [{ itemIdentifier: 'm-w2' }] });
    expect(rows.w2.status).toBe('RUNNING');
    expect('error' in rows.w2).toBe(false);
    const out2 = await worker(sqsEvent([{ messageId: 'm-w2', body, receive: 2 }]));
    expect(out2).toEqual({ batchItemFailures: [] });
    expect(rows.w2.status).toBe('DONE');
    expect('error' in rows.w2).toBe(false);
  });

  it('redelivers a malformed message without failing its good batch-mate', async () => {
    rows.ok = { job_id: 'ok', status: 'PENDING' };
    const out = await worker(
      sqsEvent([
        { messageId: 'good', body: JSON.stringify({ job_id: 'ok', payload: { input: 'hi' } }) },
        { messageId: 'bad', body: '{not json' },
      ]),
    );
    expect(out).toEqual({ batchItemFailures: [{ itemIdentifier: 'bad' }] });
    expect(rows.ok.status).toBe('DONE');
  });
});

afterAll(flush);
