/**
 * Lambda Durable Function - Calls REST API using AWS Durable Execution SDK
 * Note: Node.js 22.x has built-in durable execution support
 */

/**
 * Lambda Durable Function - Calls REST API using AWS Durable Execution SDK
 */
import { withDurableExecution } from '@aws/durable-execution-sdk-js';

const DEFAULT_API_URL = process.env.API_URL || 'https://jsonplaceholder.typicode.com/posts/1';

export const handler = withDurableExecution(async (event, context) => {
  context.logger.info('Starting durable REST API call');
  
  // Get API URL from event or use default
  const apiUrl = event.url || DEFAULT_API_URL;
  
  context.logger.info(`Using API URL: ${apiUrl}`);
  
  // Execute the REST API call as a durable step
  const result = await context.step('Call REST API', async (stepCtx) => {
    stepCtx.logger.info(`Calling REST API: ${apiUrl}`);
    
    try {
      const response = await fetch(apiUrl, {
        method: 'GET',
        signal: AbortSignal.timeout(30000) // 30 second timeout
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      
      stepCtx.logger.info(`API call successful: ${response.status}`);
      
      return {
        status: 'success',
        statusCode: response.status,
        data: data
      };
      
    } catch (error) {
      stepCtx.logger.error(`API call failed: ${error.message}`);
      return {
        status: 'error',
        error: error.message
      };
    }
  });
  
  // Pause for 2 seconds without consuming CPU cycles or incurring usage charges
  await context.wait({ seconds: 2 });
  
  // Context logger is replay aware and will not log the same message multiple times
  context.logger.info('Waited for 2 seconds without consuming CPU.');
  
  // Return response based on result
  if (result.status === 'success') {
    const response = {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: 'API call successful',
        url: apiUrl,
        data: result.data
      })
    };
    return response;
  } else {
    const response = {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: 'API call failed',
        url: apiUrl,
        details: result.error
      })
    };
    return response;
  }
});
