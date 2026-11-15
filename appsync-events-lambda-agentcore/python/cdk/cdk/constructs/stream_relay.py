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
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.standard_lambda = StandardLambda(
            self,
            "Lambda",
            handler="index.handler",
            code_path="functions/stream_relay",
            timeout=Duration.minutes(5),
            environment={
                "AGENT_RUNTIME_ARN": agent_runtime_arn,
            },
        )

        # Grant permission to invoke AgentCore runtime
        self.standard_lambda.function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["bedrock-agentcore:InvokeAgentRuntime"],
                resources=[
                    agent_runtime_arn,
                    f"{agent_runtime_arn}/*",
                ],
            ),
        )
