import * as cdk from 'aws-cdk-lib';
import { Topic } from 'aws-cdk-lib/aws-sns';
import { CfnSchedule } from 'aws-cdk-lib/aws-scheduler';
import { Effect, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { CfnOutput } from 'aws-cdk-lib';

export class EventbridgeScheduleToSnsCdkTypescriptStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create SNS Topic
    const snsTopic = new Topic(this, 'my-sns-topic')

    // Create IAM that can be assumed by EventBridge Scheduler
    const schedulerRole = new Role(this, 'schedule-role', {
      assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
    });

    // Create IAM policy to allow EventBridge Scheduler to send messages to SNS
    schedulerRole.addToPolicy(new PolicyStatement({
      effect: Effect.ALLOW,
      actions: ['sns:Publish'],
      resources: [snsTopic.topicArn]
    }));

    // Creates EventBridge Schedule
    const mySchedule = new CfnSchedule(this, 'my-schedule', {
      flexibleTimeWindow: {
        mode: 'OFF'
      },
      scheduleExpression: 'rate(5 minute)',
      description: 'Schedule to send message to Amazon SNS every 5 minutes',
      target: {
        arn: snsTopic.topicArn,
        roleArn: schedulerRole.roleArn,
        input: 'This message was sent using EventBridge Scheduler!'
      }
    });

    // CloudFormation Stack Outputs
    new CfnOutput(this, 'SCHEDULE_NAME', { value: mySchedule.ref });
    new CfnOutput(this, 'SNS_TOPIC_NAME', { value: snsTopic.topicArn });
  }
}