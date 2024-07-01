using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using AWS.Lambda.Powertools.Logging;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace LambdaAuthorizer;

public class AuthorizerFunction
{

    /// <summary>
    /// Authorize HTTP request by looking at the Authorization header 
    /// </summary>
    /// <param name="input">The event for the Lambda function handler to process.</param>
    /// <param name="context">The ILambdaContext that provides methods for logging and describing the Lambda environment.</param>
    /// <returns></returns>
    [Logging(LogEvent = true)]
    public APIGatewayCustomAuthorizerResponse FunctionHandler(APIGatewayCustomAuthorizerRequest request, ILambdaContext context)
    {
        Logger.LogInformation("Made it in S3 authorizer FunctionHandler()");

        // Custom Authorization logic 
        string effect = request.AuthorizationToken == "mytesttoken" ? "Allow" : "Deny";

        // Allow both the PUT and GET operations in the policy document. 
        // Sameple request.MethodArn values for the GET or PUT methods
        //  arn:aws:execute-api:us-east-1:123456789012:oph8mlur0b/prod/GET/s3
        //  arn:aws:execute-api:us-east-1:123456789012:oph8mlur0b/prod/PUT/s3
        var authResponse = new APIGatewayCustomAuthorizerResponse()
        {
            PrincipalID = "auth-user",
            PolicyDocument = new APIGatewayCustomAuthorizerPolicy()
            {
                Statement = new List<APIGatewayCustomAuthorizerPolicy.IAMPolicyStatement>
            {
                new APIGatewayCustomAuthorizerPolicy.IAMPolicyStatement()
                {
                    Effect =  effect,
                    Resource = new HashSet<string> { request.MethodArn.Replace("/PUT/", "/GET/"), request.MethodArn.Replace("/GET/","/PUT/") },
                    Action = new HashSet<string> { "execute-api:Invoke" }
                }
            }
            }
        };

        Logger.LogInformation(authResponse);
        return authResponse;
    }
}
