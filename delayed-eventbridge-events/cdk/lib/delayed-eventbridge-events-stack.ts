import * as cdk from 'aws-cdk-lib';
import { Duration } from 'aws-cdk-lib';
import { EventBus, Rule } from 'aws-cdk-lib/aws-events';
import { LambdaFunction } from 'aws-cdk-lib/aws-events-targets';
import { Effect, Policy, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Construct } from 'constructs';
import * as path from 'path';

export class DelayedEventbridgeEventsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a new eventbus for our demo
    const eventBus = new EventBus(this, 'CustomBus', {
      eventBusName: 'MyCustomBus',
    });

    // need to create role and policy for scheduler to put events onto our bus
    const launchRole = new Role(this, 'scheduler-role', {
      assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
    });

    new Policy(this, 'schedule-policy', {
      policyName: 'ScheduleToPutEvents',
      roles: [launchRole],
      statements: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          actions: ['events:PutEvents'],
          resources: [eventBus.eventBusArn],
        }),
      ],
    });

    // Listen to UserCreated and create the schedule.
    const processUserCreatedFunction: NodejsFunction = new NodejsFunction(this, 'process-user-created', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_16_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/process-user-created/index.ts'),
      environment: {
        SCHEDULE_ROLE_ARN: launchRole.roleArn,
        EVENTBUS_ARN: eventBus.eventBusArn
      },
      initialPolicy: [
        // Give lambda permission to create group, schedule and pass IAM role to the scheduler
        new PolicyStatement({
          actions: ['scheduler:CreateSchedule', 'iam:PassRole', 'scheduler:CreateScheduleGroup'],
          resources: ['*'],
        }),
      ],
    });

    // EventBridge rule to listen to UserCreated so we can process it and create schedule
    new Rule(this, 'UserCreatedRule', {
      description: 'Listen to UseCreated events',
      eventPattern: {
        source: ['myapp.users'],
        detailType: ['UserCreated'],
      },
      eventBus,
    }).addTarget(new LambdaFunction(processUserCreatedFunction));

    // Function that listens to schedule directly onto EventBridge and "email a customer" as an example
    const emailCustomer: NodejsFunction = new NodejsFunction(this, 'email-customer', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_16_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/email-customer/index.ts'),
    });

    // Rule to match schedules for users and attach our email customer lambda.
    new Rule(this, 'UserCreated24HoursAgoRule', {
      description: 'Custom notification event when the user has been created 24 hours ago',
      eventPattern: {
        source: ['scheduler.notifications'],
        detailType: ['UserCreated24HoursAgo'],
      },
      eventBus,
    }).addTarget(new LambdaFunction(emailCustomer));

  }
}
