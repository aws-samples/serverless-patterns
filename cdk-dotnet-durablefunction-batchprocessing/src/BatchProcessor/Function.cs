using Amazon.DynamoDBv2;
using Amazon.Lambda.Core;
using Amazon.Lambda.DurableExecution;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;
using Amazon.S3;

[assembly: LambdaSerializer(typeof(DefaultLambdaJsonSerializer))]

namespace BatchProcessor;

/// <summary>
/// Lambda Durable Function that processes a batch of files using dynamic fan-out/fan-in.
///
/// Workflow:
///   1. List all files under the specified S3 prefix (unknown count at design time).
///   2. Dynamically create a parallel branch for each discovered file.
///   3. Wait for all branches to complete (each processes one file).
///   4. Aggregate results and write a summary report to S3.
/// </summary>
internal sealed class BatchProcessorHandler
{
    private static readonly IAmazonS3 S3Client = new AmazonS3Client();
    private static readonly IAmazonDynamoDB DynamoDbClient = new AmazonDynamoDBClient();

    private static readonly string TableName =
        Environment.GetEnvironmentVariable("RESULTS_TABLE_NAME")
        ?? throw new InvalidOperationException("RESULTS_TABLE_NAME environment variable is not set.");

    private static readonly string BucketName =
        Environment.GetEnvironmentVariable("FILES_BUCKET_NAME")
        ?? throw new InvalidOperationException("FILES_BUCKET_NAME environment variable is not set.");

    private readonly FileProcessingService _fileService = new(S3Client);
    private readonly ReportWriter _reportWriter = new(S3Client, DynamoDbClient, TableName);

    public static async Task Main()
    {
        var handler = new BatchProcessorHandler();
        var serializer = new DefaultLambdaJsonSerializer();
        using var wrapper = HandlerWrapper.GetHandlerWrapper<DurableExecutionInvocationInput, DurableExecutionInvocationOutput>(
            handler.Handler, serializer);
        using var bootstrap = new LambdaBootstrap(wrapper);
        await bootstrap.RunAsync();
    }

    public Task<DurableExecutionInvocationOutput> Handler(
        DurableExecutionInvocationInput input, ILambdaContext context)
        => DurableFunction.WrapAsync<BatchInput, BatchSummary>(Workflow, input, context);

    private async Task<BatchSummary> Workflow(BatchInput input, IDurableContext ctx)
    {
        var bucket = input.Bucket ?? BucketName;

        // Capture current time inside a step so it's checkpointed for deterministic replay.
        var startTime = await ctx.StepAsync(
            (_, _) => Task.FromResult(DateTime.UtcNow),
            name: "capture-start-time");

        var batchId = $"batch-{startTime:yyyyMMdd-HHmmss}";

        // ──────────────────────────────────────────────────────────────────
        // Step 1: List all files under the prefix (checkpointed).
        // The file count is unknown at design time — discovered at runtime.
        // ──────────────────────────────────────────────────────────────────
        var fileKeys = await ctx.StepAsync(
            async (_, ct) => await _fileService.ListFilesAsync(bucket, input.Prefix, ct),
            name: "list-files",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        if (fileKeys.Count == 0)
        {
            // No files found — write an empty summary
            return new BatchSummary(
                BatchId: batchId,
                SourceBucket: bucket,
                SourcePrefix: input.Prefix,
                TotalFiles: 0,
                TotalBytes: 0,
                SuccessCount: 0,
                FailureCount: 0,
                ReportKey: "",
                CompletedAt: startTime);
        }

        // ──────────────────────────────────────────────────────────────────
        // Step 2: Dynamic Fan-Out — create a parallel branch for EACH file.
        // The number of branches is determined at runtime by the list result.
        // ──────────────────────────────────────────────────────────────────
        var branches = fileKeys.Select(key =>
            new DurableBranch<FileProcessingResult>(
                Path.GetFileName(key),
                async (branchCtx, ct) =>
                {
                    // Process the file
                    var result = await branchCtx.StepAsync(
                        async (_, t) => await _fileService.ProcessFileAsync(bucket, key, t),
                        name: "process-file",
                        config: new StepConfig { RetryStrategy = RetryStrategy.Default },
                        cancellationToken: ct);

                    // Write per-file result to DynamoDB
                    await branchCtx.StepAsync(
                        async (_, t) => await _reportWriter.WriteFileResultAsync(batchId, result, t),
                        name: "write-result",
                        config: new StepConfig { RetryStrategy = RetryStrategy.Default },
                        cancellationToken: ct);

                    return result;
                }))
            .ToList();

        var batch = await ctx.ParallelAsync(
            branches,
            name: "process-all-files",
            config: new ParallelConfig
            {
                MaxConcurrency = 10,
                CompletionConfig = CompletionConfig.AllCompleted()
            });

        // ──────────────────────────────────────────────────────────────────
        // Step 3: Fan-In — aggregate results and write summary report.
        // ──────────────────────────────────────────────────────────────────
        var successfulResults = batch.GetResults();
        var totalBytes = successfulResults.Sum(r => r.SizeBytes);

        var summary = new BatchSummary(
            BatchId: batchId,
            SourceBucket: bucket,
            SourcePrefix: input.Prefix,
            TotalFiles: batch.TotalCount,
            TotalBytes: totalBytes,
            SuccessCount: batch.SuccessCount,
            FailureCount: batch.FailureCount,
            ReportKey: "",
            CompletedAt: await ctx.StepAsync(
                (_, _) => Task.FromResult(DateTime.UtcNow),
                name: "capture-completion-time"));

        // Write the JSON summary report to S3
        var reportKey = await ctx.StepAsync(
            async (_, ct) => await _reportWriter.WriteSummaryReportAsync(
                bucket, summary, successfulResults, ct),
            name: "write-summary-report",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        return summary with { ReportKey = reportKey };
    }
}
