using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Logs;
using Amazon.CDK.AWS.SecretsManager;
using Constructs;
using System.Collections.Generic;

namespace Cdk
{
    public class CdkStack : Stack
    {
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Setup VPC and Subnet 
            var vpc = new Vpc(this, "myvpc", new VpcProps
            {
                IpAddresses = IpAddresses.Cidr("10.0.0.0/16"),
                MaxAzs = 2, // use 2 availability zones
                NatGateways = 0, // don't create any nat gateways
                SubnetConfiguration = new[]
                {
                    new SubnetConfiguration
                    {
                        CidrMask = 24,
                        Name = "private",
                        SubnetType = SubnetType.PRIVATE_ISOLATED,
                    }
                }
            });

            // Setup Secrets Manager
            var secretKey = "MySecret";
            var secret = new Secret(this, "Secret", new SecretProps
            {
                SecretName = secretKey,
                SecretStringValue = new SecretValue("Welcome to serverlessland!"),
                Description = "Application secret value"
            });

            // Create a new Security Group
            var lambdaSecurityGroup = new SecurityGroup(this, "LambdaSecurityGroup", new SecurityGroupProps
            {
                SecurityGroupName = "MyLambdaSecurityGroup",
                Vpc = vpc,
                AllowAllOutbound = true,
            });

            // Create a new VPC endpoint for Secrets Manager
            var endpoint = new InterfaceVpcEndpoint(this, "SecretsManagerEndpoint", new InterfaceVpcEndpointProps
            {
                Service = new InterfaceVpcEndpointAwsService("secretsmanager"),
                Vpc = vpc,
                PrivateDnsEnabled = true,
                SecurityGroups = new[] { lambdaSecurityGroup },
                Subnets = new SubnetSelection { SubnetType = SubnetType.PRIVATE_ISOLATED },
            });

            // Create the inline policy
            var inlinePolicy = new Policy(this, "LambdaFunctionInlinePolicy", new PolicyProps
            {
                PolicyName = "AllowCreateNetworkInterface",
                Statements = new[]
                {
                    new PolicyStatement(new PolicyStatementProps
                    {
                        Effect = Effect.ALLOW,
                        Actions = new [] { "ec2:CreateNetworkInterface", "ec2:DescribeNetwork*", "ec2:DeleteNetworkInterface" },
                        Resources = new [] { "*" }
                    }),
                    new PolicyStatement(new PolicyStatementProps
                    {
                        Effect = Effect.ALLOW,
                        Actions = new [] { "secretsmanager:GetSecretValue" },
                        Resources = new [] { secret.SecretArn }
                    })
                }
            });
            //Lambda Function IAM role
            var lambdaIAMRole = new Role(this, "LambdaFunctionRole", new RoleProps
            {
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com"),
                Description = "IAM Role for the lambda function"
            });
            lambdaIAMRole.AttachInlinePolicy(inlinePolicy);

            // Lambda Function Build Commands
            var buildOption = new BundlingOptions()
            {
                Image = Runtime.DOTNET_6.BundlingImage,
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

            //Lambda function
            var lambdaFunctionName = "SecretsManagerLambdaFunction";
            var lambdaFunction = new Function(this, "LambdaFunction", new FunctionProps
            {
                FunctionName= lambdaFunctionName,
                MemorySize = 256,
                Timeout = Duration.Seconds(30),
                Runtime = Runtime.DOTNET_6,
                Handler = "SecretsManagerLambda::SecretsManagerLambda.Function::FunctionHandler",
                Role = lambdaIAMRole,
                Environment = new Dictionary<string, string>(1)
                {
                    {"SECRET_KEY", secretKey}
                },
                Code = Code.FromAsset("../lambda/SecretsManagerLambda/", new Amazon.CDK.AWS.S3.Assets.AssetOptions
                {
                    Bundling = buildOption
                }),
                Vpc = vpc,
                VpcSubnets = new SubnetSelection()
                {
                    SubnetType = SubnetType.PRIVATE_ISOLATED,
                },
                SecurityGroups = new[] { lambdaSecurityGroup },
            });

            // CloudWatch Log Group
            var cloudWatchLogGroup = new LogGroup(this, "CloudWatchLogs", new LogGroupProps
            {
                LogGroupName = $"/aws/lambda/{lambdaFunctionName}",
                RemovalPolicy = RemovalPolicy.DESTROY,
                Retention = RetentionDays.ONE_DAY
            });

            //Grant Cloudwatch permission
            cloudWatchLogGroup.GrantWrite(lambdaFunction);
        }
    }
}