/**
 * Input for the video generation workflow
 */
export interface VideoGenerationInput {
    prompt: string;
    durationSeconds?: number;
    seed?: number;
}

/**
 * State tracked across polling iterations
 */
export interface AsyncInvokeState {
    invocationArn: string;
    status: 'InProgress' | 'Completed' | 'Failed';
    checkCount: number;
    failureMessage?: string;
}

/**
 * Final result returned by the handler
 */
export interface VideoGenerationResult {
    invocationArn: string;
    status: string;
    outputS3Uri: string;
    totalChecks: number;
    prompt: string;
    completedAt: string;
}