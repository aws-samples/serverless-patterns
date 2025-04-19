const { Logger } = require('@aws-lambda-powertools/logger');
const { Metrics } = require('@aws-lambda-powertools/metrics');
const { Tracer } = require('@aws-lambda-powertools/tracer');
const AWS = require('aws-sdk');

// Initialize Powertools
const logger = new Logger({
    serviceName: process.env.POWERTOOLS_SERVICE_NAME,
    logLevel: 'INFO'
});

const metrics = new Metrics({
    namespace: process.env.POWERTOOLS_METRICS_NAMESPACE,
    serviceName: process.env.POWERTOOLS_SERVICE_NAME
});

const tracer = new Tracer({
    serviceName: process.env.POWERTOOLS_SERVICE_NAME
});

// Capture AWS SDK
const awsSDK = tracer.captureAWS(AWS);

const processMessage = async (message, messageId, messageType) => {
    try {
        // Add trace annotations
        tracer.putAnnotation('messageId', messageId);
        tracer.putAnnotation('messageType', messageType);

        console.log(`Processing ${messageType} message: ${messageId}`, message);
        logger.info('Processing message', { messageId, message, messageType });

        if (messageType === 'json') {
            console.log('Processing JSON message:', {
                id: message.id,
                data: message.data
            });
        } else {
            console.log('Processing plain text message:', message);
        }

        // Simulate processing
        await new Promise(resolve => setTimeout(resolve, 100));

        console.log(`Successfully processed ${messageType} message: ${messageId}`);
        
        metrics.addMetric('SuccessfulMessages', 'Count', 1);
        metrics.addMetric(`Successful${messageType.toUpperCase()}Messages`, 'Count', 1);
        return true;
    } catch (error) {
        console.error(`Error processing ${messageType} message ${messageId}:`, error);
        logger.error('Failed to process message', { 
            messageId,
            messageType,
            error: error.message 
        });
        metrics.addMetric('FailedMessages', 'Count', 1);
        metrics.addMetric(`Failed${messageType.toUpperCase()}Messages`, 'Count', 1);
        return false;
    }
};

const parseMessage = (body) => {
    try {
        const jsonMessage = JSON.parse(body);
        return { message: jsonMessage, type: 'json' };
    } catch (error) {
        return { message: body, type: 'text' };
    }
};

const handler = async (event) => {
    console.log('Lambda invocation started', { Records: event.Records.length });
    const batchItemFailures = [];

    try {
        tracer.putAnnotation('batchSize', event.Records.length);
        console.log(`Processing batch of ${event.Records.length} messages`);
        logger.info('Starting batch processing', { 
            batchSize: event.Records.length 
        });

        metrics.addMetric('BatchSize', 'Count', event.Records.length);

        for (const record of event.Records) {
            try {
                console.log('Processing record:', record.messageId);
                
                const { message, type } = parseMessage(record.body);
                const success = await processMessage(message, record.messageId, type);
                
                if (!success) {
                    console.log(`Failed to process message: ${record.messageId}`);
                    batchItemFailures.push({ itemIdentifier: record.messageId });
                }
            } catch (error) {
                console.error(`Error processing record ${record.messageId}:`, error);
                logger.error('Record processing failed', { 
                    messageId: record.messageId,
                    error: error.message 
                });
                batchItemFailures.push({ itemIdentifier: record.messageId });
            }
        }

        const results = {
            total: event.Records.length,
            failed: batchItemFailures.length,
            succeeded: event.Records.length - batchItemFailures.length
        };

        tracer.putAnnotation('processedMessages', results.total);
        tracer.putAnnotation('failedMessages', results.failed);

        console.log('Batch processing completed', results);
        logger.info('Batch processing completed', results);

        metrics.publishStoredMetrics();
        return { batchItemFailures };
    } catch (error) {
        console.error('Fatal error in batch processing:', error);
        logger.error('Batch processing error', { error: error.message });
        throw error;
    }
};

// Wrap handler with Powertools
exports.handler = handler;