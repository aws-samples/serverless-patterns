from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
)
import aws_cdk.aws_iot_alpha as iot
import aws_cdk.aws_iot_actions_alpha as actions

class IotSnsSqsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "IotSnsSqsCdkQueue",
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "IotSnsSqsCdkTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))

        topic_rule = iot.TopicRule(self, "IotSnsSqsCdkRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/data'"),
            actions=[
                actions.SnsTopicAction(topic,
                    message_format=actions.SnsActionMessageFormat.JSON
                )
            ]
        )