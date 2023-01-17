using System.Collections.Generic;

using Amazon.CDK;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Pipes;
using Amazon.CDK.AWS.SQS;

using Constructs;
using XaasKit.CDK.AWS.Lambda.DotNet;
using Function = Amazon.CDK.AWS.Lambda.Function;
using FunctionProps = Amazon.CDK.AWS.Lambda.FunctionProps;
using AssetOptions = Amazon.CDK.AWS.S3.Assets.AssetOptions;
using BundlingOptions = Amazon.CDK.BundlingOptions;

namespace Cdk
{
    public class CdkStack : Stack
    {
        internal CdkStack(
            Construct scope,
            string id,
            IStackProps props = null) : base(
            scope,
            id,
            props)
        {
            var source = new Queue(
                this,
                "SourceSQSQueue");
            
            var target = new Queue(
                this,
                "TargetSQSQueue");

            var sourcePolicy = new PolicyDocument(
                new PolicyDocumentProps
                {
                    Statements = new[]
                    {
                        new PolicyStatement(
                            new PolicyStatementProps
                            {
                                Resources = new[] { source.QueueArn },
                                Actions = new[] { "sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueAttributes" },
                                Effect = Effect.ALLOW
                            })
                    }
                });

            var targetPolicy = new PolicyDocument(
                new PolicyDocumentProps
                {
                    Statements = new[]
                    {
                        new PolicyStatement(
                            new PolicyStatementProps
                            {
                                Resources = new[] { target.QueueArn },
                                Actions = new[] { "sqs:SendMessage", "sqs:GetQueueAttributes" },
                                Effect = Effect.ALLOW
                            })
                    }
                });
            
            var buildCommands = new[]
            {
                "cd /asset-input",
                "export DOTNET_CLI_HOME=\"/tmp/DOTNET_CLI_HOME\"",
                "export PATH=\"$PATH:/tmp/DOTNET_CLI_HOME/.dotnet/tools\"",
                "dotnet tool install -g Amazon.Lambda.Tools",
                "dotnet publish -c Release -o /asset-output"
            };

            var lambdaHandlerRole = new Role(this, "DynamoDbHandlerRole", new RoleProps()
            {
                RoleName = "DynamoDbHandlerRole",
                Description = "Role assumed by the DynamoDbLambdaFunction",
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com"),
            });

            var handler = new DotNetFunction(this, "EnrichmentHandler", new DotNetFunctionProps()
            {
                Runtime =Runtime.DOTNET_6,
                Timeout = Duration.Seconds(30),
                ProjectDir = "code/src/EnrichmentHandler",
                Handler = "EnrichmentHandler::EnrichmentHandler.Function::FunctionHandler",
                Role = lambdaHandlerRole
            });

            var enrichmentPolicy = new PolicyDocument(
                new PolicyDocumentProps
                {
                    Statements = new[]
                    {
                        new PolicyStatement(
                            new PolicyStatementProps
                            {
                                Resources = new[] { handler.FunctionArn },
                                Actions = new[] { "lambda:InvokeFunction" },
                                Effect = Effect.ALLOW
                            })
                    }
                });

            var pipeRole = new Role(
                this,
                "PipeRole",
                new RoleProps
                {
                    AssumedBy = new ServicePrincipal("pipes.amazonaws.com"),
                    InlinePolicies = new Dictionary<string, PolicyDocument>(2)
                    {
                        { "SourcePolicy", sourcePolicy },
                        { "TargetPolicy", targetPolicy },
                        { "EnrichmentPolicy", enrichmentPolicy },
                    }
                });

            var pipe = new CfnPipe(
                this,
                "Pipe",
                new CfnPipeProps
                {
                    RoleArn = pipeRole.RoleArn,
                    Source = source.QueueArn,
                    SourceParameters = new CfnPipe.PipeSourceParametersProperty()
                    {
                        SqsQueueParameters = new CfnPipe.PipeSourceSqsQueueParametersProperty
                        {
                            BatchSize = 1,
                            MaximumBatchingWindowInSeconds = 10
                        }
                    },
                    Target = target.QueueArn,
                    TargetParameters = new CfnPipe.PipeTargetParametersProperty
                    {
                        SqsQueueParameters = new CfnPipe.PipeTargetSqsQueueParametersProperty()
                        {
                        }
                    },
                    Enrichment = handler.FunctionArn,
                    EnrichmentParameters = new CfnPipe.PipeEnrichmentParametersProperty()
                    {
                        
                    }
                });

            var outputQueueName = new CfnOutput(
                this,
                "QueueUrlOutput",
                new CfnOutputProps()
                {
                    ExportName = "QueueUrlOutput",
                    Value = source.QueueName
                });
        }
    }
}