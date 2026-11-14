using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Constructs;

namespace Cdk
{
    public class CdkStack : Stack
    {
        private string executionRoleName = "DockerImageFunction-execution-role";
        private string functionName = "DockerImageFunction";

        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Create Lambda execution role
            Role lambdaExecutionRole = new Role(this, "DockerImageFunction-execution-role", new RoleProps
            {
                RoleName = executionRoleName,
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com")
            });

            // Add AWS Managed Policies
            // The below permissions are used only for DEVELOPMENT purpose and should not be used for PRODUCTION purpose.
            // Best practice is to use LEAST privilege
            lambdaExecutionRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("AWSLambda_FullAccess"));
            lambdaExecutionRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"));


            // Create a Lambda function
            DockerImageCode dockerImageCode = DockerImageCode.FromImageAsset("code/src/AWSLamdaDemo");
            DockerImageFunction dockerImageFunction = new DockerImageFunction(this, "DockerImageFunction", new DockerImageFunctionProps
            {
                FunctionName = functionName,
                Code = dockerImageCode,
                Role = lambdaExecutionRole,
                Timeout = Duration.Seconds(30),
                MemorySize = 256
            });

            // Defines an API Gateway REST API resource backed by our lambda function.
            new LambdaRestApi(this, "Endpoint", new LambdaRestApiProps
            {
                Handler = dockerImageFunction
            });
        }
    }
}