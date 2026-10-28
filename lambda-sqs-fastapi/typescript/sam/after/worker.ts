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

import { BatchProcessor, EventType, processPartialResponse } from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { Tracer } from '@aws-lambda-powertools/tracer';
import { ConditionalCheckFailedException, DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, UpdateCommand } from '@aws-sdk/lib-dynamodb';
import type { Context, SQSBatchResponse, SQSEvent, SQSRecord } from 'aws-lambda';
import { fetchSource, publishResult, transform, TransientError, type JobPayload } from './steps';

// Powertools: JSON logs with the Lambda context, X-Ray subsegments for every
// SDK call, EMF metrics, and the SQS partial-batch bookkeeping.
const logger = new Logger();
const tracer = new Tracer();
const metrics = new Metrics();
const processor = new BatchProcessor(EventType.SQS);

const table = process.env.JOBS_TABLE!;
// SDK timeouts well inside the 60s function timeout, so a slow table call
// fails fast and is retried by SQS instead of running the whole batch into a
// Lambda timeout.
const sdk = { maxAttempts: 3, requestHandler: { connectionTimeout: 2_000, requestTimeout: 5_000 } };
const ddb = DynamoDBDocumentClient.from(tracer.captureAWSv3Client(new DynamoDBClient(sdk)), {
  marshallOptions: { removeUndefinedValues: true },
});

type Fields = Record<string, unknown>;

const now = (): number => Math.floor(Date.now() / 1000);

/**
 * SET the given fields (and REMOVE the named ones) on an EXISTING row. Every
 * name is aliased: status, step, error and result are DynamoDB reserved words.
 * attribute_exists(job_id) stops a message redelivered after the row's TTL
 * from phantom-creating a row with no expires_at; the caller sees
 * ConditionalCheckFailedException.
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
      ConditionExpression: 'attribute_exists(job_id)',
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
  metrics.addMetric('JobsDone', MetricUnit.Count, 1);
  logger.info('job DONE', { jobId, attempt });
}

/**
 * One SQS record. Throwing marks THIS record failed (SQS redelivers it and,
 * after maxReceiveCount, moves it to the DLQ); returning consumes it. The
 * BatchProcessor turns those outcomes into the partial batch response, so one
 * bad message never fails - and re-runs - its already-done batch-mates.
 */
const recordHandler = async (record: SQSRecord): Promise<void> => {
  const attempt = Number(record.attributes?.ApproximateReceiveCount ?? '1');
  // A body we cannot parse or identify is redelivered and lands in the DLQ.
  const body = JSON.parse(record.body) as { job_id?: string; payload?: JobPayload };
  if (typeof body !== 'object' || body === null || Array.isArray(body) || !body.job_id) {
    throw new Error('message is not a job object with a job_id');
  }
  const jobId = body.job_id;
  try {
    await runOne(jobId, body.payload ?? {}, attempt);
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    if (err instanceof TransientError) {
      // Let SQS redeliver: do NOT mark FAILED yet. The row stays RUNNING; the
      // error is recorded only when the job ends FAILED, so a GET during the
      // redelivery window never shows RUNNING-with-error.
      logger.warn('transient failure, will redeliver', { jobId, attempt, error: message });
      throw err;
    }
    if (err instanceof ConditionalCheckFailedException) {
      // No row to update (expired or never created): nothing to retry.
      logger.error('job has no row (expired or never created); dropping message', { jobId });
      return;
    }
    // A permanent error fails this job only; the message is consumed.
    logger.error('job FAILED (permanent)', { jobId, attempt, error: message });
    metrics.addMetric('JobsFailed', MetricUnit.Count, 1);
    try {
      await update(jobId, { status: 'FAILED', error: message, updated_at: now() });
    } catch (updateErr) {
      if (updateErr instanceof ConditionalCheckFailedException) {
        logger.error('job has no row (expired or never created); dropping message', { jobId });
        return;
      }
      // Could not record the failure: fail the record so SQS redelivers it
      // rather than losing the outcome, and never fail the whole batch.
      logger.error('could not mark job FAILED, will redeliver', {
        jobId,
        error: updateErr instanceof Error ? updateErr.message : String(updateErr),
      });
      throw updateErr;
    }
  }
};

/**
 * SQS batch handler. Returns batchItemFailures so only failed messages are
 * redelivered (ReportBatchItemFailures is set on the event source mapping).
 */
export const handler = async (event: SQSEvent, context: Context): Promise<SQSBatchResponse> => {
  logger.addContext(context);
  metrics.captureColdStartMetric();
  try {
    // throwOnFullBatchFailure: false - a batch where every record failed still
    // comes back as a partial response (same redelivery, no thrown error).
    // processInParallel: false - run the records one after another, as the
    // hand-rolled loop did; drop it to run a batch's jobs concurrently.
    return await processPartialResponse(event, recordHandler, processor, {
      context,
      processInParallel: false,
      throwOnFullBatchFailure: false,
    });
  } finally {
    if (metrics.hasStoredMetrics()) metrics.publishStoredMetrics();
  }
};
