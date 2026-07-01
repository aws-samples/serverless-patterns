const {
  withDurableExecution,
  withRetry,
  createRetryStrategy,
} = require('@aws/durable-execution-sdk-js');

const enrichRetryStrategy = createRetryStrategy({
  maxAttempts: 3,
  initialDelay: { seconds: 1 },
  maxDelay: { seconds: 30 },
  backoffRate: 2,
});

async function handler(event, context) {
  const orderId = event.orderId || 'ORDER-001';
  context.logger.info(`Starting durable order processing for ${orderId}`);

  // Step 1: Validate input
  const validatedOrder = await context.step('validate-input', async () => {
    context.logger.info(`Validating order ${orderId}`);
    if (!event.nodejsLambdaArn) throw new Error('nodejsLambdaArn is required');
    return { orderId, nodejsLambdaArn: event.nodejsLambdaArn, receivedAt: new Date().toISOString() };
  });

  // Step 2: Call the enricher Lambda using context.invoke()
  // context.invoke() provides automatic checkpointing and suspends the function
  // while waiting for the result, without consuming compute resources.
  const enrichment = await withRetry(
    context,
    'enrich-order',
    (ctx) => ctx.invoke('enrich-order', validatedOrder.nodejsLambdaArn, { orderId }),
    { retryStrategy: enrichRetryStrategy }
  );

  // Durable wait — survives crashes and restarts
  context.logger.info('Pausing for 5 seconds...');
  await context.wait({ seconds: 5 });
  context.logger.info('Resumed after 5 seconds');

  // Step 3: Finalize
  const result = await context.step('finalize-order', async () => {
    context.logger.info(`Finalizing order ${orderId}`);
    return {
      orderId,
      status: 'COMPLETED',
      enrichedData: enrichment,
      finalizedAt: new Date().toISOString()
    };
  });

  context.logger.info(`Order ${orderId} processed successfully`);
  return result;
}

exports.handler = withDurableExecution(handler);