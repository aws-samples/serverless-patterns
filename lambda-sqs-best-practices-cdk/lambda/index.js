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
const processMessage = async (message, messageId) => {

    try {
        logger.info('Processing message', { messageId, message });
        // Validate message
        if (typeof message !== 'object' || !message.id || !message.data) {
            throw new Error('Invalid message format');
        }
        // Simulate processing
        await new Promise(resolve => setTimeout(resolve, 100));
        metrics.addMetric('SuccessfulMessages', 'Count', 1);
        logger.info('Message processed successfully', { messageId });
        return true;
    } catch (error) {
        logger.error('Failed to process message', {
            messageId,
            error: error.message
        });
        metrics.addMetric('FailedMessages', 'Count', 1);
        return false;
    }
};
const parseMessage = (body) => {
    try {
        return JSON.parse(body);
    } catch (error) {
        throw new Error('Invalid JSON format');
    }
};
const handler = async (event) => {
    const batchStartTime = Date.now();
    const batchItemFailures = [];

    //Creating subsegment for Batchprocessing annotations
    const subsegment = tracer.getSegment().addNewSubsegment('BatchProcessing');
    try {
        subsegment.addAnnotation('batchSize', event.Records.length);
        logger.info('Starting batch processing', {
            batchSize: event.Records.length
        });
        metrics.addMetric('BatchSize', 'Count', event.Records.length);
        for (const record of event.Records) {
            try {
                const message = parseMessage(record.body);
                const success = await processMessage(message, record.messageId);
                if (!success) {
                    batchItemFailures.push({ itemIdentifier: record.messageId });
                }
            } catch (error) {
                logger.error('Record processing failed', {
                    messageId: record.messageId,
                    error: error.message
                });
                batchItemFailures.push({ itemIdentifier: record.messageId });
            }
        }
        const batchProcessingTime = Date.now() - batchStartTime;

        // final batch processing result for calculating succeded/failed messages
        const batch_results = {
            total: event.Records.length,
            failed: batchItemFailures.length,
            succeeded: event.Records.length - batchItemFailures.length
        };
        //Adding batch processing annotations
        subsegment.addAnnotation('processedMessages', batch_results.total);
        subsegment.addAnnotation('failedMessages', batch_results.failed);
        logger.info('Batch processing completed', batch_results);
        metrics.addMetric('BatchProcessingTime', 'Milliseconds', batchProcessingTime);
        metrics.publishStoredMetrics();
        //Returning partial batch failure here ( if any )
        return { batchItemFailures };
    } catch (error) {
        logger.error('Batch processing error', { error: error.message });
        throw error;
    } finally {
        subsegment.close();
    }
};
exports.handler = handler;