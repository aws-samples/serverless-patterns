using System;
using System.Text.Json;
using System.Threading.Tasks;
using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace EnrichmentHandler
{
    public class Function
    {
        public Function()
        {
        }

        public async Task<String> FunctionHandler(object request, ILambdaContext context)
        {
            context.Logger.LogLine(JsonSerializer.Serialize(request));
            
            return "Ok";
        }
    }
}
