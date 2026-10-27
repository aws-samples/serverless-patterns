/**
 * BEFORE - the poller.
 *
 * Runs every minute. Scans the table for PENDING (or stale RUNNING) rows,
 * claims one with a conditional update, runs the steps, and writes progress
 * back after every step so a crash can be resumed by the next poll.
 *
 * Everything in this file is the "where was I?" bookkeeping that durable
 * functions do for you. Compare with after/job.ts.
 */

import { ConditionalCheckFailedException, DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, ScanCommand, UpdateCommand } from '@aws-sdk/lib-dynamodb';
import { fetchSource, publishResult, transform, TransientError } from './steps';

const table = process.env.JOBS_TABLE!;
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}), {
  marshallOptions: { removeUndefinedValues: true },
});

// A RUNNING row older than this is assumed crashed and is picked up again.
const STALE_AFTER_SECONDS = 120;
const MAX_ATTEMPTS = 3;
const MAX_JOBS_PER_POLL = 25;

type Row = Record<string, any>;

const now = (): number => Math.floor(Date.now() / 1000);

/**
 * SET the given fields. Every name is aliased: status, error and result are
 * DynamoDB reserved words, and a bare name in an UpdateExpression fails.
 */
async function update(
  jobId: string,
  fields: Row,
  condition?: string,
  condValues: Row = {},
): Promise<void> {
  const keys = Object.keys(fields);
  const names = Object.fromEntries(keys.map((k, i) => [`#f${i}`, k]));
  const values = Object.fromEntries(keys.map((k, i) => [`:v${i}`, fields[k]]));
  await ddb.send(
    new UpdateCommand({
      TableName: table,
      Key: { job_id: jobId },
      UpdateExpression: 'SET ' + keys.map((_, i) => `#f${i} = :v${i}`).join(', '),
      ExpressionAttributeNames: names,
      ExpressionAttributeValues: { ...values, ...condValues },
      ...(condition ? { ConditionExpression: condition } : {}),
    }),
  );
}

/** Take ownership of a row. Returns false if another poller got it first. */
async function claim(job: Row): Promise<boolean> {
  try {
    await update(
      job.job_id,
      { status: 'RUNNING', updated_at: now() },
      '#f0 = :pending OR (#f0 = :running AND #f1 < :stale)',
      { ':pending': 'PENDING', ':running': 'RUNNING', ':stale': now() - STALE_AFTER_SECONDS },
    );
    return true;
  } catch (err) {
    if (err instanceof ConditionalCheckFailedException) return false;
    throw err;
  }
}

/** Persist all step outputs so far so a restart can skip finished steps. */
const checkpoint = (jobId: string, step: string, outputs: Row) =>
  update(jobId, { step, outputs, updated_at: now() });

const finish = (jobId: string, status: string, fields: Row = {}) =>
  update(jobId, { status, updated_at: now(), ...fields });

async function runJob(job: Row): Promise<void> {
  const jobId: string = job.job_id;
  const payload = job.payload ?? {};
  const outputs: Row = { ...(job.outputs ?? {}) };
  let attempts: number = job.attempts ?? 0;

  try {
    // Each step: skip if a previous attempt already finished it, else run and checkpoint.
    if (!('fetch_source' in outputs)) {
      outputs.fetch_source = await fetchSource(jobId, payload);
      await checkpoint(jobId, 'fetch_source', outputs);
    }
    if (!('transform' in outputs)) {
      outputs.transform = await transform(jobId, outputs.fetch_source, attempts + 1);
      await checkpoint(jobId, 'transform', outputs);
    }
    if (!('publish_result' in outputs)) {
      outputs.publish_result = await publishResult(jobId, outputs.transform);
      await checkpoint(jobId, 'publish_result', outputs);
    }
    await finish(jobId, 'DONE', { result: outputs.publish_result });
    console.info(`job ${jobId} DONE`);
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    if (err instanceof TransientError) {
      attempts += 1;
      if (attempts >= MAX_ATTEMPTS) {
        console.error(`job ${jobId} FAILED after ${attempts} attempts: ${message}`);
        await finish(jobId, 'FAILED', { error: message, attempts });
      } else {
        // Put it back for the next poll. No backoff, no jitter: you would add those by hand.
        console.warn(`job ${jobId} attempt ${attempts} failed, requeued: ${message}`);
        await finish(jobId, 'PENDING', { error: message, attempts });
      }
    } else {
      console.error(`job ${jobId} FAILED: ${message}`);
      await finish(jobId, 'FAILED', { error: message });
    }
  }
}

/**
 * Every PENDING or stale RUNNING row. Scan's Limit counts rows READ, not rows
 * matched, so a single limited scan would skip pending jobs once the table
 * holds more than a page of finished rows. Paginate instead.
 */
async function dueJobs(stale: number): Promise<Row[]> {
  const due: Row[] = [];
  let startKey: Row | undefined;
  do {
    const page = await ddb.send(
      new ScanCommand({
        TableName: table,
        FilterExpression: '#s = :pending OR (#s = :running AND #u < :stale)',
        ExpressionAttributeNames: { '#s': 'status', '#u': 'updated_at' },
        ExpressionAttributeValues: { ':pending': 'PENDING', ':running': 'RUNNING', ':stale': stale },
        ExclusiveStartKey: startKey,
      }),
    );
    due.push(...(page.Items ?? []));
    startKey = page.LastEvaluatedKey;
  } while (startKey && due.length < MAX_JOBS_PER_POLL);
  return due.slice(0, MAX_JOBS_PER_POLL);
}

export const handler = async (): Promise<{ processed: number }> => {
  let processed = 0;
  for (const job of await dueJobs(now() - STALE_AFTER_SECONDS)) {
    if (await claim(job)) {
      await runJob(job);
      processed += 1;
    }
  }
  return { processed };
};
