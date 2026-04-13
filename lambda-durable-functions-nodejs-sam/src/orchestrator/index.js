const { LambdaClient, InvokeCommand } = require('@aws-sdk/client-lambda');
const { withDurableExecution } = require('@aws/durable-execution-sdk-js');

const lambda = new LambdaClient();

async function handler(event, context) {
  const orderId = event.orderId || 'ORDER-001';
  console.log(`[Step 0] Starting durable order processing for ${orderId}`);

  // Step 1: Validate input
  const validatedOrder = await context.step('validate-input', async () => {
    console.log(`[Step 1] Validating order ${orderId}`);
    if (!event.nodejsLambdaArn) throw new Error('nodejsLambdaArn is required');
    return { orderId, nodejsLambdaArn: event.nodejsLambdaArn, receivedAt: new Date().toISOString() };
  });

  // Step 2: Call the enricher Lambda
  // If this Lambda crashes AFTER this step, replay skips it and uses the cached result
  const enrichment = await context.step('enrich-order', async () => {
    console.log(`[Step 2] Invoking enricher Lambda for ${orderId}`);
    const response = await lambda.send(new InvokeCommand({
      FunctionName: validatedOrder.nodejsLambdaArn,
      Payload: JSON.stringify({ orderId })
    }));
    return JSON.parse(Buffer.from(response.Payload).toString());
  });

  // Durable wait — survives crashes and restarts
  console.log(`[Wait] Pausing for 5 seconds...`);
  await context.wait({ seconds: 5 });
  console.log(`[Wait] Resumed after 5 seconds`);

  // Step 3: Finalize
  const result = await context.step('finalize-order', async () => {
    console.log(`[Step 3] Finalizing order ${orderId}`);
    return {
      orderId,
      status: 'COMPLETED',
      enrichedData: enrichment,
      finalizedAt: new Date().toISOString()
    };
  });

  console.log(`[Done] Order ${orderId} processed successfully`);
  return result;
}

exports.handler = withDurableExecution(handler);