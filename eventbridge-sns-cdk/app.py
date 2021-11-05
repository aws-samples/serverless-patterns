#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from aws_cdk import (
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_events as events,
    aws_events_targets as targets,
    core
)
# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

class EventbridgeSnsCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
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
        cdk.CfnOutput(self, "SNS topic name", description="SNS topic name", value=MySnsTopic.topic_name)
        cdk.CfnOutput(self, "SNS topic ARN", description="SNS topic ARN", value=MySnsTopic.topic_arn)


app = core.App()
EventbridgeSnsCdkStack(app,"EventbridgeSnsCdkExample")
app.synth()
