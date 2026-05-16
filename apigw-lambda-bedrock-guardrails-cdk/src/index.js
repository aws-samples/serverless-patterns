const { BedrockRuntimeClient, InvokeModelCommand } = require('@aws-sdk/client-bedrock-runtime');

const client = new BedrockRuntimeClient();

exports.handler = async (event) => {
  const body = JSON.parse(event.body || '{}');
  const prompt = body.prompt || 'Hello';

  const response = await client.send(new InvokeModelCommand({
    modelId: process.env.MODEL_ID,
    contentType: 'application/json',
    accept: 'application/json',
    guardrailIdentifier: process.env.GUARDRAIL_ID,
    guardrailVersion: process.env.GUARDRAIL_VERSION,
    body: JSON.stringify({
      anthropic_version: 'bedrock-2023-05-31',
      max_tokens: 512,
      messages: [{ role: 'user', content: prompt }],
    }),
  }));

  const result = JSON.parse(new TextDecoder().decode(response.body));

  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      response: result.content?.[0]?.text,
      stopReason: result.stop_reason,
      guardrailAction: response.guardrailAction || 'NONE',
      usage: result.usage,
    }),
  };
};
