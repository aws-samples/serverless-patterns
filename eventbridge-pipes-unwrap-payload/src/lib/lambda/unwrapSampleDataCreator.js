const { SQSClient, SendMessageCommand } = require('@aws-sdk/client-sqs');

const sqsClient = new SQSClient();

const lamdaEnrichmentSourceQueue = process.env.LAMBDA_ENRICHMENT_SOURCE_QUEUE_URL;
const stepFunctionsEnrichmentSourceQueue = process.env.STEP_FUNCTIONS_ENRICHMENT_SOURCE_QUEUE_URL;

const nestedPayload = {
    "source": "someSubSystem",
    "data": {
        "someDummyData": "someDummyData2"
    }
};
const stringifiedContent = {
    "first_name": "John",
    "name": "Doe",
    "alreadyStringifiedContent": JSON.stringify(nestedPayload)
};

function createSqsMessage(queue, payload) {
    return {
        QueueUrl: queue,
        MessageBody: JSON.stringify(payload)
    };
}

function withPayload(number) {
    return {
        "messageID": "message" + number,
        "source": "unwrapSampleDataCreator",
        "payload": JSON.stringify(stringifiedContent)
    };
}

exports.handler = async (event) => {
    console.log("Queue URL: " + lamdaEnrichmentSourceQueue);
    console.log("Queue URL: " + stepFunctionsEnrichmentSourceQueue);

    for (let i = 0; i < 3; i++) {
        await sqsClient.send(new SendMessageCommand(createSqsMessage(lamdaEnrichmentSourceQueue, withPayload(i))));
        await sqsClient.send(new SendMessageCommand(createSqsMessage(stepFunctionsEnrichmentSourceQueue, withPayload(i))));
    }

    return {
        statusCode: 200,
        body: JSON.stringify('Success'),
    };
}
