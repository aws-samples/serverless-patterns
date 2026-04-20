import { LocalDurableTestRunner } from '@aws/durable-execution-sdk-js-testing';
import { handler } from '../src/batch-processor/index';

describe('Batch Processor', () => {
  beforeAll(async () => {
    await LocalDurableTestRunner.setupTestEnvironment({ skipTime: true });
  });

  afterAll(async () => {
    await LocalDurableTestRunner.teardownTestEnvironment();
  });

  it('should process all items in parallel', async () => {
    const runner = new LocalDurableTestRunner({
      handlerFunction: handler,
    });

    const execution = await runner.run({
      payload: {
        items: [
          { id: '1' },
          { id: '2' },
          { id: '3' }
        ]
      }
    });

    if (execution.getStatus() === 'FAILED') {
      console.log('Error:', execution.getError());
    }

    expect(execution.getStatus()).toBe('SUCCEEDED');
    expect(execution.getResult()).toEqual({
      total: 3,
      successful: 3
    });

    const operations = execution.getOperations();
    expect(operations.length).toBeGreaterThan(0);
  });
});
