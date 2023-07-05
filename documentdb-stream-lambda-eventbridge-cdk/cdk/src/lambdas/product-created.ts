import { EventBridgeEvent } from 'aws-lambda';

const productCreated = async (event: EventBridgeEvent<string, string>): Promise<void> => {
  console.log('Product Created with Event: ', event);
};

export const main = productCreated;
