using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.Core;
using Amazon.Lambda.SQSEvents;
using rawLambda.model;
using System.Text.Json;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace rawLambda;

public class Function
{
    private readonly AmazonDynamoDBClient _dynamoDbClient;

    public Function()
    {
        this._dynamoDbClient = new AmazonDynamoDBClient();
    }

    public async Task FunctionHandler(SQSEvent input, ILambdaContext context)
    {
        foreach (var message in input.Records)
        {
            await ProcessMessageAsync(message, context);
        }
    }

    private async Task ProcessMessageAsync(SQSEvent.SQSMessage message, ILambdaContext context)
    {
        context.Logger.LogInformation(message.Body);
        var body = JsonSerializer.Deserialize<MessageParse>(message.Body);
        var req = JsonSerializer.Deserialize<GitUser>(body.Message);
        context.Logger.LogInformation(req.login);

        await this._dynamoDbClient.PutItemAsync(Environment.GetEnvironmentVariable("TABLE_NAME"),
                new Dictionary<string, AttributeValue>()
                {
                    {"login", new AttributeValue(req.login)},
                    {"type", new AttributeValue(req.type)},
                    {"datatype", new AttributeValue("rawdata")}
                });
    }
}
