import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnSchedule, CfnScheduleGroup } from 'aws-cdk-lib/aws-scheduler';
import { Effect, Policy, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Queue } from 'aws-cdk-lib/aws-sqs';

export class ScheduleEc2InstancesStartAndStopStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // list of your instance ids you want to start and stop. (Example below)
    const instanceIds = ['i-0592cdaf40c14c22a'];

    // need to create role and policy for scheduler to stop and start instances
    const schedulerRole = new Role(this, 'scheduler-role', {
      assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
    });

    new Policy(this, 'schedule-policy', {
      policyName: 'ScheduleToStopEC2Instances',
      roles: [schedulerRole],
      statements: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          actions: ['ec2:startInstances', 'ec2:stopInstances'],

          // policy has access to any ec2 resource, you may want to change if you want more
          // control here.
          resources: ['*'],
        }),
      ],
    });

    // DLQ for any schedules that fail
    const DLQ = new Queue(this, 'queue', {
      queueName: 'instance-manager-dlq',
    });

    // create a group for our schedules
    const group = new CfnScheduleGroup(this, 'instance-manager', {
      name: 'instance-manager'
    })

    // Start all instances every day at 7:00 (Europe/London) timezone
    new CfnSchedule(this, 'start-instances', {
      groupName: group.name,
      flexibleTimeWindow: {
        mode: 'OFF',
      },
      // Every morning at 7:00am Monday to Friday
      scheduleExpression: `cron(0 7 ? * MON-FRI *)`,
      // find more timezones here https://www.iana.org/time-zones
      scheduleExpressionTimezone: 'Europe/London',
      description: 'Event that start instances',
      target: {
        deadLetterConfig: {
          arn: DLQ.queueArn,
        },
        arn: 'arn:aws:scheduler:::aws-sdk:ec2:startInstances',
        roleArn: schedulerRole.roleArn,
        input: JSON.stringify({ InstanceIds: instanceIds }),
      },
    });

    // Terminate all instances every day at 18:00 (Europe/London) timezone
    new CfnSchedule(this, 'stop-instances', {
      groupName: group.name,
      flexibleTimeWindow: {
        mode: 'OFF',
      },
      // Every evening at 18:00pm Monday to Friday
      scheduleExpression: `cron(0 18 ? * MON-FRI *)`,
      // find more timezones here https://www.iana.org/time-zones
      scheduleExpressionTimezone: 'Europe/London',
      description: 'Event that will stop instances',
      target: {
        deadLetterConfig: {
          arn: DLQ.queueArn,
        },
        arn: 'arn:aws:scheduler:::aws-sdk:ec2:stopInstances',
        roleArn: schedulerRole.roleArn,
        input: JSON.stringify({ InstanceIds: instanceIds }),
      },
    });
  }
}
