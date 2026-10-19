import { LambdaClient, SendDurableExecutionCallbackSuccessCommand } from "@aws-sdk/client-lambda";

const client = new LambdaClient({ region: process.env.AWS_REGION });

export const handler = async (event) => {
  let body;
  if (typeof event.body === 'string') {
    body = JSON.parse(event.body);
  } else {
    body = event;
  }

  const callbackId = body.callbackId;
  const result = JSON.stringify(body.payload || {});

  if (!callbackId) {
    return {
      statusCode: 400,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ error: "Missing callbackId" })
    };
  }

  await client.send(new SendDurableExecutionCallbackSuccessCommand({
    CallbackId: callbackId,
    Result: result
  }));

  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: "Callback sent" })
  };
};
