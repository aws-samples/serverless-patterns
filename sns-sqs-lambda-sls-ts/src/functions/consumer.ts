import {SQSEvent, SQSHandler, Context} from "aws-lambda";

export const handler: SQSHandler = async (event: SQSEvent, context: Context): Promise<void> => {
    console.log({event, context})
}