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
            self,
            'logs',
            removal_policy = cdk.RemovalPolicy.DESTROY,
            retention = logs.RetentionDays.ONE_DAY
        )

        # EventBridge Rule
        rule = events.Rule(
            self, "Rule",
        )
        rule.add_event_pattern(
            source=["cdk.myApp"],
            detail_type=["transaction"]
        )
        rule.add_target(targets.CloudWatchLogGroup(log_group))


app = cdk.App()
EventBridgeCloudWatchStack(app, "EventBridgeCloudWatchExample")
app.synth() 