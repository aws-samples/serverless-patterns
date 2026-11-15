
const { SQSClient, SendMessageCommand } = require('@aws-sdk/client-sqs');
const queueUrl = process.env.QUEUE_URL;

exports.handler = async (event) => {

    const client = new SQSClient();
    
    const messageWithManyDetails = {
        "id": "1234567890",
        "source": "systemA",
        "customer": {
            "first_name": "John",
            "middle_names": "Michael Frankie",
            "last_name": "Doe",
        },
        "data": {
            "someDummyData1": "someDummyData1",
            "someDummyData2": "someDummyData2",
            "someDummyData3": "someDummyData3"
        }
    };

    const messageParams = {
        QueueUrl: queueUrl,
        MessageBody: JSON.stringify(messageWithManyDetails)
    };
    
    const command = new SendMessageCommand(messageParams);
    const response = await client.send(command);
    
    return response;
}
