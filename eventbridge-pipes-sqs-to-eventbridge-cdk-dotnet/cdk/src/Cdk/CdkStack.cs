namespace Cdk
{
    using System.Collections.Generic;

    using Amazon.CDK;
    using Amazon.CDK.AWS.Events;
    using Amazon.CDK.AWS.IAM;
    using Amazon.CDK.AWS.Pipes;
    using Amazon.CDK.AWS.SQS;

    using Constructs;

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
            var target = new EventBus(
                this,
                "TargetEventBus");

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
                                Resources = new[] { target.EventBusArn },
                                Actions = new[] { "events:PutEvents" },
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
                        { "TargetPolicy", targetPolicy }
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
                            BatchSize = 5,
                            MaximumBatchingWindowInSeconds = 120
                        }
                    },
                    Target = target.EventBusArn,
                    TargetParameters = new CfnPipe.PipeTargetParametersProperty
                    {
                        EventBridgeEventBusParameters = new CfnPipe.PipeTargetEventBridgeEventBusParametersProperty
                        {
                            Source = "myapp.orders",
                            DetailType = "OrderCreated",
                        },
                        InputTemplate = @"{
                            ""orderId"": ""<$.body.orderId>"",
                            ""customerId"": ""<$.body.customerId>""
                        }"
                    }
                });

            var outputQueueName = new CfnOutput(
                this,
                "QueueNameOutput",
                new CfnOutputProps()
                {
                    ExportName = "QueueName",
                    Value = source.QueueUrl
                });
        }
    }
}