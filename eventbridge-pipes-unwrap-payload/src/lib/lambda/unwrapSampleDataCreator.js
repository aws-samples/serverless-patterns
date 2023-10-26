const { SQSClient, SendMessageCommand } = require('@aws-sdk/client-sqs');

const sqsClient = new SQSClient();

const lamdaEnrichmentSourceQueue = process.env.LAMBDA_ENRICHMENT_SOURCE_QUEUE_URL;
const stepFunctionsEnrichmentSourceQueue = process.env.STEP_FUNCTIONS_ENRICHMENT_SOURCE_QUEUE_URL;

// This sample message contains nested attributes that are already stringified.
// Our goal is to unwrap this nested structure using EventBridge Pipes.
function createSqsMessage(queue, number) {
    return {
        QueueUrl: queue,
        MessageBody: JSON.stringify({
            "messageID": "message" + number,
            "source": "unwrapSampleDataCreator",
            // the contents of this attribute is stored as string
            "payload": JSON.stringify({
                    "first_name": "John",
                    "name": "Doe",
                    // the contents of this attribute is stored as string
                    "alreadyStringifiedContent": JSON.stringify({
                            "source": "someSubSystem",
                            "data": {
                                "someDummyData": "someDummyData2"
                            }
                        })
                })
        })
    };
}

exports.handler = async (event) => {
    console.log("Queue URL: " + lamdaEnrichmentSourceQueue);

    for (let i = 0; i < 3; i++) {
        await sqsClient.send(new SendMessageCommand(createSqsMessage(lamdaEnrichmentSourceQueue, i)));
        await sqsClient.send(new SendMessageCommand(createSqsMessage(stepFunctionsEnrichmentSourceQueue, i)));
    }

    return {
        statusCode: 200,
        body: JSON.stringify('Success'),
    };
}
