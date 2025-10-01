import {
  BedrockRuntimeClient,
  InvokeModelCommand,
  InvokeModelCommandInput,
} from "@aws-sdk/client-bedrock-runtime";

const region = process.env.AWS_REGION || "us-east-1";
const client = new BedrockRuntimeClient({ region });

interface AppSyncEvent {
  arguments: {
    prompt: string;
  };
}

// Expected response structure for Claude 3 Messages API
interface Claude3MessagesResponseBody {
  id: string;
  type: string;
  role: "assistant";
  content: Array<{
    type: "text";
    text: string;
  }>;
  model: string;
  stop_reason: string;
  // other fields might exist
}

export const handler = async (event: AppSyncEvent): Promise<string> => {
  console.log("Received AppSync event:", JSON.stringify(event, null, 2));

  const userPrompt = event.arguments.prompt;

  if (
    !userPrompt ||
    typeof userPrompt !== "string" ||
    userPrompt.trim() === ""
  ) {
    console.error(
      "Validation Error: Prompt is required and must be a non-empty string."
    );
    throw new Error("Prompt is required and must be a non-empty string.");
  }

  // Model ID from environment variable, defaults to a common Claude 3 Sonnet ID.
  // IMPORTANT: Replace with your specific model ID if different and verified.
  const modelId =
    process.env.MODEL_ID || "anthropic.claude-3-sonnet-20240229-v1:0";
  const anthropicVersion =
    process.env.ANTHROPIC_VERSION || "bedrock-2023-05-31";

  // Default parameters from your example, can be overridden by environment variables
  const maxTokens = process.env.MAX_TOKENS
    ? parseInt(process.env.MAX_TOKENS)
    : 200;
  const temperature = process.env.TEMPERATURE
    ? parseFloat(process.env.TEMPERATURE)
    : 1;
  const topP = process.env.TOP_P ? parseFloat(process.env.TOP_P) : 0.999;
  const topK = process.env.TOP_K ? parseInt(process.env.TOP_K) : 250;
  // const stopSequences = process.env.STOP_SEQUENCES ? JSON.parse(process.env.STOP_SEQUENCES) : [];

  // Construct the payload for Claude 3 Messages API
  const bedrockRequestBody = {
    anthropic_version: anthropicVersion,
    max_tokens: maxTokens,
    temperature: temperature,
    top_p: topP,
    top_k: topK,
    // stop_sequences: stopSequences, // Bedrock API expects an array of strings
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: userPrompt,
          },
        ],
      },
    ],
  };

  const invokeParams: InvokeModelCommandInput = {
    modelId: modelId,
    contentType: "application/json",
    accept: "application/json",
    body: JSON.stringify(bedrockRequestBody),
  };

  try {
    console.log(
      `Invoking Bedrock model '${modelId}' with payload: ${JSON.stringify(
        bedrockRequestBody
      ).substring(0, 500)}...`
    );
    const command = new InvokeModelCommand(invokeParams);
    const response = await client.send(command);

    const responseBodyString = new TextDecoder().decode(response.body);
    const responseBody = JSON.parse(
      responseBodyString
    ) as Claude3MessagesResponseBody;

    console.log(
      "Bedrock raw response body:",
      JSON.stringify(responseBody, null, 2)
    );

    if (
      !responseBody.content ||
      !Array.isArray(responseBody.content) ||
      responseBody.content.length === 0 ||
      !responseBody.content[0].text
    ) {
      console.error(
        "Bedrock response error: 'content[0].text' field is missing or invalid.",
        responseBody
      );
      throw new Error(
        "Bedrock response error: 'content[0].text' field is missing or invalid in model output."
      );
    }

    return responseBody.content[0].text.trim();
  } catch (error: any) {
    console.error("Error invoking Bedrock model:", error);
    throw new Error(
      `Bedrock invocation failed for model ${modelId}: ${
        error.message || "Unknown error"
      }`
    );
  }
};
