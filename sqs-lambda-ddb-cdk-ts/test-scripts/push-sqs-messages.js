const AWS = require('aws-sdk');
const { v4: uuidv4 } = require('uuid');

AWS.config.update({ region: 'YOUR_REGION' }); // Replace 'YOUR_REGION' with your AWS region (i.e. us-west-2)

const sqs = new AWS.SQS({ apiVersion: '2012-11-05' });

// Replace 'YOUR_SQS_QUEUE_URL' with your SQS queue URL
// You can obtain this from the CloudFormation outputs of the stack
const SQS_QUEUE_URL = 'YOUR_SQS_QUEUE_URL'

const generateRandomData = (size) => {
    // Generate dummy data to fill ~1KB
    const randomData = Array(size).fill('#').join('');
    return randomData;
};

const pushBatchToSQS = async (n) => {
    const batch = [];
    for (let i = 0; i < n; i++) {
        // Generate a unique ID for each message and create a dummy payload with the ID and random data. 
        // The ID is used to track the message in DynamoDB and the dummy data is used to fill the payload. 
        const uuid = uuidv4();
        const body = {
            id: uuid,
            payload: generateRandomData(1000 - uuid.length)
        }

        // Create an SQS message object with the ID and dummy payload.
        batch.push({
            Id: uuid,
            MessageBody: JSON.stringify(body)
        })
    };

    // Create an SQS batch request object with the batch of messages.
    const params = {
        Entries: batch,
        QueueUrl: SQS_QUEUE_URL,
    };

    // Try sending batch to SQS, catch any errors and log them to the console. 
    try {
        await sqs.sendMessageBatch(params).promise();
        console.log(`Batch of ${n} items pushed to SQS at ${new Date().toISOString()}`);
    } catch (error) {
        console.error('Error pushing batch to SQS:', error);
    }
};

const n = process.argv[2]; // Number of items to push, passed as a command-line argument

const t = process.argv[3]; // Time interval between each item batch, in milliseconds, passed as a command-line argument

// Check if n and t are valid numbers, and if so, start the interval loop.
if (!n || isNaN(n)) {
    console.error('Please provide a valid number for the batch size.');
} else if (!t || isNaN(t)) {
    console.error('Please provide a valid number for the time interval (in milliseconds) between batches.');
} else {
    setInterval(() => {
        pushBatchToSQS(parseInt(n, 10));
    }, t);
}