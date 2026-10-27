/**
 * The job's business steps. Identical in before/ and after/.
 *
 * Three steps, each slow or flaky in a way real jobs are:
 *   1. fetchSource   - pulls input (simulated I/O)
 *   2. transform     - CPU work; fails on attempt 1 for 'flaky' inputs
 *   3. publishResult - writes the output somewhere
 *
 * The migration changes HOW these run, not WHAT they do.
 */

import { createHash } from 'node:crypto';
import { setTimeout as sleep } from 'node:timers/promises';

// transform() throws on its FIRST attempt for inputs containing this word,
// then succeeds. It stands in for a transient dependency failure (throttle,
// timeout, 5xx). Keyed off the attempt number the caller passes in, so it
// behaves the same in a fresh execution environment as in a warm one.
export const FLAKY_MARKER = 'flaky';

/** A failure that is safe to retry. */
export class TransientError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'TransientError';
  }
}

export interface JobPayload {
  input?: string;
}

export interface Source {
  job_id: string;
  source: string;
  bytes: number;
}

export interface Transformed {
  job_id: string;
  digest: string;
  length: number;
}

export interface Published {
  job_id: string;
  published: boolean;
  digest: string;
}

export async function fetchSource(jobId: string, payload: JobPayload): Promise<Source> {
  await sleep(500);
  const text = payload.input ?? '';
  return { job_id: jobId, source: text, bytes: text.length };
}

export async function transform(jobId: string, source: Source, attempt: number): Promise<Transformed> {
  const text = source.source;
  if (text.includes(FLAKY_MARKER) && attempt === 1) {
    throw new TransientError('downstream dependency timed out');
  }
  await sleep(500);
  const digest = createHash('sha256').update(text).digest('hex');
  return { job_id: jobId, digest, length: source.bytes };
}

export async function publishResult(jobId: string, result: Transformed): Promise<Published> {
  await sleep(500);
  return { job_id: jobId, published: true, digest: result.digest };
}
