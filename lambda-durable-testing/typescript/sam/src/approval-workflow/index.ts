import { DurableContext, withDurableExecution } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    const request = await context.step('create-request', async () => {
      return { requestId: event.requestId, status: 'pending' };
    });

    try {
      const approval = await context.waitForCallback('approval', 86400);
      return { status: 'approved', approvedBy: approval.userId };
    } catch (error) {
      return { status: 'timeout' };
    }
  }
);
