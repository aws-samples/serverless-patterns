exports.handler = async (event) => {
  console.log('='.repeat(60));
  console.log('💵 TAX CALCULATION WORKER - Started');
  console.log('='.repeat(60));
  
  console.log(JSON.stringify({ 
    timestamp: new Date().toISOString(), 
    level: 'INFO', 
    message: 'Tax calculation started', 
    event 
  }));

  try {
    const { orderId, subtotal, state } = event;

    console.log(`\n📋 Order ID: ${orderId}`);
    console.log(`💰 Subtotal: $${subtotal?.toFixed(2) || '0.00'}`);
    console.log(`📍 State: ${state || 'N/A'}`);

    if (!orderId || subtotal === undefined || !state) {
      console.log('❌ Validation failed - Missing required fields');
      return {
        statusCode: 400,
        success: false,
        message: 'Missing required fields: orderId, subtotal, or state'
      };
    }

    // State tax rates (simplified - real implementation would use tax service)
    const stateTaxRates = {
      'CA': 0.0725,  // California
      'NY': 0.0400,  // New York
      'TX': 0.0625,  // Texas
      'FL': 0.0600,  // Florida
      'WA': 0.0650,  // Washington
      'IL': 0.0625,  // Illinois
      'PA': 0.0600,  // Pennsylvania
      'OH': 0.0575,  // Ohio
      'GA': 0.0400,  // Georgia
      'NC': 0.0475,  // North Carolina
      'MI': 0.0600,  // Michigan
      'NJ': 0.0663,  // New Jersey
      'VA': 0.0530,  // Virginia
      'MA': 0.0625,  // Massachusetts
      'AZ': 0.0560,  // Arizona
      'TN': 0.0700,  // Tennessee
      'IN': 0.0700,  // Indiana
      'MO': 0.0423,  // Missouri
      'MD': 0.0600,  // Maryland
      'WI': 0.0500   // Wisconsin
    };

    const taxRate = stateTaxRates[state] || 0.0500; // Default 5% for unknown states
    const taxAmount = parseFloat((subtotal * taxRate).toFixed(2));

    // Determine jurisdiction
    const jurisdiction = state in stateTaxRates ? `${state} State Tax` : `${state} State Tax (Default Rate)`;

    console.log('\n🧮 Tax Calculation:');
    console.log(`   Tax Rate: ${(taxRate * 100).toFixed(2)}%`);
    console.log(`   Tax Amount: $${taxAmount.toFixed(2)}`);
    console.log(`   Jurisdiction: ${jurisdiction}`);

    // Simulate processing time (50-150ms)
    await new Promise(resolve => setTimeout(resolve, 50 + Math.random() * 100));

    const result = {
      statusCode: 200,
      success: true,
      taxAmount,
      taxRate,
      subtotal,
      jurisdiction,
      state,
      message: 'Tax calculated successfully',
      calculatedAt: new Date().toISOString()
    };

    console.log(JSON.stringify({ 
      timestamp: new Date().toISOString(), 
      level: 'INFO', 
      message: 'Tax calculation completed', 
      orderId,
      taxAmount,
      taxRate,
      state
    }));

    console.log('\n' + '='.repeat(60));
    console.log('✅ TAX CALCULATION WORKER - Completed Successfully');
    console.log('='.repeat(60) + '\n');

    return result;

  } catch (error) {
    console.log('\n' + '='.repeat(60));
    console.log('❌ TAX CALCULATION WORKER - Failed');
    console.log(`   Error: ${error.message}`);
    console.log('='.repeat(60) + '\n');
    
    console.error(JSON.stringify({ 
      timestamp: new Date().toISOString(), 
      level: 'ERROR', 
      message: 'Tax calculation failed', 
      error: error.message,
      stack: error.stack
    }));

    return {
      statusCode: 500,
      success: false,
      message: `Tax calculation failed: ${error.message}`
    };
  }
};
