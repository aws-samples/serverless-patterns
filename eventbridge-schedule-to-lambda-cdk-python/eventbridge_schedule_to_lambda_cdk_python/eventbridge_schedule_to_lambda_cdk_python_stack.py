from aws_cdk import (
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_scheduler as scheduler,
)
from constructs import Construct


class EventbridgeScheduleToLambdaCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda function
        scheduler_lambda_function = _lambda.Function(
            self,
            'SchedulerLambdaFunctionPython',
            runtime=_lambda.Runtime.PYTHON_3_10,
            code=_lambda.Code.from_asset('./src'),
            handler='lambda_function.lambda_handler'
        )

        # Create schedule role
        scheduler_role = iam.Role(self, "scheduler-role",
                                  assumed_by=iam.ServicePrincipal(
                                      "scheduler.amazonaws.com")
                                  )

        # Create IAM policy
        scheduler_events_policy = iam.PolicyStatement(
            actions=["lambda:InvokeFunction"],
            resources=[scheduler_lambda_function.function_arn],
            effect=iam.Effect.ALLOW,
        )

        # Add IAM policy to schedule role
        scheduler_role.add_to_policy(scheduler_events_policy)

        # Create schedule to invoke the Lambda function every 5 minutes
        my_schedule = scheduler.CfnSchedule(self, "my-schedule",
                                            flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                                                mode="OFF",
                                            ),
                                            schedule_expression="rate(5 minute)",
                                            target=scheduler.CfnSchedule.TargetProperty(
                                                arn=scheduler_lambda_function.function_arn,
                                                role_arn=scheduler_role.role_arn,
                                                input="{\"input\": \"This message was sent using EventBridge Scheduler!\"}"
                                            )
                                            )

        # CloudFormation Stack Outputs
        CfnOutput(self, "SCHEDULE_NAME", value=my_schedule.ref)
        CfnOutput(self, "LAMBDA_FUNCTION_ARN",
                  value=scheduler_lambda_function.function_arn)
