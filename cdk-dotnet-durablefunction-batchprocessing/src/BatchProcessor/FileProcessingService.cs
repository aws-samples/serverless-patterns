using System.Security.Cryptography;
using Amazon.S3;
using Amazon.S3.Model;

namespace BatchProcessor;

/// <summary>
/// Service that processes individual files: reads content, computes stats, and returns results.
/// </summary>
internal sealed class FileProcessingService(IAmazonS3 s3Client)
{
    private readonly IAmazonS3 _s3Client = s3Client;

    /// <summary>
    /// Lists all object keys under the given prefix.
    /// </summary>
    public async Task<List<string>> ListFilesAsync(string bucket, string prefix, CancellationToken ct)
    {
        var keys = new List<string>();
        string? continuationToken = null;

        do
        {
            var response = await _s3Client.ListObjectsV2Async(new ListObjectsV2Request
            {
                BucketName = bucket,
                Prefix = prefix,
                ContinuationToken = continuationToken
            }, ct);

            foreach (var obj in response.S3Objects)
            {
                // Skip "directory" markers (keys ending in /)
                if (!obj.Key.EndsWith('/'))
                {
                    keys.Add(obj.Key);
                }
            }

            continuationToken = response.IsTruncated == true ? response.NextContinuationToken : null;
        }
        while (continuationToken is not null);

        return keys;
    }

    /// <summary>
    /// Processes a single file: downloads it, computes line count, word count, size, and SHA-256 hash.
    /// </summary>
    public async Task<FileProcessingResult> ProcessFileAsync(string bucket, string key, CancellationToken ct)
    {
        using var response = await _s3Client.GetObjectAsync(bucket, key, ct);
        using var stream = response.ResponseStream;
        using var reader = new StreamReader(stream);

        var content = await reader.ReadToEndAsync(ct);

        var lineCount = content.Split('\n').Length;
        var wordCount = content.Split([' ', '\t', '\n', '\r'], StringSplitOptions.RemoveEmptyEntries).Length;
        var sizeBytes = response.ContentLength;

        var hashBytes = SHA256.HashData(System.Text.Encoding.UTF8.GetBytes(content));
        var contentHash = Convert.ToHexStringLower(hashBytes);

        var fileName = Path.GetFileName(key);

        return new FileProcessingResult(
            FileName: fileName,
            SizeBytes: sizeBytes,
            LineCount: lineCount,
            WordCount: wordCount,
            ContentHash: contentHash);
    }
}
