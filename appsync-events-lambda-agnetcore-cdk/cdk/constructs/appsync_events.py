"""CDK Construct for AppSync Events API used by the chat interface."""

from constructs import Construct
from aws_cdk import (
    CfnOutput,
    aws_appsync as appsync,
    aws_logs as logs,
)


class AppSyncEventsConstruct(Construct):
    """Creates an AppSync Event API with a chat channel namespace."""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Auth provider — using API key for now, swap to Cognito/IAM as needed
        api_key_provider = appsync.AppSyncAuthProvider(
            authorization_type=appsync.AppSyncAuthorizationType.API_KEY,
        )

        # Event API
        self.api = appsync.EventApi(
            self,
            "ChatEventApi",
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

        # Responses namespace — no handler, used by stream relay to publish
        # agent responses without re-triggering the invoker Lambda
        self.api.add_channel_namespace("responses")

        # Outputs
        CfnOutput(self, "EventApiHttpEndpoint", value=self.api.http_dns)
        CfnOutput(self, "EventApiRealtimeEndpoint", value=self.api.realtime_dns)
        CfnOutput(self, "EventApiApiKey", value=self.api.api_keys["Default"].attr_api_key)
