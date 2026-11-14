import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand, DeleteCommand } from '@aws-sdk/lib-dynamodb';
import { ApiGatewayManagementApiClient, PostToConnectionCommand } from '@aws-sdk/client-apigatewaymanagementapi';
import { BedrockRuntimeClient, InvokeModelCommand } from '@aws-sdk/client-bedrock-runtime';

const ddbClient = new DynamoDBClient({});
const ddb = DynamoDBDocumentClient.from(ddbClient);
// Bedrock client using region from environment variable
const bedrock = new BedrockRuntimeClient({ region: process.env.BEDROCK_REGION });

export const handler = async (event) => {
  const { routeKey, connectionId } = event.requestContext;
  const tableName = process.env.CONNECTIONS_TABLE;

  try {
    switch (routeKey) {
      case '$connect':
        await ddb.send(new PutCommand({
          TableName: tableName,
          Item: { connectionId }
        }));
        return { statusCode: 200 };

      case '$disconnect':
        await ddb.send(new DeleteCommand({
          TableName: tableName,
          Key: { connectionId }
        }));
        return { statusCode: 200 };

      case '$default':
        const message = JSON.parse(event.body || '{}');
        const userMessage = message.data || 'Hello';
        
        const apiGw = new ApiGatewayManagementApiClient({
          endpoint: `https://${event.requestContext.domainName}/${event.requestContext.stage}`
        });
        
        try {
          // Invoke Bedrock Claude model
          const bedrockResponse = await bedrock.send(new InvokeModelCommand({
            modelId: process.env.BEDROCK_MODEL_ID,
            body: JSON.stringify({
              anthropic_version: 'bedrock-2023-05-31',
              max_tokens: 1000,
              messages: [{
                role: 'user',
                content: userMessage
              }]
            })
          }));
          
          const responseBody = JSON.parse(new TextDecoder().decode(bedrockResponse.body));
          const aiResponse = responseBody.content[0].text;
          
          await apiGw.send(new PostToConnectionCommand({
            ConnectionId: connectionId,
            Data: JSON.stringify({ message: aiResponse })
          }));
        } catch (bedrockError) {
          console.error('Bedrock error:', bedrockError);
          await apiGw.send(new PostToConnectionCommand({
            ConnectionId: connectionId,
            Data: JSON.stringify({ 
              message: `Sorry, I'm having trouble connecting to the AI service. Please try again in a moment.` 
            })
          }));
        }
        
        return { statusCode: 200 };

      default:
        return { statusCode: 400, body: 'Unknown route' };
    }
  } catch (error) {
    console.error('Error:', error);
    return { statusCode: 500, body: JSON.stringify({ error: error.message }) };
  }
};