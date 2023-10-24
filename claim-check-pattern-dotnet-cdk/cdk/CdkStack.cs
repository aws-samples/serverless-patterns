using System.Collections.Generic;
using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Constructs;
using Amazon.CDK.AWS.Events;
using Amazon.CDK.AWS.SQS;
using Amazon.CDK.AWS.StepFunctions;
using Amazon.CDK.AWS.Logs;
using LogGroupProps = Amazon.CDK.AWS.Logs.LogGroupProps;
using Amazon.CDK.AWS.Pipes;

namespace Cdk
{
    public class CdkStack : Stack
    {
        private const string tableName = "ClaimCheckTable";

        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {   
            var claimCheckTable=createTable();
            var queues=createQueues();
            var functions=createFunctions(queues.SampleDataWriteQueue, claimCheckTable);                        
            var targetWorkflow=createWorkflow();
            var claimCheckApplicationBus=createEventBus();
            createRules(claimCheckApplicationBus, queues.SampleProcessorInputQueue);
            createPipes(queues.SampleProcessorInputQueue, queues.SampleDataWriteQueue, claimCheckApplicationBus, targetWorkflow, functions.ClaimCheckRetrievalLambda, functions.ClaimCheckSplitLambda);
        }

        private StateMachine createWorkflow()
        {
            var name="ClaimCheckTargetWorkflow";
            var targetWorkflow = new StateMachine(this, name, new StateMachineProps {
                TracingEnabled= true,
                Logs = new LogOptions {
                    Destination= new LogGroup(this, "ClaimCheckTargetWorkflowLogGroup", new LogGroupProps {RemovalPolicy= RemovalPolicy.DESTROY, LogGroupName="/aws/stepFunctions/ClaimCheckWorkflow"}),
                    Level=LogLevel.ALL
                },
                StateMachineName=name,
                DefinitionBody=new ChainDefinitionBody(new Pass(this, "Process Message"))
            });
            return targetWorkflow;
        }

        private void createRules(EventBus claimCheckApplicationBus, Queue sampleProcessorInputQueue)
        {
            var target=new LogGroup(this, "ClaimTargetLog", new LogGroupProps {
                LogGroupName= "/aws/eventBus/rules/targets/claimCheckTargetLog",
                RemovalPolicy= RemovalPolicy.DESTROY,
            });
            var targets= new List<Amazon.CDK.AWS.Events.Targets.CloudWatchLogGroup> { new Amazon.CDK.AWS.Events.Targets.CloudWatchLogGroup(target) };
            // Send all events on claimCheckApplicationBusRule to CloudWatch Logs to demonstrate only ids are passed on bus        
            var claimCheckApplicationBusRule = new Rule(this, "ClaimCheckApplicationBusRule", new RuleProps {
                RuleName= "ClaimCheckApplicationBusRule",
                EventBus= claimCheckApplicationBus,
                EventPattern=new EventPattern {
                    Source=Match.AnythingBut("Blocked"),
                    //Source= Match.Prefix("")
                },
                Targets=targets.ToArray()
            });

            var sampleProcessorInputQueueRule = new Rule(this, "SampleProcessorInputQueueRule", new RuleProps {
                RuleName= "SampleProcessorInputQueueRule",
                EventBus=claimCheckApplicationBus,
                EventPattern=new EventPattern {
                    Source=Match.AnythingBut("Blocked"),
                    //Source= Match.Prefix("")
                },
                Targets=new List<Amazon.CDK.AWS.Events.Targets.SqsQueue>{new Amazon.CDK.AWS.Events.Targets.SqsQueue(sampleProcessorInputQueue)}.ToArray()
            });
        }

