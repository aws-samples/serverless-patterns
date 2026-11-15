using Amazon.Lambda.Core;
using Amazon.Lambda.S3Events;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.Textract;
using Amazon.Textract.Model;
using System.Net;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace TextractLambda;

public class Function
{
    private static readonly AmazonTextractClient _textractClient = new();
    private static readonly AmazonS3Client _s3Client = new();

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
                var response = await _textractClient.DetectDocumentTextAsync(new DetectDocumentTextRequest
                {
                    Document = new Document
                    {
                        S3Object = new Amazon.Textract.Model.S3Object
                        {
                            Bucket = bucketName,
                            Name = objectKey
                        }
                    }
                });

                context.Logger.LogInformation(response.ResponseMetadata.ToString());

                var rawText = ExtractText(response.Blocks, "LINE"); // Change "LINE" to "WORD" for word-level extraction
                context.Logger.LogInformation(string.Join("\n", rawText));
                var outputKey = $"output/{objectKey.Split('/').Last()}_{Guid.NewGuid():N}.txt";
                await _s3Client.PutObjectAsync(new PutObjectRequest
                {
                    BucketName = bucketName,
                    Key = outputKey,
                    ContentBody = string.Join("\n", rawText)
                });

                context.Logger.LogInformation("Document processed successfully!");
            }
            catch (Exception e)
            {
                context.Logger.LogError(e.Message);
                context.Logger.LogError(e.StackTrace);
                throw;
            }
        }
    }

    private static List<string> ExtractText(List<Block> blocks, string blockType)
    {
        var text = new List<string>();
        foreach (var block in blocks)
        {
            if (block.BlockType == blockType)
            {
                text.Add(block.Text);
            }
        }
        return text;
    }
}