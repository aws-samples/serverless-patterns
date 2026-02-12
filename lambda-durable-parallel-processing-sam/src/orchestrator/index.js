const { LambdaClient, InvokeCommand } = require('@aws-sdk/client-lambda');
const { withDurableExecution } = require('@aws/durable-execution-sdk-js');

const lambdaClient = new LambdaClient({
  maxAttempts: 3,
  retryMode: 'adaptive'
});

// Structured Logger
class Logger {
  constructor(context) {
    this.requestId = context?.awsRequestId || 'unknown';
    this.functionName = context?.functionName || 'unknown';
  }

  log(level, message, metadata = {}) {
    const logEntry = {
      timestamp: new Date().toISOString(),
      level,
      requestId: this.requestId,
      functionName: this.functionName,
      message,
      ...metadata
    };
    console.log(JSON.stringify(logEntry));
  }

  info(message, metadata) { this.log('INFO', message, metadata); }
  error(message, metadata) { this.log('ERROR', message, metadata); }
  warn(message, metadata) { this.log('WARN', message, metadata); }
  debug(message, metadata) { this.log('DEBUG', message, metadata); }
}

// Custom Error Classes
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

class WorkerInvocationError extends Error {
  constructor(message, workerName, cause) {
    super(message);
    this.name = 'WorkerInvocationError';
    this.workerName = workerName;
    this.cause = cause;
  }
}

// Validation Functions
function validateEvent(event, logger) {
  if (!event) {
    throw new ValidationError('Event object is null or undefined', 'event');
  }

  if (!event.orderId) {
    throw new ValidationError('orderId is required', 'orderId');
  }

  if (!event.items || !Array.isArray(event.items) || event.items.length === 0) {
    throw new ValidationError('items array is required and must not be empty', 'items');
  }

  if (!event.customer || !event.customer.id) {
    throw new ValidationError('customer.id is required', 'customer.id');
  }

  if (!event.customer.address || !event.customer.address.state) {
    throw new ValidationError('customer.address.state is required for tax calculation', 'customer.address.state');
  }

  logger.info('Event validation successful', { 
    orderId: event.orderId, 
    itemCount: event.items.length,
    customerId: event.customer.id
  });

  return event;
}

// Worker Invocation Helper
async function invokeWorker(functionArn, payload, workerName, logger) {
  logger.info(`Invoking ${workerName} worker`, { functionArn, payload });

  try {
    const command = new InvokeCommand({
      FunctionName: functionArn,
      InvocationType: 'RequestResponse',
      Payload: JSON.stringify(payload)
    });

    const response = await lambdaClient.send(command);

    if (response.FunctionError) {
      const errorPayload = JSON.parse(Buffer.from(response.Payload).toString());
      logger.error(`${workerName} worker returned error`, { 
        functionError: response.FunctionError, 
        errorPayload 
      });
      throw new WorkerInvocationError(
        `${workerName} worker error: ${response.FunctionError}`, 
        workerName, 
        errorPayload
      );
    }

    const result = JSON.parse(Buffer.from(response.Payload).toString());
    logger.info(`${workerName} worker invocation successful`, { 
      statusCode: result.statusCode,
      success: result.success
    });
    
    return result;
  } catch (error) {
    if (error instanceof WorkerInvocationError) throw error;
    
    logger.error(`Failed to invoke ${workerName} worker`, { 
      error: error.message, 
      stack: error.stack 
    });
    throw new WorkerInvocationError(
      `Failed to invoke ${workerName} worker`, 
      workerName, 
      error
    );
  }
}

