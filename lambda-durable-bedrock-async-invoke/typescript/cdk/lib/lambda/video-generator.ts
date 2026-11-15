import { DurableContext, withDurableExecution } from '@aws/durable-execution-sdk-js';
import {
    BedrockRuntimeClient,
    StartAsyncInvokeCommand,
    GetAsyncInvokeCommand,
} from '@aws-sdk/client-bedrock-runtime';

import { VideoGenerationInput, AsyncInvokeState, VideoGenerationResult } from './types';
import { bedrockRetryStrategy, defaultRetryStrategy } from './retry-strategies';

const BEDROCK_MODEL_ID = process.env.BEDROCK_MODEL_ID ?? 'amazon.nova-reel-v1:1';
const BEDROCK_REGION = process.env.BEDROCK_REGION ?? 'us-east-1';
const OUTPUT_BUCKET = process.env.OUTPUT_BUCKET_NAME ?? '';

// Maximum number of polling iterations before treating the invocation as timed out
const MAX_POLL_CHECKS = 10;

const bedrockClient = new BedrockRuntimeClient({ region: BEDROCK_REGION });

/**
 * Start a Bedrock async invocation for video generation.
 */
async function startVideoGeneration(
    client: BedrockRuntimeClient,
    event: VideoGenerationInput,
    idempotencyToken: string,
    stepCtx: { logger: { info: (msg: string, data?: any) => void } },
): Promise<string> {
    const s3OutputUri = `s3://${OUTPUT_BUCKET}/videos/${idempotencyToken}/`;

    stepCtx.logger.info('Starting Bedrock async invocation', {
        model: BEDROCK_MODEL_ID,
        outputUri: s3OutputUri,
    });

    const response = await client.send(
        new StartAsyncInvokeCommand({
            modelId: BEDROCK_MODEL_ID,
            clientRequestToken: idempotencyToken,
            modelInput: {
                taskType: 'TEXT_VIDEO',
                textToVideoParams: {
                    text: event.prompt,
                },
                videoGenerationConfig: {
                    durationSeconds: event.durationSeconds ?? 6,
                    fps: 24,
                    dimension: '1280x720',
                    seed: event.seed ?? 0,
                },
            },
            outputDataConfig: {
                s3OutputDataConfig: {
                    s3Uri: s3OutputUri,
                },
            },
        }),
    );

    const arn = response.invocationArn!;
    stepCtx.logger.info('Bedrock async invocation started', { invocationArn: arn });
    return arn;
}

/**
 * Check the current status of a Bedrock async invocation.
 */
async function checkInvocationStatus(
    client: BedrockRuntimeClient,
    currentState: AsyncInvokeState,
    ctx: { logger: { info: (msg: string, data?: any) => void } },
): Promise<AsyncInvokeState> {
    ctx.logger.info('Checking Bedrock async invocation status', {
        invocationArn: currentState.invocationArn,
        checkNumber: currentState.checkCount + 1,
    });

    const response = await client.send(
        new GetAsyncInvokeCommand({
            invocationArn: currentState.invocationArn,
        }),
    );

    const status = (response.status as AsyncInvokeState['status']) ?? 'InProgress';

    ctx.logger.info('Bedrock invocation status retrieved', {
        invocationArn: currentState.invocationArn,
        status,
        failureMessage: response.failureMessage,
    });

    return {
        invocationArn: currentState.invocationArn,
        status,
        checkCount: currentState.checkCount + 1,
        failureMessage: response.failureMessage,
    };
}

/**
 * Build the final result from the completed polling state.
 * Throws if the generation failed or timed out.
 */
