from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
)
from constructs import Construct

class SfnInsideSfnCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        innerSfnPassState = sfn.Pass(self, 'PassState');

        innerSfn = sfn.StateMachine(self, 'InnerStepFunction',
            definition = innerSfnPassState,
            timeout=Duration.minutes(60)
        )

        task1 = tasks.StepFunctionsStartExecution(self, "StepFunction1",
          state_machine=innerSfn,
          integration_pattern=sfn.IntegrationPattern.RUN_JOB,
          input=sfn.TaskInput.from_object({
              "input.$": "$.Output.input"
          }),
          output_path="$",
          result_selector = {
                "Output.$": "$.Output"
          }
        )

        task2 = tasks.StepFunctionsStartExecution(self, "StepFunction2",
          state_machine=innerSfn,
          integration_pattern=sfn.IntegrationPattern.RUN_JOB,
          input=sfn.TaskInput.from_object({
              "input.$": "$.Output.input"
          }),
          output_path="$",
          result_selector = {
                "Output.$": "$.Output"
          }
        )

        task3 = tasks.StepFunctionsStartExecution(self, "StepFunction3",
          state_machine=innerSfn,
          integration_pattern=sfn.IntegrationPattern.RUN_JOB,
          input=sfn.TaskInput.from_object({
              "input.$": "$.Output.input"
          }),
          output_path="$",
          result_selector = {
                "Output.$": "$.Output"
          }
        )

        outer_sfn = sfn.StateMachine(self, "OuterStepFunction",
                definition=task1.next(task2).next(task3),
                timeout=Duration.minutes(60)
        )

        CfnOutput(self, "StepFunctionArn",
            value = outer_sfn.state_machine_arn,
            export_name = 'OuterStepFunctionArn',
            description = 'Outer Step Function arn')
