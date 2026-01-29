import { CloudDurableTestRunner } from '@aws/durable-execution-sdk-js-testing';

describe('Order Processor - Cloud Integration Tests', () => {
  it('should execute in AWS', async () => {
    const runner = new CloudDurableTestRunner({
      functionName: 'df-test-examples-OrderProcessorFunction-7G4n6adUSHKl:$LATEST',
    });

    const execution = await runner.run({ payload: {} });

    if (execution.getStatus() === 'FAILED') {
      console.log('Execution failed:', execution.getError());
    }

    expect(execution.getStatus()).toBe('SUCCEEDED');
    expect(execution.getResult()).toEqual({
      order: { orderId: '123', total: 50 },
      notification: { sent: true }
    });
  }, 600000);
});
