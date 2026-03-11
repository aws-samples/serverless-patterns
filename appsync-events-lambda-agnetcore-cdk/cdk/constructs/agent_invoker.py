"""CDK Construct for the Agent Invoker Lambda integrated with AppSync Events.

Thin dispatcher — receives events from AppSync, invokes the stream relay
Lambda asynchronously, and returns immediately.
"""

from aws_cdk import (
    Duration,
    aws_appsync as appsync,
    aws_lambda as lambda_,
)
from constructs import Construct

from cdk.constructs.standard_lambda import StandardLambda


class AgentInvokerConstruct(Construct):
    """Creates the agent invoker Lambda and wires it to an AppSync Event API."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        event_api: appsync.EventApi,
        stream_relay_function: lambda_.IFunction,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_function = StandardLambda(
            self,
            "AgentInvokerLambda",
            handler="index.handler",
            code_path="functions/agent_invoker",
            timeout=Duration.seconds(10),
            environment={
                "STREAM_RELAY_ARN": stream_relay_function.function_arn,
            },
        )

        # Grant permission to invoke the stream relay async
        stream_relay_function.grant_invoke(self.lambda_function.function)

        # Register Lambda as a data source on the Event API
        lambda_ds = event_api.add_lambda_data_source(
            "AgentInvokerDS",
            self.lambda_function.function,
        )

        # Add the chat namespace with direct Lambda integration
        # Validation is handled in the Lambda (direct mode cannot use JS handlers)
        event_api.add_channel_namespace(
            "chat",
            publish_handler_config=appsync.HandlerConfig(
                data_source=lambda_ds,
                direct=True,
                lambda_invoke_type=appsync.LambdaInvokeType.REQUEST_RESPONSE,
            ),
        )
