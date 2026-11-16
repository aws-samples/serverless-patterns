using Amazon.Lambda.Core;
using Amazon.S3;
using Amazon.S3.Model;
using CallbackPatternSample.Models;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace storeTaskTokenFunction;

public class Function
{
    AmazonS3Client s3Client;
    public Function()
    {
        s3Client = new AmazonS3Client();
    }
    public class Payload
    {
        public Order? Input { get; set; }
        public string? TaskToken { get; set; }
    }

    // Store token into s3 storage
    public async Task<Order?> FunctionHandler(Payload input, ILambdaContext context)
    {
        PutObjectRequest request = new PutObjectRequest();
        request.BucketName = Environment.GetEnvironmentVariable("TokenStoreBucket");
        request.Key = input.Input?.OrderId.ToString();
        request.ContentBody = input.TaskToken;
        await s3Client.PutObjectAsync(request);
        return input.Input;
    }
}
