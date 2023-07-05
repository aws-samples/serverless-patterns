import { PutEventsCommand } from '@aws-sdk/client-eventbridge';
import { eventBridgeClient } from '../clients/eventbridge';
import { DocumentDBStreamEvent } from '../types/documentdb-stream-event';

const productsCdc = async (event: DocumentDBStreamEvent): Promise<void> => {
  console.log(JSON.stringify(event, null, 2));
  try {
    const { events } = event;
    const eventBridgeEvents = events.map((event) => ({
      EventBusName: process.env.DEFAULT_EVENT_BUS! || 'default',
      Detail: JSON.stringify({
        documentKey: event.event.documentKey,
        fullDocument: event.event.fullDocument || {},
        updateDescription: event.event.updateDescription || {},
      }),
      DetailType: getEventType(event.event.operationType),
      Source: 'products.cdc',
    }));
    const response = await eventBridgeClient.send(
      new PutEventsCommand({
        Entries: eventBridgeEvents,
      })
    );
    console.log('EventBridge Response', response);
  } catch (error) {
    console.error('Error in products CDC:', error);
    throw error;
  }
};

function getEventType(operationType: string) {
  switch (operationType) {
    case 'insert':
      return 'productCreated';
    case 'update':
      return 'productUpdated';
    case 'delete':
      return 'productDeleted';
    default:
      return 'UnknownEvent';
  }
}

export const main = productsCdc;
