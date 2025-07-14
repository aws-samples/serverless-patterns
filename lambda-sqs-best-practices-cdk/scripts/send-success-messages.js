const { SQSClient, SendMessageBatchCommand, ReceiveMessageCommand, GetQueueAttributesCommand } = require('@aws-sdk/client-sqs');

// Initialize SQS client
const sqs = new SQSClient({
    region: process.env.AWS_REGION || 'us-east-1'
});

const QUEUE_URL = process.env.QUEUE_URL;
const DLQ_URL = process.env.DLQ_URL;
const MESSAGE_COUNT = 50;
const BATCH_SIZE = 10;

// Create valid message with id and data
const createMessage = (index) => {
    return JSON.stringify({
        id: `id-${index}`,
        data: `Sample data for message ${index}`
    });
};

async function sendMessages() {
    console.log(`Sending ${MESSAGE_COUNT} messages...`);
    let successCount = 0;
    
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
            successCount += response.Successful?.length || 0;
            
            // Log progress
            console.log(`Progress: ${Math.round((successCount / MESSAGE_COUNT) * 100)}%`);
        } catch (error) {
            console.error('Batch send error:', error);
        }
    }

    console.log(`Successfully sent ${successCount} messages`);
}

async function getDLQCount() {
    try {
        const response = await sqs.send(new GetQueueAttributesCommand({
            QueueUrl: DLQ_URL,
            AttributeNames: ['ApproximateNumberOfMessages']
        }));
        return parseInt(response.Attributes?.ApproximateNumberOfMessages || '0');
    } catch (error) {
        console.error('Error getting DLQ count:', error.message);
        return 0;
    }
}

async function getDLQMessages() {
    console.log('\nRetrieving DLQ messages...');
    const messages = [];
    let emptyCount = 0;
    
    while (emptyCount < 3) {
        try {
            const response = await sqs.send(new ReceiveMessageCommand({
                QueueUrl: DLQ_URL,
                MaxNumberOfMessages: 10,
                WaitTimeSeconds: 2,
                AttributeNames: ['All']
            }));
            
            if (!response.Messages?.length) {
                emptyCount++;
                continue;
            }
            
            emptyCount = 0;
            messages.push(...response.Messages);
            console.log(`Retrieved ${response.Messages.length} messages (Total: ${messages.length})`);
        } catch (error) {
            console.error('DLQ retrieval error:', error.message);
            break;
        }
    }
    
    return messages;
}

async function runTest() {
    if (!QUEUE_URL || !DLQ_URL) {
        console.error('Please set QUEUE_URL and DLQ_URL environment variables');
        process.exit(1);
    }
    
    await sendMessages();
    
    console.log('\nWaiting 30 seconds for message processing...');
    await new Promise(resolve => setTimeout(resolve, 30000));
    
    const dlqCount = await getDLQCount();
    console.log(`\nDLQ Count (Approximate): ${dlqCount}`);
    
    if (dlqCount > 0) {
        const dlqMessages = await getDLQMessages();
        console.log(`\n=== DLQ Messages (${dlqMessages.length}) ===`);
        dlqMessages.forEach((msg, i) => {
            console.log(`${i + 1}. ID: ${msg.MessageId}`);
            console.log(`   Body: ${msg.Body.substring(0, 80)}...`);
            console.log(`   Receive Count: ${msg.Attributes?.ApproximateReceiveCount || 'N/A'}`);
        });
    } else {
        console.log('No messages found in DLQ');
    }
}

if (require.main === module) {
    runTest().catch(console.error);
}