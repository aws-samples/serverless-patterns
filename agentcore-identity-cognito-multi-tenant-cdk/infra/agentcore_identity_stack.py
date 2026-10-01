#!/usr/bin/env python3

from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_iam as iam,
    aws_ecr_assets as ecr_assets,
    aws_bedrockagentcore as bedrockagentcore,
    aws_cognito as cognito,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

# Tenant groups seeded in the Cognito user pool. Each end user belongs to
# exactly one of these groups, which becomes their tenant boundary. The group
# name (minus the "tenant-" prefix) is used as the DynamoDB partition key.
TENANT_GROUPS = ["tenant-acme", "tenant-globex"]
TENANT_GROUP_PREFIX = "tenant-"


class AgentCoreIdentityStack(Stack):
    """Multi-tenant Amazon Bedrock AgentCore Runtime secured by Amazon Cognito.

    Inbound requests are authenticated by AgentCore Identity using a custom JWT
    authorizer that trusts the Cognito user pool. The agent derives the caller's
    tenant from the validated token claims and can only ever read that tenant's
    partition in DynamoDB, giving prompt-injection-resistant tenant isolation.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ------------------------------------------------------------------
        # Amazon Cognito user pool (the inbound OAuth2 / JWT identity provider)
        # ------------------------------------------------------------------
        user_pool = cognito.UserPool(
            self,
            "UserPool",
            user_pool_name=f"{self.stack_name}-user-pool",
            self_sign_up_enabled=False,
            sign_in_aliases=cognito.SignInAliases(username=True),
            password_policy=cognito.PasswordPolicy(min_length=8),
            removal_policy=RemovalPolicy.DESTROY,
        )

        user_pool_client = cognito.UserPoolClient(
            self,
            "UserPoolClient",
            user_pool=user_pool,
            user_pool_client_name=f"{self.stack_name}-client",
            generate_secret=False,
            auth_flows=cognito.AuthFlow(user_password=True),
        )

        # One Cognito group per tenant. The "cognito:groups" claim is included in
        # the access token, so the agent can read it after AgentCore validates
        # the token.
        for group_name in TENANT_GROUPS:
            cognito.CfnUserPoolGroup(
                self,
                f"Group-{group_name}",
                user_pool_id=user_pool.user_pool_id,
                group_name=group_name,
                description=f"Tenant group for {group_name}",
            )

        # ------------------------------------------------------------------
        # Per-tenant data store (pool model: one table, partitioned by tenant)
        # ------------------------------------------------------------------
        tenant_table = dynamodb.Table(
            self,
            "TenantTable",
            partition_key=dynamodb.Attribute(
                name="tenant_id", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="record_id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # ------------------------------------------------------------------
        # Container image for the agent
        # ------------------------------------------------------------------
        agent_image = ecr_assets.DockerImageAsset(
            self,
            "AgentImage",
            directory="./agent-code",
            platform=ecr_assets.Platform.LINUX_ARM64,
        )

        agent_name = f"{self.stack_name.replace('-', '_')}_Agent"

        # ------------------------------------------------------------------
        # Execution role for the AgentCore Runtime
        # ------------------------------------------------------------------
        agent_role = iam.Role(
            self,
            "AgentCoreRole",
            assumed_by=iam.ServicePrincipal(
                "bedrock-agentcore.amazonaws.com",
                conditions={
                    "StringEquals": {"aws:SourceAccount": self.account},
                    "ArnLike": {
                        "aws:SourceArn": f"arn:aws:bedrock-agentcore:{self.region}:{self.account}:*"
                    },
                },
            ),
            inline_policies={
                "AgentCorePolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            sid="ECRImageAccess",
                            actions=[
                                "ecr:BatchGetImage",
                                "ecr:GetDownloadUrlForLayer",
                            ],
                            resources=[agent_image.repository.repository_arn],
                        ),
                        iam.PolicyStatement(
                            sid="ECRTokenAccess",
                            # ecr:GetAuthorizationToken does not support
                            # resource-level permissions.
                            actions=["ecr:GetAuthorizationToken"],
                            resources=["*"],
                        ),
                        iam.PolicyStatement(
                            actions=[
                                "logs:DescribeLogStreams",
                                "logs:CreateLogGroup",
                            ],
                            resources=[
                                f"arn:aws:logs:{self.region}:{self.account}:log-group:/aws/bedrock-agentcore/runtimes/*"
                            ],
                        ),
                        iam.PolicyStatement(
                            actions=["logs:DescribeLogGroups"],
                            resources=[
                                f"arn:aws:logs:{self.region}:{self.account}:log-group:*"
                            ],
                        ),
                        iam.PolicyStatement(
                            actions=["logs:CreateLogStream", "logs:PutLogEvents"],
                            resources=[
                                f"arn:aws:logs:{self.region}:{self.account}:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*"
                            ],
                        ),
                        iam.PolicyStatement(
                            actions=[
                                "xray:PutTraceSegments",
                                "xray:PutTelemetryRecords",
                                "xray:GetSamplingRules",
                                "xray:GetSamplingTargets",
                            ],
                            # X-Ray actions do not support resource-level permissions.
                            resources=["*"],
                        ),
                        iam.PolicyStatement(
                            actions=["cloudwatch:PutMetricData"],
                            resources=["*"],
                            conditions={
                                "StringEquals": {
                                    "cloudwatch:namespace": "bedrock-agentcore"
                                }
                            },
                        ),
                        iam.PolicyStatement(
                            sid="GetAgentAccessToken",
                            actions=[
                                "bedrock-agentcore:GetWorkloadAccessToken",
                                "bedrock-agentcore:GetWorkloadAccessTokenForJWT",
                                "bedrock-agentcore:GetWorkloadAccessTokenForUserId",
                            ],
                            resources=[
                                f"arn:aws:bedrock-agentcore:{self.region}:{self.account}:workload-identity-directory/default",
                                f"arn:aws:bedrock-agentcore:{self.region}:{self.account}:workload-identity-directory/default/workload-identity/{agent_name}-*",
                            ],
                        ),
                        iam.PolicyStatement(
                            sid="BedrockModelInvocation",
                            actions=[
                                "bedrock:InvokeModel",
                                "bedrock:InvokeModelWithResponseStream",
                            ],
                            resources=[
                                "arn:aws:bedrock:*::foundation-model/*",
                                f"arn:aws:bedrock:{self.region}:{self.account}:*",
                            ],
                        ),
                        iam.PolicyStatement(
                            sid="TenantDataAccess",
                            # Table-level access; per-tenant isolation is enforced
                            # in the agent via the validated token's tenant claim.
                            actions=["dynamodb:Query", "dynamodb:GetItem"],
                            resources=[tenant_table.table_arn],
                        ),
                    ]
                )
            },
        )

        # ------------------------------------------------------------------
        # AgentCore Runtime with inbound Cognito JWT authorizer
        # ------------------------------------------------------------------
        discovery_url = (
            f"https://cognito-idp.{self.region}.amazonaws.com/"
            f"{user_pool.user_pool_id}/.well-known/openid-configuration"
        )

        agent_runtime = bedrockagentcore.CfnRuntime(
            self,
            "AgentRuntime",
            agent_runtime_name=agent_name,
            agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri=agent_image.image_uri
                )
            ),
            network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                network_mode="PUBLIC"
            ),
            protocol_configuration="HTTP",
            role_arn=agent_role.role_arn,
            # Forward the inbound Authorization header to the container so the
            # agent can read the validated Cognito JWT and resolve the tenant.
            request_header_configuration=bedrockagentcore.CfnRuntime.RequestHeaderConfigurationProperty(
                request_header_allowlist=["Authorization"]
            ),
            environment_variables={
                "AWS_DEFAULT_REGION": self.region,
                "TENANT_TABLE_NAME": tenant_table.table_name,
                "TENANT_GROUP_PREFIX": TENANT_GROUP_PREFIX,
            },
            authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url=discovery_url,
                    allowed_clients=[user_pool_client.user_pool_client_id],
                )
            ),
        )

        # ------------------------------------------------------------------
        # Outputs
        # ------------------------------------------------------------------
        CfnOutput(self, "UserPoolId", value=user_pool.user_pool_id)
        CfnOutput(self, "UserPoolClientId", value=user_pool_client.user_pool_client_id)
        CfnOutput(self, "AgentRuntimeArn", value=agent_runtime.attr_agent_runtime_arn)
        CfnOutput(self, "TenantTableName", value=tenant_table.table_name)
        CfnOutput(self, "TenantGroups", value=",".join(TENANT_GROUPS))
        CfnOutput(self, "Region", value=self.region)
