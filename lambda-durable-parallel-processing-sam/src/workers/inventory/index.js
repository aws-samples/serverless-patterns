exports.handler = async (event) => {
  console.log('='.repeat(60));
  console.log('📦 INVENTORY CHECK WORKER - Started');
  console.log('='.repeat(60));
  
  console.log(JSON.stringify({ 
    timestamp: new Date().toISOString(), 
    level: 'INFO', 
    message: 'Inventory check started', 
    event 
  }));

  try {
    const { orderId, items } = event;

    console.log(`\n📋 Order ID: ${orderId}`);
    console.log(`📊 Items to check: ${items?.length || 0}`);

    if (!orderId || !items) {
      console.log('❌ Validation failed - Missing required fields');
      return {
        statusCode: 400,
        success: false,
        available: false,
        message: 'Missing required fields: orderId or items'
      };
    }

    // Simulate inventory check logic
    console.log('\n🔍 Checking inventory for each item...');
    const inventoryChecks = items.map((item, index) => {
      // Simulate: 90% chance items are available
      const available = Math.random() > 0.1;
      const stockLevel = available ? item.quantity + Math.floor(Math.random() * 50) : 0;
      
      console.log(`   ${index + 1}. Product ${item.productId}: ${available ? '✅ Available' : '❌ Out of Stock'} (Stock: ${stockLevel})`);
      
      return {
        productId: item.productId,
        requestedQuantity: item.quantity,
        available,
        stockLevel
      };
    });

    const allAvailable = inventoryChecks.every(check => check.available);
    const reservationId = allAvailable ? `RES-${Date.now()}-${Math.random().toString(36).substr(2, 9)}` : null;

    console.log(`\n📌 Overall Status: ${allAvailable ? '✅ All items available' : '⚠️  Some items unavailable'}`);
    if (reservationId) {
      console.log(`🎫 Reservation ID: ${reservationId}`);
    }

    // Simulate processing time (50-200ms)
    await new Promise(resolve => setTimeout(resolve, 50 + Math.random() * 150));

    const result = {
      statusCode: 200,
      success: true,
      available: allAvailable,
      reservationId,
      items: inventoryChecks,
      message: allAvailable ? 'All items available' : 'Some items unavailable',
      checkedAt: new Date().toISOString()
    };

    console.log(JSON.stringify({ 
      timestamp: new Date().toISOString(), 
      level: 'INFO', 
      message: 'Inventory check completed', 
      orderId,
      available: allAvailable,
      itemCount: items.length
    }));

    console.log('\n' + '='.repeat(60));
    console.log('✅ INVENTORY CHECK WORKER - Completed Successfully');
    console.log('='.repeat(60) + '\n');

    return result;

  } catch (error) {
    console.log('\n' + '='.repeat(60));
    console.log('❌ INVENTORY CHECK WORKER - Failed');
    console.log(`   Error: ${error.message}`);
    console.log('='.repeat(60) + '\n');
    
    console.error(JSON.stringify({ 
      timestamp: new Date().toISOString(), 
      level: 'ERROR', 
      message: 'Inventory check failed', 
      error: error.message,
      stack: error.stack
    }));

    return {
      statusCode: 500,
      success: false,
      available: false,
      message: `Inventory check failed: ${error.message}`
    };
  }
};
