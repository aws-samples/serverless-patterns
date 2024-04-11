using Amazon.BedrockRuntime;
using Amazon.BedrockRuntime.Model;
using Amazon.Lambda.Core;
using Amazon.Lambda.S3Events;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.Util;
using System.IO;
using System.Net;
using System.Text.Json;
using System.Text.Json.Nodes;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace BedrockLambda;

public class Function
{
    private static readonly AmazonBedrockRuntimeClient bedrockClient = new();
    private static readonly AmazonS3Client s3Client = new();
    private const string claudeModelId = "anthropic.claude-3-sonnet-20240229-v1:0";
    private const string prompt = "Read all the information present in this image. give me in the data only in json";

    public async Task FunctionHandler(S3Event evnt, ILambdaContext context)
    {
        context.Logger.LogInformation("Lambda function started");
        var eventRecords = evnt.Records ?? new List<S3Event.S3EventNotificationRecord>();

        foreach (var record in eventRecords)
        {
            var s3Event = record.S3;
            if (s3Event == null)
            {
                continue;
            }

            try
            {
                var bucketName = s3Event.Bucket.Name;
                var objectKey = WebUtility.UrlDecode(s3Event.Object.Key);//Object key name are in URL-encoded format.
                context.Logger.LogInformation($"Document ready to process. BucketName : {bucketName} ObjectKey {objectKey}");

                var imageBytes = await GetObjectAsync(bucketName, objectKey);

                var extractedText = await InvokeModelAsync(prompt, imageBytes);
                context.Logger.LogInformation(extractedText);

                await PutObjectAsync(bucketName, objectKey, extractedText);

                context.Logger.LogInformation("Document extracted successfully!");

            }
            catch (Exception e)
            {
                context.Logger.LogError(e.Message);
                context.Logger.LogError(e.StackTrace);
                throw;
            }
        }
    }

    private static async Task<byte[]> GetObjectAsync(string bucketName, string objectKey) 
    {
        var response = await s3Client.GetObjectAsync(bucketName, objectKey);
        return await response.ResponseStream.ToByteArray();
    }

    private static async Task PutObjectAsync(string bucketName, string objectKey, string text)
    {
        var outputKey = $"output/{objectKey.Split('/').Last()}_{Guid.NewGuid():N}.txt";
        await s3Client.PutObjectAsync(new PutObjectRequest
        {
            BucketName = bucketName,
            Key = outputKey,
            ContentBody = text
        });
    }

    private static async Task<string> InvokeModelAsync(string prompt, byte[] imageBytes)
    {
        var requestBody = new JsonObject
        {
            ["anthropic_version"] = "bedrock-2023-05-31",
            ["max_tokens"] = 1000,
            ["messages"] = new JsonArray
            {
                new JsonObject
                {
                             ["role"] = "user",
                             ["content"] = new JsonArray
                             {
                                 new JsonObject
                                 {
                                     ["type"] = "image",
                                     ["source"] = new JsonObject
                                     {
                                         ["type"] = "base64",
                                         ["media_type"] = "image/png",
                                         ["data"] = Convert.ToBase64String(imageBytes)
                                     }
                                 },
                                 new JsonObject
                                 {
                                     ["type"] = "text",
                                     ["text"] = prompt
                                 }
                             }
                         }
            }
        };

        var response = await bedrockClient.InvokeModelAsync(new InvokeModelRequest()
        {
            ModelId = claudeModelId,
            Body = AWSSDKUtils.GenerateMemoryStreamFromString(requestBody.ToJsonString()),
            ContentType = "application/json",
            Accept = "application/json"
        });

        if (response != null && response.HttpStatusCode == HttpStatusCode.OK)
        {
            var contentJson = await JsonNode.ParseAsync(response.Body);
            var content = contentJson?["content"];
            return content?[0]["text"]?.GetValue<string>();
        }

        throw new Exception("InvokeModelAsync failed with status code " + response?.HttpStatusCode);
    }
}