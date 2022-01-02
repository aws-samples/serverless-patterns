import { CfnOutput, Duration, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const queue = new sqs.Queue(this, 'MySqsQueue');

    const lambdaRole = new iam.Role(this, 'QueueConsumerFunctionRole', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      managedPolicies: [iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaSQSQueueExecutionRole'), 
                        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole')]
    });

    const lambdaFunction = new lambda.Function(this, 'QueueConsumerFunction', {
      code: lambda.Code.fromAsset(path.join(__dirname, '../src')),
      runtime: lambda.Runtime.NODEJS_12_X,
      handler: 'app.handler',
      timeout: Duration.seconds(3),
      memorySize: 128,
      role: lambdaRole
    });

    const eventSourceMapping = new lambda.EventSourceMapping(this, 'QueueConsumerFunctionMySQSEvent', {
      target: lambdaFunction,
      batchSize: 10,
      eventSourceArn: queue.queueArn
    });

    new CfnOutput(this, 'QueueConsumerFunctionName', {
      value: lambdaFunction.functionName,
      description: 'QueueConsumerFunction function name'
    });

    new CfnOutput(this, 'SQSqueueName', {
      value: queue.queueName,
      description: 'SQS queue name'
    });

    new CfnOutput(this, 'SQSqueueARN', {
      value: queue.queueArn,
      description: 'SQS queue ARN'
    });

    new CfnOutput(this, 'SQSqueueURL', {
      value: queue.queueUrl,
      description: 'SQS queue URL'
    });
  }
}
