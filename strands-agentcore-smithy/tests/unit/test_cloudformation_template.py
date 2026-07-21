"""Unit tests for CloudFormation template structure.

Requirements: 1.1–1.9, 2.1–2.7, 3.1–3.6, 4.1–4.2, 5.1–5.2, 5.6–5.7, 7.1–7.6
"""

import json
import os

import yaml


# ---------------------------------------------------------------------------
# Custom YAML loader for CloudFormation intrinsic functions
# ---------------------------------------------------------------------------

class _CfnLoader(yaml.SafeLoader):
    pass


def _cfn_tag_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    return None


_CfnLoader.add_multi_constructor("!", _cfn_tag_constructor)

# ---------------------------------------------------------------------------
# Load template once
# ---------------------------------------------------------------------------

_TEMPLATE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "infrastructure", "cloudformation-template.yaml"
)

with open(_TEMPLATE_PATH) as _fh:
    TEMPLATE = yaml.load(_fh, Loader=_CfnLoader)

RESOURCES = TEMPLATE["Resources"]
OUTPUTS = TEMPLATE.get("Outputs", {})

# Parse Smithy model from the official AWS model file (downloaded by deploy script)
_SMITHY_MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "infrastructure", "bedrock-runtime-2023-09-30.json"
)
# Fall back to /tmp if not in infrastructure/
if not os.path.exists(_SMITHY_MODEL_PATH):
    _SMITHY_MODEL_PATH = "/tmp/bedrock-runtime-2023-09-30.json"
with open(_SMITHY_MODEL_PATH) as _smithy_fh:
    _SMITHY_PAYLOAD = _smithy_fh.read()
SMITHY_MODEL = json.loads(_SMITHY_PAYLOAD)


# ===========================================================================
# Gateway configuration tests (Requirements 2.1–2.7)
# ===========================================================================

class TestGatewayConfiguration:
    """Verify AgentCore Gateway resource configuration."""

    def setup_method(self):
        self.gateway = RESOURCES["AgentCoreGateway"]["Properties"]

    def test_protocol_type_is_mcp(self):
        """Req 2.1: ProtocolType must be MCP."""
        assert self.gateway["ProtocolType"] == "MCP"

    def test_authorizer_type_is_custom_jwt(self):
        """Req 2.2: AuthorizerType must be CUSTOM_JWT."""
        assert self.gateway["AuthorizerType"] == "CUSTOM_JWT"

    def test_custom_jwt_authorizer_key_casing(self):
        """Req 2.2: Config block must be nested under AuthorizerConfiguration.CustomJWTAuthorizer."""
        assert "AuthorizerConfiguration" in self.gateway
        auth_config = self.gateway["AuthorizerConfiguration"]
        assert "CustomJWTAuthorizer" in auth_config

    def test_discovery_url_suffix(self):
        """Req 2.3: DiscoveryUrl must end with /.well-known/openid-configuration."""
        url = self.gateway["AuthorizerConfiguration"]["CustomJWTAuthorizer"]["DiscoveryUrl"]
        assert url.endswith("/.well-known/openid-configuration")

    def test_allowed_audience_not_audience(self):
        """Req 2.4: Must use AllowedAudience, not Audience."""
        authorizer = self.gateway["AuthorizerConfiguration"]["CustomJWTAuthorizer"]
        assert "AllowedAudience" in authorizer
        assert "Audience" not in authorizer

    def test_role_arn_not_execution_role_arn(self):
        """Req 2.5: Must use RoleArn, not ExecutionRoleArn."""
        assert "RoleArn" in self.gateway
        assert "ExecutionRoleArn" not in self.gateway

    def test_gateway_target_credential_provider_type(self):
        """Req 2.7: GatewayTarget must use GATEWAY_IAM_ROLE."""
        target = RESOURCES["SmithyTarget"]["Properties"]
        cred_configs = target["CredentialProviderConfigurations"]
        assert isinstance(cred_configs, list)
        assert len(cred_configs) >= 1
        assert cred_configs[0]["CredentialProviderType"] == "GATEWAY_IAM_ROLE"

    def test_target_config_nesting(self):
        """Req 2.6: TargetConfiguration nested as Mcp.SmithyModel with S3."""
        target_config = RESOURCES["SmithyTarget"]["Properties"]["TargetConfiguration"]
        assert "Mcp" in target_config
        assert "SmithyModel" in target_config["Mcp"]
        assert "S3" in target_config["Mcp"]["SmithyModel"]


# ===========================================================================
# Gateway Execution Role tests (Requirements 3.1–3.6)
# ===========================================================================

