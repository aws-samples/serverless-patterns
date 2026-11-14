import { Handler } from 'aws-lambda';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

interface Event {
  name: string;
}

interface Response {
  response: string;
}

export const handler: Handler<Event, Response> = async (event) => {
  logger.logEventIfEnabled(event)

  const name = event.name || 'World';
  
  const response = {
    response: `Hello ${name}`
  };

  return response;
};