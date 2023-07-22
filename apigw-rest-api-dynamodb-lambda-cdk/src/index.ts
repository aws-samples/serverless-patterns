import { Handler } from "aws-cdk-lib/aws-lambda";
import { DynamoEventSource } from "aws-cdk-lib/aws-lambda-event-sources";

export const handler = async (event: DynamoEventSource) => {
    console.log('EVENT Content: \n' + JSON.stringify(event, null, 2));
};