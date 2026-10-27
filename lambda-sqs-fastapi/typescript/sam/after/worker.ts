/**
 * AFTER - the job as an SQS-triggered Lambda consumer.
 *
 * Same three steps as before/api.ts ran in-process. The difference is what is
 * NOT here: no web server, no request handling. One SQS message in, the steps
 * run, the same table row moves PENDING -> RUNNING -> DONE/FAILED.
 *
 * What SQS + Lambda gives you that the in-process worker did not:
 *   - redelivery: a crash mid-job leaves the message unacked; SQS redelivers it
 *     after the visibility timeout, so the job is retried instead of stranded.
 *   - a dead-letter queue: a message that fails maxReceiveCount times is parked
 *     in the DLQ for inspection instead of looping forever.
 *   - partial batch response: only the messages that failed are redelivered.
 *   - independent scaling: the API and the worker scale on their own.
 */

import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, UpdateCommand } from '@aws-sdk/lib-dynamodb';
import type { SQSBatchResponse, SQSEvent, SQSRecord } from 'aws-lambda';
import { fetchSource, publishResult, transform, TransientError, type JobPayload } from './steps';

const table = process.env.JOBS_TABLE!;
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}), {
  marshallOptions: { removeUndefinedValues: true },
});

type Fields = Record<string, unknown>;

const now = (): number => Math.floor(Date.now() / 1000);

/**
 * SET the given fields (and REMOVE the named ones). Every name is aliased:
 * status, step, error and result are DynamoDB reserved words.
 */
async function update(jobId: string, fields: Fields, remove: string[] = []): Promise<void> {
  const keys = Object.keys(fields);
  const names: Record<string, string> = Object.fromEntries(keys.map((k, i) => [`#f${i}`, k]));
  const values: Fields = Object.fromEntries(keys.map((k, i) => [`:v${i}`, fields[k]]));
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
      ExpressionAttributeNames: names,
      ExpressionAttributeValues: values,
    }),
  );
}

/**
 * Run the steps once. attempt is the SQS receive count: the transform's
 * transient failure clears on redelivery, so a flaky job succeeds on its
 * second delivery with no in-process retry loop.
 */
async function runOne(jobId: string, payload: JobPayload, attempt: number): Promise<void> {
  await update(jobId, { status: 'RUNNING', step: 'fetch_source', updated_at: now() });
  const source = await fetchSource(jobId, payload);
  await update(jobId, { step: 'transform', updated_at: now() });
  const result = await transform(jobId, source, attempt);
  await update(jobId, { step: 'publish_result', updated_at: now() });
  const published = await publishResult(jobId, result);
  // Clear any error from a prior failed delivery so DONE never reads as
  // DONE-with-error.
  await update(jobId, { status: 'DONE', result: published, updated_at: now() }, ['error']);
  console.info(`job ${jobId} DONE on attempt ${attempt}`);
}

/**
 * SQS batch handler. Returns batchItemFailures so only failed messages are
 * redelivered (ReportBatchItemFailures is set on the event source mapping).
 */
export const handler = async (event: SQSEvent): Promise<SQSBatchResponse> => {
  const batchItemFailures: { itemIdentifier: string }[] = [];
  for (const record of event.Records as SQSRecord[]) {
    const messageId = record.messageId;
    // Parse INSIDE the try: a single malformed message must not throw out of
    // the handler, which would fail - and redeliver - the WHOLE batch and
    // re-run its already-done batch-mates. A message we cannot parse is
    // reported as a failure so SQS redelivers it and, after maxReceiveCount,
    // moves it to the DLQ.
    let jobId = '(unparsed)';
    try {
      const attempt = Number(record.attributes?.ApproximateReceiveCount ?? '1');
      const body = JSON.parse(record.body) as { job_id?: string; payload?: JobPayload };
      if (typeof body !== 'object' || body === null || Array.isArray(body) || !body.job_id) {
        throw new Error('message is not a job object with a job_id');
      }
      jobId = body.job_id;
      await runOne(jobId, body.payload ?? {}, attempt);
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err);
      if (err instanceof TransientError) {
        // Let SQS redeliver: do NOT mark FAILED yet. The row stays RUNNING; the
        // error is recorded only when the job ends FAILED, so a GET during the
        // redelivery window never shows RUNNING-with-error.
        console.warn(`job ${jobId} transient failure, will redeliver: ${message}`);
        batchItemFailures.push({ itemIdentifier: messageId });
      } else if (jobId === '(unparsed)') {
        // Malformed message body: cannot even identify the job. Redeliver and
        // let the DLQ catch it; never fail the batch over one bad message.
        console.error(`message ${messageId} is malformed, will redeliver to DLQ: ${message}`);
        batchItemFailures.push({ itemIdentifier: messageId });
      } else {
        // A permanent error fails this job only; the message is consumed.
        console.error(`job ${jobId} FAILED (permanent): ${message}`);
        await update(jobId, { status: 'FAILED', error: message, updated_at: now() });
      }
    }
  }
  return { batchItemFailures };
};
