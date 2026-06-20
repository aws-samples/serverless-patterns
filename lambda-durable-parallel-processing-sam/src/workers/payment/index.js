exports.handler = async (event) => {
  console.log('='.repeat(60));
  console.log('💳 PAYMENT VALIDATION WORKER - Started');
  console.log('='.repeat(60));
  
  console.log(JSON.stringify({ 
    timestamp: new Date().toISOString(), 
    level: 'INFO', 
    message: 'Payment validation started', 
    event 
  }));

  try {
    const { orderId, customer, amount } = event;

    console.log(`\n📋 Order ID: ${orderId}`);
    console.log(`👤 Customer ID: ${customer?.id || 'N/A'}`);
    console.log(`💵 Amount: $${amount?.toFixed(2) || '0.00'}`);
    console.log(`💳 Payment Method: ${customer?.paymentMethod || 'credit_card'}`);

    if (!orderId || !customer || amount === undefined) {
      console.log('❌ Validation failed - Missing required fields');
      return {
        statusCode: 400,
        success: false,
        valid: false,
        message: 'Missing required fields: orderId, customer, or amount'
      };
    }

    // Simulate payment validation logic
    console.log('\n🔐 Validating payment method...');
    
    // Simulate: 95% success rate
    const isValid = Math.random() > 0.05;
    const authorizationCode = isValid ? `AUTH-${Date.now()}-${Math.random().toString(36).substr(2, 9).toUpperCase()}` : null;

    // Simulate processing time (100-300ms)
    await new Promise(resolve => setTimeout(resolve, 100 + Math.random() * 200));

    console.log(`\n${isValid ? '✅' : '❌'} Payment ${isValid ? 'Authorized' : 'Declined'}`);
    if (authorizationCode) {
      console.log(`🎫 Authorization Code: ${authorizationCode}`);
    }

    const result = {
      statusCode: 200,
      success: true,
      valid: isValid,
      authorizationCode,
      amount,
      paymentMethod: customer.paymentMethod || 'credit_card',
      message: isValid ? 'Payment validated successfully' : 'Payment validation failed',
      validatedAt: new Date().toISOString()
    };

    console.log(JSON.stringify({ 
      timestamp: new Date().toISOString(), 
      level: 'INFO', 
      message: 'Payment validation completed', 
      orderId,
      valid: isValid,
      amount
    }));

    console.log('\n' + '='.repeat(60));
    console.log('✅ PAYMENT VALIDATION WORKER - Completed Successfully');
    console.log('='.repeat(60) + '\n');

    return result;

  } catch (error) {
    console.log('\n' + '='.repeat(60));
    console.log('❌ PAYMENT VALIDATION WORKER - Failed');
    console.log(`   Error: ${error.message}`);
    console.log('='.repeat(60) + '\n');
    
    console.error(JSON.stringify({ 
      timestamp: new Date().toISOString(), 
      level: 'ERROR', 
      message: 'Payment validation failed', 
      error: error.message,
      stack: error.stack
    }));

    return {
      statusCode: 500,
      success: false,
      valid: false,
      message: `Payment validation failed: ${error.message}`
    };
  }
};
