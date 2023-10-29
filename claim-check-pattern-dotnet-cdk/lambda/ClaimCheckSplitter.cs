using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.Core;
using Amazon.Lambda.SQSEvents;
using ClaimCheckPattern.Models;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace ClaimCheckPattern;

public class ClaimCheckSplitter
{
    private static readonly AmazonDynamoDBClient DynamoDbClient = new();

    public async Task<object> FunctionHandler(SQSEvent.SQSMessage[] sqsMessages, ILambdaContext context)
    {
        // Read full message
        context.Logger.LogInformation($"Received event: {JsonSerializer.Serialize(sqsMessages)}");
        var fullMessageJson = sqsMessages[0].Body;
        var fullMessage = JsonSerializer.Deserialize<FullMessage>(fullMessageJson);
        if (fullMessage == null)
        {
            throw new Exception("Full message was null.");
        }

        // Create and store claim check mapping
        context.Logger.LogInformation($"Storing full message with id: '{fullMessage.Id}' in DynamoDB.");
        await DynamoDbClient.PutItemAsync(
            Environment.GetEnvironmentVariable("CLAIM_CHECK_TABLE"),
            new Dictionary<string, AttributeValue>
            {
                {"id", new AttributeValue($"{fullMessage.Id}")},
                {"custom_message_json", new AttributeValue(fullMessageJson)}
            }
        );
        context.Logger.LogInformation("Full message was stored successfully.");
        return new ClaimCheck
        {
            Id = fullMessage.Id
        };
    }
}
