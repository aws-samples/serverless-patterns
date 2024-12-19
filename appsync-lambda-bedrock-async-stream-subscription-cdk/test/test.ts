import { GraphQLClient } from 'graphql-request';
import { SubscriptionClient } from 'subscriptions-transport-ws';
import WebSocket from 'ws';

// Replace these with your AppSync API details
const APPSYNC_API_URL = 'https://utgypaxdjjcq3lo4y4jvk5v5pi.appsync-api.us-east-1.amazonaws.com/graphql'; // e.g., https://<api-id>.appsync-api.<region>.amazonaws.com/graphql
const APPSYNC_API_KEY = 'da2-qkexqqvs4bhhpigpaodgqdhgwu';
const WEBSOCKET_URL = APPSYNC_API_URL.replace('https', 'wss');

// Replace this with your test data
const TEST_CONVERSATION_ID = '123e4567-e89b-12d3-a456-426614174000';
const TEST_PROMPT = 'Tell me a long story';

// Initialize GraphQL client
const graphQLClient = new GraphQLClient(APPSYNC_API_URL, {
  headers: {
    'x-api-key': APPSYNC_API_KEY,
  },
});

// Function to create a conversation
async function createConversation(conversationId: string) {
  const mutation = `
    mutation CreateConversation($conversationId: ID!) {
      createConversation(conversationId: $conversationId) {
        conversationId
        status
      }
    }
  `;

  const variables = { conversationId };

  console.log('Creating conversation...');
  const response = await graphQLClient.request(mutation, variables);
  console.log('CreateConversation response:', response);
}

// Function to start a conversation
async function startConversation(prompt: string, conversationId: string) {
  const mutation = `
    mutation StartConversation($input: StartConversationInput!) {
      startConversation(input: $input) {
        conversationId
        status
      }
    }
  `;

  const variables = {
    input: { prompt, conversationId },
  };

  console.log('Starting conversation...');
  const response = await graphQLClient.request(mutation, variables);
  console.log('StartConversation response:', response);
}

// Function to subscribe to updates
function subscribeToChunks(conversationId: string) {
  return new Promise((resolve, reject) => {
    const subscriptionQuery = `
      subscription OnReceiveChunk($conversationId: ID!) {
        onReceiveChunk(conversationId: $conversationId) {
          conversationId
          chunk
        }
      }
    `;

    const client = new SubscriptionClient(WEBSOCKET_URL, {
      reconnect: true,
      connectionParams: {
        headers: { 'x-api-key': APPSYNC_API_KEY },
      },
    }, WebSocket);

    console.log('Starting subscription...');

    const subscription = client.request({
      query: subscriptionQuery,
      variables: { conversationId },
    }).subscribe({
      next(data) {
        console.log('Subscription update received:', data);
        if (data.errors) {
          reject(data.errors);
        }
      },
      error(err) {
        console.error('Subscription error:', err);
        reject(err);
      },
      complete() {
        console.log('Subscription completed.');
        resolve(null);
      },
    });

    // Close the subscription after some time (optional)
    setTimeout(() => {
      console.log('Closing subscription...');
      subscription.unsubscribe();
      client.close();
    }, 60000); // Close after 60 seconds
  });
}

// Main function to orchestrate the test
async function main() {
  try {
    // Step 1: Create a conversation
    await createConversation(TEST_CONVERSATION_ID);

    // Step 2: Start a subscription for updates
    subscribeToChunks(TEST_CONVERSATION_ID);

    // Step 3: Trigger the long-running invocation (start conversation)
    setTimeout(async () => {
      await startConversation(TEST_PROMPT, TEST_CONVERSATION_ID);
    }, 5000); // Delay to ensure subscription is established before triggering mutation

  } catch (error) {
    console.error('Error during test:', error);
  }
}

main();
