import * as cdk from 'aws-cdk-lib';
import { EventBus, Rule } from 'aws-cdk-lib/aws-events';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as scheduler from 'aws-cdk-lib/aws-scheduler';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { Construct } from 'constructs';

export class SchedulerDisableRuleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // EventBridge Event Bus
    const bus = new EventBus(this, "scheduler-bus")
    const ruleName = 'scheduler-rule'
    const rule = new Rule(this, "scheduler-rule", {
      eventBus: bus,
      eventPattern: {
        account: [this.account]
      },
      enabled: true, // default,
      ruleName: ruleName, // hardcode because rule.ruleName incorrectly returns rule name with bus name included
      targets: [] // not configuring targets to keep code concise
    })

    // SQS
    const dlq = new Queue(this, "scheduler-dlq")

    // IAM
    const schedulerRole = new iam.Role(this, 'scheduler-role', {
      assumedBy: new iam.ServicePrincipal('scheduler.amazonaws.com'),
      inlinePolicies: {
        EventBridge: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              actions: ['events:DisableRule', 'events:EnableRule'],
              resources: [rule.ruleArn],
            }),
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              actions: ['sqs:GetQueueAttributes', 'sqs:SendMessage'],
              resources: [dlq.queueArn],
            }),
          ]
        })
      }
    });


    // EventBridge Scheduler
    const disableSchedule = new scheduler.CfnSchedule(this, 'disable-rule-schedule', {
      flexibleTimeWindow: {
        mode: 'OFF',
      },
      scheduleExpression: 'cron(00 08 ? * SUN *)',
      scheduleExpressionTimezone: 'UTC',
      target: {
        arn: 'arn:aws:scheduler:::aws-sdk:eventbridge:disableRule',
        roleArn: schedulerRole.roleArn,
        input: JSON.stringify({
          EventBusName: bus.eventBusArn,
          Name: ruleName
        }),
        deadLetterConfig: {
          arn: dlq.queueArn
        },
        retryPolicy: {
          maximumRetryAttempts: 1
        }
      },
    });

    const enableSchedule = new scheduler.CfnSchedule(this, 'enable-rule-schedule', {
      flexibleTimeWindow: {
        mode: 'OFF',
      },
      scheduleExpression: 'cron(00 09 ? * SUN *)',
      scheduleExpressionTimezone: 'UTC',
      target: {
        arn: 'arn:aws:scheduler:::aws-sdk:eventbridge:enableRule',
        roleArn: schedulerRole.roleArn,
        input: JSON.stringify({
          EventBusName: bus.eventBusArn,
          Name: ruleName
        }),
        deadLetterConfig: {
          arn: dlq.queueArn
        },
        retryPolicy: {
          maximumRetryAttempts: 1
        }
      },
    });

    new cdk.CfnOutput(this, "disableScheduleArn", { value: disableSchedule.attrArn })
    new cdk.CfnOutput(this, "enableScheduleArn", { value: enableSchedule.attrArn })
    new cdk.CfnOutput(this, "busArn", { value: bus.eventBusArn })
    new cdk.CfnOutput(this, "ruleArn", { value: rule.ruleArn })
    new cdk.CfnOutput(this, "dlqArn", { value: dlq.queueArn })
    new cdk.CfnOutput(this, "roleArn", { value: schedulerRole.roleArn })
  }
}