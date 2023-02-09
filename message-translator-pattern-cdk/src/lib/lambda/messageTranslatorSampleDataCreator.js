const { SQSClient, SendMessageCommand } = require('@aws-sdk/client-sqs');
const queueUrl = process.env.QUEUE_URL;

exports.handler = async (event) => {

    const client = new SQSClient();
    
    const messageWithManyDetails = {
        "address": "1600 Pennsylvania Avenue NW, Washington, DC 20500, United States",
    };

    const messageParams = {
        QueueUrl: queueUrl,
        MessageBody: JSON.stringify(messageWithManyDetails)
    };
    
    const command = new SendMessageCommand(messageParams);
    const response = await client.send(command);
    
    return response;
}