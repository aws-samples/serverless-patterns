using Amazon.CDK;
using Constructs;
using System.Collections.Generic;


using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Events;
using Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.Pipes;
using Amazon.CDK.AWS.SQS;

using Function = Amazon.CDK.AWS.Lambda.Function;
using FunctionProps = Amazon.CDK.AWS.Lambda.FunctionProps;
using EventBus = Amazon.CDK.AWS.Events.EventBus;

namespace MyCdk
{
    /// <summary>
    /// Source SQS Queue - Pipe - 1. SourceSQSQueue 2. Pipe
    /// </summary>
    public class MyCdkStack : Stack
    {

        internal MyCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // The code that defines your stack goes here
            //source SQS
            var source = new Queue(
               this,
               "SourceSQSQueue");
            //Target lambda consumer
            var targetLambdaHandler = new Function(this,
              "targetLambda",
              new FunctionProps
              {
                  FunctionName = "ApiHandler",
                  Runtime = Runtime.DOTNET_6,
                  Code = Code.FromAsset("src/lambda-api/api.zip"),
                  Handler = "lambdaapi::lambdaapi.Function::FunctionHandler",
                  Timeout = Duration.Seconds(30),
              });
            
            //Event bus to get messages from source SQS through pipe and push to targetLambda and targetSQS
            var targetEventBus = new EventBus(
                this,
                "TargetEventBus");
            //policy for pushing events to EventBridge by pipe
            var targetPolicyeb = new PolicyDocument(
               new PolicyDocumentProps
               {
                   Statements = new[]
                   {
                        new PolicyStatement(
                            new PolicyStatementProps
                            {
                                Resources = new[] { targetEventBus.EventBusArn },
                                Actions = new[] { "events:PutEvents" },
                                Effect = Effect.ALLOW
                            })
                   }
               });
            // EventBridge Rule for pushing message to Lambda
            var consumerLambdaRule = new Rule(this, "ConsumerLambdaRule", new RuleProps
            {
                Description = "Consumer Lambda Event Bus Rule",
                EventPattern = new EventPattern
                {
                    Source = new[] { "cdk.myapp" }
                },
                EventBus = targetEventBus
            });

            //target consumer SQS
            var targetQ = new Queue(
               this,
               "TargetSQSQueue");

            // EventBridge Rule 
            var consumerSQSRule = new Rule(this, "ConsumerSQSRule", new RuleProps
            {
                Description = "Consumer SQS Rule",
                EventPattern = new EventPattern
                {
                    Source = new[] { "cdk.myapp" }
                },
                EventBus = targetEventBus
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
                                Resources = new[] { targetEventBus.EventBusArn },
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
                        { "targetPolicy", targetPolicy },
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
                        }
                   
                    },
                    Target = targetEventBus.EventBusArn,
                    TargetParameters = new CfnPipe.PipeTargetParametersProperty
                    {
                        EventBridgeEventBusParameters = new CfnPipe.PipeTargetEventBridgeEventBusParametersProperty
                        {
                            Source = "cdk.myapp",
                            DetailType = "transaction",
                        },
                        InputTemplate = @"{
                             ""DetailType"": ""<$.body.DetailType>"",
                             ""Source"": ""<$.body.Source>"",
                             ""Region"": ""<$.body.Region>""
                         }"

                    }

                    

                });
            consumerLambdaRule.AddTarget(new LambdaFunction(targetLambdaHandler));
            consumerSQSRule.AddTarget(new SqsQueue(targetQ));
        }
    }
    
}
