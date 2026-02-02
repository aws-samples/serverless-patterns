using Amazon.CDK;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.S3;
using Constructs;
using System.Net.Sockets;
using AssetOptions = Amazon.CDK.AWS.S3.Assets.AssetOptions;
using Amazon.CDK.AWS.Lambda.EventSources;

namespace S3Lambda
{
    public class S3LambdaStack : Stack
    {
        internal S3LambdaStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var bucket = new Bucket(this, "MyFirstBucket", new BucketProps
            {
                Versioned = true
            });

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
            var function = new Function(this, "lambda", new FunctionProps
            {
                MemorySize = 512,
                Timeout = Duration.Seconds(30),
                Runtime = Runtime.DOTNET_6,
                Handler = "lambda::lambda.Function::FunctionHandler",
                Code = Code.FromAsset("src\\lambda\\src\\lambda", new AssetOptions
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
                Events = new[] {new S3EventSource(bucket, new S3EventSourceProps
                {
                    Events = new[] { EventType.OBJECT_CREATED}                    
                })}

            });
        }
    }
}
