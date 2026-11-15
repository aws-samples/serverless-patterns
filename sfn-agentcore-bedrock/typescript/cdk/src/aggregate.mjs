import { BedrockRuntimeClient, ConverseCommand } from '@aws-sdk/client-bedrock-runtime';

const bedrockClient = new BedrockRuntimeClient();
const MODEL_ID = process.env.BEDROCK_MODEL_ID;

export const handler = async (event) => {
  const agentResults = event.agentResults || [];

  const responseSummary = agentResults.map((r, i) =>
    `Agent ${i + 1} (${r.agentRuntimeArn || 'unknown'}): ${r.response || 'No response'}`
  ).join('\n\n');

  const result = await bedrockClient.send(new ConverseCommand({
    modelId: MODEL_ID,
    messages: [
      {
        role: 'user',
        content: [
          {
            text: `Summarize and synthesize the following responses from multiple AI agents into a single coherent answer:\n\n${responseSummary}`,
          },
        ],
      },
    ],
  }));

  const outputText = result.output?.message?.content?.[0]?.text || '';

  return {
    summary: outputText,
    agentCount: agentResults.length,
  };
};
