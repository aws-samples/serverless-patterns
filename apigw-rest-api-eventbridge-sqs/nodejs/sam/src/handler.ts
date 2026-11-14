import { SQSEvent, SQSRecord } from "aws-lambda/trigger/sqs";

export const handler: any = async (event: SQSEvent): Promise<any> => {
  await Promise.all(event.Records.map(async (record: SQSRecord) => {
    try {
      let payload = JSON.parse(record.body);
      console.log(payload.detail);
    } catch (error) {
      console.log(error);
    }
  }));
};