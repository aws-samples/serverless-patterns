import { LocalDurableTestRunner } from '@aws/durable-execution-sdk-js-testing';
import { handler as mainHandler } from '../src/main-workflow/index';
import { handler as childHandler } from '../src/child-workflow/index';

describe('Main Workflow', () => {
  beforeAll(async () => {
    await LocalDurableTestRunner.setupTestEnvironment({ skipTime: true });
  });

  afterAll(async () => {
    await LocalDurableTestRunner.teardownTestEnvironment();
  });

  it('should invoke child function successfully', async () => {
    const runner = new LocalDurableTestRunner({
      handlerFunction: mainHandler,
    });

    runner.registerDurableFunction('child-function', childHandler);

    const execution = await runner.run({ payload: { input: 'test-data' } });

    expect(execution.getStatus()).toBe('SUCCEEDED');
    expect(execution.getResult()).toEqual({
      main: 'completed',
      child: { processed: 'test-data' }
    });
  });
});
