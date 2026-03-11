"""Main CDK stack for the AppSync Events + Lambda + AgentCore architecture."""

from aws_cdk import Stack
from constructs import Construct

from cdk.constructs.appsync_events import AppSyncEventsConstruct
from cdk.constructs.agent_invoker import AgentInvokerConstruct
from cdk.constructs.chat_agent import ChatAgentConstruct
from cdk.constructs.stream_relay import StreamRelayConstruct


class CdkStack(Stack):
    """AppSync Events chat stack with Lambda invoker and AgentCore runtime."""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.appsync_events = AppSyncEventsConstruct(self, "AppSyncEvents")

        self.chat_agent = ChatAgentConstruct(
            self,
            "AgentCoreRuntime",
            model_id=self.node.try_get_context("model_id"),
        )

        self.stream_relay = StreamRelayConstruct(
            self,
            "StreamRelay",
            agent_runtime_arn=self.chat_agent.runtime.attr_agent_runtime_arn,
            appsync_http_endpoint=self.appsync_events.api.http_dns,
            appsync_api_key=self.appsync_events.api.api_keys["Default"].attr_api_key,
        )

        self.agent_invoker = AgentInvokerConstruct(
            self,
            "AgentInvoker",
            event_api=self.appsync_events.api,
            stream_relay_function=self.stream_relay.lambda_function.function,
        )
