"""Main CDK stack for the AppSync Events + Lambda + AgentCore architecture."""

from aws_cdk import Stack
from cdk_nag import NagSuppressions
from constructs import Construct

from cdk.constructs.chat_service import ChatServiceConstruct
from cdk.constructs.chat_agent import ChatAgentConstruct
from cdk.constructs.stream_relay import StreamRelayConstruct


class ChatStack(Stack):
    """AppSync Events chat stack with Lambda invoker and AgentCore runtime."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.chat_agent = ChatAgentConstruct(
            self,
            "ChatAgent",
            model_id=self.node.try_get_context("model_id"),
        )

        self.stream_relay = StreamRelayConstruct(
            self,
            "StreamRelay",
            agent_runtime_arn=(self.chat_agent.runtime.attr_agent_runtime_arn),
        )

        self.chat_service = ChatServiceConstruct(
            self,
            "ChatService",
            stream_relay_function=(self.stream_relay.standard_lambda.function),
        )

        # Pass AppSync endpoint and API key to the stream relay so it
        # can publish response chunks back to the client.
        self.stream_relay.standard_lambda.function.add_environment(
            "APPSYNC_HTTP_ENDPOINT",
            self.chat_service.api.http_dns,
        )
        self.stream_relay.standard_lambda.function.add_environment(
            "APPSYNC_API_KEY",
            self.chat_service.api.api_keys["Default"].attr_api_key,
        )

        self._add_nag_suppressions()

    def _add_nag_suppressions(self):
        """Add cdk-nag suppressions for CDK-managed resources."""

        for child in self.node.children:
            if child.node.id.startswith("LogRetention"):
                NagSuppressions.add_resource_suppressions(
                    child,
                    [
                        {
                            "id": "AwsSolutions-IAM4",
                            "reason": ("CDK LogRetention custom resource " "uses AWS managed policy."),
                            "applies_to": [
                                "Policy::arn:<AWS::Partition>:iam::aws:" + "policy/service-role/" + "AWSLambdaBasicExecutionRole",
                            ],
                        },
                        {
                            "id": "AwsSolutions-IAM5",
                            "reason": ("CDK LogRetention custom resource " + "requires wildcard to set retention " + "on any log group."),
                            "applies_to": ["Resource::*"],
                        },
                    ],
                    apply_to_children=True,
                )

        NagSuppressions.add_resource_suppressions(
            self.chat_service,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": ("grant_invoke appends :* to allow invocation " "of any version/alias of the target Lambda."),
                    "applies_to": [
                        "Resource::<StreamRelayLambdaFunction" + "0B2B86F8.Arn>:*",
                    ],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": ("AppSync data source grant_invoke appends :* " "for Lambda version/alias invocations."),
                    "applies_to": [
                        "Resource::<ChatServiceAgentInvoker" + "Function8A4AD476.Arn>:*",
                    ],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": ("X-Ray actions do not support " + "resource-level permissions."),
                    "applies_to": ["Resource::*"],
                },
            ],
            apply_to_children=True,
        )

        NagSuppressions.add_resource_suppressions(
            self.stream_relay,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": ("AgentCore runtime ARN requires /* suffix " "for endpoint invocation."),
                    "applies_to": [
                        "Resource::<ChatAgentRuntime" + "C752A686.AgentRuntimeArn>/*",
                    ],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": ("X-Ray actions do not support " "resource-level permissions."),
                    "applies_to": ["Resource::*"],
                },
            ],
            apply_to_children=True,
        )
