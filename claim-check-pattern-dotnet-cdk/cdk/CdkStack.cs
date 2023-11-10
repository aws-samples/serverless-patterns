using System.Collections.Generic;
using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.Events;
using Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Logs;
using Amazon.CDK.AWS.Pipes;
using Amazon.CDK.AWS.SQS;
using Amazon.CDK.AWS.StepFunctions;
using Constructs;
using EventBus = Amazon.CDK.AWS.Events.EventBus;
using EventBusProps = Amazon.CDK.AWS.Events.EventBusProps;
using LogGroupProps = Amazon.CDK.AWS.Logs.LogGroupProps;

namespace Cdk
{
    /*
     * This stack contains the resources used to demo a Serverless .NET implementation of the Claim Check Pattern.
     *
     * From a high level, this stack creates resources to fulfill the following demo:
     *
     * -> A) Generation of large payloads.
     *       A Lambda function generates "large" messages and puts them on a queue for processing.
     *
     * -> B) We want to use these messages in our Event-Driven Architecture, but we don't want to send all data via our Event Bus.
     *       To solve this, an Event Bridge Pipe consumes the incoming messages and uses an enrichment step to split messages
     *       into claim checks, stored in DynamoDB. When done, the smaller claim check message is published on the Event Bus.
     *
     * -> C) Now, we want to process a claim check in a Step Function workflow. However, the workflow needs the full message
     *       in order to do its processing. To solve this, we send the claim check to another SQS queue, which is consumed
     *       by an Event Bridge Pipe. The Pipe uses a Lambda enrichment step to resolve the full message based on the claim check,
     *       before sending the full message as input to the target workflow.
     */
    public class CdkStack : Stack
    {
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Storage
            var claimCheckTable = CreateTable();

            // Queues
            var (sampleDataWriteQueue, sampleProcessorInputQueue) = CreateQueues();

            // Workflows
            var targetWorkflow = CreateWorkflow();

            // Lambda functions
            var (claimCheckSplitLambda, claimCheckRetrievalLambda) = CreateFunctions(sampleDataWriteQueue, claimCheckTable);

            // Event Bus and Rules
            var claimCheckApplicationBus = CreateEventBus();
            CreateRules(claimCheckApplicationBus, sampleProcessorInputQueue);

            // Event Bridge Pipes
            CreatePipes(
                sampleProcessorInputQueue,
                sampleDataWriteQueue,
                claimCheckApplicationBus,
                targetWorkflow,
                claimCheckRetrievalLambda,
                claimCheckSplitLambda);
        }

        /// <summary>
        /// Creates the DynamoDB table used to store the mapping between claim checks and full messages.
        /// </summary>
        private Table CreateTable()
        {
            var claimCheckTable = new Table(this, "ClaimCheckTable", new TableProps
            {
                BillingMode = BillingMode.PAY_PER_REQUEST,
                TableName = "ClaimCheckTable",
                PartitionKey = new Attribute
                {
                    Name = "id",
                    Type = AttributeType.STRING
                },
                RemovalPolicy = RemovalPolicy.DESTROY
            });
            return claimCheckTable;
        }

        /// <summary>
        /// Creates the Step Functions workflow that is the end target of the full message.
        /// </summary>
        private StateMachine CreateWorkflow()
        {
            var workflow = new StateMachine(this, "ClaimCheckTargetWorkflow", new StateMachineProps
            {
                TracingEnabled = true,
                Logs = new LogOptions
                {
                    Destination = new LogGroup(this, "ClaimCheckTargetWorkflowLogGroup", new LogGroupProps
                    {
                        LogGroupName = "/aws/stepFunctions/ClaimCheckWorkflow",
                        RemovalPolicy = RemovalPolicy.DESTROY,
                        Retention = RetentionDays.ONE_WEEK
                    }),
                    Level = LogLevel.ALL
                },
                StateMachineName = "ClaimCheckTargetWorkflow",
                DefinitionBody = new ChainDefinitionBody(new Pass(this, "Process Message"))
            });
            return workflow;
        }

