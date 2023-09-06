import { Handler } from 'aws-cdk-lib/aws-lambda';
import * as http from 'http';

async function httpGet(url: string): Promise<string> {
  try {
    const response = await new Promise<http.IncomingMessage>((resolve, reject) => {
      const request = http.request(url, resolve);
      request.on('error', reject);
      request.end();
    });

    if (response.statusCode !== 200) {
      throw new Error(`Request failed with status code ${response.statusCode}`);
    }

    let data = '';

    response.on('data', (chunk: string) => {
      data += chunk;
    });

    return new Promise<string>((resolve) => {
      response.on('end', () => {
        // 'data' now contains the response body
        resolve(data);
      });
    });
  } catch (error: any) {
    console.error(`Error: ${error.message}`);
    throw error;
  }
}

export const handler: Handler = async () => {
  console.log('fetching random VIN...');
  const url = 'https://randomvin.com/getvin.php?type=real';
  // Call the async function
  try {
    const response = await httpGet(url);
    console.log(`your random VIN is: ${response}`);
  } catch (error: any) {
    console.error(`Error Fetching VIN: ${error.message}`);
    throw error;
  }
};
