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

        var mock = new Mock<IAmazonS3>();
        mock.Setup<string>(s => s.GetPreSignedURL(It.IsAny<Amazon.S3.Model.GetPreSignedUrlRequest>()))
            .Returns("hello");

        // Invoke the lambda function and confirm the string was upper cased.
        var function = new Function(mock.Object);
        var context = new TestLambdaContext();
        var request = new APIGatewayProxyRequest();
        request.QueryStringParameters = new Dictionary<string, string>();
        request.QueryStringParameters.Add("key","value");
        var casing = function.FunctionHandler(request, context);

        Console.Write(casing.Body);

        mock.Verify(s => s.GetPreSignedURL(It.IsAny<Amazon.S3.Model.GetPreSignedUrlRequest>()), Times.Once);
    }
}