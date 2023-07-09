
import { DynamoDBStreamEvent, DynamoDBRecord } from "aws-lambda";
import { unmarshall } from "@aws-sdk/util-dynamodb";
import { EventBridgeClient, PutEventsCommand, PutEventsRequestEntry, PutEventsRequest } from '@aws-sdk/client-eventbridge';

const eventBridgeClient = new EventBridgeClient({});

export const handler = async (event: DynamoDBStreamEvent): Promise<void> => {
  let messages = [];
  await Promise.all(event.Records.map(async (record: DynamoDBRecord) => {
    let payload = unmarshall(record.dynamodb.NewImage);
    messages.push(payload);
  }));

  await eventBridge(messages);
};

async function eventBridge(messages: any[]) {
  const chunkedArray: any[][] = chunkArray(messages, 10);

  const batchPromises = [];
  for (const items of chunkedArray) {
    const entries: PutEventsRequestEntry[] = [];
    for (const item of items) {
      entries.push({
        Detail: JSON.stringify(item),
        DetailType: 'INSERTED',
        EventBusName: process.env.BUS_NAME,
        Source: 'demo.event',
      });
    }

    batchPromises.push(eventBridgeClient.send(new PutEventsCommand({
      Entries: entries
    })));
  }

  const response = await Promise.allSettled(batchPromises);
  response.forEach(promise => {
    if (promise.status === "rejected")
      console.log(promise.reason);
    else
      console.log(promise.value);
  });
}

function chunkArray(messages: any[], size: number): any[][] {
  const chunkedArr: any[][] = [];
  let index = 0;
  while (index < messages.length) {
    chunkedArr.push(messages.slice(index, size + index));
    index += size;
  }
  return chunkedArr;
}
