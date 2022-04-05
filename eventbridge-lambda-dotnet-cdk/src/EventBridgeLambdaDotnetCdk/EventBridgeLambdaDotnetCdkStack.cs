using Amazon.CDK;
using Amazon.CDK.AWS.Events;
using Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Logs;
using AssetOptions = Amazon.CDK.AWS.S3.Assets.AssetOptions;
using Constructs;
using EventBus = Amazon.CDK.AWS.Events.EventBus;
using EventBusProps = Amazon.CDK.AWS.Events.EventBusProps;
using LogGroupProps = Amazon.CDK.AWS.Logs.LogGroupProps;

namespace EventBridgeLambdaDotnetCdk
{
    public class EventBridgeLambdaDotnetCdkStack : Stack
    {
        internal EventBridgeLambdaDotnetCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // EventBridge Event Bus
            var eventBus = new EventBus(this, "MyEventBus", new EventBusProps
            {
                EventBusName = "MyEventBus"
            });
            
            // EventBridge Rule
            var consumerLambdaRule = new Rule(this, "ConsumerLambdaRule", new RuleProps
            {
                Description = "Consumer Lambda Event Bus Rule",
                EventPattern = new EventPattern
                {
                    Source = new[] { "cdk.myapp" }
                },
                EventBus = eventBus
            });
            
            // Lambda Function Build Commands
            var buildCommands = new[]
            {
                "cd /asset-input",
                "export DOTNET_CLI_HOME=\"/tmp/DOTNET_CLI_HOME\"",
                "export PATH=\"$PATH:/tmp/DOTNET_CLI_HOME/.dotnet/tools\"",
                "dotnet tool install -g Amazon.Lambda.Tools",
                "dotnet lambda package -o output.zip",
                "unzip -o -d /asset-output output.zip"
            };
            
            // Lambda Function
            var consumerLambdaHandler = new Function(this, "ConsumerLambda", new FunctionProps
            {
                MemorySize = 128,
                Timeout = Duration.Seconds(10),
                Runtime = Runtime.DOTNET_CORE_3_1,
                Code = Code.FromAsset("src/ConsumerLambda", new AssetOptions
                {
                    Bundling = new BundlingOptions
                    {
                        Image  = Runtime.DOTNET_CORE_3_1.BundlingImage,
                        Command = new []
                        {
                            "bash", "-c", string.Join(" && ", buildCommands)
                        }
                    }
                }),
                Handler = "ConsumerLambda::ConsumerLambda.Function::FunctionHandler"
            });
            
            // Set Lambda Logs Retention and Removal Policy
            new LogGroup(this, "ConsumerLambdaLogs", new LogGroupProps
            {
                LogGroupName = $"/aws/lambda/{consumerLambdaHandler.FunctionName}",
                RemovalPolicy = RemovalPolicy.DESTROY,
                Retention = RetentionDays.ONE_DAY
            });

            consumerLambdaRule.AddTarget(new LambdaFunction(consumerLambdaHandler));
        }
    }
}
