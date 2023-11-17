import { SNSClient, ListTopicsCommand } from '@aws-sdk/client-sns';
import * as os from 'os';

export async function handler(event, context) {

    const topic_arn = process.env.TOPIC_ARN;

    const sns_client = new SNSClient();

    try {

        const params = {
            TargetArn: topic_arn,
            Message: event.key1,
        };
        const command = new ListTopicsCommand(params);
        const sent_message = await sns_client.send(command);

        if (sent_message !== null) {
            console.log(`Success - Request ID: ${sent_message.$metadata.requestId}`);
        }

        return {
            statusCode: 200,
            body: "Success",
        };

    }
    catch (e) {
        {
            console.log(e);
        }

        return null;
    }
}
