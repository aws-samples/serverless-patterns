import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

import { CfnSchedule, CfnScheduleGroup } from 'aws-cdk-lib/aws-scheduler';
import { Effect, Policy, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Duration } from 'aws-cdk-lib';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

export class EventbridgeScehdulesWithCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Example function that will get invoked every 5 minutes
    const exampleFunction: NodejsFunction = new NodejsFunction(this, 'scheduled-lambda-function', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/example-func/index.ts'),
    });

    // need to create role and policy for scheduler to invoke the lambda function
    const schedulerRole = new Role(this, 'scheduler-role', {
      assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
    });

    new Policy(this, 'schedule-policy', {
      policyName: 'ScheduleToInvokeLambdas',
      roles: [schedulerRole],
      statements: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          actions: ['lambda:InvokeFunction'],
          resources: [exampleFunction.functionArn],
        }),
      ],
    });

    // Create a group for the schedule (maybe you want to add more scheudles to this group the future?)
    const group = new CfnScheduleGroup(this, 'schedule-group', {
      name: 'SchedulesForLambda',
    });

    // Creates the schedule to invoke every 5 minutes
    new CfnSchedule(this, 'my-schedule', {
      groupName: group.name,
      flexibleTimeWindow: {
        mode: 'OFF',
      },
      scheduleExpression: 'rate(5 minute)',
      target: {
        arn: exampleFunction.functionArn,
        roleArn: schedulerRole.roleArn,
      },
    });
  }
}
