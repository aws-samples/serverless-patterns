using Amazon.CDK;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Lambda.EventSources;
using Amazon.CDK.AWS.Logs;
using Amazon.CDK.AWS.S3;
using Constructs;
using XaasKit.CDK.AWS.Lambda.DotNet;

namespace Cdk
{
    public class CdkStack : Stack
    {
        private const string lambdaFunctionName = "bedrockLambdaFunction";

        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var bucket = new Bucket(this, "bedrock-bucket", new BucketProps
            {
                BucketName = $"{this.Account}-bedrock-bucket"
            });

            var invokeModelPolicy = new ManagedPolicy(this, "InvokeModelPolicy", new ManagedPolicyProps
            {
                ManagedPolicyName = "InvokeModelPolicy",
                Statements =
                [
                    new PolicyStatement(new PolicyStatementProps
                    {
                        Effect = Effect.ALLOW,
                        Actions = [ "bedrock:InvokeModel" ],
                        Resources = [ $"arn:aws:bedrock:{this.Region}::foundation-model/anthropic.claude-3-haiku-20240307-v1:0"]
                    })
                ]
            });

            var lambdaIAMRole = new Role(this, "BedrockLambdaRole", new RoleProps
            {
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com"),
                Description = "IAM Role for the Lambda function",
                ManagedPolicies =
                [
                        ManagedPolicy.FromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"),
                        invokeModelPolicy
                ]
            });

            bucket.GrantReadWrite(lambdaIAMRole);

            _ = new LogGroup(this, "CloudWatchLogs", new LogGroupProps
            {
                LogGroupName = $"/aws/lambda/{lambdaFunctionName}",
                RemovalPolicy = RemovalPolicy.DESTROY,
                Retention = RetentionDays.ONE_DAY
            });

            //XaasKit.CDK.AWS.Lambda.DotNet this CDK module are experimental and under active development.
            //https://github.com/cdklabs/awscdk-lambda-dotnet
            _ = new DotNetFunction(
            this,
            id,
            new DotNetFunctionProps()
            {
                FunctionName = lambdaFunctionName,
                MemorySize = 512,
                Timeout = Duration.Seconds(30),
                Runtime = Runtime.DOTNET_8,
                Handler = "BedrockLambda::BedrockLambda.Function::FunctionHandler",
                LogRetention = RetentionDays.ONE_DAY,
                Role = lambdaIAMRole,
                ProjectDir = "../BedrockLambda/",
                Events = [
                    new S3EventSource(bucket, new S3EventSourceProps(){
                        Events = [ EventType.OBJECT_CREATED ],
                        Filters = [
                            new NotificationKeyFilter { Prefix = "input/" },
                            new NotificationKeyFilter { Suffix = ".jpg" }
                            ]
                    }),
                    new S3EventSource(bucket, new S3EventSourceProps(){
                        Events = [ EventType.OBJECT_CREATED ],
                        Filters = [
                            new NotificationKeyFilter { Prefix = "input/" },
                            new NotificationKeyFilter { Suffix = ".png" }
                            ]
                    }),
                ]
            });
        }
    }
}