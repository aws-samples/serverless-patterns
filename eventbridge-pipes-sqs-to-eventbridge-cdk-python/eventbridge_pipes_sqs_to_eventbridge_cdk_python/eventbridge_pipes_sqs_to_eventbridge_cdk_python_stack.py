from aws_cdk import (
    CfnOutput,
    Stack,
    aws_events as events,
    aws_iam as iam,
    aws_pipes as pipes,
    aws_sqs as sqs,
)
from constructs import Construct
import json

class EventbridgePipesSqsToEventbridgeCdkPythonStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source = sqs.Queue(self, 'sqs-queue')
        target = events.EventBus(self, 'event-bus')

        source_policy = iam.PolicyStatement(
                actions=['sqs:ReceiveMessage', 'sqs:DeleteMessage', 'sqs:GetQueueAttributes'],
                resources=[source.queue_arn],
                effect=iam.Effect.ALLOW,
        )

        target_policy = iam.PolicyStatement(
                actions=['events:PutEvents'],
                resources=[target.event_bus_arn],
                effect=iam.Effect.ALLOW,
        )

        pipe_role = iam.Role(self, 'pipe-role',
            assumed_by=iam.ServicePrincipal('pipes.amazonaws.com'),
        )

        pipe_role.add_to_policy(source_policy)
        pipe_role.add_to_policy(target_policy)

        pipe = pipes.CfnPipe(self, "pipe",
            role_arn=pipe_role.role_arn,
            source=source.queue_arn,
            source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                    batch_size=5,
                    maximum_batching_window_in_seconds=60
                )
            ),
            target=target.event_bus_arn,
            target_parameters=pipes.CfnPipe.PipeTargetParametersProperty(
                event_bridge_event_bus_parameters=pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty(
                    detail_type="OrderCreated",
                    source="myapp.orders",
                ),
                input_template=json.dumps({
                    "orderId": "<$.body.orderId>",
                    "customerId": "<$.body.customerId>",
                })
            )
        )
        
        # Output
        CfnOutput(self, "QUEUE_URL", value=source.queue_url)
        CfnOutput(self, "PIPE_ARN", value=pipe.attr_arn)