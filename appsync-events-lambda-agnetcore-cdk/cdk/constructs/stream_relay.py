"""CDK Construct for the stream relay Lambda.

Consumes the SSE stream from AgentCore Runtime and publishes
chunks to AppSync Events. Invoked asynchronously by the agent invoker.
"""

from aws_cdk import (
    Duration,
    aws_iam as iam,
)
from constructs import Construct

from cdk.constructs.standard_lambda import StandardLambda


class StreamRelayConstruct(Construct):
    """Creates the stream relay Lambda that bridges AgentCore to AppSync Events."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        agent_runtime_arn: str,
        appsync_http_endpoint: str,
        appsync_api_key: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_function = StandardLambda(
            self,
            "StreamRelayLambda",
            handler="index.handler",
            code_path="functions/stream_relay",
            timeout=Duration.minutes(5),
            environment={
                "AGENT_RUNTIME_ARN": agent_runtime_arn,
                "APPSYNC_HTTP_ENDPOINT": appsync_http_endpoint,
                "APPSYNC_API_KEY": appsync_api_key,
            },
        )

        # Grant permission to invoke AgentCore runtime
        self.lambda_function.function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["bedrock-agentcore:InvokeAgentRuntime"],
                resources=[
                    agent_runtime_arn,
                    f"{agent_runtime_arn}/*",
                ],
            ),
        )
