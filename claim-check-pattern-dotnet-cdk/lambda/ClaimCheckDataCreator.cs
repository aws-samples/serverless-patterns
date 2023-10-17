using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.SQS;

namespace ServerlessPatterns.ClaimCheck;

public class ClaimCheckDataCreator
{
    private static readonly AmazonSQSClient sqsClient = new AmazonSQSClient();    
    public async Task FunctionHandler(object inputEvent, ILambdaContext context)
    {
        context.Logger.LogInformation("ClaimCheckDataCreator called.");
        var queueUrl=Environment.GetEnvironmentVariable("QUEUE_URL");
        var messageWithManyDetails = new {
            id=Guid.NewGuid().ToString(),
            source= "systemA",
            customer=new {
                first_name="John",
                middle_names="Michael Frankie",
                last_name="Doe"
            },
            data=new {
                someDummyData1="someDummyData1",
                someDummyData2="someDummyData2",
                someDummyData3="someDummyData3"
            }
        };

        context.Logger.LogInformation("Putting message on queue...");
        await sqsClient.SendMessageAsync(queueUrl, JsonSerializer.Serialize(messageWithManyDetails));
        context.Logger.LogInformation("Message put on queue.");
    }
}
