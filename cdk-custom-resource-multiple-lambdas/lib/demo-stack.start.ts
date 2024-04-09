import { SQSClient, SendMessageCommand } from "@aws-sdk/client-sqs";
import { CloudFormationCustomResourceHandler } from "aws-lambda";

const client = new SQSClient();

export const handler: CloudFormationCustomResourceHandler = async (event, context) => {
    // Logging both parameters for debugging purposes.
    console.log('Custom Resource Start');
    console.log(event);
    console.log(context);

    //
    // Optionally: add additional business logic here
    //

    // Send a message to the custom resource finalizer lambda
    await client.send(new SendMessageCommand({
        QueueUrl: event.ResourceProperties.CustomResourceQueueUrl!,
        MessageBody: JSON.stringify(event),
    }));
}