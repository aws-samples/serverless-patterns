import { EventBridgeEvent } from 'aws-lambda';

interface UserCreated24HoursAgo {
  id: string;
  firstName: string;
  lastName: string;
}

/**
 * Example of a consumer for the UserCreated24HoursAgo event, if you wanted to email them you could put your email code here
 */
export async function handler(event: EventBridgeEvent<'UserCreated24HoursAgo', UserCreated24HoursAgo>) {
  console.log('Email the customer 24 hours ago after they were created.')
}
