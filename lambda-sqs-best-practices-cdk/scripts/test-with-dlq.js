const { SQSClient, SendMessageBatchCommand, ReceiveMessageCommand } = require('@aws-sdk/client-sqs');

const sqs = new SQSClient({ region: process.env.AWS_REGION || 'us-east-1' });
const QUEUE_URL = process.env.QUEUE_URL;
const DLQ_URL = process.env.DLQ_URL;
const TOTAL_MESSAGES = 50;
const BATCH_SIZE = 10;

const createMessage = (index) => index % 5 === 0 ? JSON.stringify("invalid message") : JSON.stringify({ id: `id-${index + 1}`, data: `Sample data for message ${index + 1}` });

async function sendMessages() {
    console.log(`Sending ${TOTAL_MESSAGES} messages in batches of ${BATCH_SIZE}`);
    const batches = Math.ceil(TOTAL_MESSAGES / BATCH_SIZE);
    const results = [];
    
    for (let i = 0; i < batches; i++) {
        const startIndex = i * BATCH_SIZE;
        const batchSize = Math.min(BATCH_SIZE, TOTAL_MESSAGES - startIndex);
        const entries = Array.from({ length: batchSize }, (_, j) => ({ Id: `msg-${startIndex + j + 1}`, MessageBody: createMessage(startIndex + j), MessageAttributes: { MessageNumber: { DataType: "Number", StringValue: (startIndex + j + 1).toString() } } }));

        try {
            const response = await sqs.send(new SendMessageBatchCommand({ QueueUrl: QUEUE_URL, Entries: entries }));
            console.log(`Batch ${i + 1}/${batches}: ${response.Successful?.length || 0} sent, ${response.Failed?.length || 0} failed`);
            if (response.Failed?.length) response.Failed.forEach(fail => console.error(`Failed message ${fail.Id}: ${fail.Code} - ${fail.Message}`));
            results.push(...entries);
        } catch (error) {
            console.error(`Batch ${i + 1} error:`, error.message);
        }
    }
    return results;
}

async function getDLQMessages() {
    console.log('\nRetrieving DLQ messages...');
    const messages = [];
    let emptyCount = 0;
    
    while (emptyCount < 3) {
        try {
            const response = await sqs.send(new ReceiveMessageCommand({ QueueUrl: DLQ_URL, MaxNumberOfMessages: 10, WaitTimeSeconds: 5, AttributeNames: ['All'], MessageAttributeNames: ['All'] }));
            
            if (!response.Messages?.length) {
                emptyCount++;
                console.log(`No messages (${emptyCount}/3)`);
                continue;
            }
            
            emptyCount = 0;
            messages.push(...response.Messages);
            console.log(`Retrieved ${response.Messages.length} messages (Total: ${messages.length})`);
            
            response.Messages.forEach(msg => displayDLQMessage(msg));
        } catch (error) {
            console.error('DLQ retrieval error:', error.message);
            break;
        }
    }
    return messages;
}

function displayDLQMessage(msg) {
    const receiveCount = parseInt(msg.Attributes?.ApproximateReceiveCount || '0');
    const messageNumber = msg.MessageAttributes?.MessageNumber?.StringValue;
    const messageType = msg.Body.includes('invalid message') ? 'INVALID' : 'VALID';
    
    console.log(`\nDLQ Message: ID=${msg.MessageId}, #=${messageNumber || 'N/A'}, Count=${receiveCount}, Type=${messageType}`);
    console.log(`Body: ${msg.Body.substring(0, 100)}${msg.Body.length > 100 ? '...' : ''}`);
}

async function runTest() {
    if (!QUEUE_URL || !DLQ_URL) {
        console.error('Error: QUEUE_URL and DLQ_URL environment variables required');
        process.exit(1);
    }

    console.log('Starting SQS DLQ test...\n');
    console.log('Test running on following resources :')
    console.log('SourceQueue URL:', QUEUE_URL);
    console.log('DLQ URL :', DLQ_URL);
    console.log('Region :', process.env.AWS_REGION);
    const sentMessages = await sendMessages();
    console.log(`\nSent ${sentMessages.length} messages. Waiting for DLQ processing...`);
    await new Promise(resolve => setTimeout(resolve, 150000));
    const dlqMessages = await getDLQMessages();

    console.log('\n=== Test Summary ===');
    console.log(`Messages sent: ${sentMessages.length}`);
    console.log(`DLQ messages processed: ${dlqMessages.length}`);
    console.log(`Success rate: ${((sentMessages.length - dlqMessages.length) / sentMessages.length * 100).toFixed(1)}%`);
}

runTest().catch(error => {
    console.error('Test failed:', error.message);
    process.exit(1);
});