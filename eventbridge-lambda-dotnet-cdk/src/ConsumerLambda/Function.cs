using System;
using System.Text.Json;
using Amazon.Lambda.CloudWatchEvents;
using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace ConsumerLambda
{
    public class Function
    {
        public void FunctionHandler(CloudWatchEvent<object> input, ILambdaContext context)
        {
            var payloadModel = JsonSerializer.Serialize(input);
            Console.WriteLine($"Input:..{payloadModel}");
        }
    }
}
