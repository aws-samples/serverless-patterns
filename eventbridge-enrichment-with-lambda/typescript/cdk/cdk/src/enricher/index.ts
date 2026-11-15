import { PutEventsCommand, EventBridgeClient } from '@aws-sdk/client-eventbridge';
const client = new EventBridgeClient({});

// Enrich data from anyway, DynamoDB, API Call.... this mock returns some dummy information
const getUser = async (userId: string) => {
  return Promise.resolve({
    id: userId,
    name: 'David',
    lastName: 'Boyne',
  });
};

// enrich the event by the name (of course replace this with your code to get information or do whatever you want....)
const enrich = async (event: any) => {
  const eventName = event['detail-type'];

  switch (eventName) {
    case 'OrderCreated':
      const user = await getUser(event?.detail?.data?.userId);
      return {
        ...event.detail,
        data: {
          ...event.detail.data,
          user,
        },
      };
    default:
      return event.detail;
  }
};

export async function handler(event: any) {
  console.log('Enrich event based on the name...', JSON.stringify(event, null, 4));

  // Take off the enrichment flag first, downstream consumers dont need this.
  delete event?.detail?.metadata?.enrich;

  const enrichedEventDetail = await enrich(event);

  await client.send(
    new PutEventsCommand({
      Entries: [
        {
          EventBusName: process.env.EVENT_BUS_NAME,
          DetailType: event['detail-type'],
          Source: event['source'],
          Detail: JSON.stringify(enrichedEventDetail),
        },
      ],
    })
  );
}
