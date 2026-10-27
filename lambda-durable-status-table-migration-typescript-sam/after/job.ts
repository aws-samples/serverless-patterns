/**
 * AFTER - the job as a Lambda durable function.
 *
 * Same three steps as before/worker.ts. The difference is what is NOT here:
 * no scan, no claim, no stale-row detection, no hand-written checkpoint
 * writes, no attempt counter. context.step() records each step's result;
 * on a crash or retry the runtime replays and skips finished steps.
 *
 * Public job id -> durable execution name. The API passes the job_id as
 * DurableExecutionName, so the same id can never start the job twice.
 */

import {
  createRetryStrategy,
  DurableContext,
  JitterStrategy,
  withDurableExecution,
} from '@aws/durable-execution-sdk-js';
import { fetchSource, JobPayload, publishResult, Published, transform } from './steps';

interface JobEvent {
  job_id: string;
  payload?: JobPayload;
}

// Step 2 is the flaky one. Give it a bounded exponential backoff with jitter
// instead of a hand-rolled attempt counter. (retryPresets.default allows six
// attempts over ~2.5 minutes; three is enough for a transient blip.)
const RETRY_TRANSIENT = createRetryStrategy({
  maxAttempts: 3,
  initialDelay: { seconds: 1 },
  maxDelay: { seconds: 10 },
  backoffRate: 2,
  jitter: JitterStrategy.HALF,
});

export const handler = withDurableExecution(
  async (event: JobEvent, context: DurableContext): Promise<Published> => {
    const jobId = event.job_id;
    const payload = event.payload ?? {};
    context.logger.info(`job ${jobId} started`);

    const source = await context.step('fetch_source', async (step) => {
      step.logger.info(`fetching source for ${jobId}`);
      return fetchSource(jobId, payload);
    });

    const result = await context.step(
      'transform',
      async (step) => {
        // step.attempt is the runtime's retry counter; before/worker.ts keeps this by hand.
        step.logger.info(`transform attempt ${step.attempt} for ${jobId}`);
        return transform(jobId, source, step.attempt);
      },
      { retryStrategy: RETRY_TRANSIENT },
    );

    const published = await context.step('publish_result', async (step) => {
      // Steps run at-least-once per retry by default: if the invocation dies
      // between the step body finishing and its checkpoint landing, the body
      // runs again on replay. This stand-in has no external effect, so that is
      // safe. A real publish to a non-idempotent sink needs an idempotency key
      // minted in an earlier step, or StepSemantics.AtMostOncePerRetry.
      step.logger.info(`publishing result for ${jobId}`);
      return publishResult(jobId, result);
    });

    context.logger.info(`job ${jobId} done`);
    // Same shape the status table stored under `result`, so GET responses match.
    return published;
  },
);
