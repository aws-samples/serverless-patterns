import { DurableContext, withDurableExecution } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    const result = await context.step('child-step', async () => {
      return { processed: event.data };
    });
    return result;
  }
);
