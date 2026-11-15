import { DynamoDBStreamEvent } from 'aws-lambda';
import { EventBridgeClient, PutEventsCommand } from '@aws-sdk/client-eventbridge';
import { unmarshall } from '@aws-sdk/util-dynamodb';

const client = new EventBridgeClient({});

// function to take events and throw them onto EventBridge
export async function handler(events: DynamoDBStreamEvent) {
  console.log('Events', JSON.stringify(events, null, 4));

  const mappedEvents = events.Records.map((record) => {
    return {
      Detail: JSON.stringify(unmarshall(record.dynamodb?.NewImage as any)),
      DetailType: 'UserCreated',
      Source: 'myapp.users',
      EventBusName: process.env.EVENT_BUS_NAME,
      Resources: [record.eventSourceARN || ''],
    };
  });

  console.log('mappedEvents', JSON.stringify(mappedEvents, null, 4));

  await client.send(
    new PutEventsCommand({
      Entries: mappedEvents
    })
  );
}
