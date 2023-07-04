import { EventBridgeEvent } from 'aws-lambda';

const userCreated = async (event: EventBridgeEvent<string, string>): Promise<void> => {};

export const main = userCreated;
