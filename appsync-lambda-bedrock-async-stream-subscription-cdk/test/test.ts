import { Amplify } from 'aws-amplify';
import { generateClient } from 'aws-amplify/api';

// AppSync API Configuration

const APPSYNC_API_URL = '<REPLACE THIS WITH THE DEPLOYED GRAPHQL URL>';
const APPSYNC_API_KEY = '<REPLACE THIS WITH THE DEPLOYED GRAPHQL API KEY>';

// Configure Amplify
Amplify.configure({
  API: {
    GraphQL: {
      endpoint: APPSYNC_API_URL,
      defaultAuthMode: 'apiKey',
      apiKey: APPSYNC_API_KEY
    }
  }
});

// Generate Amplify client
const client = generateClient();

async function startConversation(prompt: string, conversationId: string) {
  const mutation = `
    mutation StartConversation($input: StartConversationInput!) {
      startConversation(input: $input) {
        conversationId
        status
      }
    }
  `;

  console.log('Starting conversation...');
  const response = await client.graphql({
    query: mutation,
    variables: { input: { prompt, conversationId } }
  });
  console.log('StartConversation response:', response);
}

function subscribeToChunks(conversationId: string) {
  const subscription = `
    subscription OnReceiveChunk($conversationId: ID!) {
      onReceiveChunk(conversationId: $conversationId) {
        conversationId
        chunk
      }
    }
  `;

  console.log('Starting subscription...');
  
  // Explicitly cast to `Observable`
  const observable = client.graphql<any>({
    query: subscription,
    variables: { conversationId }
  }) as unknown as { subscribe: Function };

  const subscriptionInstance = observable.subscribe({
    next: (data: { data?: { onReceiveChunk?: { conversationId: string; chunk: string } } }) => {
      console.log('Received chunk:', data?.data?.onReceiveChunk);
    },
    error: (error: Error) => {
      console.error('Subscription error:', error);
    },
    complete: () => {
      console.log('Subscription completed');
    }
  });

  return subscriptionInstance;
}

async function main() {
  try {
    const TEST_CONVERSATION_ID = '123e4567-e89b-12d3-a456-426614174000';
    const TEST_PROMPT = 'Tell me a joke';

    // Step 1: Subscribe to chunks
    const subscription = subscribeToChunks(TEST_CONVERSATION_ID);

    // Step 2: Start the long-running invocation (start conversation)
    setTimeout(async () => {
      await startConversation(TEST_PROMPT, TEST_CONVERSATION_ID);
    }, 2000);

    // Cleanup on process exit
    process.on('SIGINT', () => {
      console.log('Cleaning up...');
      subscription.unsubscribe();
      process.exit();
    });

  } catch (error) {
    console.error('Error during test:', error);
    process.exit(1);
  }
}

main();
