using Xunit;
using Amazon.Lambda.TestUtilities;
using Microsoft.Extensions.Configuration;
using DataIngestFunction.Models;
using Amazon.SQS;
using Amazon.SQS.Model;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;

namespace DataIngestFunction.Tests;

public class FunctionTest
{

    [Fact]
    public async Task TestFunction()
    {
        // Set Environment avriables using ConfigurationBuilder
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(new Dictionary<string, string?>
            {
                { "KINESIS_STREAM_NAME", "AnalyticsDataStream" }
            })
            .Build();

        var context = new TestLambdaContext();
        var function = new DataIngestFunction(config);
        var data = GenerateRandomData();

        var returnValue = await function.FunctionHandler(data, context);
        Assert.NotEmpty(returnValue);

        var testLogger = context.Logger as TestLambdaLogger;
        Assert.Contains("Data ingested successfully. Sequence number", testLogger!.Buffer.ToString());

        // Wait for a while and check record in DynamoDB
        await Task.Delay(TimeSpan.FromSeconds(5));

        // Check record in DynamoDB
        var dynamoDbClient = new AmazonDynamoDBClient();
        var tableName = "processed-data-table";
        var id = data.Id;
        var getItemRequest = new GetItemRequest
        {
            TableName = tableName,
            Key = new Dictionary<string, AttributeValue>
            {
                { "Id", new AttributeValue { S = id } }
            }
        };

        var getItemResponse = await dynamoDbClient.GetItemAsync(getItemRequest);
        Assert.NotNull(getItemResponse.Item);
    }

    [Fact]
    public async Task TestMalformedDataIngestion()
    {
        // Set Environment variables using ConfigurationBuilder
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(new Dictionary<string, string?>
            {
                { "KINESIS_STREAM_NAME", "AnalyticsDataStream" }
            })
            .Build();

        var context = new TestLambdaContext();
        var function = new DataIngestFunction(config);
        var malformedData = GenerateMalformedData();

        var returnValue = await function.FunctionHandler(malformedData, context);
        Assert.NotEmpty(returnValue);

        // Check record in SQS
        var sqsClient = new AmazonSQSClient();
        var queueUrl = "kinesis-lambda-dlq";
        List<string> messages = [];

        while (true)
        {
            // Get latest one of the messages from the queue
            var receiveMessageRequest = new ReceiveMessageRequest
            {
                QueueUrl = queueUrl,
                MaxNumberOfMessages = 10,
                WaitTimeSeconds = 10 // Set to 0 to receive immediately
            };
            var response = await sqsClient.ReceiveMessageAsync(receiveMessageRequest);
            if (response.Messages.Count > 0)
            {
                messages.AddRange(response.Messages.Select(m => m.Body));
            }
            else
            {
                break;
            }
        }

        Assert.True(messages.Count > 0);
        Assert.Single(messages, m => m.Contains(returnValue));
    }

    private static DataModel GenerateRandomData()
    {
        return new DataModel
        {
            Id = Guid.NewGuid().ToString(),
            Timestamp = DateTime.UtcNow,
            Value = new Random().Next(1, 100),
            Category = new[] { "A", "B", "C" }[new Random().Next(3)]
        };
    }

    private static DataModel GenerateMalformedData()
    {
        return new DataModel
        {
            Id = null,
            Timestamp = DateTime.UtcNow,
            Value = -1,
            Category = "InvalidCategory"
        };
    }
}