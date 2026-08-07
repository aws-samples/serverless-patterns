using Amazon.S3;
using Amazon.S3.Model;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Formats.Jpeg;
using SixLabors.ImageSharp.Formats.Png;
using SixLabors.ImageSharp.PixelFormats;
using SixLabors.ImageSharp.Processing;

namespace ImageProcessor;

/// <summary>
/// Service that performs the actual image manipulation operations.
/// Each method is designed to be called from a durable step.
/// </summary>
internal sealed class ImageProcessingService(IAmazonS3 s3Client)
{
    private const int ThumbnailMaxWidth = 200;
    private const int ThumbnailMaxHeight = 200;

    private readonly IAmazonS3 _s3Client = s3Client;

    /// <summary>
    /// Downloads the source image from S3, resizes it to a thumbnail, and uploads the result.
    /// </summary>
    public async Task<ThumbnailResult> GenerateThumbnailAsync(
        string bucket, string key, CancellationToken ct)
    {
        using var response = await _s3Client.GetObjectAsync(bucket, key, ct);
        using var sourceStream = response.ResponseStream;
        using var image = await Image.LoadAsync(sourceStream, ct);

        image.Mutate(x => x.Resize(new ResizeOptions
        {
            Size = new Size(ThumbnailMaxWidth, ThumbnailMaxHeight),
            Mode = ResizeMode.Max
        }));

        var outputKey = GetOutputKey(key, "thumbnails");

        using var outputStream = new MemoryStream();
        await image.SaveAsync(outputStream, new JpegEncoder { Quality = 80 }, ct);
        outputStream.Position = 0;

        await _s3Client.PutObjectAsync(new PutObjectRequest
        {
            BucketName = bucket,
            Key = outputKey,
            InputStream = outputStream,
            ContentType = "image/jpeg"
        }, ct);

        return new ThumbnailResult(outputKey, image.Width, image.Height);
    }

    /// <summary>
    /// Downloads the source image from S3, overlays a watermark logo in the bottom-right corner,
    /// and uploads the result.
    /// </summary>
    public async Task<WatermarkResult> ApplyWatermarkAsync(
        string bucket, string key, CancellationToken ct)
    {
        using var response = await _s3Client.GetObjectAsync(bucket, key, ct);
        using var sourceStream = response.ResponseStream;
        using var image = await Image.LoadAsync<Rgba32>(sourceStream, ct);

        // Load the watermark logo from the bundled file
        var watermarkPath = Path.Combine(AppContext.BaseDirectory, "watermark.png");
        using var watermark = await Image.LoadAsync(watermarkPath, ct);

        // Resize watermark to fit within 50x50 px, preserving aspect ratio
        watermark.Mutate(w => w.Resize(new ResizeOptions
        {
            Size = new Size(50, 50),
            Mode = ResizeMode.Max
        }));

        // Position in the bottom-right corner with a 10px margin
        const int margin = 10;
        var x = image.Width - watermark.Width - margin;
        var y = image.Height - watermark.Height - margin;

        image.Mutate(ctx => ctx.DrawImage(watermark, new Point(x, y), opacity: 0.5f));

        // Apply 5px rounded corners and dark border
        ApplyRoundedCornersAndBorder(image, 20f, 3);

        var outputKey = GetOutputKey(key, "watermarked");

        using var outputStream = new MemoryStream();
        await image.SaveAsync(outputStream, new PngEncoder(), ct);
        outputStream.Position = 0;

        await _s3Client.PutObjectAsync(new PutObjectRequest
        {
            BucketName = bucket,
            Key = outputKey,
            InputStream = outputStream,
            ContentType = "image/png"
        }, ct);

        return new WatermarkResult(outputKey);
    }

