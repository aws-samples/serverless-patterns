using Amazon.Lambda.Core;
using Amazon.SecretsManager.Model;
using Amazon.SecretsManager;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace SecretsManagerLambda;

public class Function
{
    public async Task<string> FunctionHandler(string input, ILambdaContext context)
    {
        var secretValue = await GetSecret();
        context.Logger.LogInformation($"Received {secretValue} from Secrets Manager");
        return "success";
    }

    static async Task<string> GetSecret()
    {
        string secretName = Environment.GetEnvironmentVariable("SECRET_KEY");
        IAmazonSecretsManager client = new AmazonSecretsManagerClient();
        GetSecretValueRequest request = new GetSecretValueRequest
        {
            SecretId = secretName,
            VersionStage = "AWSCURRENT", // VersionStage defaults to AWSCURRENT if unspecified.
        };

        GetSecretValueResponse response;

        try
        {
            response = await client.GetSecretValueAsync(request);
        }
        catch (Exception e)
        {
            // For a list of the exceptions thrown, see
            // https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            throw e;
        }

        return response.SecretString;

        // Your code goes here
    }
}
