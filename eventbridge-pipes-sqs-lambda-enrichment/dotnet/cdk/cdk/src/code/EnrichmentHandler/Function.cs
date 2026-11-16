using System;
using System.Text.Json;
using System.Threading.Tasks;
using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace EnrichmentHandler
{
    using System.Collections.Generic;

    using Amazon.Lambda.SQSEvents;

    public class Function
    {
        public Function()
        {
        }

        public async Task<List<EnrichedData>> FunctionHandler(List<SQSEvent.SQSMessage> messageInput)
        {
            var output = new List<EnrichedData>(messageInput.Count);

            foreach (var input in messageInput)
            {
                var message = JsonSerializer.Deserialize<InputMessage>(input.Body);
                
                output.Add(new EnrichedData($"Hello, {message.Name}", "Some enriched data"));
            }

            return output;
        }
    }
}
