const { BedrockRuntimeClient, InvokeModelCommand } = require('@aws-sdk/client-bedrock-runtime');

const client = new BedrockRuntimeClient();

exports.handler = async (event) => {
  const prompt = event.prompt || 'What is Amazon Bedrock? Answer in 2 sentences.';
  const teamName = process.env.TEAM_NAME || 'unknown';

  const response = await client.send(new InvokeModelCommand({
    modelId: process.env.MODEL_ID,
    contentType: 'application/json',
    accept: 'application/json',
    body: JSON.stringify({
      anthropic_version: 'bedrock-2023-05-31',
      max_tokens: 256,
      messages: [{ role: 'user', content: prompt }],
    }),
  }));

  const body = JSON.parse(new TextDecoder().decode(response.body));
  return {
    statusCode: 200,
    team: teamName,
    costAllocationTags: { team: teamName, 'cost-center': process.env.COST_CENTER || 'tagged-on-role' },
    response: body.content[0].text,
    note: 'This invocation is attributed to the IAM role tagged with team and cost-center. Check CUR 2.0 for line_item_iam_principal.',
  };
};
