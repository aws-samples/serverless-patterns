import { DurableContext, withDurableExecution, createRetryStrategy } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    const payment = await context.step('process-payment', async () => {
      const response = await fetch('https://api.payments.com/charge', {
        method: 'POST',
        body: JSON.stringify({ amount: event.amount })
      });
      if (!response.ok) throw new Error('Payment failed');
      return response.json();
    }, {
      retryStrategy: createRetryStrategy({
        maxAttempts: 3,
        backoffRate: 2,
        initialInterval: 1000
      })
    });

    return payment;
  }
);