        private void createPipes(Queue sampleProcessorInputQueue, Queue sampleDataWriteQueue, EventBus claimCheckApplicationBus, StateMachine targetWorkflow, Function claimCheckRetrievalLambda, Function claimCheckSplitLambda)
        {           
            var splitPipeRole = new Role(this, "ClaimCheckSplitRole", new RoleProps {
                AssumedBy= new ServicePrincipal("pipes.amazonaws.com"),
            });

            var retrievalPipeRole = new Role(this, "ClaimCheckRetrievalRole", new RoleProps{
                AssumedBy= new ServicePrincipal("pipes.amazonaws.com"),
            });

            var name="ClaimCheckEnrichmentPipe";
            var claimCheckEnrichmentPipe = new CfnPipe(this, name, new CfnPipeProps {
                RoleArn=retrievalPipeRole.RoleArn,
                Source=sampleProcessorInputQueue.QueueArn,
                Target=targetWorkflow.StateMachineArn,
                Enrichment=claimCheckRetrievalLambda.FunctionArn,
                SourceParameters=new CfnPipe.PipeSourceParametersProperty()
                {
                    SqsQueueParameters=new CfnPipe.PipeSourceSqsQueueParametersProperty { BatchSize = 1 }
                },
                TargetParameters=new CfnPipe.PipeTargetParametersProperty {
                    StepFunctionStateMachineParameters=new CfnPipe.PipeTargetStateMachineParametersProperty { InvocationType= "FIRE_AND_FORGET" }
                },
                Name=name
            });

            name="ClaimCheckSplitPipe";
            var claimCheckSplitPipe = new CfnPipe(this, "ClaimCheckSplitPipe", new CfnPipeProps {
                RoleArn=splitPipeRole.RoleArn,
                Source=sampleDataWriteQueue.QueueArn,
                Target=claimCheckApplicationBus.EventBusArn,
                Enrichment=claimCheckSplitLambda.FunctionArn,
                SourceParameters=new CfnPipe.PipeSourceParametersProperty()
                {
                    SqsQueueParameters=new CfnPipe.PipeSourceSqsQueueParametersProperty { BatchSize = 1 }
                },
                Name=name
            });
            
            sampleDataWriteQueue.GrantConsumeMessages(splitPipeRole);
            claimCheckSplitLambda.GrantInvoke(splitPipeRole);
            claimCheckApplicationBus.GrantPutEventsTo(splitPipeRole);
            sampleProcessorInputQueue.GrantConsumeMessages(retrievalPipeRole);
            targetWorkflow.GrantStartExecution(retrievalPipeRole);
            claimCheckRetrievalLambda.GrantInvoke(retrievalPipeRole);
        }

        private dynamic createQueues()
        {
            var deadLetterQueue1 = new Queue(this, "ClaimCheckDeadLetterQueue1", new QueueProps { EnforceSSL= true, QueueName="SampleDataWriteQueueDLQ" });
            var deadLetterQueue2 = new Queue(this, "ClaimCheckDeadLetterQueue2", new QueueProps { EnforceSSL= true, QueueName="SampleProcessorInputQueueDLQ" });

            // Step 1: Create sample data of a "large" payload and put it in an SQS queue
            // Implementation= an AWS Lambda function ("claimCheckSampleDataCreatorLambda") creates this sample data and puts it in the SQS queue ("sampleDataWriteQueue")
            var name="SampleDataWriteQueue";
            var sampleDataWriteQueue=new Queue(this, "SampleDataWriteQueue", new QueueProps { 
                EnforceSSL=true, 
                DeadLetterQueue=new DeadLetterQueue {
                    MaxReceiveCount=1,
                    Queue=deadLetterQueue1
                },
                QueueName=name
            });

            name="SampleProcessorInputQueue";
            var sampleProcessorInputQueue = new Queue(this, "SampleProcessorInputQueue", new QueueProps {
                EnforceSSL= true,
                DeadLetterQueue = new DeadLetterQueue {
                    MaxReceiveCount= 1,
                    Queue= deadLetterQueue2,
                },
                QueueName=name
            });

            return new {
                SampleDataWriteQueue=sampleDataWriteQueue,
                SampleProcessorInputQueue=sampleProcessorInputQueue
            };
        }

