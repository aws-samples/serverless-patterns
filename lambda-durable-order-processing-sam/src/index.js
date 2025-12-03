const { withDurableExecution } = require('@aws/durable-execution-sdk-js');
const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, PutCommand, UpdateCommand } = require('@aws-sdk/lib-dynamodb');

const dynamoClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(dynamoClient);
const ORDERS_TABLE = process.env.ORDERS_TABLE;

/**
 * Order Processing Durable Function
 * 
 * This function demonstrates a multi-step order processing workflow:
 * 1. Validate order
 * 2. Check inventory
 * 3. Process payment
 * 4. Reserve inventory
 * 5. Wait for fulfillment preparation
 * 6. Ship order
 * 7. Send confirmation
 */
exports.handler = withDurableExecution(async (event, context) => {
  console.log('Starting order processing', { event });
  
  const order = typeof event === 'string' ? JSON.parse(event) : event;
  const orderId = order.orderId || `order-${Date.now()}`;
  
  try {
    // Step 1: Validate Order
    const validatedOrder = await context.step('validate-order', async () => {
      console.log('Validating order', { orderId });
      
      // Simulate validation logic
      if (!order.items || order.items.length === 0) {
        throw new Error('Order must contain at least one item');
      }
      
      if (!order.customerId) {
        throw new Error('Customer ID is required');
      }
      
      // Calculate total
      const total = order.items.reduce((sum, item) => {
        return sum + (item.price * item.quantity);
      }, 0);
      
      const validated = {
        ...order,
        orderId,
        total,
        status: 'validated',
        validatedAt: new Date().toISOString()
      };
      
      // Save to DynamoDB
      await docClient.send(new PutCommand({
        TableName: ORDERS_TABLE,
        Item: validated
      }));
      
      return validated;
    });
    
    // Step 2: Check Inventory
    const inventoryCheck = await context.step('check-inventory', async () => {
      console.log('Checking inventory', { orderId });
      
      // Simulate inventory check
      const available = validatedOrder.items.every(item => {
        // Simulate: 90% chance items are in stock
        return Math.random() > 0.1;
      });
      
      if (!available) {
        throw new Error('Insufficient inventory');
      }
      
      await updateOrderStatus(orderId, 'inventory-checked');
      
      return {
        available: true,
        checkedAt: new Date().toISOString()
      };
    });
    
    // Step 3: Process Payment
    const paymentResult = await context.step('process-payment', async () => {
      console.log('Processing payment', { orderId, amount: validatedOrder.total });
      
      // Simulate payment processing
      // In real scenario, this would call a payment gateway
      const paymentId = `pay-${Date.now()}`;
      
      // Simulate: 95% success rate
      if (Math.random() < 0.05) {
        throw new Error('Payment declined');
      }
      
      await updateOrderStatus(orderId, 'payment-processed');
      
      return {
        paymentId,
        amount: validatedOrder.total,
        status: 'success',
        processedAt: new Date().toISOString()
      };
    });
    
    // Step 4: Reserve Inventory
    const reservation = await context.step('reserve-inventory', async () => {
      console.log('Reserving inventory', { orderId });
      
      // Simulate inventory reservation
      const reservationId = `res-${Date.now()}`;
      
      await updateOrderStatus(orderId, 'inventory-reserved');
      
      return {
        reservationId,
        items: validatedOrder.items,
        reservedAt: new Date().toISOString()
      };
    });
    
    // Step 5: Wait for fulfillment preparation (simulate warehouse processing time)
    console.log('Waiting for fulfillment preparation', { orderId });
    await context.wait({ seconds: 30 }); // In production, this could be hours
    
    // Step 6: Ship Order
    const shipment = await context.step('ship-order', async () => {
      console.log('Shipping order', { orderId });
      
      // Simulate shipping
      const trackingNumber = `TRK-${Date.now()}`;
      const carrier = 'FastShip';
      
      await updateOrderStatus(orderId, 'shipped');
      
      return {
        trackingNumber,
        carrier,
        estimatedDelivery: new Date(Date.now() + 3 * 24 * 60 * 60 * 1000).toISOString(),
        shippedAt: new Date().toISOString()
      };
    });
    
    // Step 7: Send Confirmation
    const confirmation = await context.step('send-confirmation', async () => {
      console.log('Sending confirmation', { orderId });
      
      // Simulate sending email/SMS
      const notification = {
        type: 'email',
        recipient: order.customerEmail || 'customer@example.com',
        subject: `Order ${orderId} Confirmed`,
        sentAt: new Date().toISOString()
      };
      
      await updateOrderStatus(orderId, 'completed');
      
      return notification;
    });
    
    // Return final result
    const result = {
      orderId,
      status: 'completed',
      order: validatedOrder,
      payment: paymentResult,
      shipment,
      completedAt: new Date().toISOString()
    };
    
    console.log('Order processing completed', { result });
    return result;
    
  } catch (error) {
    console.error('Order processing failed', { orderId, error: error.message });
    
    // Compensation logic - rollback changes
    await context.step('compensate', async () => {
      console.log('Running compensation logic', { orderId });
      
      await updateOrderStatus(orderId, 'failed', error.message);
      
      // In production, you would:
      // - Refund payment if processed
      // - Release inventory reservation
      // - Notify customer of failure
      
      return {
        compensated: true,
        reason: error.message
      };
    });
    
    throw error;
  }
});

/**
 * Helper function to update order status in DynamoDB
 */
async function updateOrderStatus(orderId, status, errorMessage = null) {
  const updateExpression = errorMessage 
    ? 'SET #status = :status, errorMessage = :error, updatedAt = :updatedAt'
    : 'SET #status = :status, updatedAt = :updatedAt';
  
  const expressionAttributeValues = errorMessage
    ? { ':status': status, ':error': errorMessage, ':updatedAt': new Date().toISOString() }
    : { ':status': status, ':updatedAt': new Date().toISOString() };
  
  await docClient.send(new UpdateCommand({
    TableName: ORDERS_TABLE,
    Key: { orderId },
    UpdateExpression: updateExpression,
    ExpressionAttributeNames: {
      '#status': 'status'
    },
    ExpressionAttributeValues: expressionAttributeValues
  }));
}
