using System.Text.Json;
using Amazon.Lambda;
using Amazon.Lambda.Core;
using Amazon.Lambda.Model;
using Amazon.Lambda.S3Events;

namespace ImageProcessor;

/// <summary>
/// Thin trigger function invoked by S3 event notifications.
/// Extracts bucket/key from the S3 event and invokes the durable image processor.
/// </summary>
internal sealed class S3TriggerHandler
{
    private static readonly IAmazonLambda LambdaClient = new AmazonLambdaClient();

    private static readonly string ImageProcessorFunctionArn =
        System.Environment.GetEnvironmentVariable("IMAGE_PROCESSOR_FUNCTION_ARN")
        ?? throw new InvalidOperationException("IMAGE_PROCESSOR_FUNCTION_ARN environment variable is not set.");

    public async Task Handler(S3Event s3Event, ILambdaContext context)
    {
        foreach (var record in s3Event.Records)
        {
            var bucket = record.S3.Bucket.Name;
            var key = record.S3.Object.Key;

            context.Logger.LogInformation($"Processing S3 event: s3://{bucket}/{key}");

            var payload = JsonSerializer.Serialize(new { Bucket = bucket, Key = key });

            await LambdaClient.InvokeAsync(new InvokeRequest
            {
                FunctionName = $"{ImageProcessorFunctionArn}:$LATEST",
                InvocationType = InvocationType.Event,
                Payload = payload
            });

            context.Logger.LogInformation($"Durable execution started for s3://{bucket}/{key}");
        }
    }
}
