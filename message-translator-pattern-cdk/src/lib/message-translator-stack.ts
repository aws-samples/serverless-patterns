import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class MessageTranslatorStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const deadLetterQueue = new sqs.Queue(this, 'ClaimCheckDeadLetterQueue', {
      enforceSSL: true,
    });

    const sourceQueue = new sqs.Queue(this, 'MessageTranslatorSourceQueue', {
      enforceSSL: true,
      deadLetterQueue: {
        maxReceiveCount: 1,
        queue: deadLetterQueue,
      }
    });

    const targetStepFunctionsWorkflow = new sfn.StateMachine(this, 'MessageTranslatorTargetStepFunctionsWorkflow', {
      definition: sfn.Chain.start(new sfn.Pass(this, 'Process Message', {})),
      tracingEnabled: true,
      logs: {
        destination: new logs.LogGroup(this, 'MessageTranslatorTargetStepFunctionsWorkflowLogGroup', {
          logGroupName: '/aws/vendedlogs/MessageTranslatorTargetStepFunctionsWorkflowLogGroup',
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
        level: sfn.LogLevel.ALL,
      },
    });

    // This sample uses a Lambda function to simulate a geocoding endpoint. To integrate with an existing geocoding endpoint, we could use either API Destinations or API Gateway instead.
    const enrichmentLambda = new lambda.Function(this, 'MessageTranslatorEnrichmentLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'messageTranslatorEnrichmentLambda.handler',
    });

    // role with permission to read events from the source queue and write to the target step functions workflow
    const pipeRole = new iam.Role(this, 'MessageTranslatorRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });

    sourceQueue.grantConsumeMessages(pipeRole);
    targetStepFunctionsWorkflow.grantStartExecution(pipeRole);
    enrichmentLambda.grantInvoke(pipeRole);

    const messageTranslatorPipe = new pipes.CfnPipe(this, 'MessageTranslatorPipe', {
      roleArn: pipeRole.roleArn,
      source: sourceQueue.queueArn,
      target: targetStepFunctionsWorkflow.stateMachineArn,
      enrichment: enrichmentLambda.functionArn,
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

    const messageTranslatorSampleDataCreator = new lambda.Function(this, 'MessageTranslatorSampleDataCreatorLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'messageTranslatorSampleDataCreator.handler',
      environment: {
        QUEUE_URL: sourceQueue.queueUrl,
      }
    });
    sourceQueue.grantSendMessages(messageTranslatorSampleDataCreator);
 
    // Relevant outputs so that the user can trigger this pattern and watch it in action.
    new cdk.CfnOutput(this, "MessageTranslatorSampleDataCreatorLambdaArn", {
      value: messageTranslatorSampleDataCreator.functionArn,
      exportName: "MessageTranslatorSampleDataCreatorLambdaArn",
      description: "The Arn of the Lambda function that can be used to test the Claim Check Pipe. Invoke this function to see the pipe in action.",
    });
    new cdk.CfnOutput(this, "TargetStepFunctionsWorkflowArn", {
      value: targetStepFunctionsWorkflow.stateMachineArn,
      exportName: "TargetStateMachineArn",
      description: "The ARN of the target workflow. After invoking the SampleDataCreatorLambda, you can use this ARN to view the execution history of the workflow and see the result.",
    });
  }
}

