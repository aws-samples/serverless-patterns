from aws_cdk import (
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_sqs as _sqs,
    aws_scheduler as scheduler,
)
from constructs import Construct

class EventbridgeScheduleToSqsCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## Create SQS queue
        my_sqs_queue = _sqs.Queue(self, "my-sqs-queue")

        ## Create schedule role
        scheduler_role = iam.Role(self, "scheduler-role",
            assumed_by=iam.ServicePrincipal("scheduler.amazonaws.com")
        )

        ## Create IAM policy
        scheduler_events_policy = iam.PolicyStatement(
                actions=["sqs:SendMessage"],
                resources=[my_sqs_queue.queue_arn],
                effect=iam.Effect.ALLOW,
        )

        ## Add IAM policy to schedule role
        scheduler_role.add_to_policy(scheduler_events_policy)

        ## Create schedule to send a message to SQS every 5 minutes
        my_schedule = scheduler.CfnSchedule(self, "my-schedule",
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="OFF",
                ),
                schedule_expression="rate(5 minute)",
                target=scheduler.CfnSchedule.TargetProperty(
                    arn=my_sqs_queue.queue_arn,
                    role_arn=scheduler_role.role_arn,
                    input="This message was sent using EventBridge Scheduler!"
                )
            )

        ## Output
        CfnOutput(self, "SCHEDULE_NAME", value=my_schedule.ref)
        CfnOutput(self, "SQS_QUEUE_NAME", value=my_sqs_queue.queue_name)
