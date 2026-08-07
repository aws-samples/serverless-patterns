using System.Diagnostics.CodeAnalysis;

namespace BatchProcessor;

/// <summary>
/// Input to the durable workflow — specifies which S3 prefix to scan for files.
/// </summary>
[SuppressMessage("Performance", "CA1812:Avoid uninstantiated internal classes", Justification = "Deserialized by Lambda runtime")]
internal sealed record BatchInput(string Bucket, string Prefix);

/// <summary>
/// Result of processing a single file.
/// </summary>
internal sealed record FileProcessingResult(
    string FileName,
    long SizeBytes,
    int LineCount,
    int WordCount,
    string ContentHash);

/// <summary>
/// Final summary report written to S3 after all files are processed.
/// </summary>
internal sealed record BatchSummary(
    string BatchId,
    string SourceBucket,
    string SourcePrefix,
    int TotalFiles,
    long TotalBytes,
    int SuccessCount,
    int FailureCount,
    string ReportKey,
    DateTime CompletedAt);
