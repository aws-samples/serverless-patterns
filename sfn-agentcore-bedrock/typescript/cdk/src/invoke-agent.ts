import { BedrockAgentCoreClient, InvokeAgentRuntimeCommand } from '@aws-sdk/client-bedrock-agentcore';

const client = new BedrockAgentCoreClient();

export const handler = async (event: { agentRuntimeArn: string; prompt: string }) => {
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
    if (typeof (reader as any)[Symbol.asyncIterator] === 'function') {
      for await (const chunk of reader as any) {
        fullResponse += typeof chunk === 'string' ? chunk : new TextDecoder().decode(chunk as Uint8Array);
      }
    } else {
      fullResponse = String(reader);
    }
  }

  return {
    agentRuntimeArn,
    response: fullResponse || 'No response',
    sessionId: response.runtimeSessionId,
  };
};