        private EventBus createEventBus()
        {
            // Step 2= We want to put this event on our application bus. However, we don"t want to put the entire payload on the bus, only the claim check.
            // Implementation= we use an EventBridge Pipe to split the payload.
            // Internally, this Pipe uses an AWS Lambda function ("claimCheckSplitLambda") as enrichment, putting the payload into DynamoDB.
            
            var claimCheckApplicationBus = new EventBus(this, "ClaimCheckApplicationBus", new EventBusProps {
                EventBusName="ClaimCheckApplicationBus"
            });

            return claimCheckApplicationBus;
        }

        private dynamic createFunctions(Queue sampleDataWriteQueue, Table claimCheckTable)
        {
            /*var buildOption = new BundlingOptions()
            {
                Image = Runtime.DOTNET_6.,
                User = "root",
                OutputType = BundlingOutput.ARCHIVED,
                Command = new string[]{
                    "/bin/sh",
                    "-c",
                    " dotnet tool install -g Amazon.Lambda.Tools"+
                    " && dotnet build"+
                    " && dotnet lambda package --output-package /asset-output/function.zip"
                }
            };*/
            var lambdaRuntime=Runtime.DOTNET_6;
            var lambdaBinPath="../lambda/bin/debug/net6.0";

            var functionName="ClaimCheckSampleDataCreatorLambda";
            var claimCheckSampleDataCreatorLambda = new Function(this, functionName, new FunctionProps {
                Runtime= lambdaRuntime,
                Code=Code.FromAsset(lambdaBinPath),
                Handler="ClaimCheckFunctions::ServerlessPatterns.ClaimCheck.ClaimCheckDataCreator::FunctionHandler",
                Environment=new Dictionary<string, string>(1) {
                    {"QUEUE_URL", sampleDataWriteQueue.QueueUrl},
                },         
                Timeout=Duration.Seconds(15),
                FunctionName=functionName            
            });
            sampleDataWriteQueue.GrantSendMessages(claimCheckSampleDataCreatorLambda);

            functionName="ClaimCheckRetrievalLambda";
            var claimCheckRetrievalLambda = new Function(this, functionName, new FunctionProps {
                Runtime= lambdaRuntime,
                Code=Code.FromAsset(lambdaBinPath),
                Handler="ClaimCheckFunctions::ServerlessPatterns.ClaimCheck.ClaimCheckRetriever::FunctionHandler",
                Environment=new Dictionary<string, string>(1) {
                    {"CLAIM_CHECK_TABLE",claimCheckTable.TableName}
                },
                Timeout=Duration.Seconds(15),
                FunctionName=functionName
            });
            claimCheckTable.GrantReadData(claimCheckRetrievalLambda);

            functionName="ClaimCheckSplitLambda";
            var claimCheckSplitLambda = new Function(this, functionName, new FunctionProps {
                Runtime= lambdaRuntime,
                Code=Code.FromAsset(lambdaBinPath),
                Handler="ClaimCheckFunctions::ServerlessPatterns.ClaimCheck.ClaimCheckSplitter::FunctionHandler",
                Environment=new Dictionary<string, string>(1) {
                    {"CLAIM_CHECK_TABLE", claimCheckTable.TableName},
                },
                Timeout=Duration.Seconds(15),
                FunctionName=functionName
            });
            claimCheckTable.GrantWriteData(claimCheckSplitLambda);

            return new {
                ClaimCheckRetrievalLambda=claimCheckRetrievalLambda,
                ClaimCheckSplitLambda=claimCheckSplitLambda,
                ClaimCheckSampleDataCreatorLambda=claimCheckSampleDataCreatorLambda
            };
        }

        private Table createTable()
        {            
            var claimCheckTable = new Table(this, tableName, new TableProps {
                BillingMode = BillingMode.PAY_PER_REQUEST,
                TableName = tableName,
                PartitionKey=new Attribute { Name= "id", Type= AttributeType.STRING },
                RemovalPolicy= RemovalPolicy.DESTROY
            });
            return claimCheckTable;
        }
    }
}
