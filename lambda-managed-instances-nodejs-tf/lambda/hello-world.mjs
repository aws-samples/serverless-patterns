import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

export const handler = async (event) => {
    logger.logEventIfEnabled(event);

    const name = event.name || 'World';
    
    const response = {
        response: `Hello ${name}`
    };

    return response;
};