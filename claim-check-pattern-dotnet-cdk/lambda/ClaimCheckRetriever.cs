using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.Core;
using Amazon.SQS.Model;

namespace ServerlessPatterns.ClaimCheck;

public class ClaimCheckRetriever
{
    private static readonly AmazonDynamoDBClient dynamoDbClient = new AmazonDynamoDBClient();    
    public async Task<GetItemResponse> FunctionHandler(Message[] sqsMessages, ILambdaContext context)
    {
        context.Logger.LogInformation($"Received event: {JsonSerializer.Serialize(sqsMessages)}");
        context.Logger.LogInformation($"sqsMessages[0]: {sqsMessages[0].Body}");
        var customMessage = Newtonsoft.Json.JsonConvert.DeserializeObject<dynamic>(sqsMessages[0].Body);
        context.Logger.LogInformation($"customMessage:{customMessage}");
        if(customMessage==null) throw new Exception("customMessage was null!");
        var id=Convert.ToString(customMessage.detail.id); // ID from the inner message, NOT the event!
        context.Logger.LogInformation($"id:{id}");
    
        var item=await dynamoDbClient.GetItemAsync(
            Environment.GetEnvironmentVariable("CLAIM_CHECK_TABLE"),
            new Dictionary<string, AttributeValue>()
            {
                {"id", new AttributeValue(id)},
            }
        );
        //var customJsonMessage=item.Item["custom_message_json"];
        //context.Logger.LogInformation($"customJsonMessage from DynamoDB:{customJsonMessage}]");
        context.Logger.LogInformation($"item from DynamoDB:{JsonSerializer.Serialize(item)}]");
        return item;
    }
}
