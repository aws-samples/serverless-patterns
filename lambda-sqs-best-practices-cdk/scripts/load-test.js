const AWS = require('aws-sdk');
const sqs = new AWS.SQS();

AWS.config.update({ 
    region: process.env.AWS_REGION || 'us-east-1' // Default to us-east-1 or your preferred region
});

const QUEUE_URL = process.env.QUEUE_URL;
const MESSAGE_COUNT = parseInt(process.env.MESSAGE_COUNT || '100');
const BATCH_SIZE = 10;

// Create message with 10% chance of failure
const createMessage = (index) => {
    // Random number between 0 and 1
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
            await sqs.sendMessageBatch({
                QueueUrl: QUEUE_URL,
                Entries: entries
            }).promise();
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
    sendMessages();
}
