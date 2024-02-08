'use strict';
import { Handler, LambdaFunctionURLEvent, LambdaFunctionURLResult} from 'aws-lambda';

const SLEEP_SEC = parseInt(process.env['SLEEP_SEC'] || '0');
const VERSION = process.env['VERSION'];

export const handler: Handler = async (event:LambdaFunctionURLEvent, context: any):Promise<LambdaFunctionURLResult> => {
    
    await sleep(SLEEP_SEC*1000);
    console.log('version_'+VERSION);

    const response:LambdaFunctionURLResult = {
        'statusCode': 200,
        'body': JSON.stringify({'event': event, 'version': VERSION})
    }
    return response
};

function sleep(milliseconds:number) {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
}