from aws_cdk import (
    CfnOutput,
    Stack,
    aws_events as events,
    aws_events_targets as event_target,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_pipes as pipes,
    aws_sqs as sqs,
)
from constructs import Construct

class EventbridgePipesSqsToMultipleSqsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create queues
        source_queue = sqs.Queue(self, 'source-sqs-queue')
        target_queue_order_created = sqs.Queue(self, 'target-sqs-queue-order-created')
        target_queue_order_updated = sqs.Queue(self, 'target-sqs-queue-order-updated')

        # Create event bus
        event_bus = events.EventBus(self, 'event-bus')

        # Add event bus rule and target for order created queue
        event_rule_order_created = events.Rule(self, 'event-rule-order-created',
            event_bus=event_bus,
            event_pattern=events.EventPattern(
                source=['myapp.orders'],
                detail={
                        'type': ['OrderCreated']
                    },
            ),
        );

        event_rule_order_created.add_target(event_target.SqsQueue(target_queue_order_created, message=events.RuleTargetInput.from_event_path('$.detail')))

        # Add event bus rule and target for order updated queue
        event_rule_order_updated = events.Rule(self, 'event-rule-order-updated',
            event_bus=event_bus,
            event_pattern=events.EventPattern(
                source=['myapp.orders'],
                detail={
                        'type': ['OrderUpdated']
                    },
            ),
        );

        event_rule_order_updated.add_target(event_target.SqsQueue(target_queue_order_updated, message=events.RuleTargetInput.from_event_path('$.detail')))

        # Create Pipe enrichment Lambda function
        enrichment_lambda = _lambda.Function(
            self, 'enrichment-lambda',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='index.handler',
            retry_attempts=0,
        )

        # Create Pipe policies and role
        pipe_source_policy = iam.PolicyStatement(
                actions=['sqs:ReceiveMessage', 'sqs:DeleteMessage', 'sqs:GetQueueAttributes'],
                resources=[source_queue.queue_arn],
                effect=iam.Effect.ALLOW,
        )

        pipe_enrichment_policy = iam.PolicyStatement(
                actions=['lambda:InvokeFunction'],
                resources=[enrichment_lambda.function_arn],
                effect=iam.Effect.ALLOW,
        )

        pipe_target_policy = iam.PolicyStatement(
                actions=['events:PutEvents'],
                resources=[event_bus.event_bus_arn],
                effect=iam.Effect.ALLOW,
        )

        pipe_role = iam.Role(self, 'pipe-role',
            assumed_by=iam.ServicePrincipal('pipes.amazonaws.com'),
        )

        pipe_role.add_to_policy(pipe_source_policy)
        pipe_role.add_to_policy(pipe_target_policy)
        pipe_role.add_to_policy(pipe_enrichment_policy)

        # Create Pipe
        pipe = pipes.CfnPipe(self, "pipe",
            role_arn=pipe_role.role_arn,
            source=source_queue.queue_arn,
            source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                    batch_size=1,
                )
            ),
            enrichment=enrichment_lambda.function_arn,
            target=event_bus.event_bus_arn,
            target_parameters=pipes.CfnPipe.PipeTargetParametersProperty(
                event_bridge_event_bus_parameters=pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty(
                    source="myapp.orders",
                )
            )
        )

        # Output
        CfnOutput(self, "SourceQueueUrl", value=source_queue.queue_url)
        CfnOutput(self, "TargetQueueOrderCreated", value=target_queue_order_created.queue_url)
        CfnOutput(self, "TargetQueueOrderUpdated", value=target_queue_order_updated.queue_url)
        CfnOutput(self, "PIPE_ARN", value=pipe.attr_arn)