class TestGatewayExecutionRole:
    """Verify GatewayExecutionRole IAM configuration."""

    def setup_method(self):
        self.role = RESOURCES["GatewayExecutionRole"]["Properties"]
        # Collect all policy statements across all policies
        self.all_statements = []
        for policy in self.role["Policies"]:
            stmts = policy["PolicyDocument"]["Statement"]
            self.all_statements.extend(stmts)
        # Flatten all resource ARNs
        self.all_resources = []
        for stmt in self.all_statements:
            res = stmt.get("Resource", [])
            if isinstance(res, str):
                self.all_resources.append(res)
            elif isinstance(res, list):
                self.all_resources.extend(res)
        # Flatten all actions
        self.all_actions = []
        for stmt in self.all_statements:
            actions = stmt.get("Action", [])
            if isinstance(actions, str):
                self.all_actions.append(actions)
            elif isinstance(actions, list):
                self.all_actions.extend(actions)

    def test_trust_policy_principal(self):
        """Trust policy must allow bedrock-agentcore.amazonaws.com."""
        trust = self.role["AssumeRolePolicyDocument"]
        principals = []
        for stmt in trust["Statement"]:
            svc = stmt.get("Principal", {}).get("Service", "")
            if isinstance(svc, str):
                principals.append(svc)
            elif isinstance(svc, list):
                principals.extend(svc)
        assert "bedrock-agentcore.amazonaws.com" in principals

    def test_token_vault_default_arn(self):
        """Req 3.1: Must include token-vault/default ARN pattern."""
        assert any("token-vault/default" in r and "apikeycredentialprovider" not in r
                    for r in self.all_resources)

    def test_apikeycredentialprovider_wildcard_arn(self):
        """Req 3.2: Must include apikeycredentialprovider/* ARN pattern."""
        assert any("apikeycredentialprovider/*" in r for r in self.all_resources)

    def test_workload_identity_directory_default_arn(self):
        """Req 3.3: Must include workload-identity-directory/default ARN."""
        assert any(
            "workload-identity-directory/default" in r
            and "workload-identity" not in r.split("workload-identity-directory/default")[1][:1]
            or r.endswith("workload-identity-directory/default")
            for r in self.all_resources
        )

    def test_workload_identity_wildcard_arn(self):
        """Req 3.4: Must include workload-identity-directory/default/workload-identity/{gateway}-* ARN."""
        assert any(
            "workload-identity-directory/default/workload-identity/" in r
            for r in self.all_resources
        )

    def test_bedrock_runtime_permissions(self):
        """Req 3.5: Must include bedrock:InvokeModel."""
        required_actions = {"bedrock:InvokeModel"}
        assert required_actions.issubset(set(self.all_actions))

    def test_no_apigateway_get_permission(self):
        """Req 3.6: Must NOT include apigateway:GET."""
        for action in self.all_actions:
            assert "apigateway" not in action.lower()


# ===========================================================================
# Smithy model tests (Requirements 1.1–1.9)
# ===========================================================================

class TestSmithyModel:
    """Verify inline Smithy model structure."""

    def setup_method(self):
        self.shapes = SMITHY_MODEL["shapes"]
        # Find service shape
        self.service = None
        for key, shape in self.shapes.items():
            if shape.get("type") == "service":
                self.service = shape
                self.service_key = key
                break

    def test_smithy_version(self):
        """Smithy model must be version 2.0."""
        assert SMITHY_MODEL["smithy"] == "2.0"

    def test_service_has_restjson1_trait(self):
        """Req 1.1: Service must have aws.protocols#restJson1 trait."""
        assert "aws.protocols#restJson1" in self.service.get("traits", {})

    def test_service_version(self):
        """Service must have a version string."""
        assert self.service["version"] is not None
        assert len(self.service["version"]) > 0

    def test_defines_invoke_model_operation(self):
        """Must define InvokeModel with POST method."""
        op = self.shapes["com.amazonaws.bedrockruntime#InvokeModel"]
        http = op["traits"]["smithy.api#http"]
        assert http["method"] == "POST"
        assert "/model/" in http["uri"]

    def test_has_operations(self):
        """Service must define operations (via resources)."""
        resources = self.service.get("resources", [])
        assert len(resources) > 0

    def test_model_under_10mb(self):
        """Req 1.8: Smithy model must be under 10MB."""
        assert len(_SMITHY_PAYLOAD.encode("utf-8")) < 10 * 1024 * 1024


# ===========================================================================
# Lambda configuration tests (Requirements 5.1, 5.2, 5.6, 5.7)
# ===========================================================================

