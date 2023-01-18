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
using Amazon.CDK.AWS.Logs;

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
            
            var lambdaHandlerRole = new Role(this, "EnrichmentHandlerRole", new RoleProps()
            {
                RoleName = "EnrichmentHandlerRole",
                Description = "Role assumed by the EnrichmentHandlerRole",
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com"),
            });

            // Define a Lambda function to use for enrichment
            // The Lambda function needs to be pre-compiled and package before running 'cdk deploy'
            var handler = new Function(this,
                "EnrichmentHandler",
                new FunctionProps
            {
                FunctionName = "EnrichmentHandler",
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset("../cdk/src/code/EnrichmentHandler/output.zip"),
                Handler = "EnrichmentHandler::EnrichmentHandler.Function::FunctionHandler",
                Role = lambdaHandlerRole,
                Timeout = Duration.Seconds(30),
            });

            // A policy for pipes to use that allows read from SQS.
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

            // A policy for pipes to use that allows messages to be sent to SQS
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

            // A policy for pipes to use that allows Lambda invoke
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

            // Create the pipe
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