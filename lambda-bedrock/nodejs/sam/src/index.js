
const {
  BedrockRuntimeClient,
  ConversationRole,
  ConverseCommand,
} = require( "@aws-sdk/client-bedrock-runtime");

const client = new BedrockRuntimeClient({ region: "us-west-2" });

const modelId = "us.amazon.nova-lite-v1:0";

exports.handler = async event => {
  const { text } = event

  const inputText =`provide a summary of the following text in 5 bulletpoints; 
  extract 5 tags to categorize the article in a CMS;
  provide output as a json object with properties :
  "summary" as a list of bulletpoints and "tags" as a list of tags;
  <text>${text}</text>
  `;

  const message = {
    content: [{ text: inputText }],
    role: ConversationRole.USER,
  };

  const request = {
    modelId,
    messages: [message],
    inferenceConfig: {
      maxTokens: 500, // The maximum response length
      temperature: 0.5, // Using temperature for randomness control
      //topP: 0.9,        // Alternative: use topP instead of temperature
    },
  };

  let responseText = "", statusCode = 200;

  try {
    const response = await client.send(new ConverseCommand(request));
    responseText = response.output.message.content[0].text;
    console.log(response.output.message.content[0].text);
  } catch (error) {
    console.error(`ERROR: Can't invoke '${modelId}'. Reason: ${error.message}`);
    responseText = `ERROR: Can't invoke '${modelId}'. Reason: ${error.message}`;
    statusCode = 500;
  }

  const response = {
    statusCode,
    body: JSON.stringify(responseText),
  }

  return response;
  
}
