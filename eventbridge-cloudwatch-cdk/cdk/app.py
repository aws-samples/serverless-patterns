from aws_cdk import (
    aws_events as events,
    aws_events_targets as targets,
    aws_logs as logs,
    core as cdk,
)


class EventBridgeCloudWatchStack(cdk.Stack):
    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)

        # CloudWatch Logs Group
        log_group = logs.LogGroup(
            self, "logs",
            retention=logs.RetentionDays.ONE_DAY,
            removal_policy = cdk.RemovalPolicy.DESTROY
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
        rule.add_event_pattern(
            source=["my-cdk-application"],
            detail_type=["message"]
        )
        rule.add_target(targets.CloudWatchLogGroup(log_group))

        cdk.CfnOutput(
            self, "LogGroupName",
            description="Name of CloudWatch Log Group",
            value=log_group.log_group_name
        )

app = cdk.App()
EventBridgeCloudWatchStack(app, "EventBridgeCloudWatchExample")
app.synth() 