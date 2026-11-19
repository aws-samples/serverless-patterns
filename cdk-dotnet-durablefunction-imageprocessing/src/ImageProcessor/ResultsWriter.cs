using System.Globalization;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;

namespace ImageProcessor;

/// <summary>
/// Writes the aggregated pipeline results to DynamoDB.
/// </summary>
internal sealed class ResultsWriter(IAmazonDynamoDB dynamoDb, string tableName)
{
    private readonly IAmazonDynamoDB _dynamoDb = dynamoDb;
    private readonly string _tableName = tableName;

    /// <summary>
    /// Persists the final pipeline result to DynamoDB.
    /// This operation is idempotent — writing the same ImageId overwrites the previous entry.
    /// </summary>
    public async Task WriteResultAsync(PipelineResult result, CancellationToken ct)
    {
        ArgumentNullException.ThrowIfNull(result);

        var item = new Dictionary<string, AttributeValue>
        {
            ["ImageId"] = new() { S = result.ImageId },
            ["SourceBucket"] = new() { S = result.SourceBucket },
            ["SourceKey"] = new() { S = result.SourceKey },
            ["ThumbnailKey"] = new() { S = result.Thumbnail.OutputKey },
            ["ThumbnailWidth"] = new() { N = result.Thumbnail.Width.ToString(CultureInfo.InvariantCulture) },
            ["ThumbnailHeight"] = new() { N = result.Thumbnail.Height.ToString(CultureInfo.InvariantCulture) },
            ["WatermarkKey"] = new() { S = result.Watermark.OutputKey },
            ["OriginalWidth"] = new() { N = result.Metadata.Width.ToString(CultureInfo.InvariantCulture) },
            ["OriginalHeight"] = new() { N = result.Metadata.Height.ToString(CultureInfo.InvariantCulture) },
            ["Format"] = new() { S = result.Metadata.Format },
            ["FileSizeBytes"] = new() { N = result.Metadata.FileSizeBytes.ToString(CultureInfo.InvariantCulture) },
            ["CompletedAt"] = new() { S = result.CompletedAt.ToString("O", CultureInfo.InvariantCulture) }
        };

        await _dynamoDb.PutItemAsync(new PutItemRequest
        {
            TableName = _tableName,
            Item = item
        }, ct);
    }
}
