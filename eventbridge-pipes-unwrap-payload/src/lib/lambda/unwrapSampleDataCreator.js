const snsTopicArn = process.env.SNS_TOPIC_ARN;
const { SNSClient, PublishCommand } = require("@aws-sdk/client-sns");

const snsClient = new SNSClient();

function createSnsMessage(payload) {
    return {
        TopicArn: snsTopicArn,
        Message: JSON.stringify(payload)
        //Message: payload
    };
}

function withPayload(number) {
    return {
        "messageID": "message" + number,
        "source": "unwrapSampleDataCreator",
        "payload": {
            "source": "someSubSystem",
            "data": {
                "someDummyData": "someDummyData2"
            }
        }
    };
}

exports.handler = async (event) => {

    for (let i = 0; i < 3; i++) {
        await snsClient.send(new PublishCommand(createSnsMessage(withPayload(i))));
    }

    return {
        statusCode: 200,
        body: JSON.stringify('Success'),
    };
}