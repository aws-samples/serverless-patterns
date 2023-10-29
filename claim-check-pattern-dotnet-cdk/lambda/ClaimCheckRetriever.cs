using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.CloudWatchEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.SQSEvents;
using ClaimCheckPattern.Models;

namespace ClaimCheckPattern;

public class ClaimCheckRetriever
{
    private static readonly AmazonDynamoDBClient DynamoDbClient = new();

    public async Task<FullMessage> FunctionHandler(SQSEvent.SQSMessage[] sqsMessages, ILambdaContext context)
    {
        // Read message
        context.Logger.LogInformation($"Received event: {JsonSerializer.Serialize(sqsMessages)}");

        var cloudWatchEvent = JsonSerializer.Deserialize<CloudWatchEvent<ClaimCheck>>(sqsMessages[0].Body, new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        });
        if (cloudWatchEvent == null)
        {
            throw new Exception("Claim check was null.");
        }

        var claimCheck = cloudWatchEvent.Detail;

        // Get item from DynamoDB
        context.Logger.LogInformation($"Resolving full message in DynamoDB using Claim check id: '{claimCheck.Id}'.");
        var tableName = Environment.GetEnvironmentVariable("CLAIM_CHECK_TABLE");
        var getItemResponse = await DynamoDbClient.GetItemAsync(
            tableName,
            new Dictionary<string, AttributeValue>
            {
                {"id", new AttributeValue($"{claimCheck.Id}")},
            }
        );
        var fullMessageJson = getItemResponse.Item["custom_message_json"].S;
        var fullMessage = JsonSerializer.Deserialize<FullMessage>(fullMessageJson);
        if (fullMessage == null)
        {
            throw new Exception("Full message item from DynamoDB was null.");
        }
        context.Logger.LogInformation("Full message was resolved successfully.");
        return fullMessage;
    }
}
