using System.Globalization;
using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.S3;
using Amazon.S3.Model;

namespace BatchProcessor;

/// <summary>
/// Writes per-file results to DynamoDB and the final summary report to S3.
/// </summary>
internal sealed class ReportWriter(IAmazonS3 s3Client, IAmazonDynamoDB dynamoDb, string tableName)
{
    private readonly IAmazonS3 _s3Client = s3Client;
    private readonly IAmazonDynamoDB _dynamoDb = dynamoDb;
    private readonly string _tableName = tableName;

    /// <summary>
    /// Writes a single file's processing result to DynamoDB.
    /// </summary>
    public async Task WriteFileResultAsync(string batchId, FileProcessingResult result, CancellationToken ct)
    {
        ArgumentNullException.ThrowIfNull(result);

        var item = new Dictionary<string, AttributeValue>
        {
            ["BatchId"] = new() { S = batchId },
            ["FileName"] = new() { S = result.FileName },
            ["SizeBytes"] = new() { N = result.SizeBytes.ToString(CultureInfo.InvariantCulture) },
            ["LineCount"] = new() { N = result.LineCount.ToString(CultureInfo.InvariantCulture) },
            ["WordCount"] = new() { N = result.WordCount.ToString(CultureInfo.InvariantCulture) },
            ["ContentHash"] = new() { S = result.ContentHash }
        };

        await _dynamoDb.PutItemAsync(new PutItemRequest
        {
            TableName = _tableName,
            Item = item
        }, ct);
    }

    /// <summary>
    /// Writes the final batch summary report as JSON to S3.
    /// </summary>
    public async Task<string> WriteSummaryReportAsync(
        string bucket,
        BatchSummary summary,
        IReadOnlyList<FileProcessingResult> results,
        CancellationToken ct)
    {
        ArgumentNullException.ThrowIfNull(summary);

        var report = new
        {
            summary.BatchId,
            summary.SourceBucket,
            summary.SourcePrefix,
            summary.TotalFiles,
            summary.TotalBytes,
            summary.SuccessCount,
            summary.FailureCount,
            summary.CompletedAt,
            Files = results
        };

        var reportJson = JsonSerializer.Serialize(report, new JsonSerializerOptions
        {
            WriteIndented = true
        });

        var reportKey = $"reports/{summary.BatchId}.json";

        await _s3Client.PutObjectAsync(new PutObjectRequest
        {
            BucketName = bucket,
            Key = reportKey,
            ContentBody = reportJson,
            ContentType = "application/json"
        }, ct);

        return reportKey;
    }
}
