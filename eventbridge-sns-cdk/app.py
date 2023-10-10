#!/usr/bin/env python3

from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    aws_sns as sns,
    aws_events as events,
    aws_events_targets as targets
)
from constructs import Construct

class EventbridgeSnsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #SNS Topic
        MySnsTopic = sns.Topic(
            self, "MySnsTopic"
        )

        # Custom EventBridge Bus
        custom_bus = events.EventBus(
            self, "bus",
            event_bus_name="test-bus-cdk"
        )

        # EventBridge Rule
        rule = events.Rule(
            self, "rule",
            event_bus=custom_bus
        )

        # Event Pattern to filter events
        rule.add_event_pattern(
            source=["my-application"],
            detail_type=["message"]
        )

        # SNS topic as target for Eventbridge Rue
        rule.add_target(targets.SnsTopic(MySnsTopic))

        # CDK Outputs
        CfnOutput(self, "SNS topic name", description="SNS topic name", value=MySnsTopic.topic_name)
        CfnOutput(self, "SNS topic ARN", description="SNS topic ARN", value=MySnsTopic.topic_arn)


app = App()
EventbridgeSnsCdkStack(app,"EventbridgeSnsCdkExample")
app.synth()
