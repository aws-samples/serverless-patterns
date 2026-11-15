"""CDK Construct for the chat agent — AgentCore runtime + S3 session bucket.

Creates:
- S3 bucket for conversation session storage (Strands S3SessionManager)
- Docker image from agents/chat/
- IAM role with Bedrock, ECR, CloudWatch, X-Ray, and S3 policies
- CfnRuntime with HTTP protocol and PUBLIC network
"""

import json
from pathlib import Path

from constructs import Construct
from aws_cdk import (
    CfnOutput,
    RemovalPolicy,
    Stack,
    aws_bedrockagentcore as agentcore,
    aws_ecr_assets as ecr_assets,
    aws_iam as iam,
    aws_s3 as s3,
)
from cdk_nag import NagSuppressions

INFERENCE_PROFILES_FILE = Path(__file__).parent / "inference_profiles.json"


def resolve_inference_profile(model_id: str, region: str) -> str:
    """Resolve a base model ID to its cross-region inference profile for the given region.

    Raises ValueError if the model or region is not found in the mapping.
    """
    if not INFERENCE_PROFILES_FILE.exists():
        raise ValueError(f"Inference profiles mapping not found at {INFERENCE_PROFILES_FILE}. ")

    with open(INFERENCE_PROFILES_FILE, encoding="utf-8") as f:
        mappings = json.load(f)

    if model_id not in mappings:
        available = ", ".join(sorted(mappings.keys())) or "(none)"
        raise ValueError(f"Model '{model_id}' not found in inference profiles mapping. Available models: {available}. ")

    region_map = mappings[model_id]
    if region not in region_map:
        available = ", ".join(sorted(region_map.keys()))
        raise ValueError(f"Model '{model_id}' does not support cross-region inference in '{region}'. Supported regions: {available}. ")

    return region_map[region]


class ChatAgentConstruct(Construct):
    """Creates the chat agent runtime with session persistence."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        model_id: str,
        environment_variables: dict = None,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)

        # Resolve base model ID to cross-region inference profile
        inference_profile_id = resolve_inference_profile(model_id, stack.region)

        self.session_bucket = s3.Bucket(
            self,
            "SessionBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
        )

        agent_image = ecr_assets.DockerImageAsset(
            self,
            "AgentImage",
            directory="agents",
            file="chat/Dockerfile",
            platform=ecr_assets.Platform.LINUX_ARM64,
            build_args={"AWS_REGION": stack.region},
            exclude=["**/__pycache__", "**/*.pyc"],
        )

        self.runtime_role = iam.Role(
            self,
            "RuntimeRole",
            assumed_by=iam.ServicePrincipal(
                "bedrock-agentcore.amazonaws.com",
            ),
            inline_policies=self._build_policies(
                stack,
                agent_image,
                self.session_bucket,
            ),
        )

        merged_env = {
            "BEDROCK_MODEL_ID": inference_profile_id,
            "AWS_REGION": stack.region,
            "SESSION_BUCKET": self.session_bucket.bucket_name,
            **(environment_variables or {}),
        }

        # AgentCore Runtime — L1 construct (no L2 available yet)
        runtime_name = f"{stack.stack_name.replace('-', '_')}_chat_agent"
        self.runtime = agentcore.CfnRuntime(
            self,
            "Runtime",
            agent_runtime_name=runtime_name,
            role_arn=self.runtime_role.role_arn,
            agent_runtime_artifact=agentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                container_configuration=agentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri=agent_image.image_uri,
                ),
            ),
            network_configuration=agentcore.CfnRuntime.NetworkConfigurationProperty(
                network_mode="PUBLIC",
            ),
            protocol_configuration="HTTP",
            environment_variables=merged_env,
            description="Chat agent runtime with session persistence",
        )

        CfnOutput(self, "RuntimeArn", value=self.runtime.attr_agent_runtime_arn)
        CfnOutput(self, "RuntimeName", value=runtime_name)
        CfnOutput(
            self,
            "SessionBucketName",
            value=self.session_bucket.bucket_name,
        )

        NagSuppressions.add_resource_suppressions(
            self.session_bucket,
            [
                {
                    "id": "AwsSolutions-S1",
                    "reason": "Access logs not required for sample code.",
                }
            ],
        )

        NagSuppressions.add_resource_suppressions(
            self.runtime_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Bedrock foundation model and inference profile ARNs require wildcards — the model is resolved at synth time from inference_profiles.json.",
                    "applies_to": [
                        "Resource::arn:aws:bedrock:*::foundation-model/*",
                        f"Resource::arn:aws:bedrock:{stack.region}:<AWS::AccountId>:inference-profile/*",
                    ],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": (
                        "ecr:GetAuthorizationToken requires Resource::* (account-wide token, cannot be scoped). "
                        "X-Ray actions (PutTraceSegments, PutTelemetryRecords, GetSamplingRules, GetSamplingTargets) "
                        "do not support resource-level permissions per AWS documentation."
                    ),
                    "applies_to": ["Resource::*"],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "S3 session objects require wildcard suffix for read/write/delete operations.",
                    "applies_to": [
                        "Resource::<ChatAgentSessionBucket56C92AD6.Arn>/*",
                    ],
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "AgentCore runtime log group name is determined at deploy time.",
                    "applies_to": [
                        f"Resource::arn:aws:logs:{stack.region}:<AWS::AccountId>:log-group:/aws/bedrock-agentcore/runtimes/*",
                    ],
                },
            ],
        )

    @staticmethod
    def _build_policies(stack, agent_image, session_bucket):
        """Build IAM inline policies for the runtime."""
        return {
            "Bedrock": iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        actions=[
                            "bedrock:InvokeModel",
                            "bedrock:InvokeModelWithResponseStream",
                        ],
                        resources=[
                            "arn:aws:bedrock:*::foundation-model/*",
                            f"arn:aws:bedrock:{stack.region}:{stack.account}:inference-profile/*",
                        ],
                    ),
                ],
            ),
            "ECR": iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        actions=["ecr:GetAuthorizationToken"],
                        resources=["*"],
                    ),
                    iam.PolicyStatement(
                        actions=[
                            "ecr:BatchGetImage",
                            "ecr:GetDownloadUrlForLayer",
                            "ecr:BatchCheckLayerAvailability",
                        ],
                        resources=[agent_image.repository.repository_arn],
                    ),
                ],
            ),
            "S3Sessions": iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        actions=[
                            "s3:GetObject",
                            "s3:PutObject",
                            "s3:DeleteObject",
                        ],
                        resources=[f"{session_bucket.bucket_arn}/*"],
                    ),
                    iam.PolicyStatement(
                        actions=["s3:ListBucket"],
                        resources=[session_bucket.bucket_arn],
                    ),
                ],
            ),
            "CloudWatchLogs": iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        actions=[
                            "logs:DescribeLogStreams",
                            "logs:CreateLogGroup",
                            "logs:DescribeLogGroups",
                            "logs:CreateLogStream",
                            "logs:PutLogEvents",
                        ],
                        resources=[
                            f"arn:aws:logs:{stack.region}:{stack.account}:log-group:/aws/bedrock-agentcore/runtimes/*",
                        ],
                    ),
                ],
            ),
            "XRay": iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        actions=[
                            "xray:PutTraceSegments",
                            "xray:PutTelemetryRecords",
                            "xray:GetSamplingRules",
                            "xray:GetSamplingTargets",
                        ],
                        resources=["*"],
                    ),
                ],
            ),
        }
