import * as cdk from 'aws-cdk-lib';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { CfnSchedule } from 'aws-cdk-lib/aws-scheduler';
import { Effect, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { CfnOutput } from 'aws-cdk-lib';

export class EventbridgeScheduleToSqsCdkTypescriptStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create SQS queue
    const sqsQueue = new Queue(this, 'my-sqs-queue')

    // Create IAM that can be assumed by EventBridge Scheduler
    const schedulerRole = new Role(this, 'schedule-role', {
      assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
    });

    // Add IAM policy to allow EventBridge Scheduler to send messages to SQS
    schedulerRole.addToPolicy(new PolicyStatement({
      effect: Effect.ALLOW,
      actions: ['sqs:SendMessage'],
      resources: [sqsQueue.queueArn]
    }));

    // Creates EventBridge Schedule
    const mySchedule = new CfnSchedule(this, 'my-schedule', {
      flexibleTimeWindow: {
        mode: 'OFF'
      },
      scheduleExpression: 'rate(5 minute)',
      description: 'Schedule to send message to Amazon SQS every 5 minutes',
      target: {
        arn: sqsQueue.queueArn,
        roleArn: schedulerRole.roleArn,
        input: 'This message was sent using EventBridge Scheduler!'
      }
    });

    // CloudFormation Stack Outputs
    new CfnOutput(this, 'SCHEDULE_NAME', { value: mySchedule.ref });
    new CfnOutput(this, 'SQS_QUEUE_NAME', { value: sqsQueue.queueName });
  }
}
