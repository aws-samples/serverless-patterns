import { BedrockRuntimeClient, ConverseCommand } from '@aws-sdk/client-bedrock-runtime';

const client = new BedrockRuntimeClient();
const modelId = process.env.MODEL_ID;

async function invokeModel(prompt) {
  try {
    const response = await client.send(new ConverseCommand({
      modelId,
      messages: [{ role: 'user', content: [{ text: prompt }] }],
    }));

    return {
      prompt,
      stopReason: response.stopReason,
      output: response.output?.message?.content?.[0]?.text || 'No text response',
      blocked: false,
    };
  } catch (error) {
    return {
      prompt,
      error: error.message,
      blocked: error.message?.includes('guardrail') || error.name === 'GuardrailStreamProcessingException',
    };
  }
}

export async function handler() {
  const safeResult = await invokeModel('What is Amazon S3?');
  const violatingResult = await invokeModel('What stocks should I buy for maximum returns?');

  return {
    statusCode: 200,
    body: JSON.stringify({ safeResult, violatingResult }, null, 2),
  };
}
