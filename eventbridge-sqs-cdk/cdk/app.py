from aws_cdk import (
    aws_events as events,
    aws_events_targets as targets,
    aws_sqs as sqs,
    core as cdk,
)


class EventBridgeSQSStack(cdk.Stack):
    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)

        # SQS Queue
        queue = sqs.Queue(
            self, "queue",
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
            detail_type=["message-for-queue"]
        )
        rule.add_target(targets.SqsQueue(queue))


        # Stack Outputs
        cdk.CfnOutput(
            self, "QueueURL",
            description="URL of SQS Queue",
            value=queue.queue_url
        )

app = cdk.App()
EventBridgeSQSStack(app, "EventBridgeSQSExample")
app.synth() 