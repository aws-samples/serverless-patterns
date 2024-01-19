import * as cdk from "aws-cdk-lib";
import { Template } from "aws-cdk-lib/assertions";
import { EventBridgeScheduleStepFunctionStack } from "../lib/evenbridge-schedule-stepfunction-stack";

test("Schedule and StepFunction Statemachine Created", () => {
  const app = new cdk.App();
  // WHEN
  const stack = new EventBridgeScheduleStepFunctionStack(app, "MyTestStack");
  // THEN
  const template = Template.fromStack(stack);
  template.hasResourceProperties("AWS::StepFunctions::StateMachine", {
    StateMachineName: "simple-state-machine",
  });
  template.hasResourceProperties("AWS::Scheduler::Schedule", {
    ScheduleExpression: "cron(*/5 * * * ? *)",
  });
});
