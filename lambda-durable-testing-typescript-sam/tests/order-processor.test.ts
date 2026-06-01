import { LocalDurableTestRunner } from '@aws/durable-execution-sdk-js-testing';
import { handler } from '../src/order-processor/index';

describe('Order Processor', () => {
  beforeAll(async () => {
    await LocalDurableTestRunner.setupTestEnvironment({ skipTime: true });
  });

  afterAll(async () => {
    await LocalDurableTestRunner.teardownTestEnvironment();
  });

  it('should process order successfully', async () => {
    const runner = new LocalDurableTestRunner({
      handlerFunction: handler,
    });

    const execution = await runner.run();

    expect(execution.getStatus()).toBe('SUCCEEDED');
    expect(execution.getResult()).toEqual({
      order: { orderId: '123', total: 50 },
      notification: { sent: true }
    });
  });

  it('should execute operations in correct order', async () => {
    const runner = new LocalDurableTestRunner({
      handlerFunction: handler,
    });

    const execution = await runner.run();

    const operations = execution.getOperations();
    expect(operations).toHaveLength(3);

    const createOrder = runner.getOperationByIndex(0);
    expect(createOrder.getType()).toBe('STEP');
    expect(createOrder.getStatus()).toBe('SUCCEEDED');
    expect(createOrder.getStepDetails()?.result).toEqual({
      orderId: '123',
      total: 50
    });

    const waitOp = runner.getOperationByIndex(1);
    expect(waitOp.getType()).toBe('WAIT');
    expect(waitOp.getWaitDetails()?.waitSeconds).toBe(300);

    const notification = runner.getOperationByIndex(2);
    expect(notification.getStepDetails()?.result).toEqual({ sent: true });
  });
});
