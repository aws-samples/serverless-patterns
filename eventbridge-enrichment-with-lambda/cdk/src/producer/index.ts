import { PutEventsCommand, EventBridgeClient } from '@aws-sdk/client-eventbridge';
const client = new EventBridgeClient({});

export async function handler(event: any) {

  await client.send(
    new PutEventsCommand({
      Entries: [
        {
          EventBusName: process.env.EVENT_BUS_NAME,
          DetailType: 'OrderCreated',
          Detail: JSON.stringify({
            metadata: {
              enrich: true
            },
            data: {
              user: {
                id: 'd9df3e81-eafd-4872-b960-adc84d49812e',
              },
            },
          }),
          Source: 'myapp.orders',
        },
      ],
    })
  );
}