    /// <summary>
    /// Downloads the source image metadata from S3 and extracts dimensions and format info.
    /// </summary>
    public async Task<ImageMetadata> ExtractMetadataAsync(
        string bucket, string key, CancellationToken ct)
    {
        // Get object metadata for file size
        var metadataResponse = await _s3Client.GetObjectMetadataAsync(bucket, key, ct);
        var fileSize = metadataResponse.ContentLength;

        // Load the image to extract dimensions and format
        using var response = await _s3Client.GetObjectAsync(bucket, key, ct);
        using var sourceStream = response.ResponseStream;
        var imageInfo = await Image.IdentifyAsync(sourceStream, ct);

        return new ImageMetadata(
            Width: imageInfo.Width,
            Height: imageInfo.Height,
            Format: imageInfo.Metadata.DecodedImageFormat?.Name ?? "Unknown",
            FileSizeBytes: fileSize);
    }

    private static string GetOutputKey(string sourceKey, string folder)
    {
        var fileName = Path.GetFileNameWithoutExtension(sourceKey);
        var extension = Path.GetExtension(sourceKey);
        return $"{folder}/{fileName}{extension}";
    }

    /// <summary>
    /// Applies rounded corners and a dark border to the image.
    /// Works at the pixel level to avoid ImageSharp.Drawing dependency.
    /// </summary>
    private static void ApplyRoundedCornersAndBorder(Image<Rgba32> image, float cornerRadius, int borderWidth)
    {
        var width = image.Width;
        var height = image.Height;
        var borderColor = new Rgba32(30, 30, 30, 255);
        var r2 = cornerRadius * cornerRadius;

        image.ProcessPixelRows(accessor =>
        {
            for (var y = 0; y < height; y++)
            {
                var row = accessor.GetRowSpan(y);
                for (var x = 0; x < width; x++)
                {
                    // Check if pixel is outside the rounded rectangle
                    if (IsOutsideRoundedRect(x, y, width, height, cornerRadius, r2))
                    {
                        row[x] = new Rgba32(0, 0, 0, 0); // Transparent
                    }
                    // Check if pixel is in the border zone
                    else if (IsInBorderZone(x, y, width, height, cornerRadius, borderWidth, r2))
                    {
                        row[x] = borderColor;
                    }
                }
            }
        });
    }

    private static bool IsOutsideRoundedRect(int x, int y, int width, int height, float r, float r2)
    {
        // Only corners need checking
        if (x < r && y < r) // Top-left
            return DistanceSquared(x, y, r, r) > r2;
        if (x >= width - r && y < r) // Top-right
            return DistanceSquared(x, y, width - r - 1, r) > r2;
        if (x < r && y >= height - r) // Bottom-left
            return DistanceSquared(x, y, r, height - r - 1) > r2;
        if (x >= width - r && y >= height - r) // Bottom-right
            return DistanceSquared(x, y, width - r - 1, height - r - 1) > r2;
        return false;
    }

    private static bool IsInBorderZone(int x, int y, int width, int height, float r, int borderWidth, float r2)
    {
        // Check if on the straight border edges
        if (x < borderWidth || x >= width - borderWidth || y < borderWidth || y >= height - borderWidth)
        {
            return !IsOutsideRoundedRect(x, y, width, height, r, r2);
        }

        // Check inner corner arcs
        var innerR = r - borderWidth;
        if (innerR <= 0) return false;
        var innerR2 = innerR * innerR;

        if (x < r && y < r)
            return DistanceSquared(x, y, r, r) > innerR2;
        if (x >= width - r && y < r)
            return DistanceSquared(x, y, width - r - 1, r) > innerR2;
        if (x < r && y >= height - r)
            return DistanceSquared(x, y, r, height - r - 1) > innerR2;
        if (x >= width - r && y >= height - r)
            return DistanceSquared(x, y, width - r - 1, height - r - 1) > innerR2;

        return false;
    }

    private static float DistanceSquared(float x1, float y1, float x2, float y2)
    {
        var dx = x1 - x2;
        var dy = y1 - y2;
        return (dx * dx) + (dy * dy);
    }
}
