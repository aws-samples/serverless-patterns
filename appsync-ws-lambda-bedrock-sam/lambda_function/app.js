const { BedrockRuntimeClient, InvokeModelCommand } = require('@aws-sdk/client-bedrock-runtime');

const client = new BedrockRuntimeClient({ region: process.env.BEDROCK_REGION });

exports.handler = async (event) => {
  const input = {
    modelId: process.env.MODEL_ID,
    contentType: 'application/json',
    accept: 'application/json',
    body: JSON.stringify({
      anthropic_version: 'bedrock-2023-05-31',
      max_tokens: 1000,
      messages: [{
        role: 'user',
        content: event.arguments.input
      }]
    })
  };

  const command = new InvokeModelCommand(input);
  const response = await client.send(command);
  const result = JSON.parse(new TextDecoder().decode(response.body));
  
  return result.content[0].text;
};
