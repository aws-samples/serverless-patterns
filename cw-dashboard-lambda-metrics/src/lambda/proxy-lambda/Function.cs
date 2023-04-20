using Amazon.Lambda.Core;
using AWS.Lambda.Powertools.Metrics;
using System.Text.Json;
using RestSharp;


// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace proxy_lambda;

public class inputModel{
    public string requestUrl {get; set;}
}

public class Function
{

    /// <summary>
    /// A simple function that takes a string and does a ToUpper
    /// </summary>
    /// <param name="input"></param>
    /// <param name="context"></param>
    /// <returns></returns>
    [Metrics(Namespace = "MyDotNetApp", Service = "ProxyCall")]
    public string FunctionHandler(inputModel input, ILambdaContext context)
    {
        context.Logger.LogInformation(input.requestUrl);
        Metrics.AddMetric("Proxy-Request", 1, MetricUnit.Count);
        var options = new RestClientOptions(input.requestUrl)
        {
            MaxTimeout = -1,
        };
        var client = new RestClient(options);
        var request = new RestRequest();
        RestResponse response = client.ExecuteAsync(request).Result;
        if (response.IsSuccessStatusCode)
        {
            Metrics.AddMetric("Proxy-Successful", 1, MetricUnit.Count);
        }
        return string.IsNullOrWhiteSpace(response.Content) ? "No content recieved for the request" : response.Content;
    }
}
