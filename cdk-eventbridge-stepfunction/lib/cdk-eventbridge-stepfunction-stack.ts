import { Stack, StackProps, CfnOutput, Duration } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as path from "path";
import { aws_lambda as lambda } from "aws-cdk-lib";
import { aws_lambda_nodejs as lambdaNode } from "aws-cdk-lib";
import { aws_stepfunctions as sfn } from "aws-cdk-lib";
import { aws_stepfunctions_tasks as tasks } from "aws-cdk-lib";
import { aws_events as events } from "aws-cdk-lib";
import { aws_events_targets as eventsTarget } from "aws-cdk-lib";

import {EventBridgeTypes} from "../handlers/stepfunctions/waitUntil/sendReminder";

export class CdkEventbridgeStepfunctionStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Create an EventBus to receive and send events.
    const bus = new events.EventBus(this, "reminderEventBus");
    // Output the name of the new bus.
    new CfnOutput(this, "reminderBus", { value: bus.eventBusName });

    // Define the wait task.
    // Because we're subscribing to an EventBridge event, the "at" field
    // is under the detail.
    const waitTask = new sfn.Wait(this, "waitUntil", {
      time: sfn.WaitTime.timestampPath("$.detail.at"),
    });

    // Define the sendReminder task.
    const sendReminderHandler = new lambdaNode.NodejsFunction(
      this,
      "sendReminderHandler",
      {
        runtime: lambda.Runtime.NODEJS_12_X,
        handler: "handler",
        entry: path.join(
          __dirname,
          "../handlers/stepfunctions/waitUntil/sendReminder/index.ts"
        ),
        memorySize: 1024,
        environment: {
          EVENT_BUS: bus.eventBusName,
        },
      }
    );
    // Grant permission to send to the bus.
    bus.grantPutEventsTo(sendReminderHandler);
    // Set up the Lambda function to be a task.
    const sendReminderTask = new tasks.LambdaInvoke(
      this,
      "sendReminder",
      {
        lambdaFunction: sendReminderHandler,
        outputPath: "$.Payload", // Return the output from the Lambda function.
      }
    );

    // Configure a delay for the sendReminderTask.
    const reminderMachineDefinition = waitTask.next(
      sendReminderTask
    );

    // Construct the state machine.
    const reminderMachine = new sfn.StateMachine(this, "reminder", {
      definition: reminderMachineDefinition,
      timeout: Duration.days(90),
    });

    // Configure EventBridge to start the reminder machine when a remind event is received.
    const reminderMachineTarget = new eventsTarget.SfnStateMachine(
      reminderMachine
    );
    new events.Rule(this, "startReminder", {
      eventBus: bus,
      targets: [reminderMachineTarget],
      eventPattern: {
        detailType: [EventBridgeTypes.StartReminder],
      },
    });
  }
}
