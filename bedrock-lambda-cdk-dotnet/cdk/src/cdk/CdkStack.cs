using Amazon.CDK;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Lambda.EventSources;
using Amazon.CDK.AWS.Logs;
using Amazon.CDK.AWS.S3;
using Constructs;

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
                Statements = new[]
                {
                    new PolicyStatement(new PolicyStatementProps
                    {
                        Effect = Effect.ALLOW,
                        Actions = new[] { "bedrock:InvokeModel" },
                        Resources = new[] { $"arn:aws:bedrock:{this.Region}::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0" }
                    })
                }
            });

            var lambdaIAMRole = new Role(this, "BedrockLambdaRole", new RoleProps
            {
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com"),
                Description = "IAM Role for the Lambda function",
                ManagedPolicies = new[]
                {
                        ManagedPolicy.FromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"),
                        invokeModelPolicy
                }
            });

            bucket.GrantReadWrite(lambdaIAMRole);

            _ = new LogGroup(this, "CloudWatchLogs", new LogGroupProps
            {
                LogGroupName = $"/aws/lambda/{lambdaFunctionName}",
                RemovalPolicy = RemovalPolicy.DESTROY,
                Retention = RetentionDays.ONE_DAY
            });

            var buildOption = new BundlingOptions()
            {
                Image = Runtime.DOTNET_8.BundlingImage,
                User = "root",
                OutputType = BundlingOutput.ARCHIVED,
                Command = new string[]{
               "/bin/sh",
                "-c",
                " dotnet tool install -g Amazon.Lambda.Tools"+
                " && dotnet build"+
                " && dotnet lambda package --output-package /asset-output/function.zip"
                }
            };

            _ = new Function(this, "BedrockFunction", new FunctionProps
            {
                FunctionName = lambdaFunctionName,
                MemorySize = 512,
                Timeout = Duration.Seconds(30),
                Runtime = Runtime.DOTNET_8,
                Handler = "BedrockLambda::BedrockLambda.Function::FunctionHandler",
                Role = lambdaIAMRole,
                Code = Code.FromAsset("../BedrockLambda/", new Amazon.CDK.AWS.S3.Assets.AssetOptions
                {
                    Bundling = buildOption
                }),
                Events = new[] {new S3EventSource(bucket, new S3EventSourceProps
                {
                    Events = new[] { EventType.OBJECT_CREATED },
                    Filters = [
                        new NotificationKeyFilter { Prefix = "input/" },
                        new NotificationKeyFilter { Suffix = ".jpg" },
                        new NotificationKeyFilter { Suffix = ".png" }
                    ]
                })}
            });
        }
    }
}