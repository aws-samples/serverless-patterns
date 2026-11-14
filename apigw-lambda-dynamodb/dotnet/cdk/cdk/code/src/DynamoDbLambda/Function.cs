using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace DynamoDbLambda
{
    public class Function
    {
        private readonly AmazonDynamoDBClient _dynamoDbClient;

        public Function()
        {
            this._dynamoDbClient = new AmazonDynamoDBClient();
        }

        public async Task<APIGatewayProxyResponse> FunctionHandler(APIGatewayProxyRequest request, ILambdaContext context)
        {
            await this._dynamoDbClient.PutItemAsync(Environment.GetEnvironmentVariable("TABLE_NAME"),
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
}