function buildResult(
    finalState: AsyncInvokeState,
    event: VideoGenerationInput,
    idempotencyToken: string,
    stepCtx: { logger: { info: (msg: string, data?: any) => void; error: (msg: string, data?: any) => void } },
): VideoGenerationResult {
    if (finalState.status === 'Failed') {
        stepCtx.logger.error('Video generation failed', {
            invocationArn: finalState.invocationArn,
            failureMessage: finalState.failureMessage,
        });
        throw new Error(
            `Video generation failed: ${finalState.failureMessage ?? 'Unknown error'}`,
        );
    }

    if (finalState.status !== 'Completed') {
        stepCtx.logger.error('Video generation timed out', {
            invocationArn: finalState.invocationArn,
            checkCount: finalState.checkCount,
        });
        throw new Error(
            `Video generation timed out after ${finalState.checkCount} polling attempts (status: ${finalState.status})`,
        );
    }

    const outputUri = `s3://${OUTPUT_BUCKET}/videos/${idempotencyToken}/`;

    stepCtx.logger.info('Video generation completed', {
        invocationArn: finalState.invocationArn,
        totalChecks: finalState.checkCount,
        outputUri,
    });

    return {
        invocationArn: finalState.invocationArn,
        status: finalState.status,
        outputS3Uri: outputUri,
        totalChecks: finalState.checkCount,
        prompt: event.prompt,
        completedAt: new Date().toISOString(),
    };
}

/**
 * AI Video Generation Pipeline — Demonstrates Bedrock Async Invoke with durable functions
 *
 * This durable function orchestrates Amazon Nova Reel video generation:
 * 1. Generates a deterministic idempotency token (checkpointed for replay safety)
 * 2. Starts a Bedrock async invocation (video output written to S3)
 * 3. Polls GetAsyncInvoke with exponential backoff using waitForCondition
 * 4. Returns the S3 location of the generated video
 *
 * Without durable functions you would need a separate polling mechanism
 * (Step Functions, EventBridge, or a cron-based poller). Here the entire
 * flow is a single, linear function with automatic state persistence and
 * zero compute cost during waits.
 */
export const handler = withDurableExecution(
    async (event: VideoGenerationInput, context: DurableContext): Promise<VideoGenerationResult> => {
        context.logger.info('Starting video generation workflow', {
            prompt: event.prompt,
            durationSeconds: event.durationSeconds ?? 6,
        });

        try {
            // Step 1: Generate idempotency token
            // This is in its own step so the token is checkpointed. If the
            // subsequent Bedrock call fails and retries, the same token is
            // reused and the request stays idempotent.
            const idempotencyToken = await context.step(
                'generate-idempotency-token',
                async (): Promise<string> => {
                    return `video-${Date.now()}-${Math.random().toString(36).substring(2, 10)}`;
                },
            );

            // Step 2: Start the async Bedrock invocation
            const invocationArn = await context.step(
                'start-video-generation',
                async (stepCtx) => startVideoGeneration(bedrockClient, event, idempotencyToken, stepCtx),
                { retryStrategy: bedrockRetryStrategy },
            );

            // Step 3: Poll for completion using waitForCondition with exponential backoff
            // The durable function suspends during each wait interval, incurring zero
            // compute charges while the video is being generated.
            const finalState = await context.waitForCondition(
                'wait-for-video-ready',
                async (currentState: AsyncInvokeState, ctx) =>
                    checkInvocationStatus(bedrockClient, currentState, ctx),
                {
                    initialState: {
                        invocationArn,
                        status: 'InProgress' as const,
                        checkCount: 0,
                    },
                    waitStrategy: (state: AsyncInvokeState, attempt: number) => {
                        if (state.status === 'Completed' || state.status === 'Failed') {
                            return { shouldContinue: false };
                        }

                        // Guard against infinite polling
                        if (state.checkCount >= MAX_POLL_CHECKS) {
                            return { shouldContinue: false };
                        }

                        // Exponential backoff starting at 30s: 30s, 60s, 60s, ... capped at 60s.
                        // Nova Reel generation takes minutes so a higher initial delay avoids
                        // unnecessary API calls.
                        const delaySeconds = Math.min(30 * Math.pow(2, attempt - 1), 60);

                        return {
                            shouldContinue: true,
                            delay: { seconds: delaySeconds },
                        };
                    },
                },
            );

            // Step 4: Build the final result
            const result = await context.step(
                'build-result',
                async (stepCtx) => buildResult(finalState, event, idempotencyToken, stepCtx),
                { retryStrategy: defaultRetryStrategy },
            );

            context.logger.info('Video generation workflow completed', {
                invocationArn: result.invocationArn,
                status: result.status,
            });

            return result;
        } catch (error: any) {
            context.logger.error('Video generation workflow failed', {
                error: error.message,
                prompt: event.prompt,
            });
            throw error;
        }
    },
);
