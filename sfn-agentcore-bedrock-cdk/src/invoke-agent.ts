import { BedrockAgentCoreClient, InvokeAgentRuntimeCommand } from '@aws-sdk/client-bedrock-agentcore';

const client = new BedrockAgentCoreClient();

export const handler = async (event) => {
  const { agentRuntimeArn, prompt } = event;

  const response = await client.send(new InvokeAgentRuntimeCommand({
    agentRuntimeArn,
    payload: Buffer.from(JSON.stringify({ prompt })),
    contentType: 'application/json',
    accept: 'application/json',
  }));

  // Collect streaming response
  let fullResponse = '';
  if (response.response) {
    const reader = response.response;
    if (typeof reader[Symbol.asyncIterator] === 'function') {
      for await (const chunk of reader) {
        fullResponse += typeof chunk === 'string' ? chunk : new TextDecoder().decode(chunk);
      }
    } else {
      fullResponse = reader.toString();
    }
  }

  return {
    agentRuntimeArn,
    response: fullResponse || 'No response',
    sessionId: response.runtimeSessionId,
  };
};
