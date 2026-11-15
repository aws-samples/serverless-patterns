using Amazon.Lambda.Core;
using Amazon.Lambda.S3Events;
using Amazon.S3;
using AWS.Lambda.Powertools.Logging;
using AWS.Lambda.Powertools.Metrics;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace LambdaFileProcessor; 

public class S3Function
{
    IAmazonS3 S3Client { get; set; }

    /// <summary>
    /// Default constructor. This constructor is used by Lambda to construct the instance. When invoked in a Lambda environment
    /// the AWS credentials will come from the IAM role associated with the function and the AWS region will be set to the
    /// region the Lambda function is executed in.
    /// </summary>
    public S3Function()
    {
        S3Client = new AmazonS3Client();
    }

    /// <summary>
    /// Constructs an instance with a preconfigured S3 client. This can be used for testing the outside of the Lambda environment.
    /// </summary>
    /// <param name="s3Client"></param>
    public S3Function(IAmazonS3 s3Client)
    {
        this.S3Client = s3Client;
    }

    /// <summary>
    /// This method is called for every Lambda invocation. This method takes in an S3 event object and can be used 
    /// to respond to S3 notifications.
    /// </summary>
    /// <param name="evnt">The S3 event containing the bucket name and object key</param>
    /// <param name="context">Context object that contains information about the invocation, function, and execution environment</param>
    /// <returns></returns>
    [Logging(LogEvent = true)]
    [Metrics(CaptureColdStart = true, Namespace = "lambda-file-processor")]
    public async Task<string?> FunctionHandler(S3Event evnt, ILambdaContext context)
    {
        Logger.LogInformation("Made it in FunctionHandler()");

        var s3Event = evnt.Records?[0].S3;
        if (s3Event == null)
        {
            return null;
        }

        try
        {
            var response = await this.S3Client.GetObjectMetadataAsync(s3Event.Bucket.Name, s3Event.Object.Key);

            // Create a custom metric to track the number of files processed. 
            Metrics.AddMetric("Processed File", 1, MetricUnit.Count);

            // Write log
            Logger.LogInformation($"Finished processing object {s3Event.Object.Key} from bucket {s3Event.Bucket.Name}");

            return response.Headers.ContentType;
        }
        catch (Exception e)
        {
            Logger.LogInformation($"Error getting object {s3Event.Object.Key} from bucket {s3Event.Bucket.Name}. Make sure they exist and your bucket is in the same region as this function.");
            Logger.LogInformation(e.Message);
            Logger.LogInformation(e.StackTrace);
            throw;
        }
    }
}