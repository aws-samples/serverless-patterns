import * as cdk from 'aws-cdk-lib';
import { EventBus } from 'aws-cdk-lib/aws-events';
import { Effect, Policy, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { CfnSchedule, CfnScheduleGroup } from 'aws-cdk-lib/aws-scheduler';
import { v4 } from 'uuid';

export class EventbridgeSchedulerIntoEventbridgeStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // custom event bus, you can change this to yours or create a new one
    const eventBus = EventBus.fromEventBusName(this, 'bus', 'MyCustomBus');

    // need to create role and policy for scheduler to invoke the lambda function
    const schedulerRole = new Role(this, 'scheduler-role', {
      assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
    });

    new Policy(this, 'schedule-policy', {
      policyName: 'ScheduleToPutEventsIntoDefaultEventBus',
      roles: [schedulerRole],
      statements: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          actions: ['events:PutEvents'],
          resources: [eventBus.eventBusArn],
        }),
      ],
    });

    // Create a group for the schedule (maybe you want to add more scheudles to this group the future?)
    const group = new CfnScheduleGroup(this, 'schedule-group', {
      name: 'RecurringSchedulesIntoEventBus',
    });

    // Creates the schedule to invoke every 5 minutes
    new CfnSchedule(this, 'my-schedule', {
      groupName: group.name,
      flexibleTimeWindow: {
        mode: 'OFF',
      },
      // run every 5 minutes
      scheduleExpression: 'rate(5 minute)',
      description: 'Event that is raised every 5 minutes into event bus',
      target: {
        arn: eventBus.eventBusArn,
        roleArn: schedulerRole.roleArn,
        // using templated targets, we can trigger eventbridge directly
        eventBridgeParameters: {
          detailType: 'ScheduleTriggered',
          source: 'scheduled.events'
        },
        // your eventbridge payload
        input: JSON.stringify({
          metadata: {
            id: v4(),
            domain: 'SCHEDULED_EVENT'
          },
          data: {
            firstName: 'David',
            lastName: 'Boyne'            
          }
        })
      },
    });
  }
}
