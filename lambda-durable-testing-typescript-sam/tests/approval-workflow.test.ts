import { LocalDurableTestRunner } from '@aws/durable-execution-sdk-js-testing';
import { handler } from '../src/approval-workflow/index';

describe('Approval Workflow', () => {
  beforeAll(async () => {
    await LocalDurableTestRunner.setupTestEnvironment({ skipTime: true });
  });

  afterAll(async () => {
    await LocalDurableTestRunner.teardownTestEnvironment();
  });

  it('should timeout when no approval is received', async () => {
    const runner = new LocalDurableTestRunner({
      handlerFunction: handler,
    });

    const execution = await runner.run({ payload: { requestId: '123' } });

    expect(execution.getStatus()).toBe('SUCCEEDED');
    expect(execution.getResult()).toEqual({ status: 'timeout' });
  });
});
