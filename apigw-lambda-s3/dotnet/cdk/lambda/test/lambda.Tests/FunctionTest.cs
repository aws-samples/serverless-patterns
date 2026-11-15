using Xunit;
using Amazon.Lambda.Core;
using Amazon.Lambda.TestUtilities;
using Amazon.Lambda.APIGatewayEvents;
using Moq;
using Amazon.S3;

namespace lambda.Tests;

public class FunctionTest
{
    [Fact]
    public void TestToUpperFunction()
    {

        Environment.SetEnvironmentVariable("BUCKET_NAME", "test-bucket");
        Environment.SetEnvironmentVariable("QUERYSTRING_KEY", "key");

        var mock = new Mock<IAmazonS3>();
        mock.Setup(s => s.GetObjectMetadataAsync("test-bucket", "value", It.IsAny<CancellationToken>()))
            .ReturnsAsync(new Amazon.S3.Model.GetObjectMetadataResponse { HttpStatusCode = System.Net.HttpStatusCode.OK });
        mock.Setup<string>(s => s.GetPreSignedURL(It.IsAny<Amazon.S3.Model.GetPreSignedUrlRequest>()))
            .Returns("hello");

        // Invoke the Lambda function and confirm it returns the presigned URL.
        var function = new Function(mock.Object);
        var context = new TestLambdaContext();
        var request = new APIGatewayProxyRequest();
        request.QueryStringParameters = new Dictionary<string, string>();
        request.QueryStringParameters.Add("key","value");
        var casing = function.FunctionHandler(request, context);

        Console.Write(casing.Body);

        Assert.Equal(200, casing.StatusCode);
        Assert.Equal("hello", casing.Body);
        mock.Verify(s => s.GetPreSignedURL(It.IsAny<Amazon.S3.Model.GetPreSignedUrlRequest>()), Times.Once);
    }
}