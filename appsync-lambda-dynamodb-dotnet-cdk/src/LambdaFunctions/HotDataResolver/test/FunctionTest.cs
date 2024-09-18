using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.TestUtilities;
using Xunit;

namespace HotDataResolver.Tests;

public class FunctionTests : IDisposable
{
    private const string HotDataTableName = "hot-data-table";
    private readonly HotDataResolverFunction _function;
    private readonly AmazonDynamoDBClient _dynamoDbClient;

    public FunctionTests()
    {
        Environment.SetEnvironmentVariable("HOT_DATA_TABLE", HotDataTableName);
        _function = new HotDataResolverFunction();
        _dynamoDbClient = new AmazonDynamoDBClient();
    }

    public void Dispose()
    {
        GC.SuppressFinalize(this);
        _dynamoDbClient.Dispose();
        _function.Dispose();
    }

    [Fact]
    public async Task FunctionHandler_ValidId_ReturnsData()
    {
        // Arrange
        var id = Guid.NewGuid().ToString();
        var content = "Test Content - " + Guid.NewGuid().ToString();
        var timestamp = DateTime.UtcNow;

        // Arrange
        var putItemRequest = new PutItemRequest
        {
            TableName = HotDataTableName,
            Item = new Dictionary<string, AttributeValue>
            {
                { "id", new AttributeValue { S = id } },
                { "content", new AttributeValue { S = content } },
                { "timestamp", new AttributeValue { S = timestamp.ToString("O") } }
            }
        };
        await _dynamoDbClient.PutItemAsync(putItemRequest);

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

        // Delete item from DynamoDB
        var deleteItemRequest = new DeleteItemRequest
        {
            TableName = HotDataTableName,
            Key = new Dictionary<string, AttributeValue>
            {
                { "id", new AttributeValue { S = id } }
            }
        };
        await _dynamoDbClient.DeleteItemAsync(deleteItemRequest);        
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
            _function.FunctionHandler(input, new TestLambdaContext()));
    }
}