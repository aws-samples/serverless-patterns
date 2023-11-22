import { Handler } from 'aws-lambda';

export const handler: Handler = async (event, context) => {
    console.log('Event from Scheduler: \n' + JSON.stringify(event, null, 2));
};