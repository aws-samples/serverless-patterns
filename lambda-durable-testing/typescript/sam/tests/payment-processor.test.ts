import { LocalDurableTestRunner } from '@aws/durable-execution-sdk-js-testing';
import { handler } from '../src/payment-processor/index';

// Store original fetch
const originalFetch = global.fetch;

describe('Payment Processor', () => {
  beforeAll(async () => {
    await LocalDurableTestRunner.setupTestEnvironment({ skipTime: true });
  });

  afterAll(async () => {
    await LocalDurableTestRunner.teardownTestEnvironment();
  });

  beforeEach(() => {
    // Mock fetch for the payment API only
    global.fetch = jest.fn((url: string | URL | Request, ...args) => {
      const urlString = url.toString();
      // Let checkpoint server calls through
      if (urlString.includes('127.0.0.1') || urlString.includes('localhost')) {
        return originalFetch(url as any, ...args);
      }
      // Mock external API calls
      return Promise.reject(new Error('Unmocked fetch call'));
    }) as any;
  });

  afterEach(() => {
    global.fetch = originalFetch;
  });

  it('should succeed on first attempt', async () => {
    (global.fetch as jest.Mock).mockImplementation((url: string | URL | Request, ...args) => {
      const urlString = url.toString();
      if (urlString.includes('127.0.0.1') || urlString.includes('localhost')) {
        return originalFetch(url as any, ...args);
      }
      if (urlString.includes('api.payments.com')) {
        return Promise.resolve({
          ok: true,
          json: async () => ({ transactionId: 'txn-123', status: 'success' })
        });
      }
      return Promise.reject(new Error('Unmocked fetch'));
    });

    const runner = new LocalDurableTestRunner({
      handlerFunction: handler,
    });

    const execution = await runner.run({ payload: { amount: 100 } });

    expect(execution.getStatus()).toBe('SUCCEEDED');
    expect(execution.getResult()).toEqual({
      transactionId: 'txn-123',
      status: 'success'
    });
  });

  it('should retry on failure and eventually succeed', async () => {
    let callCount = 0;
    (global.fetch as jest.Mock).mockImplementation((url: string | URL | Request, ...args) => {
      const urlString = url.toString();
      if (urlString.includes('127.0.0.1') || urlString.includes('localhost')) {
        return originalFetch(url as any, ...args);
      }
      if (urlString.includes('api.payments.com')) {
        callCount++;
        if (callCount === 1) {
          return Promise.reject(new Error('Network error'));
        }
        return Promise.resolve({
          ok: true,
          json: async () => ({ transactionId: 'txn-456', status: 'success' })
        });
      }
      return Promise.reject(new Error('Unmocked fetch'));
    });

    const runner = new LocalDurableTestRunner({
      handlerFunction: handler,
    });

    const execution = await runner.run({ payload: { amount: 100 } });

    expect(execution.getStatus()).toBe('SUCCEEDED');
    expect(execution.getResult()).toEqual({
      transactionId: 'txn-456',
      status: 'success'
    });
  });

  it('should fail after exhausting retries', async () => {
    (global.fetch as jest.Mock).mockImplementation((url: string | URL | Request, ...args) => {
      const urlString = url.toString();
      if (urlString.includes('127.0.0.1') || urlString.includes('localhost')) {
        return originalFetch(url as any, ...args);
      }
      if (urlString.includes('api.payments.com')) {
        return Promise.reject(new Error('Persistent failure'));
      }
      return Promise.reject(new Error('Unmocked fetch'));
    });

    const runner = new LocalDurableTestRunner({
      handlerFunction: handler,
    });

    const execution = await runner.run({ payload: { amount: 100 } });

    expect(execution.getStatus()).toBe('FAILED');
    const error = execution.getError();
    expect(error?.errorMessage).toBe('Persistent failure');
    expect(error?.errorType).toBe('StepError');
  });
});
