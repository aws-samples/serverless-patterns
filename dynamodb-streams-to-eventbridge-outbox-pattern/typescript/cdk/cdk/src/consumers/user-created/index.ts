import { EventBridgeEvent } from 'aws-lambda';

// function to take events and throw them onto EventBridge
export async function handler(event: EventBridgeEvent<'UserCreated', any>) {
  console.log('UserCreated Event', JSON.stringify(event, null, 4));
}
