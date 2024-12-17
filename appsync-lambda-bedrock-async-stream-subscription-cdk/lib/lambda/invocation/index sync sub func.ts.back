import { BedrockRuntimeClient, InvokeModelWithResponseStreamCommand } from "@aws-sdk/client-bedrock-runtime";
import { GraphQLClient } from 'graphql-request';
import { v4 as uuidv4 } from 'uuid';

interface AppSyncEvent {
  arguments: {
    input: string;
  };
}

export const handler = async (event: AppSyncEvent) => {
  console.log('Step 2: Lambda received event:', JSON.stringify(event, null, 2));
  
  const bedrockClient = new BedrockRuntimeClient();
  const graphQLClient = new GraphQLClient(process.env.APPSYNC_ENDPOINT!, {
    headers: {
      'x-api-key': process.env.APPSYNC_API_KEY!
    },
  });
  
  try {
    const input = event.arguments.input;
    if (!input) {
      throw new Error('Input is required');
    }
    
    const conversationId = uuidv4();
    console.log('Generated conversationId:', conversationId);
    
    // Initial response to client
    const response = {
      conversationId,
      status: "PROCESSING"
    };
    
    // Invoke Bedrock with streaming
    const params = {
      modelId: "anthropic.claude-v2",
      contentType: "application/json",
      accept: "application/json",
      body: JSON.stringify({
        anthropic_version: "bedrock-2023-05-31",
        max_tokens: 4096,
        messages: [{
          role: "user",
          content: input
        }]
      })
    };
    
    console.log('Step 3: Invoking Bedrock with params:', JSON.stringify(params, null, 2));
    const command = new InvokeModelWithResponseStreamCommand(params);
    const stream = await bedrockClient.send(command);

    // Process stream and send updates via mutations
    if (stream.body) {
      let accumulatedText = '';
      
      for await (const chunk of stream.body) {
        if (chunk.chunk?.bytes) {
          const parsed = JSON.parse(
            Buffer.from(chunk.chunk.bytes).toString("utf-8")
          );
          console.log('Received chunk from Bedrock:', parsed);
          
          if (parsed.delta?.text) {
            accumulatedText += parsed.delta.text;
            
            // Send mutation to AppSync
            const mutation = `
              mutation SendChunk($conversationId: ID!, $chunk: String!) {
                sendChunk(conversationId: $conversationId, chunk: $chunk) {
                  conversationId
                  chunk
                }
              }
            `;
            
            try {
              const mutationResponse = await graphQLClient.request(mutation, {
                conversationId,
                chunk: parsed.delta.text
              });
              console.log('Step 4: Mutation sent to AppSync:', mutationResponse);
            } catch (error) {
              console.error('Error sending mutation to AppSync:', error);
              if (error instanceof Error) {
                console.error(error.message);
              }
            }
          }
        }
      }
      
      console.log('Step 4: Completed streaming. Total response:', accumulatedText);
    }

    return response;
    
  } catch (error) {
    console.error('Lambda execution error:', error);
    if (error instanceof Error) {
      return {
        conversationId: 'error',
        status: error.message
      };
    }
    return {
      conversationId: 'error',
      status: 'Unknown error occurred'
    };
  }
};
