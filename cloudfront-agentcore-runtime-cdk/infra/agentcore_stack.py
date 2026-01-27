#!/usr/bin/env python3

from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_iam as iam,
    aws_ecr_assets as ecr_assets,
    aws_bedrockagentcore as bedrockagentcore,
    aws_cognito as cognito,
)
from constructs import Construct


class AgentcoreStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        user_pool = cognito.UserPool(self, "UserPool",
            user_pool_name=f"{self.stack_name}-user-pool",
            self_sign_up_enabled=False,
            sign_in_aliases=cognito.SignInAliases(username=True),
            password_policy=cognito.PasswordPolicy(min_length=8),
            removal_policy=RemovalPolicy.DESTROY
        )

        user_pool_client = cognito.UserPoolClient(self, "UserPoolClient",
            user_pool=user_pool,
            user_pool_client_name=f"{self.stack_name}-client",
            generate_secret=False,
            auth_flows=cognito.AuthFlow(user_password=True, custom=True)
        )

        a2a_docker_image = ecr_assets.DockerImageAsset(self, "A2aAgentImage",
            directory="./agent-code/a2a",
            platform=ecr_assets.Platform.LINUX_ARM64
        )

        http_docker_image = ecr_assets.DockerImageAsset(self, "HttpAgentImage",
            directory="./agent-code/http",
            platform=ecr_assets.Platform.LINUX_ARM64
        )

        mcp_docker_image = ecr_assets.DockerImageAsset(self, "McpAgentImage",
            directory="./agent-code/mcp",
            platform=ecr_assets.Platform.LINUX_ARM64
        )

        a2a_agent_name = f"{self.stack_name.replace('-', '_')}_A2a_Agent"

        agent_role = iam.Role(self, "AgentCoreRole",
            assumed_by=iam.ServicePrincipal("bedrock-agentcore.amazonaws.com",
                conditions={
                    "StringEquals": {"aws:SourceAccount": self.account},
                    "ArnLike": {"aws:SourceArn": f"arn:aws:bedrock-agentcore:{self.region}:{self.account}:*"}
                }
            ),
            inline_policies={
                "AgentCorePolicy": iam.PolicyDocument(statements=[
                    iam.PolicyStatement(
                        sid="ECRImageAccess",
                        actions=["ecr:BatchGetImage", "ecr:GetDownloadUrlForLayer"],
                        resources=[a2a_docker_image.repository.repository_arn, http_docker_image.repository.repository_arn, mcp_docker_image.repository.repository_arn]
                    ),
                    iam.PolicyStatement(
                        sid="ECRTokenAccess",
                        actions=["ecr:GetAuthorizationToken"],
                        resources=["*"]
                    ),
                    iam.PolicyStatement(
                        actions=["logs:DescribeLogStreams", "logs:CreateLogGroup"],
                        resources=[f"arn:aws:logs:{self.region}:{self.account}:log-group:/aws/bedrock-agentcore/runtimes/*"]
                    ),
                    iam.PolicyStatement(
                        actions=["logs:DescribeLogGroups"],
                        resources=[f"arn:aws:logs:{self.region}:{self.account}:log-group:*"]
                    ),
                    iam.PolicyStatement(
                        actions=["logs:CreateLogStream", "logs:PutLogEvents"],
                        resources=[f"arn:aws:logs:{self.region}:{self.account}:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*"]
                    ),
                    iam.PolicyStatement(
                        actions=["xray:PutTraceSegments", "xray:PutTelemetryRecords", "xray:GetSamplingRules", "xray:GetSamplingTargets"],
                        resources=["*"]
                    ),
                    iam.PolicyStatement(
                        actions=["cloudwatch:PutMetricData"],
                        resources=["*"],
                        conditions={"StringEquals": {"cloudwatch:namespace": "bedrock-agentcore"}}
                    ),
                    iam.PolicyStatement(
                        sid="GetAgentAccessToken",
                        actions=["bedrock-agentcore:GetWorkloadAccessToken", "bedrock-agentcore:GetWorkloadAccessTokenForJWT", "bedrock-agentcore:GetWorkloadAccessTokenForUserId"],
                        resources=[
                            f"arn:aws:bedrock-agentcore:{self.region}:{self.account}:workload-identity-directory/default",
                            f"arn:aws:bedrock-agentcore:{self.region}:{self.account}:workload-identity-directory/default/workload-identity/{a2a_agent_name}-*"
                        ]
                    ),
                    iam.PolicyStatement(
                        sid="BedrockModelInvocation",
                        actions=["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
                        resources=["arn:aws:bedrock:*::foundation-model/*", f"arn:aws:bedrock:{self.region}:{self.account}:*"]
                    )
                ])
            }
        )

        discovery_url = f"https://cognito-idp.{self.region}.amazonaws.com/{user_pool.user_pool_id}/.well-known/openid-configuration"

        a2a_agent_runtime = bedrockagentcore.CfnRuntime(self, "AgentRuntime",
            agent_runtime_name=a2a_agent_name,
            agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri=a2a_docker_image.image_uri
                )
            ),
            network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(network_mode="PUBLIC"),
            protocol_configuration="A2A",
            role_arn=agent_role.role_arn,
            environment_variables={"AWS_DEFAULT_REGION": self.region},
            authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url=discovery_url,
                    allowed_clients=[user_pool_client.user_pool_client_id]
                )
            )
        )

        http_agent_name = f"{self.stack_name.replace('-', '_')}_Http_Agent"
        http_agent_runtime = bedrockagentcore.CfnRuntime(self, "HttpAgentRuntime",
            agent_runtime_name=http_agent_name,
            agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri=http_docker_image.image_uri
                )
            ),
            network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(network_mode="PUBLIC"),
            protocol_configuration="HTTP",
            role_arn=agent_role.role_arn,
            environment_variables={"AWS_DEFAULT_REGION": self.region},
            authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url=discovery_url,
                    allowed_clients=[user_pool_client.user_pool_client_id]
                )
            )
        )

        mcp_agent_name = f"{self.stack_name.replace('-', '_')}_Mcp_Agent"
        mcp_agent_runtime = bedrockagentcore.CfnRuntime(self, "McpAgentRuntime",
            agent_runtime_name=mcp_agent_name,
            agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri=mcp_docker_image.image_uri
                )
            ),
            network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(network_mode="PUBLIC"),
            protocol_configuration="MCP",
            role_arn=agent_role.role_arn,
            environment_variables={"AWS_DEFAULT_REGION": self.region},
            authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url=discovery_url,
                    allowed_clients=[user_pool_client.user_pool_client_id]
                )
            )
        )

        self.a2a_agent_runtime_arn = a2a_agent_runtime.attr_agent_runtime_arn
        self.http_agent_runtime_arn = http_agent_runtime.attr_agent_runtime_arn
        self.mcp_agent_runtime_arn = mcp_agent_runtime.attr_agent_runtime_arn

        CfnOutput(self, "A2aAgentRuntimeArn", value=a2a_agent_runtime.attr_agent_runtime_arn)
        CfnOutput(self, "HttpAgentRuntimeArn", value=http_agent_runtime.attr_agent_runtime_arn)
        CfnOutput(self, "McpAgentRuntimeArn", value=mcp_agent_runtime.attr_agent_runtime_arn)
        CfnOutput(self, "UserPoolId", value=user_pool.user_pool_id)
        CfnOutput(self, "UserPoolClientId", value=user_pool_client.user_pool_client_id)
        CfnOutput(self, "CognitoDiscoveryUrl", value=f"https://cognito-idp.{self.region}.amazonaws.com/{user_pool.user_pool_id}/.well-known/openid-configuration")
