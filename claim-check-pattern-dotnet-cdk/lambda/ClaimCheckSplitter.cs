using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace ServerlessPatterns.ClaimCheck;

public class ClaimCheckSplitter
{
    private static readonly AmazonDynamoDBClient dynamoDbClient = new AmazonDynamoDBClient();    
    public async Task<object> FunctionHandler(dynamic eventInput, ILambdaContext context)
    {        
        context.Logger.LogInformation($"Received event: {JsonSerializer.Serialize(eventInput)}"); // JSON.stringify(event, null, 2)
        context.Logger.LogInformation($"Records[0]: {eventInput[0]}");
        var body = JsonSerializer.Deserialize(eventInput[0].body);
        context.Logger.LogInformation($"body:{body}");

        await dynamoDbClient.PutItemAsync(
            Environment.GetEnvironmentVariable("CLAIM_CHECK_TABLE"),
            new Dictionary<string, AttributeValue>()
            {
                {"id", new AttributeValue(body.id)},
                {"message", new AttributeValue(JsonSerializer.Serialize(body))}
            }
        );

        return new {
            eventType= "Some_Event_Type",
            id=body.id,
        };
    }
}
