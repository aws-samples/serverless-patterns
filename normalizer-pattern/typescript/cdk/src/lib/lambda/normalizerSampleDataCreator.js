
const { SQSClient, SendMessageCommand } = require('@aws-sdk/client-sqs');
const queueUrl = process.env.QUEUE_URL;



exports.handler = async (event) => {

    const message1 = {
        "source": "systemA",
        "customer": {
            "first_name": "John",
            "middle_names": "Michael Frankie",
            "last_name": "Doe",
        },
        "data": {
            "someDummyData": "someDummyData1"
        }
    };
    const message2 = {
        "source": "systemB",
        "first_name": "John",
        "name": "Doe",
        "data": {
            "someDummyData": "someDummyData2"
        }
    };
    const message3 = {
        "source": "systemC",
        "sender": "John Doe",
        "data": {
            "someDummyData": "someDummyData3"
        }
    };

    const message1Params = {
        QueueUrl: queueUrl,
        MessageBody: JSON.stringify(message1)
    };
    const message2Params = {
        QueueUrl: queueUrl,
        MessageBody: JSON.stringify(message2)
    };
    const message3Params = {
        QueueUrl: queueUrl,
        MessageBody: JSON.stringify(message3)
    };


    const client = new SQSClient();

    await client.send(new SendMessageCommand(message1Params));
    await client.send(new SendMessageCommand(message2Params));
    await client.send(new SendMessageCommand(message3Params));

    return {
        statusCode: 200,
        body: JSON.stringify('Success'),
    };
}
