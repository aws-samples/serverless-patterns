using Amazon.Lambda.Core;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Serialization.SystemTextJson;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace lambda;

public class Function
{
    private const string envBucketName = "BUCKET_NAME";
    private const string envQueryStringKey = "QUERYSTRING_KEY";
    private const string responseForKeyNotFound = "Object key not found in the request";


    IAmazonS3 S3Client { get; set; }

    /// <summary>
    /// Default constructor. This constructor is used by Lambda to construct the instance. When invoked in a Lambda environment
    /// the AWS credentials will come from the IAM role associated with the function and the AWS region will be set to the
    /// region the Lambda function is executed in.
    /// </summary>
    public Function()
    {
        S3Client = new AmazonS3Client();
    }

    /// <summary>
    /// Constructs an instance with a preconfigured S3 client. This can be used for testing the outside of the Lambda environment.
    /// </summary>
    /// <param name="s3Client"></param>
    public Function(IAmazonS3 s3Client)
    {
        this.S3Client = s3Client;
    }

    /// <summary>
    /// This method is called for every Lambda invocation. This method takes in an S3 event object and can be used 
    /// to respond to S3 notifications.
    /// </summary>
    /// <param name="evnt"></param>
    /// <param name="context"></param>
    /// <returns></returns>
    public APIGatewayProxyResponse FunctionHandler(APIGatewayProxyRequest apirequest, ILambdaContext context)
    {
        var bucketName = Environment.GetEnvironmentVariable(envBucketName);
        var objectKey = apirequest.QueryStringParameters != null && apirequest.QueryStringParameters.ContainsKey(Environment.GetEnvironmentVariable(envQueryStringKey)) ?
                                    apirequest.QueryStringParameters[Environment.GetEnvironmentVariable(envQueryStringKey)] : string.Empty;
        context.Logger.Log(bucketName);

        try
        {
            if (!string.IsNullOrWhiteSpace(objectKey))
            {
                //Checking for Key Exists - if not throw error
                var file_response = S3Client.GetObjectMetadataAsync(bucketName, objectKey);
                context.Logger.LogInformation(file_response.Result.HttpStatusCode.ToString());
                context.Logger.Log(string.Join(Environment.NewLine, apirequest.QueryStringParameters));

                var request = new GetPreSignedUrlRequest()
                {
                    BucketName = bucketName,
                    Key = objectKey,
                    Expires = DateTime.UtcNow.AddMinutes(1),
                };

                return new APIGatewayProxyResponse()
                {
                    StatusCode = 200,
                    Body = S3Client.GetPreSignedURL(request)
                };
            }
            else
            {
                return new APIGatewayProxyResponse()
                {
                    StatusCode = 404,
                    Body = responseForKeyNotFound
                };
            }
        }
        catch (Exception e)
        {
            return new APIGatewayProxyResponse()
                {
                    StatusCode = 500,
                    Body = "Make sure the key exist in your bucket"
                };
            context.Logger.LogInformation("Error getting signedURL. Make sure the key exist in your bucket.");
            context.Logger.LogInformation(e.Message);
            context.Logger.LogInformation(e.StackTrace);
        }
    }
}
