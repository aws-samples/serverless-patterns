using System.Collections.Generic;

using Amazon.CDK;
using Amazon.CDK.AWS.Events;
using EventTargets = Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.IoT;
using Amazon.CDK.AWS.IoT.Alpha;
using Amazon.CDK.AWS.IoT.Actions.Alpha;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Logs;
using Constructs;
using AssetOptions = Amazon.CDK.AWS.S3.Assets.AssetOptions;

namespace Net6BundlingZipFileLambdaCdk
{
    public class Net6LambdaCdkStack : Stack
    {
        internal Net6LambdaCdkStack(Constructs.Construct scope, 
            string id,
            IStackProps props = null) : base(scope, id, props)
        {
            IEnumerable<string> commands = new[]
            {
                "cd /asset-input",
                "export XDG_DATA_HOME=\"/tmp/DOTNET_CLI_HOME\"",
                "export DOTNET_CLI_HOME=\"/tmp/DOTNET_CLI_HOME\"",
                "export PATH=\"$PATH:/tmp/DOTNET_CLI_HOME/.dotnet/tools\"",
                "dotnet tool install -g Amazon.Lambda.Tools",
                "dotnet lambda package -o output.zip",
                "unzip -o -d /asset-output output.zip"
            };

            var lambdaHandlerRole = new Role(this, "lambdaHandlerRole", new RoleProps()
            {
                RoleName = "LambdaHandlerRole",
                Description = "Role assumed by the LambdaFunction",
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com"),
            });

            var func = new Function(this,
                "zip-lambda-function",
                new FunctionProps
            {
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset("../Lambda", new AssetOptions
                {
                    Bundling = new BundlingOptions
                    {
                      Image  = Runtime.DOTNET_6.BundlingImage,
                      Command = new []
                      {
                          "bash", "-c", string.Join(" && ", commands)
                      }
                    }
                }),
                Handler = "Lambda::Lambda.Function::FunctionHandler"

            });

            new CfnThing(this, "MyIotThing", new CfnThingProps { ThingName = "MyIotThing" });


            var iotTopicRule = new TopicRule(this, "TopicRule", new TopicRuleProps
            {
                TopicRuleName = "MyTopicRule",  // optional
                Description = "invokes the lambda function",  // optional
                Sql = IotSql.FromStringAsVer20160323("SELECT * FROM 'MyIotThing'"),
                Actions = new[] { new LambdaFunctionAction(func) }
            });

            func.AddPermission("GrantIotRule", new Permission { Principal = new ServicePrincipal("iot.amazonaws.com"), SourceArn = iotTopicRule.TopicRuleArn });

        }

    }
}
