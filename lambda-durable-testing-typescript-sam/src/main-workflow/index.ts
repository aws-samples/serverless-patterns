import { DurableContext, withDurableExecution } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    const childResult = await context.invoke('child-function', {
      data: event.input
    });

    return { main: 'completed', child: childResult };
  }
);
