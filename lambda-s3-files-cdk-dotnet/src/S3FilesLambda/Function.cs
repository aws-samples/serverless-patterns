using Amazon.Lambda.Core;
using System.Text.Json.Serialization;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace S3FilesLambda;

public class Function
{
    private static readonly string MountPath = Environment.GetEnvironmentVariable("MOUNT_PATH") ?? "/mnt/s3data";

    public FileOperationResponse FunctionHandler(FileOperationRequest request, ILambdaContext context)
    {
        var action = request.Action ?? "list";

        return action.ToLowerInvariant() switch
        {
            "write" => HandleWrite(request, context),
            "read" => HandleRead(request, context),
            _ => HandleList(request, context)
        };
    }

    private FileOperationResponse HandleWrite(FileOperationRequest request, ILambdaContext context)
    {
        var filename = request.Filename ?? "hello.txt";
        var content = request.Content ?? $"Written by Lambda at {DateTime.UtcNow:O}";
        var filePath = SafePath(filename);

        var directory = Path.GetDirectoryName(filePath);
        if (!string.IsNullOrEmpty(directory))
        {
            Directory.CreateDirectory(directory);
        }

        File.WriteAllText(filePath, content);

        context.Logger.LogInformation($"Written file: {filePath}");

        return new FileOperationResponse
        {
            Status = "written",
            Path = filePath,
            Size = System.Text.Encoding.UTF8.GetByteCount(content)
        };
    }

    private FileOperationResponse HandleRead(FileOperationRequest request, ILambdaContext context)
    {
        var filename = request.Filename ?? "hello.txt";
        var filePath = SafePath(filename);

        if (!File.Exists(filePath))
        {
            return new FileOperationResponse
            {
                Status = "not_found",
                Path = filePath
            };
        }

        var content = File.ReadAllText(filePath);

        context.Logger.LogInformation($"Read file: {filePath}");

        return new FileOperationResponse
        {
            Status = "read",
            Path = filePath,
            Content = content,
            Size = content.Length
        };
    }

    private FileOperationResponse HandleList(FileOperationRequest request, ILambdaContext context)
    {
        var dir = request.Directory ?? "";
        var targetPath = SafePath(dir);

        if (!System.IO.Directory.Exists(targetPath))
        {
            return new FileOperationResponse
            {
                Status = "not_found",
                Path = targetPath
            };
        }

        var entries = System.IO.Directory.GetFileSystemEntries(targetPath)
            .Select(entry =>
            {
                var isDir = System.IO.Directory.Exists(entry);
                return new FileEntry
                {
                    Name = Path.GetFileName(entry),
                    Type = isDir ? "directory" : "file"
                };
            })
            .ToList();

        context.Logger.LogInformation($"Listed directory: {targetPath} ({entries.Count} entries)");

        return new FileOperationResponse
        {
            Status = "listed",
            Path = targetPath,
            Count = entries.Count,
            Entries = entries
        };
    }

    /// <summary>
    /// Resolve user input to a safe path under MOUNT_PATH. Throws on traversal.
    /// </summary>
    private string SafePath(string userInput)
    {
        var resolved = Path.GetFullPath(Path.Combine(MountPath, userInput));

        if (!resolved.StartsWith(MountPath + Path.DirectorySeparatorChar) && resolved != MountPath)
        {
            throw new InvalidOperationException($"Path traversal blocked: {userInput}");
        }

        return resolved;
    }
}

public class FileOperationRequest
{
    [JsonPropertyName("action")]
    public string? Action { get; set; }

    [JsonPropertyName("filename")]
    public string? Filename { get; set; }

    [JsonPropertyName("content")]
    public string? Content { get; set; }

    [JsonPropertyName("directory")]
    public string? Directory { get; set; }
}

public class FileOperationResponse
{
    [JsonPropertyName("status")]
    public string Status { get; set; } = "";

    [JsonPropertyName("path")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    public string? Path { get; set; }

    [JsonPropertyName("content")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    public string? Content { get; set; }

    [JsonPropertyName("size")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public int Size { get; set; }

    [JsonPropertyName("count")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public int Count { get; set; }

    [JsonPropertyName("entries")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    public List<FileEntry>? Entries { get; set; }
}

public class FileEntry
{
    [JsonPropertyName("name")]
    public string Name { get; set; } = "";

    [JsonPropertyName("type")]
    public string Type { get; set; } = "";
}
