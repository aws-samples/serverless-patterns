import { LocalDurableTestRunner, OperationType, OperationStatus } from '@aws/durable-execution-sdk-js-testing';
import { handler } from './video-generator';

// Mock the Bedrock Runtime client
jest.mock('@aws-sdk/client-bedrock-runtime', () => {
    const MOCK_INVOCATION_ARN =
        'arn:aws:bedrock:us-east-1:123456789012:async-invoke/abc123def456';

    let callCount = 0;

    return {
        BedrockRuntimeClient: jest.fn().mockImplementation(() => ({
            send: jest.fn().mockImplementation((command: any) => {
                if (command.constructor.name === 'StartAsyncInvokeCommand') {
                    return Promise.resolve({
                        invocationArn: MOCK_INVOCATION_ARN,
                    });
                }
                if (command.constructor.name === 'GetAsyncInvokeCommand') {
                    callCount++;
                    // Simulate: first two checks return InProgress, third returns Completed
                    if (callCount >= 3) {
                        return Promise.resolve({
                            invocationArn: MOCK_INVOCATION_ARN,
                            status: 'Completed',
                            outputDataConfig: {
                                s3OutputDataConfig: {
                                    s3Uri: 's3://test-bucket/videos/output/',
                                },
                            },
                        });
                    }
                    return Promise.resolve({
                        invocationArn: MOCK_INVOCATION_ARN,
                        status: 'InProgress',
                    });
                }
                return Promise.reject(new Error('Unknown command'));
            }),
        })),
        StartAsyncInvokeCommand: jest.fn().mockImplementation((input: any) => ({
            constructor: { name: 'StartAsyncInvokeCommand' },
            input,
        })),
        GetAsyncInvokeCommand: jest.fn().mockImplementation((input: any) => ({
            constructor: { name: 'GetAsyncInvokeCommand' },
            input,
        })),
    };
});

describe('Video Generator - Bedrock Async Invoke', () => {
    beforeAll(() => LocalDurableTestRunner.setupTestEnvironment({ skipTime: true }));
    afterAll(() => LocalDurableTestRunner.teardownTestEnvironment());

    it('should start async invocation and poll until completion', async () => {
        const runner = new LocalDurableTestRunner({
            handlerFunction: handler,
        });

        const execution = await runner.run({
            payload: {
                prompt: 'A golden retriever playing fetch on a sunny beach',
                durationSeconds: 6,
            },
        });

        const result = execution.getResult() as any;

        // Verify the workflow completed successfully
        expect(result).toBeDefined();
        expect(result.status).toBe('Completed');
        expect(result.prompt).toBe('A golden retriever playing fetch on a sunny beach');
        expect(result.invocationArn).toContain('async-invoke');
        expect(result.totalChecks).toBeGreaterThanOrEqual(1);
        expect(result.completedAt).toBeDefined();

        // Verify the idempotency token step ran
        const tokenStep = runner.getOperation('generate-idempotency-token');
        expect(tokenStep).toBeDefined();
        expect(tokenStep.getType()).toBe(OperationType.STEP);
        expect(tokenStep.getStatus()).toBe(OperationStatus.SUCCEEDED);

        // Verify the start-video-generation step ran
        const startStep = runner.getOperation('start-video-generation');
        expect(startStep).toBeDefined();
        expect(startStep.getType()).toBe(OperationType.STEP);
        expect(startStep.getStatus()).toBe(OperationStatus.SUCCEEDED);

        // Verify the waitForCondition polling ran
        const waitOp = runner.getOperation('wait-for-video-ready');
        expect(waitOp).toBeDefined();

        // Verify the build-result step ran
        const resultStep = runner.getOperation('build-result');
        expect(resultStep).toBeDefined();
        expect(resultStep.getType()).toBe(OperationType.STEP);
        expect(resultStep.getStatus()).toBe(OperationStatus.SUCCEEDED);
    });
});