import { withDurableExecution, DurableContext } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(async (event: { orderId: string }, context: DurableContext) => {
  context.logger.info("Starting step-wait-step execution for order", event.orderId);

  const validated = await context.step("validate-order", async () => {
    context.logger.info("Validating order", event.orderId);
    return { orderId: event.orderId, status: "validated", validatedAt: Date.now() };
  });

  context.logger.info("Order validated, waiting 5 seconds before processing");
  await context.wait("wait 5s", { seconds: 5 });

  const processed = await context.step("process-order", async () => {
    context.logger.info("Processing order", event.orderId);
    return { 
      orderId: validated.orderId, 
      status: "processed", 
      validatedAt: validated.validatedAt,
      processedAt: Date.now() 
    };
  });

  context.logger.info("Step-wait-step execution completed for order", event.orderId);
  return processed;
});