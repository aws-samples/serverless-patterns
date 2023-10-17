using System.Dynamic;
using System.Text.Json;
using System.Text.Json.Serialization;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
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
        var customMessage=Newtonsoft.Json.JsonConvert.DeserializeObject<dynamic>(bodyStr);
        context.Logger.LogInformation($"customMessage:{customMessage}");
        if(customMessage==null) throw new Exception("customMessage was null!");
        var id=Convert.ToString(customMessage.id);
        context.Logger.LogInformation($"customMessage.id:{id}");

        await dynamoDbClient.PutItemAsync(
            Environment.GetEnvironmentVariable("CLAIM_CHECK_TABLE"),
            new Dictionary<string, AttributeValue>()
            {
                {"id", new AttributeValue(id)},
                {"custom_message_json", new AttributeValue(bodyStr)}
            }
        );

        return new {
            eventType= "Some_Event_Type",
            id=id,
        };
    }
}
