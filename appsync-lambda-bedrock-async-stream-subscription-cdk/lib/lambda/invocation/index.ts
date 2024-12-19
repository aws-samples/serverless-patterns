import { BedrockRuntimeClient, InvokeModelWithResponseStreamCommand } from '@aws-sdk/client-bedrock-runtime';
import { GraphQLClient } from 'graphql-request';

interface Event {
  input: {
    conversationId: string;
    prompt: string;
  };
}

function sanitizeGraphQLString(text: string): string {
  return text
    .replace(/[\n\r]/g, ' ')    // Replace newlines with spaces
    .replace(/\\/g, '\\\\')     // Escape backslashes
    .replace(/"/g, '\\"')       // Escape double quotes
    .replace(/\t/g, ' ')        // Replace tabs with spaces
    .trim();                    // Remove leading/trailing whitespace
}

export const handler = async (event: Event) => {
  console.log('Received event:', JSON.stringify(event));

  const { conversationId, prompt } = event.input;

  if (!conversationId || !prompt) {
    console.error('Invalid input: Missing conversationId or prompt');
    return;
  }

  console.log(`Starting Bedrock stream for conversationId: ${conversationId}`);

  const bedrockClient = new BedrockRuntimeClient({});
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
  const params = {
    modelId: 'anthropic.claude-v2',
    contentType: 'application/json',
    accept: 'application/json',
    body: JSON.stringify({
      anthropic_version: 'bedrock-2023-05-31',
      max_tokens: 4096,
      messages: [{ role: 'user', content: input }],
    }),
  };

  const command = new InvokeModelWithResponseStreamCommand(params);
  const stream = await bedrockClient.send(command);

  if (!stream.body) {
    throw new Error('No response stream received from Bedrock');
  }

  let buffer = '';
  const chunkSize = 100; // Adjust based on your needs

  try {
    for await (const chunk of stream.body) {
      if (!chunk.chunk?.bytes) continue;

      const parsed = JSON.parse(Buffer.from(chunk.chunk.bytes).toString('utf-8'));
      if (!parsed.delta?.text) continue;

      buffer += parsed.delta.text;

      // Send chunks when buffer reaches certain size or contains complete sentences
      if (buffer.length >= chunkSize || buffer.match(/[.!?]\s/)) {
        const sanitizedChunk = sanitizeGraphQLString(buffer);
        if (sanitizedChunk) {
          await sendChunkToAppSync(graphQLClient, conversationId, sanitizedChunk);
        }
        buffer = '';
      }
    }

    // Send any remaining text in buffer
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
