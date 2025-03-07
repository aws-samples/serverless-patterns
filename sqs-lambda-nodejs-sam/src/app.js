/**
 * Process individual SQS record
 * 
 * @param {Object} record - The SQS record to process
 * @returns {Object} Processing result with success status
 */
async function processSQSMessage(record) {
    const messageBody = record.body;
    try {
        // Randomly fail some messages for demonstration
        if (Math.random() < 0.2) {
            console.log(`Randomly failing message: ${record.body}`);
            throw new Error('Random processing failure');
        }

        // Extract message body
        const messageBody = record.body;
        // Log the message for debugging
        console.log(`Processing message: ${record.messageId}`);
        // Simulate some processing, add your business logic here
        await new Promise(resolve => setTimeout(resolve, 100));

        console.log(`Successfully processed message: ${record.body}`);
        return { success: true };
    } catch (error) {
        console.error(`Failed to process record ${record.messageId}:`, error);
        return { success: false };
    }
};

exports.handler = async (event) => {
    console.log('Received event:', JSON.stringify(event, null, 2));
    const batchItemFailures = [];

    // Process each record individually
    for (const record of event.Records) {
        const result = await processSQSMessage(record);
        if (!result.success) {
            batchItemFailures.push({
                itemIdentifier: record.messageId
            });
        }
    }

    // Return the failed items to be returned to the queue
    return {
        batchItemFailures: batchItemFailures
    };
}; 