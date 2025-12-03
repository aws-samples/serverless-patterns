const { LambdaClient, InvokeCommand } = require('@aws-sdk/client-lambda');

const lambda = new LambdaClient({});
const FUNCTION_NAME = process.env.AWS_LAMBDA_FUNCTION_NAME.replace('-initiator', '-processor') + ':prod';

/**
 * Order Initiator Function
 * 
 * This function receives order requests via API Gateway and invokes
 * the durable order processing function asynchronously.
 */
exports.handler = async (event) => {
  console.log('Received order request', { event });
  
  try {
    // Parse request body
    const body = JSON.parse(event.body || '{}');
    
    // Validate required fields
    if (!body.customerId) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          error: 'customerId is required'
        })
      };
    }
    
    if (!body.items || body.items.length === 0) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          error: 'items array is required and must not be empty'
        })
      };
    }
    
    // Generate order ID
    const orderId = `order-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    
    const order = {
      orderId,
      customerId: body.customerId,
      customerEmail: body.customerEmail,
      items: body.items,
      createdAt: new Date().toISOString()
    };
    
    // Invoke durable function asynchronously
    const invokeCommand = new InvokeCommand({
      FunctionName: FUNCTION_NAME,
      InvocationType: 'Event', // Asynchronous invocation
      Payload: JSON.stringify(order)
    });
    
    await lambda.send(invokeCommand);
    
    console.log('Order processing initiated', { orderId });
    
    return {
      statusCode: 202,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: 'Order processing initiated',
        orderId,
        statusUrl: `/orders/${orderId}`
      })
    };
    
  } catch (error) {
    console.error('Error initiating order', { error: error.message });
    
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: 'Failed to initiate order processing',
        message: error.message
      })
    };
  }
};
