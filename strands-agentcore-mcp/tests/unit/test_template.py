"""SAM template assertion tests.

Loads infrastructure/template.yaml (the AWS SAM template) and asserts the
structural / casing / configuration requirements from the sam-migration spec.

These tests guard against:
  - SAM-transform regressions (Transform directive, AWS::Serverless::Function,
    BuildMethod: makefile, no inline ZipFile, no Lambda Layer)
  - AgentCore Gateway property casing that has bitten this project before
    (see .kiro/steering/project-conventions.md)
  - IAM least-privilege scoping (no wildcard Resource, ARN-scoped policies)
  - The MCP API authorization model (NONE + AWS_PROXY + scoped permission)
  - Stack outputs consumed by downstream tooling (incl. GatewayId)

Validates: Requirements 1.1, 1.2, 2.3, 2.4, 2.6, 3.1, 5.1-5.6, 6.1-6.4,
7.1-7.3, 9.x, 12.1-12.3, 13.1
"""

import os
import re
from typing import Any, Dict, List

import pytest
import yaml

# ---------------------------------------------------------------------------
# CloudFormation tag constructors — allow yaml.safe_load to handle !Ref,
# !Sub, !GetAtt, !If, !Select, !Join, !Split, !Equals, !Not, !And, !Or
# ---------------------------------------------------------------------------

def _cfn_tag_constructor(loader, tag_suffix, node):
    """Generic constructor that returns a dict {tag: value} for any CFN tag."""
    if isinstance(node, yaml.ScalarNode):
        return {tag_suffix: loader.construct_scalar(node)}
    elif isinstance(node, yaml.SequenceNode):
        return {tag_suffix: loader.construct_sequence(node, deep=True)}
    elif isinstance(node, yaml.MappingNode):
        return {tag_suffix: loader.construct_mapping(node, deep=True)}
    return {tag_suffix: None}


class CloudFormationLoader(yaml.SafeLoader):
    pass


for _tag in ("!Ref", "!Sub", "!GetAtt", "!If", "!Select", "!Join",
             "!Split", "!Equals", "!Not", "!And", "!Or", "!Base64",
             "!Condition", "!FindInMap", "!ImportValue", "!Transform"):
    CloudFormationLoader.add_multi_constructor(
        _tag, lambda loader, tag_suffix, node, t=_tag: _cfn_tag_constructor(
            loader, t, node
        )
    )


# ---------------------------------------------------------------------------
# Fixture: load the SAM template once per session
# ---------------------------------------------------------------------------

TEMPLATE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "infrastructure", "template.yaml"
)


@pytest.fixture(scope="session")
def template() -> Dict[str, Any]:
    """Load and parse the SAM template."""
    with open(TEMPLATE_PATH, "r") as fh:
        return yaml.load(fh, Loader=CloudFormationLoader)


@pytest.fixture(scope="session")
def resources(template) -> Dict[str, Any]:
    return template["Resources"]


