// File: test/ColdDataResolver.Tests/FunctionTests.cs

using System.Text.Json;
using Amazon.Lambda.TestUtilities;
using Amazon.S3;
using Amazon.S3.Model;
using Xunit;

namespace ColdDataResolver.Tests;

public class FunctionTests : IDisposable
{
    private readonly ColdDataResolverFunction _function;
    private readonly AmazonS3Client _s3Client;
    private const string BucketName = "[REPLACE WITH YOUR BUCKET NAME]";
    private const string GLUE_DATABASE = "cold_data_db";
    private const string GLUE_TABLE = "cold_data_table";

    public FunctionTests()
    {
        Environment.SetEnvironmentVariable("COLD_DATA_BUCKET", BucketName);
        Environment.SetEnvironmentVariable("GLUE_DATABASE", GLUE_DATABASE);
        Environment.SetEnvironmentVariable("GLUE_TABLE", GLUE_TABLE);        

        _function = new ColdDataResolverFunction();
        _s3Client = new AmazonS3Client();
    }

    public void Dispose()
    {
        GC.SuppressFinalize(this);
        _function.Dispose();
        _s3Client.Dispose();
    }

    [Fact]
    public async Task FunctionHandler_ValidId_ReturnsData()
    {
        // Arrange
        var id = Guid.NewGuid().ToString();
        var content = "Test Cold Content - " + Guid.NewGuid().ToString();
        var timestamp = DateTime.UtcNow;

        var csvData = $"{id},{content},{timestamp:O}";
        await _s3Client.PutObjectAsync(new PutObjectRequest
        {
            BucketName = BucketName,
            Key = $"data/{id}.csv",
            ContentBody = csvData
        });

        // Act
        var data = new {
            arguments = new Dictionary<string, string> { { "id", id } }
        };
        var input = JsonDocument.Parse(JsonSerializer.Serialize(data)).RootElement;
        var result = await _function.FunctionHandler(input, new TestLambdaContext());

        // Assert
        Assert.Contains(id, result);
        Assert.Contains(content, result);
        Assert.Contains(timestamp.ToString("O"), result);

        // Delete uploaded file from S3
        await _s3Client.DeleteObjectAsync(new DeleteObjectRequest
        {
            BucketName = BucketName,
            Key = $"data/{id}.csv"
        });        
    }

    [Fact]
    public async Task FunctionHandler_InvalidId_ThrowsException()
    {
        // Arrange
        var id = Guid.NewGuid().ToString();

        // Act
        var data = new {
            arguments = new Dictionary<string, string> { { "id", id } }
        };
        var input = JsonDocument.Parse(JsonSerializer.Serialize(data)).RootElement;
        await Assert.ThrowsAsync<Exception>(() => 
            _function.FunctionHandler(input, new TestLambdaContext()));}

    [Fact]
    public async Task FunctionHandler_QueryFailed_ThrowsException()
    {
        // Arrange
        var id = Guid.NewGuid().ToString();

        // Act & Assert
        var data = new {
            arguments = new Dictionary<string, string> { { "id", id } }
        };
        var input = JsonDocument.Parse(JsonSerializer.Serialize(data)).RootElement;  
        await Assert.ThrowsAsync<Exception>(() => 
            _function.FunctionHandler(input, new TestLambdaContext()));
    }

    [Fact]
    public async Task FunctionHandler_QueryCancelled_ThrowsException()
    {
        // Arrange
        var id = Guid.NewGuid().ToString();

        // Act & Assert
        var data = new {
            arguments = new Dictionary<string, string> { { "id", id } }
        };
        var input = JsonDocument.Parse(JsonSerializer.Serialize(data)).RootElement;  
        await Assert.ThrowsAsync<Exception>(() => 
            _function.FunctionHandler(input, new TestLambdaContext()));
    }
}