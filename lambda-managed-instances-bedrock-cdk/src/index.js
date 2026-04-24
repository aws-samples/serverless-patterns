const { BedrockRuntimeClient, InvokeModelCommand } = require("@aws-sdk/client-bedrock-runtime");

const client = new BedrockRuntimeClient();
const MODEL_ID = process.env.MODEL_ID;

exports.handler = async (event) => {
  const prompt = event.prompt || "What are the benefits of Lambda Managed Instances?";

  const res = await client.send(
    new InvokeModelCommand({
      modelId: MODEL_ID,
      contentType: "application/json",
      accept: "application/json",
      body: JSON.stringify({
        anthropic_version: "bedrock-2023-05-31",
        max_tokens: 1024,
        messages: [{ role: "user", content: prompt }],
      }),
    })
  );

  const body = JSON.parse(new TextDecoder().decode(res.body));

  return {
    statusCode: 200,
    body: JSON.stringify({
      prompt,
      response: body.content[0].text,
      model: MODEL_ID,
      usage: body.usage,
    }),
  };
};
