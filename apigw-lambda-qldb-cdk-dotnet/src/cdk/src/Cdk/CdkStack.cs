using System.Collections.Generic;
using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.QLDB;
using Constructs;
using AssetOptions = Amazon.CDK.AWS.S3.Assets.AssetOptions;

namespace Cdk
{
    public class CdkStack : Stack
    {
        const string ledgerName = "MyCdkLedgerName";
        const string functionName = "FunctionQLDBService";
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Lambda Function Build Commands
            var buildCommands = new[]
            {
                "rpm -Uvh https://packages.microsoft.com/config/centos/7/packages-microsoft-prod.rpm",
                "yum -y install aspnetcore-runtime-6.0",
                "cd /asset-input",
                "export DOTNET_CLI_HOME=\"/tmp/DOTNET_CLI_HOME\"",
                "export XDG_DATA_HOME=\"/tmp/DOTNET_CLI_HOME\"",
                "export PATH=\"$PATH:/tmp/DOTNET_CLI_HOME/.dotnet/tools\"",
                "dotnet tool install -g Amazon.Lambda.Tools",
                "dotnet lambda package -o output.zip",
                "unzip -o -d /asset-output output.zip"
            };
            // Create Lambda execution role
            var lambdaExecutionRole = new Role(this, functionName + "-execution-role", new RoleProps
            {
                RoleName = functionName + "-execution-role",
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com")
            });
            
            // Add AWS Managed Policies
            // Best practice is to provide least privilege access
            lambdaExecutionRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"));
            lambdaExecutionRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("AmazonQLDBFullAccess"));
            
            // Lambda Function
            var dotnetCoreWebApiLambdaHandler = new Function(this, "DotnetCoreWebApiLambda", new FunctionProps
            {
                MemorySize = 512,
                Timeout = Duration.Seconds(30),
                Environment = new Dictionary<string, string>(1)
                {
                    {"LEDGER_NAME",ledgerName}
                },
                Runtime = Runtime.DOTNET_6,
                Handler = "dotnet-core-web-api",
                Code = Code.FromAsset("../lambda/dotnet-core-web-api/dotnet-core-web-api", new AssetOptions  
                {
                    // Note: Asset path should point to the folder where .csproj file is present. Also,this path should be relative to cdk.json
                    Bundling = new BundlingOptions
                    {
                        Image = Runtime.DOTNET_6.BundlingImage,
                        Command = new[]
                        {
                            "bash", "-c", string.Join(" && ", buildCommands)
                        },
                        User = "root"
                    }
                }),
                Role = lambdaExecutionRole
            });
            
            new CfnLedger(this, "MyCfnLedger", new CfnLedgerProps {
                PermissionsMode = "STANDARD",
                // the properties below are optional
                DeletionProtection = false,
                Name = ledgerName
            });
            
            // API Gatewaty REST API
            var restApi = new LambdaRestApi(this, "restApi", new LambdaRestApiProps
            {
                Handler = dotnetCoreWebApiLambdaHandler,
                Proxy = true  // defines a greedy proxy ("{proxy+}")
            });
            
            // Output the API Gateway REST API Url
            new CfnOutput(this, "REST API Url", new CfnOutputProps
            {
                Value = restApi.Url,
                Description = "REST API endpoint URL"
            });
        }
    }
}
