import { LambdaClient, SendDurableExecutionCallbackSuccessCommand } from "@aws-sdk/client-lambda";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

const lambdaClient = new LambdaClient({});
const ddbClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(ddbClient);

export const handler = async (event) => {
  // Extract approval ID and action from query string
  const approvalId = event.queryStringParameters?.id;
  const action = event.queryStringParameters?.action || 'approve';
  
  console.log('Callback received:', { approvalId, action });
  
  if (!approvalId) {
    return {
      statusCode: 400,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>An Error occurred!</h1><p>Missing approval ID</p></body></html>',
    };
  }
  
  try {
    // Look up the callback token from DynamoDB
    const result = await docClient.send(new GetCommand({
      TableName: process.env.CALLBACK_TABLE_NAME,
      Key: { approvalId: approvalId }
    }));
    
    if (!result.Item) {
      return {
        statusCode: 404,
        headers: { 'Content-Type': 'text/html' },
        body: '<html><body><h1>An Error occurred!</h1><p>Approval ID not found or expired</p></body></html>',
      };
    }
    
    const callbackId = result.Item.callbackId;
    
    // Send callback success to resume the durable function
    const callbackResult = {
      approved: action === 'approve',
      approvalId: approvalId,
      timestamp: new Date().toISOString()
    };
    
    const command = new SendDurableExecutionCallbackSuccessCommand({
      CallbackId: callbackId,
      Result: JSON.stringify(callbackResult)
    });
    
    await lambdaClient.send(command);
    
    const message = action === 'approve' 
      ? '<h1> Request Approved</h1><p>Thank you for approving this request!</p>'
      : '<h1>Request Rejected</h1><p>You have rejected this request!</p>';
    
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'text/html',
      },
      body: `<html><body>${message}</body></html>`,
    };
  } catch (error) {
    console.error('Error resuming workflow:', error);
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>An Error occurred</h1><p>Failed to process approval. The link may have expired.</p></body></html>',
    };
  }
};
