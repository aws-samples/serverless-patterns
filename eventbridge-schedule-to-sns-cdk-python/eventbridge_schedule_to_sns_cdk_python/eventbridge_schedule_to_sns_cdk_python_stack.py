from aws_cdk import (
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_sns as _sns,
    aws_scheduler as scheduler,
)
from constructs import Construct

class EventbridgeScheduleToSnsCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## Create SNS Topic
        my_sns_topic = _sns.Topic(self, "my-sns-topic")

        ## Create schedule role
        scheduler_role = iam.Role(self, "scheduler-role",
            assumed_by=iam.ServicePrincipal("scheduler.amazonaws.com")
        )

        ## Create IAM policy
        scheduler_events_policy = iam.PolicyStatement(
                actions=["sns:Publish"],
                resources=[my_sns_topic.topic_arn],
                effect=iam.Effect.ALLOW,
        )

        ## Add IAM policy to schedule role
        scheduler_role.add_to_policy(scheduler_events_policy)

        ## Create schedule to send a message to SNS every 5 minutes
        my_schedule = scheduler.CfnSchedule(self, "my-schedule",
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="OFF",
                ),
                schedule_expression="rate(5 minute)",
                target=scheduler.CfnSchedule.TargetProperty(
                    arn=my_sns_topic.topic_arn,
                    role_arn=scheduler_role.role_arn,
                    input="This message was sent using EventBridge Scheduler!"
                )
            )

        ## CloudFormation Stack Outputs
        CfnOutput(self, "SCHEDULE_NAME", value=my_schedule.ref)
        CfnOutput(self, "SNS_TOPIC_NAME", value=my_sns_topic.topic_arn)