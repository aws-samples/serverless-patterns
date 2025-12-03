const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require('@aws-sdk/lib-dynamodb');
const { LambdaClient, ListDurableExecutionsCommand, GetDurableExecutionCommand } = require('@aws-sdk/client-lambda');

const dynamoClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(dynamoClient);
const lambda = new LambdaClient({});

const ORDERS_TABLE = process.env.ORDERS_TABLE;
const FUNCTION_NAME = process.env.AWS_LAMBDA_FUNCTION_NAME.replace('-status', '-processor');

/**
 * Order Status Function
 * 
 * This function retrieves the current status of an order by:
 * 1. Fetching order data from DynamoDB
 * 2. Checking durable execution status
 */
exports.handler = async (event) => {
  console.log('Checking order status', { event });
  
  try {
    const orderId = event.pathParameters?.orderId;
    
    if (!orderId) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          error: 'orderId is required'
        })
      };
    }
    
    // Get order from DynamoDB
    const orderResult = await docClient.send(new GetCommand({
      TableName: ORDERS_TABLE,
      Key: { orderId }
    }));
    
    if (!orderResult.Item) {
      return {
        statusCode: 404,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          error: 'Order not found',
          orderId
        })
      };
    }
    
    const order = orderResult.Item;
    
    // Try to get durable execution status
    let executionStatus = null;
    try {
      // List executions for this function
      const listCommand = new ListDurableExecutionsCommand({
        FunctionName: FUNCTION_NAME,
        MaxResults: 10
      });
      
      const executions = await lambda.send(listCommand);
      
      // Find execution for this order (this is simplified - in production you'd store execution ID)
      // For now, we'll just show the order status from DynamoDB
      executionStatus = {
        note: 'Execution details available via GetDurableExecution API with execution ID'
      };
      
    } catch (error) {
      console.warn('Could not fetch execution status', { error: error.message });
    }
    
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        orderId: order.orderId,
        status: order.status,
        customerId: order.customerId,
        total: order.total,
        items: order.items,
        createdAt: order.createdAt,
        updatedAt: order.updatedAt,
        validatedAt: order.validatedAt,
        errorMessage: order.errorMessage,
        execution: executionStatus
      })
    };
    
  } catch (error) {
    console.error('Error checking order status', { error: error.message });
    
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: 'Failed to check order status',
        message: error.message
      })
    };
  }
};