        /// <summary>
        /// Creates the rules for our custom event bus.
        /// </summary>
        private void CreateRules(IEventBus claimCheckApplicationBus, IQueue sampleProcessorInputQueue)
        {
            // This rule logs all messages to demonstrate that only claim checks are passed on the event bus.
            _ = new Rule(this, "ClaimCheckApplicationBusRule", new RuleProps
            {
                RuleName = "ClaimCheckApplicationBusRule",
                EventBus = claimCheckApplicationBus,
                EventPattern = new EventPattern
                {
                    // Match all events
                    Source = Match.Prefix("")
                },
                Targets = new IRuleTarget[]
                {
                    new CloudWatchLogGroup(new LogGroup(this, "ClaimTargetLog", new LogGroupProps
                    {
                        LogGroupName = "/aws/eventBus/rules/targets/ClaimCheckTargetLog",
                        RemovalPolicy = RemovalPolicy.DESTROY,
                        Retention = RetentionDays.ONE_WEEK
                    }))
                }
            });

            // This rule sends all events to the input processing queue.
            _ = new Rule(this, "SampleProcessorInputQueueRule", new RuleProps
            {
                RuleName = "SampleProcessorInputQueueRule",
                EventBus = claimCheckApplicationBus,
                EventPattern = new EventPattern
                {
                    // Match all events
                    Source = Match.Prefix("")
                },
                Targets = new IRuleTarget[]
                {
                    new SqsQueue(sampleProcessorInputQueue)
                }
            });
        }

        /// <summary>
        /// Creates the pipes for claim check split and retrieval.
        /// </summary>
        private void CreatePipes(
            IQueue sampleProcessorInputQueue,
            IQueue sampleDataWriteQueue,
            IEventBus claimCheckApplicationBus,
            IStateMachine targetWorkflow,
            IFunction claimCheckRetrievalLambda,
            IFunction claimCheckSplitLambda)
        {
            /*
             * Pipe: Claim Check Split
             *
             * -> 1) Source....: SQS sample data write queue (full messages).
             * -> 2) Enrichment: Full message sent to Lambda for claim check split (uses DynamoDB as storage).
             * -> 3) Target....: Claim check sent to Event Bus.
             */
            var claimCheckSplitPipeRole = new Role(this, "ClaimCheckSplitPipeRole", new RoleProps
            {
                AssumedBy = new ServicePrincipal("pipes.amazonaws.com"),
            });
            _ = new CfnPipe(this, "ClaimCheckSplitPipe", new CfnPipeProps
            {
                RoleArn = claimCheckSplitPipeRole.RoleArn,
                Source = sampleDataWriteQueue.QueueArn,
                Target = claimCheckApplicationBus.EventBusArn,
                Enrichment = claimCheckSplitLambda.FunctionArn,
                SourceParameters = new CfnPipe.PipeSourceParametersProperty
                {
                    SqsQueueParameters = new CfnPipe.PipeSourceSqsQueueParametersProperty
                    {
                        BatchSize = 1
                    }
                },
                Name = "ClaimCheckSplitPipe"
            });
            sampleDataWriteQueue.GrantConsumeMessages(claimCheckSplitPipeRole);
            claimCheckSplitLambda.GrantInvoke(claimCheckSplitPipeRole);
            claimCheckApplicationBus.GrantPutEventsTo(claimCheckSplitPipeRole);

            /*
             * Pipe: Claim Check Retrieval
             *
             * -> 1) Source....: SQS input processing queue (claim check message).
             * -> 2) Enrichment: Claim check sent to Lambda for enrichment.
             * -> 3) Target....: Full message sent to workflow.
             */
            var claimCheckEnrichmentPipeRole = new Role(this, "ClaimCheckEnrichmentPipeRole", new RoleProps
            {
                AssumedBy = new ServicePrincipal("pipes.amazonaws.com"),
            });
            _ = new CfnPipe(this, "ClaimCheckEnrichmentPipe", new CfnPipeProps
            {
                RoleArn = claimCheckEnrichmentPipeRole.RoleArn,
                Source = sampleProcessorInputQueue.QueueArn,
                Target = targetWorkflow.StateMachineArn,
                Enrichment = claimCheckRetrievalLambda.FunctionArn,
                SourceParameters = new CfnPipe.PipeSourceParametersProperty
                {
                    SqsQueueParameters = new CfnPipe.PipeSourceSqsQueueParametersProperty
                    {
                        BatchSize = 1
                    }
                },
                TargetParameters = new CfnPipe.PipeTargetParametersProperty
                {
                    StepFunctionStateMachineParameters = new CfnPipe.PipeTargetStateMachineParametersProperty
                    {
                        InvocationType = $"{ServiceIntegrationPattern.FIRE_AND_FORGET}"
                    }
                },
                Name = "ClaimCheckEnrichmentPipe"
            });
            sampleProcessorInputQueue.GrantConsumeMessages(claimCheckEnrichmentPipeRole);
            targetWorkflow.GrantStartExecution(claimCheckEnrichmentPipeRole);
            claimCheckRetrievalLambda.GrantInvoke(claimCheckEnrichmentPipeRole);
        }

