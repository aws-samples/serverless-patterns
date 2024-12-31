import { BedrockRuntimeClient, ConverseStreamCommand, ConverseStreamCommandInput } from '@aws-sdk/client-bedrock-runtime';
import { GraphQLClient } from 'graphql-request';

interface Event {
  input: {
    conversationId: string;
    prompt: string;
  };
}

function sanitizeGraphQLString(text: string): string {
  return text
    .replace(/[\n\r]/g, ' ')
    .replace(/\\/g, '\\\\')
    .replace(/"/g, '\\"')
    .replace(/\t/g, ' ')
    .trim();
}

export const handler = async (event: Event) => {
  console.log('Received event:', JSON.stringify(event));

  const { conversationId, prompt } = event.input;

  if (!conversationId || !prompt) {
    console.error('Invalid input: Missing conversationId or prompt');
    return;
  }

  console.log(`Starting Bedrock stream for conversationId: ${conversationId}`);

  // Using the us-east-1 Bedrock Inference Profile for Claude Sonnet 3.5 V2
  const bedrockClient = new BedrockRuntimeClient({
    region: 'us-east-1'
  });
  const graphQLClient = new GraphQLClient(process.env.APPSYNC_ENDPOINT!, {
    headers: { 'x-api-key': process.env.APPSYNC_API_KEY! },
  });

  try {
    await processBedrockStream(bedrockClient, graphQLClient, prompt, conversationId);
    console.log(`Successfully completed processing for conversationId: ${conversationId}`);
  } catch (error) {
    console.error(`Error during processing for conversationId ${conversationId}:`, error);
    await notifyError(graphQLClient, conversationId, error);
  }
};

async function processBedrockStream(
  bedrockClient: BedrockRuntimeClient,
  graphQLClient: GraphQLClient,
  input: string,
  conversationId: string
): Promise<void> {
  const params: ConverseStreamCommandInput = {
    modelId: 'us.anthropic.claude-3-5-sonnet-20241022-v2:0',
    messages: [
      {
        role: 'user',
        content: [
          {
            text: input
          }
        ]
      }
    ],
    inferenceConfig: {
      temperature: 0.7,
      maxTokens: 4096,
      topP: 1
    }
  };
  

  const command = new ConverseStreamCommand(params);
  const response = await bedrockClient.send(command);

  if (!response.stream) {
    throw new Error('No response stream received from Bedrock');
  }


  let buffer = '';
  const chunkSize = 100;

  try {
    for await (const event of response.stream) {
      if (event.contentBlockDelta && event.contentBlockDelta.delta) {
        const delta = event.contentBlockDelta.delta.text;
        if (delta) {
          buffer += delta;
    
          if (buffer.length >= chunkSize || buffer.match(/[.!?]\s/)) {
            const sanitizedChunk = sanitizeGraphQLString(buffer);
            if (sanitizedChunk) {
              await sendChunkToAppSync(graphQLClient, conversationId, sanitizedChunk);
            }
            buffer = '';
          }
        }
      }
    }    

    if (buffer) {
      const sanitizedChunk = sanitizeGraphQLString(buffer);
      if (sanitizedChunk) {
        await sendChunkToAppSync(graphQLClient, conversationId, sanitizedChunk);
      }
    }

    await completeStream(graphQLClient, conversationId);
  } catch (error) {
    console.error(`Error while processing stream for conversationId ${conversationId}:`, error);
    throw error;
  }
}


async function sendChunkToAppSync(
  graphQLClient: GraphQLClient,
  conversationId: string,
  chunk: string
): Promise<void> {
  const mutation = `
    mutation SendChunk($conversationId: ID!, $chunk: String!) {
      sendChunk(conversationId: $conversationId, chunk: $chunk) {
        conversationId
        chunk
      }
    }
  `;

  try {
    await graphQLClient.request(mutation, { conversationId, chunk });
    console.log(`Sent chunk to AppSync for conversationId ${conversationId}`);
  } catch (error) {
    console.error(`Failed to send chunk to AppSync for conversationId ${conversationId}:`, error);
    throw error;
  }
}

async function completeStream(
  graphQLClient: GraphQLClient,
  conversationId: string
): Promise<void> {
  const mutation = `
    mutation Complete($conversationId: ID!) {
      completeStream(conversationId: $conversationId) {
        conversationId
        status
      }
    }
  `;

  await graphQLClient.request(mutation, { conversationId });
  console.log(`Stream completed for conversationId ${conversationId}`);
}

async function notifyError(
  graphQLClient: GraphQLClient,
  conversationId: string,
  error: unknown
): Promise<void> {
  const errorMessage = error instanceof Error ? error.message : 'Unknown error';
  const sanitizedError = sanitizeGraphQLString(errorMessage);

  const mutation = `
    mutation SendError($conversationId: ID!, $error: String!) {
      sendError(conversationId: $conversationId, error: $error) {
        conversationId
        error
      }
    }
  `;

  await graphQLClient.request(mutation, {
    conversationId,
    error: sanitizedError,
  });
}
