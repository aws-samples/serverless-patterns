using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.SQS.Model;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace ServerlessPatterns.ClaimCheck;

public class ClaimCheckSplitter
{
    private static readonly AmazonDynamoDBClient dynamoDbClient = new AmazonDynamoDBClient();    
    public async Task<object> FunctionHandler(Message[] sqsMessages, ILambdaContext context)
    {        
        context.Logger.LogInformation($"Received event: {JsonSerializer.Serialize(sqsMessages)}");
        context.Logger.LogInformation($"Records[0]: {sqsMessages[0]}");
        var firstSqsMessage = sqsMessages[0];
        var bodyStr=firstSqsMessage.Body;
        var customMessage=JsonSerializer.Deserialize<dynamic>(bodyStr);
        context.Logger.LogInformation($"customMessage:{customMessage}");

        await dynamoDbClient.PutItemAsync(
            Environment.GetEnvironmentVariable("CLAIM_CHECK_TABLE"),
            new Dictionary<string, AttributeValue>()
            {
                {"id", new AttributeValue(customMessage.id)},
                {"message", new AttributeValue(JsonSerializer.Serialize(customMessage))}
            }
        );

        return new {
            eventType= "Some_Event_Type",
            id=customMessage.id,
        };
    }
}
