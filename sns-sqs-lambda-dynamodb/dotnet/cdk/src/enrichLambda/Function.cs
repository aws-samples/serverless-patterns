using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.Core;
using Amazon.Lambda.SQSEvents;
using Amazon.SQS;
using Amazon.SQS.Model;
using enrichLambda.model;
using RestSharp;
using System.Text.Json;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace enrichLambda;

public class Function
{
    private readonly AmazonDynamoDBClient dynamoDbClient;
    private readonly AmazonSQSClient amazonSQSClient;

    public Function()
    {
        this.dynamoDbClient = new AmazonDynamoDBClient();
        this.amazonSQSClient = new AmazonSQSClient(Amazon.RegionEndpoint.USEast1);
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
        var gitUser = new GitUser();
        context.Logger.LogInformation(message.Body);
        var body = JsonSerializer.Deserialize<MessageParse>(message.Body);
        gitUser = JsonSerializer.Deserialize<GitUser>(body.Message);
        context.Logger.LogInformation(gitUser.login);
        context.Logger.LogInformation(gitUser.type);

        var client = new RestClient($"https://api.github.com/users/{gitUser.login}");
        var request = new RestRequest();
        request.Method = Method.Get;
        var apiCall = client.Execute(request);

        var apiResponse = apiCall.Content;
        context.Logger.LogInformation(apiResponse);

        if (apiCall.StatusCode == System.Net.HttpStatusCode.OK)
        {
            
            var messagerequest = new SendMessageRequest
            {
                QueueUrl = Environment.GetEnvironmentVariable("ENRICH_QUEUE"),
                MessageBody = apiResponse
            };


            await amazonSQSClient.SendMessageAsync(messagerequest);

            gitUser = JsonSerializer.Deserialize<GitUser>(apiResponse);


            await this.dynamoDbClient.PutItemAsync(Environment.GetEnvironmentVariable("TABLE_NAME"),
                     new Dictionary<string, AttributeValue>()
                     {
                    {"login", new AttributeValue(gitUser.login)},
                    {"datatype", new AttributeValue("enriched")},
                    {"id", new AttributeValue(gitUser.id.ToString()) },
                    {"node_id", new AttributeValue(gitUser.node_id) },
                    {"avatar_url", new AttributeValue(gitUser.avatar_url) },
                    //{"gravatar_id",  new AttributeValue(gitUser.gravatar_id) },
                    {"url",  new AttributeValue(gitUser.url) },
                    {"html_url", new AttributeValue(gitUser.html_url) },
                    {"followers_url", new AttributeValue(gitUser.followers_url) },
                    {"following_url", new AttributeValue(gitUser.following_url) },
                    {"gists_url", new AttributeValue(gitUser.gists_url) },
                    {"starred_url", new AttributeValue(gitUser.starred_url) },
                    {"subscriptions_url", new AttributeValue(gitUser.subscriptions_url) },
                    {"organizations_url", new AttributeValue(gitUser.organizations_url) },
                    {"repos_url", new AttributeValue(gitUser.repos_url) },
                    {"events_url", new AttributeValue(gitUser.events_url) },
                    {"received_events_url", new AttributeValue(gitUser.received_events_url) },
                    {"type", new AttributeValue(gitUser.type) },
                    {"site_admin", new AttributeValue(gitUser.site_admin.ToString()) },
                    {"name", new AttributeValue(gitUser.name) },
                    //{"company", new AttributeValue(gitUser.company) },
                    {"blog", new AttributeValue(gitUser.blog) },
                    //{"location", new AttributeValue(gitUser.location) },
                    //{"email", new AttributeValue(gitUser.email) },
                    //{"hireable", new AttributeValue(gitUser.hireable) },
                    //{"bio", new AttributeValue(gitUser.bio) },
                    //{"twitter_username", new AttributeValue(gitUser.twitter_username) },
                    {"public_repos", new AttributeValue(gitUser.public_repos.ToString()) },
                    {"public_gists", new AttributeValue(gitUser.public_gists.ToString()) },
                    {"followers", new AttributeValue(gitUser.followers.ToString()) },
                    {"following", new AttributeValue(gitUser.following.ToString()) },
                    {"created_at", new AttributeValue(gitUser.created_at.ToString()) },
                    {"updated_at", new AttributeValue(gitUser.updated_at.ToString()) },
                     });
        }
        else
        {
            context.Logger.LogError($"Error while calling API for {gitUser.login}");
        }
    }
}
