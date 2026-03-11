"""Main CDK stack for the AppSync Events + Lambda + AgentCore architecture."""

from aws_cdk import Stack
from cdk_nag import NagSuppressions
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

        self._add_nag_suppressions()

    def _add_nag_suppressions(self):
        """Add cdk-nag suppressions for CDK-managed resources and grant_invoke wildcards."""

        # CDK's LogRetention custom resource Lambda — managed by CDK, not user code.
        # Suppress by finding the LogRetention singleton via node tree traversal
        # to avoid hardcoding the hash suffix in the construct path.
        for child in self.node.children:
            if child.node.id.startswith("LogRetention"):
                NagSuppressions.add_resource_suppressions(
                    child,
                    [
                        {
                            "id": "AwsSolutions-IAM4",
                            "reason": "CDK LogRetention custom resource uses AWS managed policy.",
                            "applies_to": [
                                "Policy::arn:<AWS::Partition>:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
                            ],
                        },
                        {
                            "id": "AwsSolutions-IAM5",
                            "reason": "CDK LogRetention custom resource requires wildcard to set retention on any log group.",
                            "applies_to": ["Resource::*"],
                        },
                    ],
                    apply_to_children=True,
                )

        # grant_invoke adds :* suffix for Lambda version/alias invocations.
        # The finding string includes the target Lambda's logical ID.
        NagSuppressions.add_resource_suppressions(
            self.agent_invoker,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "grant_invoke appends :* to allow invocation of any version/alias of the target Lambda.",
                    "applies_to": [
                        "Resource::<StreamRelayStreamRelayLambdaFunctionADAD4480.Arn>:*",
                    ],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "X-Ray actions do not support resource-level permissions.",
                    "applies_to": ["Resource::*"],
                },
            ],
            apply_to_children=True,
        )

        # AppSync data source role for invoking the agent invoker Lambda
        NagSuppressions.add_resource_suppressions(
            self.appsync_events,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "AppSync data source grant_invoke appends :* for Lambda version/alias invocations.",
                    "applies_to": [
                        "Resource::<AgentInvokerAgentInvokerLambdaFunction601F4165.Arn>:*",
                    ],
                },
            ],
            apply_to_children=True,
        )

        # Stream relay: AgentCore runtime ARN wildcard and X-Ray permissions
        NagSuppressions.add_resource_suppressions(
            self.stream_relay,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "AgentCore runtime ARN requires /* suffix for endpoint invocation.",
                    "applies_to": [
                        "Resource::<AgentCoreRuntime00AE1E64.AgentRuntimeArn>/*",
                    ],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "X-Ray actions do not support resource-level permissions.",
                    "applies_to": ["Resource::*"],
                },
            ],
            apply_to_children=True,
        )
