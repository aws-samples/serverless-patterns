using System.Text;
using Xunit;
using Amazon.Lambda.KinesisEvents;
using Amazon.Lambda.TestUtilities;
using DataProcessFunction.Models;
using System.Text.Json;
using DataProcessFunction.Serialization;
using Microsoft.Extensions.Configuration;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Kinesis;
using Amazon.Kinesis.Model;

namespace DataProcessFunction.Tests;

public class FunctionTest
{
    private static readonly string TableName = "processed-data-table";
    private static readonly string StreamName = "AnalyticsDataStream";
    
    [Fact]
    public async Task TestFunction()
    {
        // Set Environment avriables using ConfigurationBuilder
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(new Dictionary<string, string?>
            {
                { "PROCESSED_TABLE_NAME", TableName }
            })
            .Build();
                    
        var data = GenerateRandomData();
        var deserializedData = JsonSerializer.Serialize(data, LambdaFunctionJsonSerializerContext.Default.DataModel);

        KinesisEvent evnt = new()
        {
            Records =
            [
                new KinesisEvent.KinesisEventRecord
                {
                    AwsRegion = "us-west-2",
                    Kinesis = new KinesisEvent.Record
                    {
                        ApproximateArrivalTimestamp = DateTime.Now,
                        Data = new MemoryStream(Encoding.UTF8.GetBytes(deserializedData)),
                        PartitionKey = Guid.NewGuid().ToString(),
                        SequenceNumber = "1",
                        KinesisSchemaVersion = "1.0",
                        EncryptionType = Amazon.Kinesis.EncryptionType.NONE
                    }
                }
            ]
        };

        var context = new TestLambdaContext();

        var dataProcessFunction = new DataProcessFunction(config);
        var response = await dataProcessFunction.FunctionHandler(evnt, context);
        Assert.NotNull(response);
        Assert.Null(response.BatchItemFailures);

        var testLogger = context.Logger as TestLambdaLogger;

        var expectedLogValue = $"Processing record: {deserializedData}";
        Assert.Contains(expectedLogValue, testLogger!.Buffer.ToString());

        // Check record in DynamoDB
        var dynamoDbClient = new AmazonDynamoDBClient();
        var tableName = TableName;
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
    public async Task IntegrationTest()
    {
        var data = GenerateRandomData();
        var serializedData = JsonSerializer.Serialize(data, LambdaFunctionJsonSerializerContext.Default.DataModel);

        // Write record to Kinesis
        var kinesisClient = new AmazonKinesisClient();
        var streamName = StreamName;
        var putRecordRequest = new PutRecordRequest
        {
            StreamName = streamName,
            Data = new MemoryStream(Encoding.UTF8.GetBytes(serializedData)),
            PartitionKey = Guid.NewGuid().ToString()
        };

        var putRecordResponse = await kinesisClient.PutRecordAsync(putRecordRequest);
        Assert.NotNull(putRecordResponse);
        Assert.NotNull(putRecordResponse.SequenceNumber);

        // Wait for some time
        await Task.Delay(5000);

        // Check record in DynamoDB
        var dynamoDbClient = new AmazonDynamoDBClient();
        var tableName = TableName;
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
}