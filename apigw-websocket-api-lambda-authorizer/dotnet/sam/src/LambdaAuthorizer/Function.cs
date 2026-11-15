using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using AWS.Lambda.Powertools.Logging;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace LambdaAuthorizer;

public class Function
{
    public const string AWS_REGION = "AWS_REGION";
    public const string COGNITO_USER_POOL_ID = "COGNITO_USER_POOL_ID";
    public const string COGNITO_USER_POOL_CLIENT_ID = "COGNITO_USER_POOL_CLIENT_ID";

    [Logging(LogEvent = true)]
    public async Task<APIGatewayCustomAuthorizerResponse> LambdaAuthorizerHandler(APIGatewayCustomAuthorizerRequest request, ILambdaContext context)
    {
        try
        {
            string? userPoolId = Environment.GetEnvironmentVariable(COGNITO_USER_POOL_ID);
            string? clientId = Environment.GetEnvironmentVariable(COGNITO_USER_POOL_CLIENT_ID);
            string? region = Environment.GetEnvironmentVariable(AWS_REGION);

            if (string.IsNullOrEmpty(userPoolId))
            {
                throw new ArgumentException($"Missing ENV variable: {COGNITO_USER_POOL_ID}");
            }

            if (string.IsNullOrEmpty(clientId))
            {
                throw new ArgumentException($"Missing ENV variable: {COGNITO_USER_POOL_CLIENT_ID}");
            }

            if (string.IsNullOrEmpty(region))
            {
                throw new ArgumentException($"Missing ENV variable: {AWS_REGION}");
            }

            // 1. retrieve the id_token from the query string
            var id_token = request.QueryStringParameters.FirstOrDefault(item => item.Key.Equals("id_token", StringComparison.OrdinalIgnoreCase));
            if (id_token.Value == null)
            {
                throw new ArgumentException($"Missing id_token querystring parameter");
            }

            // 2. validate the incoming token against cognito userpool and clientId
            var claimPrincipal = await new CognitoJwtVerifier(userPoolId, clientId, region).ValidateTokenAsync(id_token.Value);


            // 3. either claimPrincipal is recieved (not null) or an exception is thrown in case of invalid token
            if (claimPrincipal != null)
            {
                string cogntioUserId = claimPrincipal.Claims.First(t => t.Type == "cognito:username").Value;
                return GenerateAllow(cogntioUserId, request.MethodArn);
            }

            // 4. most likely, won't be executed (but keep it on the safer side)
            return GenerateDeny("default", request.MethodArn);
        }
        catch (Exception ex)
        {
            Logger.LogError(ex);

            return GenerateDeny("default", request.MethodArn);
        }
    }

    private APIGatewayCustomAuthorizerResponse GenerateAllow(string principalId, string resource)
    {
        return GeneratePolicy(principalId, "Allow", resource);
    }

    private APIGatewayCustomAuthorizerResponse GenerateDeny(string principalId, string resource)
    {
        return GeneratePolicy(principalId, "Deny", resource);
    }

    private APIGatewayCustomAuthorizerResponse GeneratePolicy(string principalId, string effect, string resource)
    {
        var policyDocument = new APIGatewayCustomAuthorizerPolicy()
        {
            Version = "2012-10-17",
            Statement = new List<APIGatewayCustomAuthorizerPolicy.IAMPolicyStatement>()
                {
                    new APIGatewayCustomAuthorizerPolicy.IAMPolicyStatement()
                    {
                        Action = new HashSet<string>(){"execute-api:Invoke"},
                        Effect = effect,
                        Resource = new HashSet<string>(){resource}
                    }
                }
        };

        var response = new APIGatewayCustomAuthorizerResponse()
        {
            PrincipalID = principalId,
            PolicyDocument = policyDocument,
            Context = new APIGatewayCustomAuthorizerContextOutput()
                {
                    {"cognitoUserId", principalId}
                }
        };

        return response;
    }

}
