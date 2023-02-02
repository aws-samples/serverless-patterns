using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.Lambda;
using Constructs;
using AssetOptions = Amazon.CDK.AWS.S3.Assets.AssetOptions;

namespace Cdk
{
    public class CdkStack : Stack
    {
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

            // Lambda Function
            var dotnetCoreWebApiLambdaHandler = new Function(this, "DotnetCoreWebApiLambda", new FunctionProps
            {
                MemorySize = 512,
                Timeout = Duration.Seconds(30),
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
                })
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
