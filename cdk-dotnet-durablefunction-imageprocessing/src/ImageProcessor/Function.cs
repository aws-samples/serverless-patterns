using Amazon.DynamoDBv2;
using Amazon.Lambda.Core;
using Amazon.Lambda.DurableExecution;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;
using Amazon.S3;

[assembly: LambdaSerializer(typeof(DefaultLambdaJsonSerializer))]

namespace ImageProcessor;

/// <summary>
/// Lambda Durable Function that orchestrates an image-processing pipeline.
/// 
/// Workflow:
///   1. Fan out three parallel branches: thumbnail generation, watermark application, metadata extraction.
///   2. Fan in: aggregate all branch results.
///   3. Write the aggregated result to DynamoDB.
///   4. Return the final PipelineResult.
/// </summary>
internal sealed class ImageProcessorHandler
{
    private static readonly IAmazonS3 S3Client = new AmazonS3Client();
    private static readonly IAmazonDynamoDB DynamoDbClient = new AmazonDynamoDBClient();

    private static readonly string TableName =
        Environment.GetEnvironmentVariable("RESULTS_TABLE_NAME")
        ?? throw new InvalidOperationException("RESULTS_TABLE_NAME environment variable is not set.");

    private readonly ImageProcessingService _imageService = new(S3Client);
    private readonly ResultsWriter _resultsWriter = new(DynamoDbClient, TableName);

    public static async Task Main()
    {
        var handler = new ImageProcessorHandler();
        var serializer = new DefaultLambdaJsonSerializer();
        using var wrapper = HandlerWrapper.GetHandlerWrapper<DurableExecutionInvocationInput, DurableExecutionInvocationOutput>(
            handler.Handler, serializer);
        using var bootstrap = new LambdaBootstrap(wrapper);
        await bootstrap.RunAsync();
    }

    public Task<DurableExecutionInvocationOutput> Handler(
        DurableExecutionInvocationInput input, ILambdaContext context)
        => DurableFunction.WrapAsync<ImageInput, PipelineResult>(Workflow, input, context);

    private async Task<PipelineResult> Workflow(ImageInput input, IDurableContext ctx)
    {
        // ──────────────────────────────────────────────────────────────────
        // Fan-Out: Run thumbnail, watermark, and metadata extraction in parallel.
        // Each branch is independently checkpointed and survives Lambda re-invocations.
        // ──────────────────────────────────────────────────────────────────
        var batch = await ctx.ParallelAsync(
            [
                new DurableBranch<ProcessingBranchResult>("thumbnail", async (branchCtx, ct) =>
                {
                    var result = await branchCtx.StepAsync(
                        async (_, t) => await _imageService.GenerateThumbnailAsync(input.Bucket, input.Key, t),
                        name: "generate-thumbnail",
                        config: new StepConfig { RetryStrategy = RetryStrategy.Default },
                        cancellationToken: ct);
                    return new ProcessingBranchResult("thumbnail", Thumbnail: result, null, null);
                }),

                new DurableBranch<ProcessingBranchResult>("watermark", async (branchCtx, ct) =>
                {
                    var result = await branchCtx.StepAsync(
                        async (_, t) => await _imageService.ApplyWatermarkAsync(input.Bucket, input.Key, t),
                        name: "apply-watermark",
                        config: new StepConfig { RetryStrategy = RetryStrategy.Default },
                        cancellationToken: ct);
                    return new ProcessingBranchResult("watermark", null, Watermark: result, null);
                }),

                new DurableBranch<ProcessingBranchResult>("metadata", async (branchCtx, ct) =>
                {
                    var result = await branchCtx.StepAsync(
                        async (_, t) => await _imageService.ExtractMetadataAsync(input.Bucket, input.Key, t),
                        name: "extract-metadata",
                        config: new StepConfig { RetryStrategy = RetryStrategy.Default },
                        cancellationToken: ct);
                    return new ProcessingBranchResult("metadata", null, null, Metadata: result);
                }),
            ],
            name: "image-processing-fanout",
            config: new ParallelConfig
            {
                MaxConcurrency = 3,
                CompletionConfig = CompletionConfig.AllSuccessful()
            });

        // Fail the workflow if any branch failed
        batch.ThrowIfError();

        // ──────────────────────────────────────────────────────────────────
        // Fan-In: Aggregate all branch results into a single PipelineResult.
        // ──────────────────────────────────────────────────────────────────
        var results = batch.GetResults();
        var thumbnail = results.First(r => r.Thumbnail is not null).Thumbnail!;
        var watermark = results.First(r => r.Watermark is not null).Watermark!;
        var metadata = results.First(r => r.Metadata is not null).Metadata!;

        var imageId = Path.GetFileNameWithoutExtension(input.Key);
        var pipelineResult = new PipelineResult(
            ImageId: imageId,
            SourceBucket: input.Bucket,
            SourceKey: input.Key,
            Thumbnail: thumbnail,
            Watermark: watermark,
            Metadata: metadata,
            CompletedAt: DateTime.UtcNow);

        // ──────────────────────────────────────────────────────────────────
        // Write aggregated result to DynamoDB (idempotent — upsert by ImageId).
        // ──────────────────────────────────────────────────────────────────
        await ctx.StepAsync(
            async (_, ct) => await _resultsWriter.WriteResultAsync(pipelineResult, ct),
            name: "write-results-to-dynamodb",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        return pipelineResult;
    }
}