class TestLambdaConfiguration:
    """Verify Agent Lambda Function resource configuration."""

    def setup_method(self):
        self.lambda_props = RESOURCES["AgentLambdaFunction"]["Properties"]
        self.lambda_role = RESOURCES["AgentLambdaRole"]["Properties"]
        # Collect all actions from Lambda role policies
        self.all_actions = []
        for policy in self.lambda_role["Policies"]:
            for stmt in policy["PolicyDocument"]["Statement"]:
                actions = stmt.get("Action", [])
                if isinstance(actions, str):
                    self.all_actions.append(actions)
                elif isinstance(actions, list):
                    self.all_actions.extend(actions)

    def test_runtime_python312(self):
        """Req 5.1: Runtime must be python3.12."""
        assert self.lambda_props["Runtime"] == "python3.12"

    def test_architecture_x86_64(self):
        """Req 5.1: Architecture must be x86_64."""
        assert "x86_64" in self.lambda_props["Architectures"]

    def test_timeout_at_least_120(self):
        """Req 5.2: Timeout must be >= 120 seconds."""
        assert self.lambda_props["Timeout"] >= 120

    def test_memory_at_least_1024(self):
        """Req 5.2: MemorySize must be >= 1024 MB."""
        assert self.lambda_props["MemorySize"] >= 1024

    def test_bedrock_invoke_permissions(self):
        """Req 5.6: Must have bedrock:InvokeModel and related permissions."""
        required = {
            "bedrock:InvokeModel",
            "bedrock:InvokeModelWithResponseStream",
            "bedrock:Converse",
            "bedrock:ConverseStream",
        }
        assert required.issubset(set(self.all_actions))

    def test_agentcore_invoke_gateway_permission(self):
        """Req 5.7: Must have bedrock-agentcore:InvokeGateway permission."""
        assert "bedrock-agentcore:InvokeGateway" in self.all_actions

    def test_cloudwatch_logs_permissions(self):
        """Lambda role must have CloudWatch Logs permissions."""
        required = {"logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"}
        assert required.issubset(set(self.all_actions))


# ===========================================================================
# Cognito configuration tests (Requirements 4.1, 4.2)
# ===========================================================================

class TestCognitoConfiguration:
    """Verify Cognito User Pool and Client configuration."""

    def test_user_pool_exists(self):
        """Req 4.1: CognitoUserPool resource must exist."""
        assert "CognitoUserPool" in RESOURCES
        assert RESOURCES["CognitoUserPool"]["Type"] == "AWS::Cognito::UserPool"

    def test_user_pool_client_exists(self):
        """Req 4.2: CognitoUserPoolClient resource must exist."""
        assert "CognitoUserPoolClient" in RESOURCES
        assert RESOURCES["CognitoUserPoolClient"]["Type"] == "AWS::Cognito::UserPoolClient"

    def test_user_password_auth_flow(self):
        """Req 4.1: Must include USER_PASSWORD_AUTH explicit auth flow."""
        client_props = RESOURCES["CognitoUserPoolClient"]["Properties"]
        assert "USER_PASSWORD_AUTH" in client_props["ExplicitAuthFlows"]


# ===========================================================================
# No forbidden resources (Requirements 7.4, 7.5)
# ===========================================================================

class TestNoForbiddenResources:
    """Verify template does not contain forbidden resource types."""

    def test_no_api_gateway_resources(self):
        """Req 7.4: No AWS::ApiGateway::* or AWS::ApiGatewayV2::* resources."""
        for name, res in RESOURCES.items():
            rtype = res.get("Type", "")
            assert not rtype.startswith("AWS::ApiGateway::"), (
                f"Found API Gateway v1 resource: {name}"
            )
            assert not rtype.startswith("AWS::ApiGatewayV2::"), (
                f"Found API Gateway v2 resource: {name}"
            )

    def test_no_secrets_manager_resources(self):
        """Req 7.5: No AWS::SecretsManager::Secret resources."""
        for name, res in RESOURCES.items():
            rtype = res.get("Type", "")
            assert not rtype.startswith("AWS::SecretsManager::"), (
                f"Found Secrets Manager resource: {name}"
            )


# ===========================================================================
# Stack outputs (Requirement 7.6)
# ===========================================================================

class TestStackOutputs:
    """Verify required stack outputs are defined."""

    def test_gateway_id_output(self):
        assert "GatewayId" in OUTPUTS

    def test_cognito_user_pool_id_output(self):
        assert "CognitoUserPoolId" in OUTPUTS

    def test_cognito_client_id_output(self):
        assert "CognitoClientId" in OUTPUTS

    def test_lambda_function_name_output(self):
        assert "LambdaFunctionName" in OUTPUTS
