const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require('@aws-sdk/lib-dynamodb');

const dynamoClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(dynamoClient);
const ORDERS_TABLE = process.env.ORDERS_TABLE;

/**
 * Order Status Function (Non-Durable)
 * 
 * This is a separate, regular Lambda function for checking order status.
 * It queries DynamoDB directly without invoking the durable function.
 */
exports.handler = async (event) => {
  console.log('Checking order status', { event });
  
  try {
    const orderId = event.pathParameters?.orderId;
    
    if (!orderId) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error: 'Order ID is required' })
      };
    }
    
    const result = await docClient.send(new GetCommand({
      TableName: ORDERS_TABLE,
      Key: { orderId }
    }));
    
    if (!result.Item) {
      return {
        statusCode: 404,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          error: 'Order not found',
          orderId 
        })
      };
    }
    
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        orderId: result.Item.orderId,
        status: result.Item.status,
        customerId: result.Item.customerId,
        customerEmail: result.Item.customerEmail,
        total: result.Item.total,
        items: result.Item.items,
        createdAt: result.Item.validatedAt || result.Item.updatedAt,
        lastUpdated: result.Item.updatedAt,
        errorMessage: result.Item.errorMessage
      })
    };
  } catch (error) {
    console.error('Error getting order status', { error });
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        error: 'Failed to get order status',
        message: error.message 
      })
    };
  }
};
