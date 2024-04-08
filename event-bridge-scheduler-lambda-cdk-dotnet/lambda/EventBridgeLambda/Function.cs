using Amazon.Lambda.CloudWatchEvents;
using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace EventBridgeLambda;

public class Function
{
    /// <summary>
    ///  A simple function that triggers after scheduled time period & logs time of calling.
    /// </summary>
    /// <param name="input"></param>
    /// <param name="context"></param>
    public void FunctionHandler(CloudWatchEvent<object> input, ILambdaContext context)
    {
        context.Logger.LogInformation($"Amazon EventBridge Scheduler triggered at : {input.Time} ");
    }
}
