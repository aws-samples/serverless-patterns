using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;

namespace ServerlessPatterns.ClaimCheck;

public class ClaimCheckRetriever
{
    private static readonly AmazonDynamoDBClient dynamoDbClient = new AmazonDynamoDBClient();    
    public async Task<GetItemResponse> FunctionHandler(dynamic eventInput, ILambdaContext context)
    {
        context.Logger.LogInformation($"Received event: {JsonSerializer.Serialize(eventInput)}"); // JSON.stringify(event, null, 2)
        context.Logger.LogInformation($"Records[0]: {eventInput[0].body}");
        var body = JsonSerializer.Deserialize(eventInput[0].body);
        context.Logger.LogInformation($"body:{body}");
        context.Logger.LogInformation($"id:{body.id}");
    
        var response=await dynamoDbClient.GetItemAsync(
            Environment.GetEnvironmentVariable("CLAIM_CHECK_TABLE"),
            new Dictionary<string, AttributeValue>()
            {
                {"id", new AttributeValue(body.id)},
            }
        );
        return response;
    }
}
