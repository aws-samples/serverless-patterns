/**
 * AWS Lambda durable function - Calls REST API using AWS durable execution SDK
 */
import {
  withDurableExecution,
  createRetryStrategy,
} from '@aws/durable-execution-sdk-js';

const DEFAULT_API_URL = process.env.API_URL || 'https://jsonplaceholder.typicode.com/posts/1';
const MAX_RESPONSE_SIZE = 1_000_000; // 1 MB limit

// Retry strategy: 3 attempts, exponential backoff starting at 2s, max 30s, with jitter
const stepConfig = {
  retryStrategy: createRetryStrategy({
    maxAttempts: 3,
    initialDelay: { seconds: 2 },
    maxDelay: { seconds: 30 },
    backoffRate: 2.0,
  }),
};

export const handler = withDurableExecution(async (event, context) => {
  context.logger.info('Starting durable REST API call');

  // Get API URL from event or use default
  const apiUrl = event.url || DEFAULT_API_URL;

  context.logger.info(`Using API URL: ${apiUrl}`);

  // Execute the REST API call as a durable step
  // Transient failures (timeouts, connection errors) propagate as exceptions,
  // allowing the durable execution SDK to automatically retry the step.
  let result;
  try {
    result = await context.step('Call REST API', async (stepCtx) => {
      stepCtx.logger.info(`Calling REST API: ${apiUrl}`);

      const response = await fetch(apiUrl, {
        method: 'GET',
        signal: AbortSignal.timeout(30000) // 30 second timeout
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Validate response size before reading body
      const contentLength = response.headers.get('Content-Length');
      if (contentLength && parseInt(contentLength) > MAX_RESPONSE_SIZE) {
        stepCtx.logger.error(`Response too large: ${contentLength} bytes`);
        return {
          status: 'error',
          error: `Response size ${contentLength} bytes exceeds limit of ${MAX_RESPONSE_SIZE} bytes`
        };
      }

      const text = await response.text();
      if (text.length > MAX_RESPONSE_SIZE) {
        stepCtx.logger.error('Response body exceeded size limit');
        return {
          status: 'error',
          error: `Response body exceeds limit of ${MAX_RESPONSE_SIZE} bytes`
        };
      }

      const data = JSON.parse(text);

      stepCtx.logger.info(`API call successful: ${response.status}`);
      return {
        status: 'success',
        statusCode: response.status,
        data: data
      };
    }, stepConfig);
  } catch (error) {
    context.logger.error(`Step failed after retries: ${error.message}`);
    return {
      statusCode: 502,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: 'API call failed after retries',
        url: apiUrl,
        details: error.message
      })
    };
  }

  // Pause for 2 seconds without consuming CPU cycles or incurring usage charges
  await context.wait({ seconds: 2 });

  // Context logger is replay aware and will not log the same message multiple times
  context.logger.info('Waited for 2 seconds without consuming CPU.');

  // Return response based on result
  if (result.status === 'success') {
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: 'API call successful',
        url: apiUrl,
        data: result.data
      })
    };
  } else {
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: 'API call failed',
        url: apiUrl,
        details: result.error
      })
    };
  }
});
