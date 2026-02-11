const { LambdaClient, InvokeCommand } = require('@aws-sdk/client-lambda');
const { withDurableExecution } = require('@aws/durable-execution-sdk-js');

const lambdaClient = new LambdaClient({
  maxAttempts: 3,
  retryMode: 'adaptive'
});

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
}

class EnrichmentError extends Error {
  constructor(message, orderId, cause) {
    super(message);
    this.name = 'EnrichmentError';
    this.orderId = orderId;
    this.cause = cause;
  }
}

function validateEvent(event, logger) {
  if (!event) {
    throw new Error('Event object is null or undefined');
  }

  if (!event.orderId) {
    logger.warn('Missing orderId in event, using default', { event });
    return { orderId: 'ORDER-001', nodejsLambdaArn: event.nodejsLambdaArn };
  }

  if (!event.nodejsLambdaArn) {
    throw new Error('nodejsLambdaArn is required in event payload');
  }

  return { orderId: event.orderId, nodejsLambdaArn: event.nodejsLambdaArn };
}

async function invokeNodejsLambda(lambdaArn, orderId, logger) {
  logger.info('Invoking Node.js Lambda for enrichment', { lambdaArn, orderId });

  try {
    const command = new InvokeCommand({
      FunctionName: lambdaArn,
      InvocationType: 'RequestResponse',
      Payload: JSON.stringify({ orderId })
    });

    const response = await lambdaClient.send(command);

    if (response.FunctionError) {
      const errorPayload = JSON.parse(Buffer.from(response.Payload).toString());
      logger.error('Node.js Lambda returned error', { orderId, functionError: response.FunctionError, errorPayload });
      throw new EnrichmentError(`Lambda function error: ${response.FunctionError}`, orderId, errorPayload);
    }

    const result = JSON.parse(Buffer.from(response.Payload).toString());
    logger.info('Node.js Lambda invocation successful', { orderId, statusCode: result.statusCode });
    return result;
  } catch (error) {
    if (error instanceof EnrichmentError) throw error;
    logger.error('Failed to invoke Node.js Lambda', { orderId, error: error.message, stack: error.stack });
    throw new EnrichmentError('Failed to invoke enrichment Lambda', orderId, error);
  }
}

function finalizeOrder(orderId, enrichmentResult, logger) {
  logger.info('Finalizing order with enrichment data', { orderId, hasEnrichmentData: !!enrichmentResult });

  try {
    if (!enrichmentResult || enrichmentResult.statusCode !== 200) {
      logger.warn('Enrichment result invalid or incomplete', { orderId, enrichmentResult });
    }

    const finalResult = {
      orderId,
      status: 'COMPLETED',
      enrichedData: enrichmentResult,
      finalizedAt: new Date().toISOString(),
      message: 'Order finalized successfully'
    };

    logger.info('Order finalization complete', { orderId, status: finalResult.status });
    return finalResult;
  } catch (error) {
    logger.error('Error during order finalization', { orderId, error: error.message, stack: error.stack });
    return {
      orderId,
      status: 'PARTIALLY_COMPLETED',
      enrichedData: enrichmentResult,
      finalizedAt: new Date().toISOString(),
      message: 'Order finalized with warnings',
      error: error.message
    };
  }
}

async function handler(event, context) {
  const logger = new Logger(context);
  
  logger.info('Starting durable order processing', { event, remainingTimeMs: context.getRemainingTimeInMillis?.() });

  try {
    const { orderId, nodejsLambdaArn } = validateEvent(event, logger);
    logger.info('Event validation successful', { orderId });

    logger.info('Executing enrichment step', { orderId });
    const enrichmentResult = await context.step('enrich-order', async () => {
      return await invokeNodejsLambda(nodejsLambdaArn, orderId, logger);
    });
    logger.info('Enrichment step completed', { orderId, statusCode: enrichmentResult?.statusCode });

    logger.info('Waiting 2 seconds', { orderId });
    await context.wait({ seconds: 2 });
    logger.info('Wait completed, continuing execution', { orderId });

    logger.info('Executing finalization step', { orderId });
    const finalResult = await context.step('finalize-order', async () => {
      return finalizeOrder(orderId, enrichmentResult, logger);
    });

    logger.info('Order processing complete', { orderId, finalStatus: finalResult.status });

    return {
      success: true,
      orderId,
      enrichmentResult,
      finalResult,
      message: 'Order processed successfully with durable execution',
      processedAt: new Date().toISOString()
    };

  } catch (error) {
    logger.error('Order processing failed', { error: error.message, errorName: error.name, stack: error.stack, orderId: error.orderId });
    return {
      success: false,
      error: { name: error.name, message: error.message, orderId: error.orderId },
      message: 'Order processing failed',
      failedAt: new Date().toISOString()
    };
  }
}

exports.handler = withDurableExecution(handler);
