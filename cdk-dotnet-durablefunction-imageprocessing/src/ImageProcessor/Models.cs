using System.Diagnostics.CodeAnalysis;

namespace ImageProcessor;

/// <summary>
/// Input to the durable workflow — identifies the uploaded image.
/// </summary>
[SuppressMessage("Performance", "CA1812:Avoid uninstantiated internal classes", Justification = "Deserialized by Lambda runtime")]
internal sealed record ImageInput(string Bucket, string Key);

/// <summary>
/// Result of generating a thumbnail.
/// </summary>
internal sealed record ThumbnailResult(string OutputKey, int Width, int Height);

/// <summary>
/// Result of applying a watermark.
/// </summary>
internal sealed record WatermarkResult(string OutputKey);

/// <summary>
/// Metadata extracted from the original image.
/// </summary>
internal sealed record ImageMetadata(int Width, int Height, string Format, long FileSizeBytes);

/// <summary>
/// Per-branch result type used in the parallel fan-out.
/// Each branch produces one of the specific result types.
/// </summary>
internal sealed record ProcessingBranchResult(
    string BranchName,
    ThumbnailResult? Thumbnail,
    WatermarkResult? Watermark,
    ImageMetadata? Metadata);

/// <summary>
/// Final aggregated result written to DynamoDB and returned from the workflow.
/// </summary>
internal sealed record PipelineResult(
    string ImageId,
    string SourceBucket,
    string SourceKey,
    ThumbnailResult Thumbnail,
    WatermarkResult Watermark,
    ImageMetadata Metadata,
    DateTime CompletedAt);
