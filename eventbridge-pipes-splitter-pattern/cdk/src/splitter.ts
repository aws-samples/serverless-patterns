import { unmarshall } from '@aws-sdk/util-dynamodb';
import {DynamoDBRecord} from 'aws-lambda';

interface Ticket {
  id: string
}

export async function handler(records: DynamoDBRecord[]) {

  const newOrderRaw = records[0]?.dynamodb?.NewImage || {};
  const newOrder = unmarshall(newOrderRaw);

  const { id:orderId, userId, tickets = [] } = newOrder;

  if(!tickets){
    // return empty array for Pipes so it can continue the enrichment and not trigger downstream consumer
    return [];
  }

  // Each event will be the `detail` of the EventBridge event.
  const events = tickets.map((ticket: Ticket) => {
    return {
      id: ticket?.id,
      orderId,
      userId
    }
  });

  return events;
}


