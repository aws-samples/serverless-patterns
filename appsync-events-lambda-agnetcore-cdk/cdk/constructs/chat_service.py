"""CDK Construct for the AppSync Events API and its chat handler Lambda.

Creates:
- AppSync Event API with API key auth
- Agent invoker Lambda (thin dispatcher) wired as a direct Lambda
  integration on the ``chat`` channel namespace
- Responses namespace for outbound streaming (no handler)
"""

from constructs import Construct
from aws_cdk import (
    CfnOutput,
    Duration,
    aws_appsync as appsync,
    aws_lambda as lambda_,
    aws_logs as logs,
)
from cdk_nag import NagSuppressions

from cdk.constructs.standard_lambda import StandardLambda


class ChatServiceConstruct(Construct):
    """AppSync Event API with an integrated chat handler Lambda."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        stream_relay_function: lambda_.IFunction,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api_key_provider = appsync.AppSyncAuthProvider(
            authorization_type=appsync.AppSyncAuthorizationType.API_KEY,
        )

        self.api = appsync.EventApi(
            self,
            "EventApi",
            api_name="ChatEventApi",
            authorization_config=appsync.EventApiAuthConfig(
                auth_providers=[api_key_provider],
                connection_auth_mode_types=[
                    appsync.AppSyncAuthorizationType.API_KEY,
                ],
                default_publish_auth_mode_types=[
                    appsync.AppSyncAuthorizationType.API_KEY,
                ],
                default_subscribe_auth_mode_types=[
                    appsync.AppSyncAuthorizationType.API_KEY,
                ],
            ),
            log_config=appsync.AppSyncLogConfig(
                field_log_level=appsync.AppSyncFieldLogLevel.INFO,
                retention=logs.RetentionDays.ONE_WEEK,
            ),
        )

        # Separate "responses" namespace for outbound streaming — avoids
        # re-invocation loops where the Lambda's own publishes would
        # re-trigger the invoker.
        self.api.add_channel_namespace("responses")

        self.agent_invoker = StandardLambda(
            self,
            "AgentInvoker",
            handler="index.handler",
            code_path="functions/agent_invoker",
            timeout=Duration.seconds(10),
            environment={
                "STREAM_RELAY_ARN": stream_relay_function.function_arn,
            },
        )

        stream_relay_function.grant_invoke(
            self.agent_invoker.function,
        )

        lambda_ds = self.api.add_lambda_data_source(
            "AgentInvokerDS",
            self.agent_invoker.function,
        )

        # "chat" namespace with direct Lambda integration — AppSync invokes
        # the agent invoker Lambda synchronously on each publish.
        self.api.add_channel_namespace(
            "chat",
            publish_handler_config=appsync.HandlerConfig(
                data_source=lambda_ds,
                direct=True,
                lambda_invoke_type=(appsync.LambdaInvokeType.REQUEST_RESPONSE),
            ),
        )

        CfnOutput(
            self,
            "EventApiHttpEndpoint",
            value=self.api.http_dns,
        )
        CfnOutput(
            self,
            "EventApiRealtimeEndpoint",
            value=self.api.realtime_dns,
        )
        CfnOutput(
            self,
            "EventApiApiKey",
            value=self.api.api_keys["Default"].attr_api_key,
        )

        NagSuppressions.add_resource_suppressions(
            self.api,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": ("AWSAppSyncPushToCloudWatchLogs is the standard " "managed policy for AppSync API logging."),
                    "applies_to": [
                        "Policy::arn:<AWS::Partition>:iam::aws:policy/" "service-role/AWSAppSyncPushToCloudWatchLogs",
                    ],
                },
            ],
            apply_to_children=True,
        )