@pytest.fixture(scope="session")
def template_text() -> str:
    with open(TEMPLATE_PATH, "r") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _collect_all_statements(policies: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Flatten all policy statements from a list of inline policies."""
    stmts: List[Dict[str, Any]] = []
    for policy in policies:
        doc = policy.get("PolicyDocument", {})
        statement = doc.get("Statement", [])
        if isinstance(statement, dict):
            statement = [statement]
        stmts.extend(statement)
    return stmts


def _resource_strings(resource_value) -> List[str]:
    """Return a list of resource strings from a Resource field (str/list/dict)."""
    if isinstance(resource_value, str):
        return [resource_value]
    if isinstance(resource_value, list):
        result = []
        for r in resource_value:
            if isinstance(r, str):
                result.append(r)
            elif isinstance(r, dict):
                # !Sub / !GetAtt dict — get the template string
                result.append(list(r.values())[0])
        return result
    if isinstance(resource_value, dict):
        return [list(resource_value.values())[0]]
    return []


def _actions_list(stmt: Dict[str, Any]) -> List[str]:
    actions = stmt.get("Action", [])
    if isinstance(actions, str):
        return [actions]
    return list(actions)


def _all_role_logical_ids() -> List[str]:
    return ["AgentLambdaRole", "McpServerRole", "GatewayExecutionRole"]


def _sub_value(value):
    """Extract the underlying string from a scalar or a !Sub/!GetAtt dict.

    For !Sub with a [template, vars] list form, returns the template string.
    """
    if isinstance(value, dict):
        inner = list(value.values())[0]
        if isinstance(inner, list):
            return inner[0]
        return inner
    return value


# ---------------------------------------------------------------------------
# 1. SAM Transform directive (Requirement 1.1)
# ---------------------------------------------------------------------------

def test_transform_directive_present(template):
    """Template must declare the SAM transform AWS::Serverless-2016-10-31."""
    transform = template.get("Transform")
    transforms = transform if isinstance(transform, list) else [transform]
    assert "AWS::Serverless-2016-10-31" in transforms, (
        f"Template must declare Transform: AWS::Serverless-2016-10-31, "
        f"got {transform!r}"
    )


# ---------------------------------------------------------------------------
# 2. Both Lambda functions are AWS::Serverless::Function (Requirement 1.2)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("logical_id", ["AgentLambdaFunction", "McpServerLambda"])
def test_function_is_serverless_function(resources, logical_id):
    """Both Lambda functions must be AWS::Serverless::Function resources."""
    assert resources[logical_id]["Type"] == "AWS::Serverless::Function", (
        f"{logical_id} must be Type AWS::Serverless::Function, "
        f"got {resources[logical_id]['Type']!r}"
    )


# ---------------------------------------------------------------------------
# 3. Metadata.BuildMethod: makefile on both functions (Requirement 1.2, 9.x)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("logical_id", ["AgentLambdaFunction", "McpServerLambda"])
def test_function_build_method_makefile(resources, logical_id):
    """Each function must declare Metadata.BuildMethod: makefile (Docker-free build)."""
    metadata = resources[logical_id].get("Metadata", {})
    assert metadata.get("BuildMethod") == "makefile", (
        f"{logical_id} must declare Metadata.BuildMethod: makefile, "
        f"got {metadata.get('BuildMethod')!r}"
    )


# ---------------------------------------------------------------------------
# 4. Handler paths (Requirement 2.3, 2.4)
# ---------------------------------------------------------------------------

def test_agent_lambda_handler_path(resources):
    """AgentLambdaFunction must use handler src.agent.handler.lambda_handler."""
    fn_props = resources["AgentLambdaFunction"]["Properties"]
    assert fn_props.get("Handler") == "src.agent.handler.lambda_handler", (
        f"AgentLambdaFunction handler must be 'src.agent.handler.lambda_handler', "
        f"got {fn_props.get('Handler')!r}"
    )


def test_mcp_server_lambda_handler_path(resources):
    """McpServerLambda must use handler src.mcp_server.handler.lambda_handler."""
    fn_props = resources["McpServerLambda"]["Properties"]
    assert fn_props.get("Handler") == "src.mcp_server.handler.lambda_handler", (
        f"McpServerLambda handler must be 'src.mcp_server.handler.lambda_handler', "
        f"got {fn_props.get('Handler')!r}"
    )


# ---------------------------------------------------------------------------
# 5. CodeUri points at project root (Requirement 2.2, 9.3)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("logical_id", ["AgentLambdaFunction", "McpServerLambda"])
def test_function_codeuri_is_project_root(resources, logical_id):
    """Each function CodeUri must point at the project root ('../')."""
    fn_props = resources[logical_id]["Properties"]
    code_uri = fn_props.get("CodeUri")
    assert code_uri == "../", (
        f"{logical_id} CodeUri must be '../' (project root), got {code_uri!r}"
    )


# ---------------------------------------------------------------------------
# 6. Timeout / MemorySize (Requirement 9.1, 9.2)
# ---------------------------------------------------------------------------

def test_agent_lambda_sizing(resources):
    """AgentLambdaFunction must declare Timeout 120 and MemorySize 512."""
    fn_props = resources["AgentLambdaFunction"]["Properties"]
    assert fn_props.get("Timeout") == 120, (
        f"AgentLambdaFunction Timeout must be 120, got {fn_props.get('Timeout')!r}"
    )
    assert fn_props.get("MemorySize") == 512, (
        f"AgentLambdaFunction MemorySize must be 512, got {fn_props.get('MemorySize')!r}"
    )


def test_mcp_server_lambda_sizing(resources):
    """McpServerLambda must declare Timeout 30 and MemorySize 256."""
    fn_props = resources["McpServerLambda"]["Properties"]
    assert fn_props.get("Timeout") == 30, (
        f"McpServerLambda Timeout must be 30, got {fn_props.get('Timeout')!r}"
    )
    assert fn_props.get("MemorySize") == 256, (
        f"McpServerLambda MemorySize must be 256, got {fn_props.get('MemorySize')!r}"
    )


# ---------------------------------------------------------------------------
# 7. Environment variables (Requirement 9.4, 9.5)
# ---------------------------------------------------------------------------

def test_agent_lambda_env_vars(resources):
    """AgentLambdaFunction must receive the five required env vars."""
    fn_props = resources["AgentLambdaFunction"]["Properties"]
    env_vars = fn_props.get("Environment", {}).get("Variables", {})
    required = {
        "GATEWAY_URL",
        "COGNITO_ISSUER",
        "COGNITO_USER_POOL_ID",
        "COGNITO_CLIENT_ID",
        "BEDROCK_MODEL_ID",
    }
    missing = required - set(env_vars.keys())
    assert not missing, (
        f"AgentLambdaFunction missing env vars: {sorted(missing)}"
    )


def test_mcp_server_lambda_env_vars(resources):
    """McpServerLambda must receive the product table name via PRODUCT_TABLE."""
    fn_props = resources["McpServerLambda"]["Properties"]
    env_vars = fn_props.get("Environment", {}).get("Variables", {})
    assert "PRODUCT_TABLE" in env_vars, (
        "McpServerLambda must declare a PRODUCT_TABLE environment variable"
    )


# ---------------------------------------------------------------------------
# 8. No inline ZipFile code on either function (Requirement 3.1)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("logical_id", ["AgentLambdaFunction", "McpServerLambda"])
def test_function_no_inline_zipfile(resources, logical_id):
    """No function may declare inline Code.ZipFile (real source via SAM build)."""
    fn_props = resources[logical_id]["Properties"]
    code = fn_props.get("Code")
    if isinstance(code, dict):
        assert "ZipFile" not in code, (
            f"{logical_id} must NOT declare inline Code.ZipFile"
        )


# ---------------------------------------------------------------------------
# 9. No Lambda Layer (Requirement 2.6)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("logical_id", ["AgentLambdaFunction", "McpServerLambda"])
def test_function_no_layers(resources, logical_id):
    """No function may declare Layers (dependencies built via makefile, Req 2.6)."""
    fn_props = resources[logical_id]["Properties"]
    assert "Layers" not in fn_props, (
        f"{logical_id} must NOT declare Layers — no shared Lambda Layer"
    )


def test_no_lambda_layer_resources(resources):
    """No AWS::Serverless::LayerVersion or AWS::Lambda::LayerVersion resources."""
    layer_types = {"AWS::Serverless::LayerVersion", "AWS::Lambda::LayerVersion"}
    layers = [lid for lid, r in resources.items() if r.get("Type") in layer_types]
    assert not layers, f"Template must not declare Lambda Layer resources: {layers}"


# ---------------------------------------------------------------------------
# 10. Each function references its explicit role via Role: !GetAtt <Role>.Arn
#     and the three named roles exist (Requirement 6, design decision)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "logical_id,role_id",
    [
        ("AgentLambdaFunction", "AgentLambdaRole"),
        ("McpServerLambda", "McpServerRole"),
    ],
)
def test_function_references_explicit_role(resources, logical_id, role_id):
    """Each function must reference its explicit role via Role: !GetAtt <Role>.Arn."""
    fn_props = resources[logical_id]["Properties"]
    role = fn_props.get("Role")
    assert isinstance(role, dict), (
        f"{logical_id} must declare an explicit Role via !GetAtt, got {role!r}"
    )
    getatt_val = role.get("!GetAtt")
    assert getatt_val is not None, (
        f"{logical_id} Role must use !GetAtt <Role>.Arn, got {role!r}"
    )
    if isinstance(getatt_val, list):
        assert getatt_val == [role_id, "Arn"], (
            f"{logical_id} Role must be !GetAtt {role_id}.Arn, got {getatt_val!r}"
        )
    else:
        assert getatt_val == f"{role_id}.Arn", (
            f"{logical_id} Role must be !GetAtt {role_id}.Arn, got {getatt_val!r}"
        )


def test_named_roles_exist_with_policies(resources):
    """The three named IAM roles must exist with scoped inline policies."""
    for role_id in _all_role_logical_ids():
        assert role_id in resources, f"Template must declare role {role_id}"
        role = resources[role_id]
        assert role["Type"] == "AWS::IAM::Role", (
            f"{role_id} must be Type AWS::IAM::Role"
        )
        policies = role["Properties"].get("Policies", [])
        assert len(policies) >= 1, (
            f"{role_id} must declare at least one scoped inline policy"
        )


# ---------------------------------------------------------------------------
# 11. AgentCore Gateway casing traps (Requirements 5.1-5.6)
# ---------------------------------------------------------------------------

def test_custom_jwt_authorizer_key_exists(resources):
    """AuthorizerConfiguration.CustomJWTAuthorizer must exist (JWT all-caps, Req 5.1)."""
    gw = resources["AgentCoreGateway"]["Properties"]
    auth_config = gw.get("AuthorizerConfiguration", {})
    assert "CustomJWTAuthorizer" in auth_config, (
        "Expected 'CustomJWTAuthorizer' key under AuthorizerConfiguration"
    )


def test_custom_jwt_authorizer_wrong_casing_absent(template_text):
    """CustomJwtAuthorizer (wrong casing) must NOT appear anywhere (Req 5.1)."""
    assert "CustomJwtAuthorizer" not in template_text, (
        "Found 'CustomJwtAuthorizer' (wrong casing) — must be 'CustomJWTAuthorizer'"
    )


def test_gateway_uses_role_arn(resources):
    """AgentCoreGateway must use RoleArn, not ExecutionRoleArn (Req 5.2)."""
    gw_props = resources["AgentCoreGateway"]["Properties"]
    assert "RoleArn" in gw_props, "AgentCoreGateway must have a 'RoleArn' property"
    assert "ExecutionRoleArn" not in gw_props, (
        "AgentCoreGateway must NOT use 'ExecutionRoleArn' — use 'RoleArn'"
    )


def test_allowed_audience_present(resources):
    """CustomJWTAuthorizer must use AllowedAudience, not Audience (Req 5.3)."""
    gw = resources["AgentCoreGateway"]["Properties"]
    jwt_auth = gw["AuthorizerConfiguration"]["CustomJWTAuthorizer"]
    assert "AllowedAudience" in jwt_auth, (
        "CustomJWTAuthorizer must have 'AllowedAudience'"
    )
    assert "Audience" not in jwt_auth, (
        "CustomJWTAuthorizer must use 'AllowedAudience', not bare 'Audience'"
    )


def test_bare_audience_key_absent(template_text):
    """The bare key 'Audience:' (wrong name) must not appear (Req 5.3)."""
    matches = re.findall(r'(?<!Allowed)(?<!\w)Audience:', template_text)
    assert not matches, "Found bare 'Audience:' key — must be 'AllowedAudience'"


def test_discovery_url_ends_with_openid_configuration(resources):
    """DiscoveryUrl must end with /.well-known/openid-configuration (Req 5.5)."""
    gw = resources["AgentCoreGateway"]["Properties"]
    jwt_auth = gw["AuthorizerConfiguration"]["CustomJWTAuthorizer"]
    discovery_url = jwt_auth.get("DiscoveryUrl")
    assert discovery_url is not None, "CustomJWTAuthorizer must have 'DiscoveryUrl'"
    url_str = _sub_value(discovery_url)
    assert url_str.endswith("/.well-known/openid-configuration"), (
        f"DiscoveryUrl must end with '/.well-known/openid-configuration', "
        f"got: {url_str!r}"
    )


def test_gateway_authorizer_type(resources):
    """AgentCoreGateway must have AuthorizerType: CUSTOM_JWT (Req 5.6)."""
    gw_props = resources["AgentCoreGateway"]["Properties"]
    assert gw_props.get("AuthorizerType") == "CUSTOM_JWT", (
        f"AgentCoreGateway must have AuthorizerType: CUSTOM_JWT, "
        f"got {gw_props.get('AuthorizerType')!r}"
    )


def test_gateway_protocol_type(resources):
    """AgentCoreGateway must have ProtocolType: MCP (Req 5.6)."""
    gw_props = resources["AgentCoreGateway"]["Properties"]
    assert gw_props.get("ProtocolType") == "MCP", (
        f"AgentCoreGateway must have ProtocolType: MCP, "
        f"got {gw_props.get('ProtocolType')!r}"
    )


# ---------------------------------------------------------------------------
# 12. IAM no-wildcard + ARN scoping (Requirements 6.1-6.4)
# ---------------------------------------------------------------------------

def test_no_policy_statement_uses_wildcard_resource(resources):
    """No IAM policy statement in any role may use Resource '*' (Req 6.1)."""
    offenders = []
    for role_id in _all_role_logical_ids():
        role = resources[role_id]["Properties"]
        for stmt in _collect_all_statements(role.get("Policies", [])):
            resource = stmt.get("Resource", "")
            if isinstance(resource, str) and resource == "*":
                offenders.append(role_id)
            elif isinstance(resource, list) and "*" in resource:
                offenders.append(role_id)
    assert not offenders, (
        f"Roles with a wildcard '*' Resource (not allowed): {offenders}"
    )


def test_gateway_execution_role_agentcore_arns(resources):
    """GatewayExecutionRole must have the four required AgentCore ARN patterns (Req 6.2)."""
    role = resources["GatewayExecutionRole"]["Properties"]
    stmts = _collect_all_statements(role.get("Policies", []))

    all_resources = []
    for stmt in stmts:
        all_resources.extend(_resource_strings(stmt.get("Resource", [])))

    required_patterns = [
        "token-vault/default",
        "token-vault/default/apikeycredentialprovider/*",
        "workload-identity-directory/default",
        "workload-identity-directory/default/workload-identity/",
    ]
    for pattern in required_patterns:
        assert any(pattern in r for r in all_resources), (
            f"GatewayExecutionRole missing ARN pattern containing: {pattern!r}"
        )


def test_gateway_execution_role_execute_api_invoke(resources):
    """GatewayExecutionRole must grant execute-api:Invoke (Req 6.3)."""
    role = resources["GatewayExecutionRole"]["Properties"]
    stmts = _collect_all_statements(role.get("Policies", []))
    all_actions = []
    for stmt in stmts:
        all_actions.extend(_actions_list(stmt))
    assert any("execute-api:Invoke" in a for a in all_actions), (
        "GatewayExecutionRole must grant 'execute-api:Invoke'"
    )


def test_mcp_server_role_dynamodb_scoped_to_product_table(resources):
    """McpServerRole DynamoDB policy must scope to ProductTable.Arn (Req 6.4)."""
    role = resources["McpServerRole"]["Properties"]
    stmts = _collect_all_statements(role.get("Policies", []))

    dynamodb_actions = {"dynamodb:GetItem", "dynamodb:PutItem",
                        "dynamodb:Query", "dynamodb:Scan"}

    found_dynamo_stmt = False
    for stmt in stmts:
        actions = _actions_list(stmt)
        if any(a in dynamodb_actions for a in actions):
            found_dynamo_stmt = True
            resource = stmt.get("Resource")
            assert isinstance(resource, dict), (
                f"McpServerRole DynamoDB Resource must be !GetAtt ProductTable.Arn, "
                f"got {resource!r}"
            )
            getatt_val = resource.get("!GetAtt")
            if isinstance(getatt_val, str):
                assert getatt_val == "ProductTable.Arn", (
                    f"McpServerRole DynamoDB resource must be ProductTable.Arn, "
                    f"got {getatt_val!r}"
                )
            elif isinstance(getatt_val, list):
                assert getatt_val == ["ProductTable", "Arn"], (
                    f"McpServerRole DynamoDB resource must be ProductTable.Arn, "
                    f"got {getatt_val!r}"
                )
            else:
                pytest.fail(
                    f"McpServerRole DynamoDB Resource must be !GetAtt ProductTable.Arn, "
                    f"got {resource!r}"
                )
    assert found_dynamo_stmt, (
        "McpServerRole must declare a DynamoDB policy statement"
    )


# ---------------------------------------------------------------------------
# 13. API method NONE + AWS_PROXY + scoped permission (Requirements 7.1-7.3)
# ---------------------------------------------------------------------------

def test_mcp_method_http_method(resources):
    """McpMethod must use POST HTTP method."""
    method_props = resources["McpMethod"]["Properties"]
    assert method_props.get("HttpMethod") == "POST", (
        "McpMethod must use HttpMethod: POST"
    )


def test_mcp_method_auth_type_none(resources):
    """McpMethod must use AuthorizationType: NONE (Req 7.1)."""
    method_props = resources["McpMethod"]["Properties"]
    assert method_props.get("AuthorizationType") == "NONE", (
        "McpMethod must use AuthorizationType: NONE — AgentCore Gateway signs "
        "requests with SigV4 externally"
    )


def test_mcp_method_uses_aws_proxy(resources):
    """McpMethod must use AWS_PROXY integration type (Req 7.2)."""
    method_props = resources["McpMethod"]["Properties"]
    integration = method_props.get("Integration", {})
    assert integration.get("Type") == "AWS_PROXY", (
        "McpMethod Integration.Type must be 'AWS_PROXY'"
    )


def test_mcp_method_integration_points_to_mcp_server_lambda(resources, template_text):
    """McpMethod integration URI must reference McpServerLambda (Req 7.2)."""
    method_props = resources["McpMethod"]["Properties"]
    integration = method_props.get("Integration", {})
    uri = integration.get("Uri", {})
    uri_str = _sub_value(uri) if isinstance(uri, dict) else str(uri)
    assert "McpServerLambda" in str(uri_str) or "McpServerLambda" in template_text, (
        "McpMethod integration URI must reference McpServerLambda"
    )


def test_mcp_api_invoke_permission_scoped(resources):
    """API Gateway invoke permission must be scoped to POST /mcp on the MCP API (Req 7.3)."""
    perm = resources["McpApiInvokePermission"]["Properties"]
    assert perm.get("Action") == "lambda:InvokeFunction", (
        "McpApiInvokePermission Action must be lambda:InvokeFunction"
    )
    assert perm.get("Principal") == "apigateway.amazonaws.com", (
        "McpApiInvokePermission Principal must be apigateway.amazonaws.com"
    )
    source_arn = _sub_value(perm.get("SourceArn"))
    assert source_arn is not None, "McpApiInvokePermission must declare a SourceArn"
    assert "POST/mcp" in source_arn, (
        f"McpApiInvokePermission SourceArn must be scoped to POST/mcp, "
        f"got {source_arn!r}"
    )
    assert "${McpApi}" in source_arn, (
        f"McpApiInvokePermission SourceArn must reference the McpApi, "
        f"got {source_arn!r}"
    )


# ---------------------------------------------------------------------------
# 14. Stack Outputs incl. GatewayId and McpApiInvokeUrl shape (Req 12.1-12.3)
# ---------------------------------------------------------------------------

def test_stack_outputs_present(template):
    """Template must export all required stack outputs incl. GatewayId (Req 12.1, 12.2)."""
    outputs = template.get("Outputs", {})
    required_outputs = [
        "AgentLambdaName",
        "McpServerLambdaName",
        "CognitoUserPoolId",
        "CognitoClientId",
        "McpApiInvokeUrl",
        "GatewayUrl",
        "ProductTableName",
        "GatewayId",
    ]
    for key in required_outputs:
        assert key in outputs, f"Template Outputs must include '{key}'"


def test_mcp_api_invoke_url_shape(template):
    """McpApiInvokeUrl must resolve to the POST /prod/mcp HTTPS endpoint (Req 12.3)."""
    outputs = template.get("Outputs", {})
    value = outputs["McpApiInvokeUrl"].get("Value")
    url_str = _sub_value(value)
    expected = (
        "https://${McpApi}.execute-api.${AWS::Region}.amazonaws.com/prod/mcp"
    )
    assert url_str == expected, (
        f"McpApiInvokeUrl must be {expected!r}, got {url_str!r}"
    )


def test_gateway_id_output_resolves_from_gateway_identifier(template):
    """The GatewayId output key must resolve from !GetAtt AgentCoreGateway.GatewayIdentifier.

    The AWS::BedrockAgentCore::Gateway resource has no GatewayId attribute — the
    gateway ID is exposed via the GatewayIdentifier attribute. The output KEY
    stays 'GatewayId' (the downstream deploy.sh contract) while resolving from
    the actual attribute (Req 12.2).
    """
    outputs = template.get("Outputs", {})
    assert "GatewayId" in outputs, "Template Outputs must include 'GatewayId'"
    value = outputs["GatewayId"].get("Value")
    assert isinstance(value, dict), (
        f"GatewayId output Value must be a !GetAtt, got {value!r}"
    )
    getatt_val = value.get("!GetAtt")
    if isinstance(getatt_val, list):
        assert getatt_val == ["AgentCoreGateway", "GatewayIdentifier"], (
            f"GatewayId output must resolve from "
            f"!GetAtt AgentCoreGateway.GatewayIdentifier, got {getatt_val!r}"
        )
    else:
        assert getatt_val == "AgentCoreGateway.GatewayIdentifier", (
            f"GatewayId output must resolve from "
            f"AgentCoreGateway.GatewayIdentifier, got {getatt_val!r}"
        )


# ---------------------------------------------------------------------------
# 15. Both Lambdas use python3.12 runtime (carried over)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("logical_id", ["AgentLambdaFunction", "McpServerLambda"])
def test_function_runtime(resources, logical_id):
    """Both Lambda functions must use the python3.12 runtime."""
    fn_props = resources[logical_id]["Properties"]
    assert fn_props.get("Runtime") == "python3.12", (
        f"{logical_id} must use python3.12 runtime, got {fn_props.get('Runtime')!r}"
    )


# ---------------------------------------------------------------------------
# 16. ProductTable schema (carried over)
# ---------------------------------------------------------------------------

def test_product_table_billing_mode(resources):
    """ProductTable must use PAY_PER_REQUEST billing mode."""
    table_props = resources["ProductTable"]["Properties"]
    assert table_props.get("BillingMode") == "PAY_PER_REQUEST", (
        "ProductTable must have BillingMode: PAY_PER_REQUEST"
    )


def test_product_table_key_schema(resources):
    """ProductTable must have category (HASH) and productId (RANGE) keys."""
    table_props = resources["ProductTable"]["Properties"]
    key_schema = table_props.get("KeySchema", [])
    hash_keys = [k for k in key_schema if k.get("KeyType") == "HASH"]
    range_keys = [k for k in key_schema if k.get("KeyType") == "RANGE"]
    assert len(hash_keys) == 1 and hash_keys[0]["AttributeName"] == "category", (
        "ProductTable must have 'category' as the HASH key"
    )
    assert len(range_keys) == 1 and range_keys[0]["AttributeName"] == "productId", (
        "ProductTable must have 'productId' as the RANGE key"
    )


def test_product_table_attribute_types(resources):
    """ProductTable attributes category and productId must be type S (String)."""
    table_props = resources["ProductTable"]["Properties"]
    attr_defs = {
        a["AttributeName"]: a["AttributeType"]
        for a in table_props.get("AttributeDefinitions", [])
    }
    assert attr_defs.get("category") == "S", (
        "ProductTable 'category' attribute must be type S"
    )
    assert attr_defs.get("productId") == "S", (
        "ProductTable 'productId' attribute must be type S"
    )


# ---------------------------------------------------------------------------
# 17. MCP target is NOT declared in the template (created post-deploy, Req 4.1)
# ---------------------------------------------------------------------------

def test_no_mcp_target_resource(resources):
    """No AWS::BedrockAgentCore::GatewayTarget resource may be declared (Req 4.1)."""
    targets = [
        lid for lid, r in resources.items()
        if r.get("Type") == "AWS::BedrockAgentCore::GatewayTarget"
    ]
    assert not targets, (
        f"MCP target must be created post-deploy, not declared in template: {targets}"
    )
