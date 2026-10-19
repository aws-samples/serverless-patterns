import { withDurableExecution } from "@aws/durable-execution-sdk-js";

export const handler = withDurableExecution(async (event, context) => {
  const tenantId = context.lambdaContext.tenantId;
  const body = JSON.parse(event.body || "{}");
  const envId = process.env.AWS_LAMBDA_LOG_STREAM_NAME;

  const validated = await context.step(async (stepCtx) => {
    stepCtx.logger.info(`Step 1: Validating for tenant ${tenantId}`);
    return { tenantId, requestId: body.requestId, status: "validated", environment: envId };
  });

  const callbackResult = await context.waitForCallback(async (callbackToken) => {
    console.log(JSON.stringify({ waiting: true, callbackToken, tenantId }));
  });

  const completed = await context.step(async (stepCtx) => {
    stepCtx.logger.info(`Step 2: Completing for tenant ${tenantId}`);
    return { tenantId, requestId: body.requestId, status: "completed", callbackPayload: callbackResult, environment: envId };
  });

  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ validated, completed })
  };
});
