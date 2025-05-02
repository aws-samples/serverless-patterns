const { SQSClient, SendMessageBatchCommand } = require('@aws-sdk/client-sqs');

// Initialize SQS client
const sqs = new SQSClient({
    region: process.env.AWS_REGION || 'us-east-1'
});

const QUEUE_URL = process.env.QUEUE_URL;
const MESSAGE_COUNT = parseInt(process.env.MESSAGE_COUNT || '100');
const BATCH_SIZE = 10;

// Create message with 10% chance of failure
const createMessage = (index) => {
    const rand = Math.random();

    // 5% chance for invalid format
    if (rand < 0.05) {
        return JSON.stringify("not an object");
    }
    
    // 5% chance for missing required field
    if (rand < 0.10) {
        return JSON.stringify({ data: "missing id field" });
    }

    // 90% valid messages
    return JSON.stringify({
        id: `msg-${index}`,
        data: `test data ${index}`
    });
};

async function sendMessages() {
    console.log(`Sending ${MESSAGE_COUNT} messages...`);
    
    for (let i = 0; i < MESSAGE_COUNT; i += BATCH_SIZE) {
        const entries = Array.from({ length: Math.min(BATCH_SIZE, MESSAGE_COUNT - i) }, 
            (_, index) => ({
                Id: (i + index).toString(),
                MessageBody: createMessage(i + index)
            })
        );

        try {
            const command = new SendMessageBatchCommand({
                QueueUrl: QUEUE_URL,
                Entries: entries
            });

            const response = await sqs.send(command);
            
            if (response.Failed && response.Failed.length > 0) {
                console.warn('Some messages failed to send:', response.Failed);
            }
        } catch (error) {
            console.error('Batch send error:', error);
        }
    }

    console.log('Messages sent');
}

if (require.main === module) {
    if (!QUEUE_URL) {
        console.error('Please set QUEUE_URL environment variable');
        process.exit(1);
    }
    sendMessages().catch(console.error);
}