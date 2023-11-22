import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as scheduler from "aws-cdk-lib/aws-scheduler";
import * as iam from "aws-cdk-lib/aws-iam";
import * as sfn from "aws-cdk-lib/aws-stepfunctions";
import * as tasks from "aws-cdk-lib/aws-stepfunctions-tasks";

export class EventBridgeScheduleStepFunctionStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const pass = new sfn.Pass(this, "Workflow Pass", {
      parameters: {
        "item.$": "$",
      },
    });
    const definition = sfn.Chain.start(pass);
    const stateMachine = new sfn.StateMachine(this, "StateMachine", {
      stateMachineName: "simple-state-machine",
      definition,
    });

    const schedulerRole = new iam.Role(this, "SchedulerRole", {
      assumedBy: new iam.ServicePrincipal("scheduler.amazonaws.com"),
    });

    stateMachine.grantStartExecution(schedulerRole);
    stateMachine.grantStartSyncExecution(schedulerRole);

    const schedule = new scheduler.CfnSchedule(this, "ScheduleEvery5Min", {
      scheduleExpression: "cron(*/5 * * * ? *)", // Every 5 minutes
      flexibleTimeWindow: {
        mode: "OFF",
      },
      target: {
        arn: stateMachine.stateMachineArn,
        roleArn: schedulerRole.roleArn,
        // the properties below are optional
        input: JSON.stringify({
          scheduleTime: "<aws.scheduler.scheduled-time>",
        }),
      },
      // the properties below are optional
      description: "EventBridge Schedule invoking stepfunctions CDK",
      name: "EventBridgeScheduleFromCDK",
      state: "ENABLED",
    });
  }
}