        /// <summary>
        /// Create the SQS queues used for processing of data.
        /// </summary>
        private (IQueue sampleDataWriteQueue, IQueue sampleProcessorInputQueue) CreateQueues()
        {
            // Queue for sample data (full messages) to processed.
            var sampleDataWriteQueueDlq = new Queue(this, "SampleDataWriteQueueDLQ", new QueueProps
            {
                EnforceSSL = true,
                QueueName = "SampleDataWriteQueueDLQ"
            });
            var sampleDataWriteQueue = new Queue(this, "SampleDataWriteQueue", new QueueProps
            {
                EnforceSSL = true,
                DeadLetterQueue = new DeadLetterQueue
                {
                    MaxReceiveCount = 1,
                    Queue = sampleDataWriteQueueDlq
                },
                QueueName = "SampleDataWriteQueue"
            });

            // Queue for claim checks to be processed.
            var sampleProcessorInputQueueDlq = new Queue(this, "SampleProcessorInputQueueDLQ", new QueueProps
            {
                EnforceSSL = true,
                QueueName = "SampleProcessorInputQueueDLQ"
            });
            var sampleProcessorInputQueue = new Queue(this, "SampleProcessorInputQueue", new QueueProps
            {
                EnforceSSL = true,
                DeadLetterQueue = new DeadLetterQueue
                {
                    MaxReceiveCount = 1,
                    Queue = sampleProcessorInputQueueDlq,
                },
                QueueName = "SampleProcessorInputQueue"
            });

            return (sampleDataWriteQueue, sampleProcessorInputQueue);
        }

        /// <summary>
        /// Create the custom Event Bus.
        /// </summary>
        private IEventBus CreateEventBus()
        {
            return new EventBus(this, "ClaimCheckApplicationBus", new EventBusProps
            {
                EventBusName = "ClaimCheckApplicationBus"
            });
        }

        /// <summary>
        /// Create the .NET Lambda functions used for
        /// 1/ generating sample data,
        /// 2/ splitting full messages into claim checks and for
        /// 3/ retrieving a full message based on a claim check.
        /// </summary>
        private (IFunction claimCheckSplitLambda, IFunction claimCheckRetrievalLambda) CreateFunctions(IQueue sampleDataWriteQueue, ITable claimCheckTable)
        {
            const string lambdaBinPath = "../lambda/bin/Debug/net6.0";

            // Lambda for generation of sample data
            var claimCheckSampleDataCreatorLambda = new Function(this, "ClaimCheckSampleDataCreatorLambda", new FunctionProps
            {
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset(lambdaBinPath),
                Handler = "ClaimCheckPattern::ClaimCheckPattern.ClaimCheckDataCreator::FunctionHandler",
                Environment = new Dictionary<string, string>(1)
                {
                    {"QUEUE_URL", sampleDataWriteQueue.QueueUrl}
                },
                Timeout = Duration.Seconds(15),
                FunctionName = "ClaimCheckSampleDataCreatorLambda",
                LogRetention = RetentionDays.ONE_WEEK
            });
            sampleDataWriteQueue.GrantSendMessages(claimCheckSampleDataCreatorLambda);

            // Lambda for splitting a full message into a claim check
            var claimCheckSplitLambda = new Function(this, "ClaimCheckSplitLambda", new FunctionProps
            {
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset(lambdaBinPath),
                Handler = "ClaimCheckPattern::ClaimCheckPattern.ClaimCheckSplitter::FunctionHandler",
                Environment = new Dictionary<string, string>(1)
                {
                    {"CLAIM_CHECK_TABLE", claimCheckTable.TableName}
                },
                Timeout = Duration.Seconds(15),
                FunctionName = "ClaimCheckSplitLambda",
                LogRetention = RetentionDays.ONE_WEEK
            });
            claimCheckTable.GrantWriteData(claimCheckSplitLambda);

            // Lambda for retrieving a full message from a claim check
            var claimCheckRetrievalLambda = new Function(this, "ClaimCheckRetrievalLambda", new FunctionProps
            {
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset(lambdaBinPath),
                Handler = "ClaimCheckPattern::ClaimCheckPattern.ClaimCheckRetriever::FunctionHandler",
                Environment = new Dictionary<string, string>(1)
                {
                    {"CLAIM_CHECK_TABLE", claimCheckTable.TableName}
                },
                Timeout = Duration.Seconds(15),
                FunctionName = "ClaimCheckRetrievalLambda",
                LogRetention = RetentionDays.ONE_WEEK
            });
            claimCheckTable.GrantReadData(claimCheckRetrievalLambda);

            return new(claimCheckSplitLambda, claimCheckRetrievalLambda);
        }
    }
}
