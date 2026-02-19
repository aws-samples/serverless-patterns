exports.handler = async (event) => {
  console.log('='.repeat(60));
  console.log('📦 SHIPPING CALCULATION WORKER - Started');
  console.log('='.repeat(60));
  
  console.log(JSON.stringify({ 
    timestamp: new Date().toISOString(), 
    level: 'INFO', 
    message: 'Shipping calculation started', 
    event 
  }));

  try {
    const { orderId, items, address } = event;

    console.log(`\n📋 Order ID: ${orderId}`);
    console.log(`📍 Destination: ${address?.state || 'N/A'}, ${address?.zipCode || 'N/A'}`);
    console.log(`📊 Items: ${items?.length || 0}`);

    if (!orderId || !items || !address) {
      console.log('❌ Validation failed - Missing required fields');
      return {
        statusCode: 400,
        success: false,
        message: 'Missing required fields: orderId, items, or address'
      };
    }

    // Calculate total weight (simulate)
    console.log('\n⚖️  Calculating total weight...');
    const totalWeight = items.reduce((sum, item) => {
      const itemWeight = 1.5; // lbs per item (simulated)
      return sum + (itemWeight * item.quantity);
    }, 0);
    console.log(`   Total Weight: ${totalWeight.toFixed(2)} lbs`);

    // Determine shipping cost based on weight and location
    const baseRate = 5.99;
    const perPoundRate = 0.75;
    const shippingCost = parseFloat((baseRate + (totalWeight * perPoundRate)).toFixed(2));

    console.log('\n💰 Calculating shipping cost...');
    console.log(`   Base Rate: $${baseRate.toFixed(2)}`);
    console.log(`   Per Pound Rate: $${perPoundRate.toFixed(2)}`);
    console.log(`   Total Shipping: $${shippingCost.toFixed(2)}`);

    // Estimate delivery days based on location
    const stateZones = {
      'CA': 2, 'OR': 2, 'WA': 2, 'NV': 2, 'AZ': 3,
      'NY': 4, 'NJ': 4, 'PA': 4, 'MA': 4,
      'TX': 3, 'FL': 4, 'IL': 3
    };
    const estimatedDeliveryDays = stateZones[address.state] || 5;

    // Select carrier based on weight
    const carrier = totalWeight > 10 ? 'FedEx' : 'USPS';

    console.log('\n🚚 Delivery Information:');
    console.log(`   Carrier: ${carrier}`);
    console.log(`   Estimated Delivery: ${estimatedDeliveryDays} days`);

    // Simulate processing time (75-200ms)
    await new Promise(resolve => setTimeout(resolve, 75 + Math.random() * 125));

    const result = {
      statusCode: 200,
      success: true,
      shippingCost,
      estimatedDeliveryDays,
      carrier,
      totalWeight,
      address: {
        state: address.state,
        zipCode: address.zipCode
      },
      message: 'Shipping calculated successfully',
      calculatedAt: new Date().toISOString()
    };

    console.log(JSON.stringify({ 
      timestamp: new Date().toISOString(), 
      level: 'INFO', 
      message: 'Shipping calculation completed', 
      orderId,
      shippingCost,
      carrier,
      estimatedDays: estimatedDeliveryDays
    }));

    console.log('\n' + '='.repeat(60));
    console.log('✅ SHIPPING CALCULATION WORKER - Completed Successfully');
    console.log('='.repeat(60) + '\n');

    return result;

  } catch (error) {
    console.log('\n' + '='.repeat(60));
    console.log('❌ SHIPPING CALCULATION WORKER - Failed');
    console.log(`   Error: ${error.message}`);
    console.log('='.repeat(60) + '\n');
    
    console.error(JSON.stringify({ 
      timestamp: new Date().toISOString(), 
      level: 'ERROR', 
      message: 'Shipping calculation failed', 
      error: error.message,
      stack: error.stack
    }));

    return {
      statusCode: 500,
      success: false,
      message: `Shipping calculation failed: ${error.message}`
    };
  }
};
