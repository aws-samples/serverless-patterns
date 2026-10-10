/**
 * Retry strategy for Bedrock API calls.
 * Skips retries on validation errors (wrong model ID, bad input, etc.)
 * and uses exponential backoff for transient failures.
 */
export function bedrockRetryStrategy(error: any, attemptCount: number) {
    if (error?.name === 'ValidationException' || error?.message?.includes('ValidationException')) {
        return { shouldRetry: false };
    }
    if (attemptCount >= 3) {
        return { shouldRetry: false };
    }
    return {
        shouldRetry: true,
        delay: { seconds: Math.pow(2, attemptCount) },
    };
}

/**
 * Default retry strategy with exponential backoff, max 3 attempts.
 */
export function defaultRetryStrategy(_error: any, attemptCount: number) {
    if (attemptCount >= 3) {
        return { shouldRetry: false };
    }
    return {
        shouldRetry: true,
        delay: { seconds: Math.pow(2, attemptCount) },
    };
}