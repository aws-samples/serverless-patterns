import { DurableContext, withDurableExecution } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    const order = await context.step('create-order', async () => {
      return { orderId: '123', total: 50 };
    });

    await context.wait({ seconds: 300 });

    const notification = await context.step('send-notification', async () => {
      return { sent: true };
    });

    return { order, notification };
  }
);
