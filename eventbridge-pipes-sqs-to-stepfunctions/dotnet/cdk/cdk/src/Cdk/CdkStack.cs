using System.Collections.Generic;

using Amazon.CDK;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Pipes;
using Amazon.CDK.AWS.SQS;
using Amazon.CDK.AWS.StepFunctions;

using Constructs;

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

            var mapState = new Map(
                this,
                "LoopMessages",
                new MapProps()
                {
                    ItemsPath = JsonPath.EntirePayload,
                });
            mapState.Iterator(
                new Wait(
                    this,
                    "WaitState",
                    new WaitProps()
                    {
                        Time = WaitTime.Duration(Duration.Seconds(10)),
                    }));

            var stepFunction = new StateMachine(
                this,
                "TargetStepFunction",
                new StateMachineProps()
                {
                    Definition = mapState,
                    StateMachineType = StateMachineType.STANDARD
                });

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
                                Resources = new[] { stepFunction.StateMachineArn },
                                Actions = new[] { "states:StartExecution" },
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
                    Target = stepFunction.StateMachineArn,
                    TargetParameters = new CfnPipe.PipeTargetParametersProperty
                    {
                        StepFunctionStateMachineParameters = new CfnPipe.PipeTargetStateMachineParametersProperty()
                        {
                            InvocationType = "FIRE_AND_FORGET"
                        }
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