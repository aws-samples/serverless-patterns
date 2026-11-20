/**
 * Run the durable job locally, no AWS account needed:
 *
 *     npm install
 *     npm test
 */

import { LocalDurableTestRunner } from '@aws/durable-execution-sdk-js-testing';
import { handler } from '../after/job';

const STEPS = ['fetch_source', 'transform', 'publish_result'];

function run(jobId: string, text: string) {
  const runner = new LocalDurableTestRunner({ handlerFunction: handler });
  const execution = runner.run({ payload: { job_id: jobId, payload: { input: text } } });
  return { runner, execution };
}

describe('status table -> durable function', () => {
  beforeAll(async () => {
    // skipTime: retry backoff completes immediately instead of sleeping.
    await LocalDurableTestRunner.setupTestEnvironment({ skipTime: true });
  });

  afterAll(async () => {
    await LocalDurableTestRunner.teardownTestEnvironment();
  });

  it('happy path completes all three steps once', async () => {
    const { runner, execution } = run('job-ok', 'hello');
    const result = await execution;
    expect(result.getStatus()).toBe('SUCCEEDED');
    expect(result.getResult()).toMatchObject({ job_id: 'job-ok', published: true });
    for (const name of STEPS) {
      const step = runner.getOperation(name);
      expect(step.getStatus()).toBe('SUCCEEDED');
      expect(step.getStepDetails()?.attempt).toBe(1);
    }
  });

  it('flaky step is retried by the runtime', async () => {
    const { runner, execution } = run('job-flaky', 'this input is flaky');
    const result = await execution;
    expect(result.getStatus()).toBe('SUCCEEDED');
    // First attempt threw TransientError; the SDK retried and the second attempt succeeded.
    const transform = runner.getOperation('transform');
    expect(transform.getStatus()).toBe('SUCCEEDED');
    expect(transform.getStepDetails()?.attempt).toBe(2);
    // The steps around it ran exactly once: no re-execution of finished work.
    expect(runner.getOperation('fetch_source').getStepDetails()?.attempt).toBe(1);
    expect(runner.getOperation('publish_result').getStepDetails()?.attempt).toBe(1);
  });

  it('replay is deterministic', async () => {
    // Same input, same job id, run twice: a durable function must produce the
    // same checkpoints and the same result on replay, and every operation is a
    // named step (tests fetch operations by name, never by index).
    const first = run('job-replay', 'hello');
    const second = run('job-replay', 'hello');
    const [a, b] = await Promise.all([first.execution, second.execution]);
    expect(a.getStatus()).toBe('SUCCEEDED');
    expect(b.getStatus()).toBe('SUCCEEDED');
    expect(a.getResult()).toEqual(b.getResult());
    for (const { runner, execution } of [first, second]) {
      const names = (await execution).getOperations().map((op) => op.getName());
      expect(new Set(names)).toEqual(new Set(STEPS));
      for (const name of STEPS) expect(runner.getOperation(name).getStatus()).toBe('SUCCEEDED');
    }
  });
});
