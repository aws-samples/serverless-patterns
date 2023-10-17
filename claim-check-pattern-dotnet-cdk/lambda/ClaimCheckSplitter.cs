using System;
using System.Collections.Generic;
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
    public async Task<APIGatewayProxyResponse> FunctionHandler(APIGatewayProxyRequest request, ILambdaContext context)
    {
        context.Logger.LogInformation("Version 0.0.3");
        await dynamoDbClient.PutItemAsync(Environment.GetEnvironmentVariable("TABLE_NAME"),
        new Dictionary<string, AttributeValue>()
        {
            {"PK", new AttributeValue("1")},
            {"SK", new AttributeValue(DateTime.Now.ToString("yyyyMMddHHmmss"))}
        });

        return new APIGatewayProxyResponse()
        {
            StatusCode = 201
        };
    }
}
