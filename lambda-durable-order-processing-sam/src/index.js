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
  
  // Parse order data - orderId comes from API Gateway template
  const orderId = event.orderId || `order-${Date.now()}`;
  const body = typeof event.body === 'string' ? JSON.parse(event.body) : event.body;
  const order = { ...body, orderId };
  
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
    
    // Step 5: Fraud Check (parallel with credit check)
    const fraudCheck = await context.step('fraud-check', async () => {
      console.log('Running fraud detection', { orderId });
      
      // Simulate fraud detection analysis
      const riskScore = Math.random() * 100;
      const isFraudulent = riskScore > 95;
      
      if (isFraudulent) {
        throw new Error('Order flagged as fraudulent');
      }
      
      await updateOrderStatus(orderId, 'fraud-checked');
      
      return {
        riskScore,
        status: 'passed',
        checkedAt: new Date().toISOString()
      };
    });
    
    // Step 6: Credit Check
    const creditCheck = await context.step('credit-check', async () => {
      console.log('Checking customer credit', { orderId });
      
      // Simulate credit check for high-value orders
      if (validatedOrder.total > 1000) {
        const creditScore = Math.floor(Math.random() * 300) + 500;
        
        if (creditScore < 600) {
          throw new Error('Insufficient credit score');
        }
        
        return {
          creditScore,
          approved: true,
          checkedAt: new Date().toISOString()
        };
      }
      
      return { skipped: true, reason: 'Order value below threshold' };
    });
    
    // Step 7: Generate Invoice
    const invoice = await context.step('generate-invoice', async () => {
      console.log('Generating invoice', { orderId });
      
      const invoiceId = `INV-${Date.now()}`;
      const invoiceData = {
        invoiceId,
        orderId,
        customerId: validatedOrder.customerId,
        items: validatedOrder.items,
        subtotal: validatedOrder.total,
        tax: validatedOrder.total * 0.08,
        total: validatedOrder.total * 1.08,
        generatedAt: new Date().toISOString()
      };
      
      await updateOrderStatus(orderId, 'invoice-generated');
      
      return invoiceData;
    });
    
    // Step 8: Wait for warehouse processing (showcases long wait without compute charges)
    console.log('Waiting for warehouse processing', { orderId });
    await updateOrderStatus(orderId, 'awaiting-warehouse');
    await context.wait({ seconds: 300 }); // 5 minutes - in production could be hours
    
    // Step 9: Pick Items from Warehouse
    const pickingResult = await context.step('pick-items', async () => {
      console.log('Picking items from warehouse', { orderId });
      
      const pickedItems = validatedOrder.items.map(item => ({
        ...item,
        binLocation: `BIN-${Math.floor(Math.random() * 1000)}`,
        pickedBy: `PICKER-${Math.floor(Math.random() * 50)}`,
        pickedAt: new Date().toISOString()
      }));
      
      await updateOrderStatus(orderId, 'items-picked');
      
      return {
        items: pickedItems,
        completedAt: new Date().toISOString()
      };
    });
    
    // Step 10: Quality Check
    const qualityCheck = await context.step('quality-check', async () => {
      console.log('Performing quality check', { orderId });
      
      // Simulate quality inspection
      const passedQC = Math.random() > 0.02; // 98% pass rate
      
      if (!passedQC) {
        throw new Error('Quality check failed - items damaged');
      }
      
      await updateOrderStatus(orderId, 'quality-checked');
      
      return {
        passed: true,
        inspector: `QC-${Math.floor(Math.random() * 20)}`,
        checkedAt: new Date().toISOString()
      };
    });
    
    // Step 11: Package Order
    const packaging = await context.step('package-order', async () => {
      console.log('Packaging order', { orderId });
      
      const packageId = `PKG-${Date.now()}`;
      const weight = validatedOrder.items.reduce((sum, item) => sum + (item.quantity * 2), 0);
      
      await updateOrderStatus(orderId, 'packaged');
      
      return {
        packageId,
        weight: `${weight} lbs`,
        dimensions: '12x10x8 inches',
        packagedBy: `PACKER-${Math.floor(Math.random() * 30)}`,
        packagedAt: new Date().toISOString()
      };
    });
    
    // Step 12: Generate Shipping Label
    const shippingLabel = await context.step('generate-shipping-label', async () => {
      console.log('Generating shipping label', { orderId });
      
      const trackingNumber = `TRK-${Date.now()}-${Math.random().toString(36).substring(2, 11).toUpperCase()}`;
      const carrier = validatedOrder.total > 500 ? 'ExpressShip' : 'StandardShip';
      
      return {
        trackingNumber,
        carrier,
        labelUrl: `https://shipping.example.com/labels/${trackingNumber}`,
        generatedAt: new Date().toISOString()
      };
    });
    
    // Step 13: Wait for carrier pickup (another long wait)
    console.log('Waiting for carrier pickup', { orderId });
    await updateOrderStatus(orderId, 'awaiting-pickup');
    await context.wait({ seconds: 180 }); // 3 minutes - in production could be hours
    
    // Step 14: Ship Order
    const shipment = await context.step('ship-order', async () => {
      console.log('Order shipped', { orderId });
      
      await updateOrderStatus(orderId, 'shipped');
      
      return {
        ...shippingLabel,
        estimatedDelivery: new Date(Date.now() + 3 * 24 * 60 * 60 * 1000).toISOString(),
        shippedAt: new Date().toISOString()
      };
    });
    
    // Step 15: Send Customer Notifications (parallel notifications)
    const notifications = await context.step('send-notifications', async () => {
      console.log('Sending customer notifications', { orderId });
      
      // Simulate sending multiple notifications
      const emailNotification = {
        type: 'email',
        recipient: order.customerEmail || 'customer@example.com',
        subject: `Order ${orderId} Shipped - Tracking: ${shippingLabel.trackingNumber}`,
        sentAt: new Date().toISOString()
      };
      
      const smsNotification = {
        type: 'sms',
        recipient: order.customerPhone || '+1234567890',
        message: `Your order ${orderId} has shipped! Track: ${shippingLabel.trackingNumber}`,
        sentAt: new Date().toISOString()
      };
      
      return {
        email: emailNotification,
        sms: smsNotification
      };
    });
    
    // Step 16: Update Loyalty Points
    const loyaltyUpdate = await context.step('update-loyalty-points', async () => {
      console.log('Updating loyalty points', { orderId });
      
      const pointsEarned = Math.floor(validatedOrder.total * 0.1); // 10% back in points
      
      return {
        customerId: validatedOrder.customerId,
        pointsEarned,
        newBalance: pointsEarned, // In production, would fetch and add to existing balance
        updatedAt: new Date().toISOString()
      };
    });
    
    // Step 17: Complete Order
    const completion = await context.step('complete-order', async () => {
      console.log('Completing order', { orderId });
      
      await updateOrderStatus(orderId, 'completed');
      
      return {
        completedAt: new Date().toISOString(),
        totalProcessingTime: Date.now() - parseInt(orderId.split('-')[1])
      };
    });
    
    // Return comprehensive result
    const result = {
      orderId,
      status: 'completed',
      order: validatedOrder,
      payment: paymentResult,
      fraudCheck,
      creditCheck,
      invoice,
      picking: pickingResult,
      qualityCheck,
      packaging,
      shipment,
      notifications,
      loyaltyPoints: loyaltyUpdate,
      completion,
      summary: {
        totalSteps: 17,
        totalWaitTime: '8 minutes (480 seconds)',
        processingTime: `${completion.totalProcessingTime}ms`
      }
    };
    
    console.log('Order processing completed successfully', { orderId, totalSteps: 17 });
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

