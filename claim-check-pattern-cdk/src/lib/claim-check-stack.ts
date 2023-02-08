import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';

export class ClaimCheckStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Prerequisites that are not specific to this pattern
    const lambdaRuntime = lambda.Runtime.NODEJS_18_X;
    const deadLetterQueue1 = new sqs.Queue(this, 'ClaimCheckDeadLetterQueue1', {
      enforceSSL: true,
    });
    const deadLetterQueue2 = new sqs.Queue(this, 'ClaimCheckDeadLetterQueue2', {
      enforceSSL: true,
    });

    // Step 1: Create sample data of a "large" payload and put it in an SQS queue
    // Implementation: an AWS Lambda function ("claimCheckSampleDataCreatorLambda") creates this sample data and puts it in the SQS queue ("sampleDataWriteQueue")
    const sampleDataWriteQueue = new sqs.Queue(this, 'SampleDataWriteQueue', {
      enforceSSL: true,
      deadLetterQueue: {
        maxReceiveCount: 1,
        queue: deadLetterQueue1,
      }
    });

    const claimCheckSampleDataCreatorLambda = new lambda.Function(this, 'ClaimCheckSampleDataCreatorLambda', {
      runtime: lambdaRuntime,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'claimCheckSampleDataCreator.handler',
      environment: {
        QUEUE_URL: sampleDataWriteQueue.queueUrl,
      }
    });
    sampleDataWriteQueue.grantSendMessages(claimCheckSampleDataCreatorLambda);

    // Step 2: We want to put this event on our application bus. However, we don't want to put the entire payload on the bus, only the claim check.
    // Implementation: we use an EventBridge Pipe to split the payload.
    // Internally, this Pipe uses an AWS Lambda function ("claimCheckSplitLambda") as enrichment, putting the payload into DynamoDB.
    
    const claimCheckApplicationBus = new events.EventBus(this, 'ClaimCheckApplicationBus', {
      eventBusName: 'ClaimCheckApplicationBus'
    });

    const claimCheckTable = new dynamodb.Table(this, 'ClaimCheckTable', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      pointInTimeRecovery: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    const claimCheckSplitLambda = new lambda.Function(this, 'ClaimCheckSplitLambda', {
      runtime: lambdaRuntime,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'claimCheckSplit.handler',
      environment: {
        CLAIM_CHECK_TABLE: claimCheckTable.tableName,
      }
    });
    claimCheckTable.grantWriteData(claimCheckSplitLambda);

    const splitPipeRole = new iam.Role(this, 'ClaimCheckSplitRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });
    sampleDataWriteQueue.grantConsumeMessages(splitPipeRole);
    claimCheckApplicationBus.grantPutEventsTo(splitPipeRole);
    claimCheckSplitLambda.grantInvoke(splitPipeRole);

    const claimCheckSplitPipe = new pipes.CfnPipe(this, 'ClaimCheckSplitPipe', {
      roleArn: splitPipeRole.roleArn,
      source: sampleDataWriteQueue.queueArn,
      target: claimCheckApplicationBus.eventBusArn,
      enrichment: claimCheckSplitLambda.functionArn,
      sourceParameters: {
        sqsQueueParameters: {
          batchSize: 1,
        },
      },
    });

    // Step 3: We want to process the event from our application bus using AWS Step Functions.
    // However, we don't have all information we need in the event. We use an EventBridge Pipe to retrieve the additional information.
    // Internally, this Pipe uses an AWS Lambda function ("ClaimCheckRetrievalLambda") as enrichment, retrieving the payload from DynamoDB.

    const sampleProcessorInputQueue = new sqs.Queue(this, 'SampleProcessorInputQueue', {
      enforceSSL: true,
      deadLetterQueue: {
        maxReceiveCount: 1,
        queue: deadLetterQueue2,
      }
    });

    const sampleProcessorInputQueueRule = new events.Rule(this, 'SampleProcessorInputQueueRule', {
      eventBus: claimCheckApplicationBus,
      eventPattern: {
        source: events.Match.prefix(''),
      },
      targets: [new targets.SqsQueue(sampleProcessorInputQueue)],
    });

    const claimCheckRetrievalLambda = new lambda.Function(this, 'ClaimCheckRetrievalLambda', {
      runtime: lambdaRuntime,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'claimCheckRetrieval.handler',
      environment: {
        CLAIM_CHECK_TABLE: claimCheckTable.tableName
      }
    });
    claimCheckTable.grantReadData(claimCheckRetrievalLambda);

    const targetWorkflow = new sfn.StateMachine(this, 'ClaimCheckTargetWorkflow', {
      definition: sfn.Chain.start(new sfn.Pass(this, 'Process Message')),
      tracingEnabled: true,
      logs: {
        destination: new logs.LogGroup(this, 'ClaimCheckTargetWorkflowLogGroup', {
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
        level: sfn.LogLevel.ALL,
      },
    });

    const retrievalPipeRole = new iam.Role(this, 'ClaimCheckRetrievalRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });
    sampleProcessorInputQueue.grantConsumeMessages(retrievalPipeRole);
    targetWorkflow.grantStartExecution(retrievalPipeRole);
    claimCheckRetrievalLambda.grantInvoke(retrievalPipeRole);

    const claimCheckEnrichmentPipe = new pipes.CfnPipe(this, 'ClaimCheckEnrichmentPipe', {
      roleArn: retrievalPipeRole.roleArn,
      source: sampleProcessorInputQueue.queueArn,
      target: targetWorkflow.stateMachineArn,
      enrichment: claimCheckRetrievalLambda.functionArn,
      sourceParameters: {
        sqsQueueParameters: {
          batchSize: 1,
        },
      },
      targetParameters: {
        stepFunctionStateMachineParameters: {
          invocationType: 'FIRE_AND_FORGET',
        },
      }
    });

    // Send all events on claimCheckApplicationBusRule to CloudWatch Logs to demonstrate only id's are passed on bus        
    const claimCheckApplicationBusRule = new events.Rule(this, 'ClaimCheckApplicationBusRule', {
      ruleName: 'claimCheckApplicationBusRule',
      eventBus: claimCheckApplicationBus,
      eventPattern: {
        source: events.Match.prefix(''),
      },
      targets: [new targets.CloudWatchLogGroup(new logs.LogGroup(this, 'ClaimTargetLog', {
        logGroupName: '/aws/events/claimTargetLog',
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      }))],
    });

    // Relevant outputs so that the user can trigger this pattern and watch it in action.
    new cdk.CfnOutput(this, "ClaimCheckSampleDataCreatorLambdaArn", {
      value: claimCheckSampleDataCreatorLambda.functionArn,
      exportName: "ClaimCheckSampleDataCreatorLambdaArn",
    });
    new cdk.CfnOutput(this, "ClaimCheckTableName", {
      value: claimCheckTable.tableName,
      exportName: "ClaimCheckTableName",
    });
    new cdk.CfnOutput(this, "ClaimCheckTargetWorkflowArn", {
      value: targetWorkflow.stateMachineArn,
      exportName: "ClaimCheckTargetWorkflowArn",
    });
  }
}
