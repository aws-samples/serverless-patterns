import { DurableContext, withDurableExecution } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    await context.parallel(
      'process-items',
      event.items.map((item: any, index: number) =>
        async (childContext: DurableContext) => {
          return await childContext.step(`process-item-${index}`, async () => {
            return { id: item.id, processed: true };
          });
        }
      )
    );

    return {
      total: event.items.length,
      successful: event.items.length
    };
  }
);