// Main Durable Handler
async function handler(event, context) {
  const logger = new Logger(context);
  const startTime = Date.now();
  
  console.log('='.repeat(80));
  console.log('🚀 DURABLE FUNCTION EXECUTION STARTED');
  console.log('='.repeat(80));
  
  logger.info('Starting parallel order processing', { 
    event, 
    remainingTimeMs: context.getRemainingTimeInMillis?.() 
  });

  try {
    // Step 1: Validate Input
    console.log('\n📋 STEP 1: Validating Input');
    const validatedEvent = await context.step('validate-input', async () => {
      console.log('   ✓ Executing validation logic...');
      return validateEvent(event, logger);
    });
    console.log('   ✅ Input validation completed successfully');

    const { orderId, items, customer } = validatedEvent;
    logger.info('Input validation complete', { orderId });

    // Step 2: Calculate Order Subtotal
    console.log('\n💰 STEP 2: Calculating Order Subtotal');
    const subtotal = await context.step('calculate-subtotal', async () => {
      console.log('   ✓ Computing subtotal from items...');
      const total = items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
      logger.info('Subtotal calculated', { orderId, subtotal: total, itemCount: items.length });
      return total;
    });
    console.log(`   ✅ Subtotal calculated: $${subtotal.toFixed(2)}`);

    // Step 3: Parallel Processing - Execute all validations concurrently
    console.log('\n⚡ STEP 3: Starting Parallel Worker Execution');
    console.log('   📤 Launching 4 concurrent workers:');
    console.log('      • Inventory Check');
    console.log('      • Payment Validation');
    console.log('      • Shipping Calculation');
    console.log('      • Tax Calculation');
    
    logger.info('Starting parallel worker execution', { orderId });
    
    const parallelResults = await context.parallel([
      // Task 1: Inventory Check
      async (childCtx) => {
        return await childCtx.step('check-inventory', async () => {
          console.log('   🔄 [Worker 1/4] Inventory Check - Executing...');
          const result = await invokeWorker(
            process.env.INVENTORY_FUNCTION_ARN,
            { orderId, items },
            'InventoryCheck',
            logger
          );
          console.log('   ✓ [Worker 1/4] Inventory Check - Completed');
          return result;
        });
      },
      
      // Task 2: Payment Validation
      async (childCtx) => {
        return await childCtx.step('validate-payment', async () => {
          console.log('   🔄 [Worker 2/4] Payment Validation - Executing...');
          const result = await invokeWorker(
            process.env.PAYMENT_FUNCTION_ARN,
            { orderId, customer, amount: subtotal },
            'PaymentValidation',
            logger
          );
          console.log('   ✓ [Worker 2/4] Payment Validation - Completed');
          return result;
        });
      },
      
      // Task 3: Shipping Calculation
      async (childCtx) => {
        return await childCtx.step('calculate-shipping', async () => {
          console.log('   🔄 [Worker 3/4] Shipping Calculation - Executing...');
          const result = await invokeWorker(
            process.env.SHIPPING_FUNCTION_ARN,
            { orderId, items, address: customer.address },
            'ShippingCalculation',
            logger
          );
          console.log('   ✓ [Worker 3/4] Shipping Calculation - Completed');
          return result;
        });
      },
      
      // Task 4: Tax Calculation
      async (childCtx) => {
        return await childCtx.step('calculate-tax', async () => {
          console.log('   🔄 [Worker 4/4] Tax Calculation - Executing...');
          const result = await invokeWorker(
            process.env.TAX_FUNCTION_ARN,
            { orderId, subtotal, state: customer.address.state },
            'TaxCalculation',
            logger
          );
          console.log('   ✓ [Worker 4/4] Tax Calculation - Completed');
          return result;
        });
      }
    ]);

    console.log('   ✅ All parallel workers completed successfully');
    
    logger.info('Parallel execution completed', { 
      orderId, 
      resultsCount: parallelResults.all.length 
    });

    // Extract results from parallel execution
    // parallel() returns an object with 'all' array containing {result, index, status}
    const results = parallelResults.all.map(item => item.result);
    const [inventoryResult, paymentResult, shippingResult, taxResult] = results;

    // Step 4: Validate All Results
    console.log('\n🔍 STEP 4: Validating Worker Results');
    const validationResult = await context.step('validate-results', async () => {
      console.log('   ✓ Checking all worker responses...');
      const failures = [];

      if (!inventoryResult.success || !inventoryResult.available) {
        failures.push({ 
          step: 'inventory', 
          reason: inventoryResult.message || 'Items not available' 
        });
      }

      if (!paymentResult.success || !paymentResult.valid) {
        failures.push({ 
          step: 'payment', 
          reason: paymentResult.message || 'Payment validation failed' 
        });
      }

      if (!shippingResult.success) {
        failures.push({ 
          step: 'shipping', 
          reason: shippingResult.message || 'Shipping calculation failed' 
        });
      }

      if (!taxResult.success) {
        failures.push({ 
          step: 'tax', 
          reason: taxResult.message || 'Tax calculation failed' 
        });
      }

      if (failures.length > 0) {
        console.log('   ❌ Validation failures detected:', failures);
        logger.warn('Validation failures detected', { orderId, failures });
        return { valid: false, failures };
      }

      console.log('   ✅ All validations passed');
      logger.info('All validations passed', { orderId });
      return { valid: true, failures: [] };
    });

    // If validation failed, return early
    if (!validationResult.valid) {
      console.log('\n❌ ORDER PROCESSING FAILED - Validation errors');
      logger.error('Order processing failed validation', { 
        orderId, 
        failures: validationResult.failures 
      });
      
      return {
        success: false,
        orderId,
        message: 'Order validation failed',
        failures: validationResult.failures,
        processingTimeMs: Date.now() - startTime,
        timestamp: new Date().toISOString()
      };
    }

    // Step 5: Calculate Final Totals
    console.log('\n🧮 STEP 5: Calculating Final Totals');
    const finalTotals = await context.step('calculate-final-totals', async () => {
      console.log('   ✓ Computing final order totals...');
      const shipping = shippingResult.shippingCost || 0;
      const tax = taxResult.taxAmount || 0;
      const total = subtotal + shipping + tax;

      console.log(`   • Subtotal: $${subtotal.toFixed(2)}`);
      console.log(`   • Shipping: $${shipping.toFixed(2)}`);
      console.log(`   • Tax:      $${tax.toFixed(2)}`);
      console.log(`   • Total:    $${total.toFixed(2)}`);

      logger.info('Final totals calculated', { 
        orderId, 
        subtotal, 
        shipping, 
        tax, 
        total 
      });

      return {
        subtotal,
        shipping,
        tax,
        total,
        currency: 'USD'
      };
    });
    console.log('   ✅ Final totals calculated');

    // Step 6: Wait before finalization (simulating async processing)
    console.log('\n⏸️  STEP 6: Durable Wait (1 second)');
    console.log('   ⚠️  Function will PAUSE here - no compute charges during wait');
    console.log('   ⚠️  Execution will be checkpointed and resumed after 1 second');
    logger.info('Waiting 1 second before finalization', { orderId });
    
    await context.wait({ seconds: 1 });
    
    console.log('   ▶️  Function RESUMED after wait period');
    console.log('   ✅ Wait completed - continuing execution');

    // Step 7: Finalize Order
    console.log('\n✨ STEP 7: Finalizing Order');
    const finalResult = await context.step('finalize-order', async () => {
      console.log('   ✓ Creating order confirmation...');
      logger.info('Finalizing order', { orderId });
      
      return {
        orderId,
        status: 'CONFIRMED',
        inventory: {
          available: inventoryResult.available,
          reservationId: inventoryResult.reservationId
        },
        payment: {
          valid: paymentResult.valid,
          authorizationCode: paymentResult.authorizationCode
        },
        shipping: {
          cost: shippingResult.shippingCost,
          estimatedDays: shippingResult.estimatedDeliveryDays,
          carrier: shippingResult.carrier
        },
        tax: {
          amount: taxResult.taxAmount,
          rate: taxResult.taxRate,
          jurisdiction: taxResult.jurisdiction
        },
        totals: finalTotals,
        confirmedAt: new Date().toISOString()
      };
    });
    console.log('   ✅ Order finalized successfully');

    const processingTime = Date.now() - startTime;
    
    console.log('\n' + '='.repeat(80));
    console.log('✅ DURABLE FUNCTION EXECUTION COMPLETED SUCCESSFULLY');
    console.log(`   Order ID: ${orderId}`);
    console.log(`   Status: ${finalResult.status}`);
    console.log(`   Processing Time: ${processingTime}ms`);
    console.log('='.repeat(80) + '\n');
    
    logger.info('Order processing complete', { 
      orderId, 
      status: finalResult.status,
      processingTimeMs: processingTime
    });

    return {
      success: true,
      orderId,
      result: finalResult,
      message: 'Order processed successfully with parallel execution',
      processingTimeMs: processingTime,
      timestamp: new Date().toISOString()
    };

  } catch (error) {
    const processingTime = Date.now() - startTime;
    
    console.log('\n' + '='.repeat(80));
    console.log('❌ DURABLE FUNCTION EXECUTION FAILED');
    console.log(`   Error: ${error.name} - ${error.message}`);
    console.log(`   Processing Time: ${processingTime}ms`);
    console.log('='.repeat(80) + '\n');
    
    logger.error('Order processing failed', { 
      error: error.message, 
      errorName: error.name, 
      stack: error.stack,
      processingTimeMs: processingTime
    });

    return {
      success: false,
      error: { 
        name: error.name, 
        message: error.message,
        field: error.field,
        workerName: error.workerName
      },
      message: 'Order processing failed',
      processingTimeMs: processingTime,
      timestamp: new Date().toISOString()
    };
  }
}

exports.handler = withDurableExecution(handler);
