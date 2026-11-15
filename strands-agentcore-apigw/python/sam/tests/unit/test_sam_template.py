"""Unit tests for SAM template validation.

Validates API Gateway resources, AgentCore resources, Cognito, Lambda,
IAM, parameters, and outputs defined in the SAM template.
"""

import pytest


# ============================================================
# 5.1 — API Gateway Resources, Dependencies, and Properties
# ============================================================


class TestRestApi:
    def test_rest_api_exists(self, resources):
        assert "RestApi" in resources
        assert resources["RestApi"]["Type"] == "AWS::ApiGateway::RestApi"

    def test_api_key_source_type_is_header(self, resources):
        props = resources["RestApi"]["Properties"]
        assert props["ApiKeySourceType"] == "HEADER"


class TestWeatherResources:
    def test_weather_resource_path(self, resources):
        props = resources["WeatherResource"]["Properties"]
        assert props["PathPart"] == "weather"

    def test_weather_current_resource_path(self, resources):
        props = resources["WeatherCurrentResource"]["Properties"]
        assert props["PathPart"] == "current"

    def test_weather_current_parent_is_weather(self, resources):
        parent_ref = resources["WeatherCurrentResource"]["Properties"]["ParentId"]
        assert parent_ref == {"Ref": "WeatherResource"}


class TestGetCurrentWeatherMethod:
    def test_method_exists(self, resources):
        assert "GetCurrentWeatherMethod" in resources
        assert resources["GetCurrentWeatherMethod"]["Type"] == "AWS::ApiGateway::Method"

    def test_http_method_is_get(self, resources):
        props = resources["GetCurrentWeatherMethod"]["Properties"]
        assert props["HttpMethod"] == "GET"

    def test_api_key_required(self, resources):
        props = resources["GetCurrentWeatherMethod"]["Properties"]
        assert props["ApiKeyRequired"] is True

    def test_authorization_type_none(self, resources):
        props = resources["GetCurrentWeatherMethod"]["Properties"]
        assert props["AuthorizationType"] == "NONE"

    def test_integration_type_http_non_proxy(self, resources):
        # Non-proxy HTTP (not HTTP_PROXY): only mapped params are forwarded, so
        # the inbound x-api-key header is not leaked to Open-Meteo (which would
        # otherwise 303-redirect to its commercial endpoint).
        integration = resources["GetCurrentWeatherMethod"]["Properties"]["Integration"]
        assert integration["Type"] == "HTTP"

    def test_integration_uri_open_meteo_forecast(self, resources):
        integration = resources["GetCurrentWeatherMethod"]["Properties"]["Integration"]
        assert "api.open-meteo.com/v1/forecast" in integration["Uri"]

    def test_declares_lat_lon_method_params(self, resources):
        # Declared as required method request params, which also drives the
        # discovered tool schema the model sees.
        req_params = resources["GetCurrentWeatherMethod"]["Properties"]["RequestParameters"]
        assert req_params.get("method.request.querystring.latitude") is True
        assert req_params.get("method.request.querystring.longitude") is True

    def test_lat_lon_mapped_to_integration(self, resources):
        # Non-proxy integration forwards nothing unless explicitly mapped, so the
        # caller's latitude/longitude must be mapped through to the backend.
        integration = resources["GetCurrentWeatherMethod"]["Properties"]["Integration"]
        req_params = integration.get("RequestParameters", {})
        assert req_params.get("integration.request.querystring.latitude") == "method.request.querystring.latitude"
        assert req_params.get("integration.request.querystring.longitude") == "method.request.querystring.longitude"

    def test_integration_has_responses(self, resources):
        # Non-proxy integrations require an IntegrationResponses mapping.
        integration = resources["GetCurrentWeatherMethod"]["Properties"]["Integration"]
        status_codes = [r["StatusCode"] for r in integration.get("IntegrationResponses", [])]
        assert "200" in status_codes

    def test_integration_injects_current_fields_server_side(self, resources):
        # The 'current' field list is injected as a static integration param so
        # the discovered tool only asks the model for latitude/longitude.
        integration = resources["GetCurrentWeatherMethod"]["Properties"]["Integration"]
        req_params = integration["RequestParameters"]
        assert "integration.request.querystring.current" in req_params
        assert "temperature_2m" in str(req_params["integration.request.querystring.current"])

    def test_no_api_key_injection(self, resources):
        # Open-Meteo requires no key — there should be no downstream key param.
        integration = resources["GetCurrentWeatherMethod"]["Properties"]["Integration"]
        req_params = integration["RequestParameters"]
        assert "integration.request.querystring.key" not in req_params


class TestGeocodingMethod:
    def test_method_exists(self, resources):
        assert "GeocodingMethod" in resources
        assert resources["GeocodingMethod"]["Type"] == "AWS::ApiGateway::Method"

    def test_resource_path(self, resources):
        assert resources["GeocodingResource"]["Properties"]["PathPart"] == "geocoding"

    def test_api_key_required(self, resources):
        assert resources["GeocodingMethod"]["Properties"]["ApiKeyRequired"] is True

    def test_integration_uri_open_meteo_geocoding(self, resources):
        integration = resources["GeocodingMethod"]["Properties"]["Integration"]
        assert "geocoding-api.open-meteo.com/v1/search" in integration["Uri"]

    def test_declares_name_method_param(self, resources):
        req_params = resources["GeocodingMethod"]["Properties"]["RequestParameters"]
        assert req_params.get("method.request.querystring.name") is True

    def test_integration_type_http_non_proxy(self, resources):
        integration = resources["GeocodingMethod"]["Properties"]["Integration"]
        assert integration["Type"] == "HTTP"

    def test_name_mapped_to_integration(self, resources):
        # Non-proxy integration forwards nothing unless mapped — the caller's
        # `name` must be mapped through to the geocoding backend.
        integration = resources["GeocodingMethod"]["Properties"]["Integration"]
        req_params = integration.get("RequestParameters", {})
        assert req_params.get("integration.request.querystring.name") == "method.request.querystring.name"

    def test_integration_has_responses(self, resources):
        integration = resources["GeocodingMethod"]["Properties"]["Integration"]
        status_codes = [r["StatusCode"] for r in integration.get("IntegrationResponses", [])]
        assert "200" in status_codes


class TestApiDeployment:
    def test_deployment_exists(self, resources):
        assert "ApiDeployment" in resources
        assert resources["ApiDeployment"]["Type"] == "AWS::ApiGateway::Deployment"

    def test_deployment_depends_on_methods(self, resources):
        depends = resources["ApiDeployment"]["DependsOn"]
        if isinstance(depends, str):
            depends = [depends]
        assert "GetCurrentWeatherMethod" in depends
        assert "GeocodingMethod" in depends


class TestApiStage:
    def test_stage_exists(self, resources):
        assert "ApiStage" in resources
        assert resources["ApiStage"]["Type"] == "AWS::ApiGateway::Stage"

    def test_stage_has_no_downstream_key_variable(self, resources):
        # Open-Meteo needs no key, so no downstream-secret stage variable.
        variables = resources["ApiStage"]["Properties"].get("Variables", {})
        assert "weatherApiKey" not in variables


class TestApiKeyAndUsagePlan:
    def test_api_key_depends_on_stage(self, resources):
        assert resources["ApiKey"].get("DependsOn") == "ApiStage" or "ApiStage" in (
            resources["ApiKey"].get("DependsOn") or []
        )

    def test_usage_plan_depends_on_stage(self, resources):
        assert resources["UsagePlan"].get("DependsOn") == "ApiStage" or "ApiStage" in (
            resources["UsagePlan"].get("DependsOn") or []
        )

    def test_usage_plan_key_links_key_to_plan(self, resources):
        props = resources["UsagePlanKey"]["Properties"]
        assert props["KeyId"] == {"Ref": "ApiKey"}
        assert props["UsagePlanId"] == {"Ref": "UsagePlan"}


# ============================================================
# 5.2 — AgentCore Gateway, GatewayTarget, and Cognito
# ============================================================


class TestAgentCoreGateway:
    def test_gateway_exists(self, resources):
        assert "AgentCoreGateway" in resources
        assert resources["AgentCoreGateway"]["Type"] == "AWS::BedrockAgentCore::Gateway"

    def test_protocol_type_mcp(self, resources):
        props = resources["AgentCoreGateway"]["Properties"]
        assert props["ProtocolType"] == "MCP"

    def test_authorizer_type_custom_jwt(self, resources):
        props = resources["AgentCoreGateway"]["Properties"]
        assert props["AuthorizerType"] == "CUSTOM_JWT"

    def test_authorizer_configuration_present(self, resources):
        props = resources["AgentCoreGateway"]["Properties"]
        auth_config = props["AuthorizerConfiguration"]
        assert "CustomJWTAuthorizer" in auth_config
        jwt = auth_config["CustomJWTAuthorizer"]
        assert "DiscoveryUrl" in jwt
        assert "AllowedAudience" in jwt

    def test_role_arn_present(self, resources):
        props = resources["AgentCoreGateway"]["Properties"]
        assert "RoleArn" in props


class TestGatewayTarget:
    def test_target_exists(self, resources):
        assert "OpenMeteoTarget" in resources
        assert resources["OpenMeteoTarget"]["Type"] == "AWS::BedrockAgentCore::GatewayTarget"

    def test_target_uses_mcp_api_gateway_block(self, resources):
        target_config = resources["OpenMeteoTarget"]["Properties"]["TargetConfiguration"]
        assert "Mcp" in target_config
        assert "ApiGateway" in target_config["Mcp"]

    def test_target_does_not_use_openapi_schema(self, resources):
        mcp = resources["OpenMeteoTarget"]["Properties"]["TargetConfiguration"]["Mcp"]
        assert "OpenApiSchema" not in mcp

    def test_target_references_rest_api(self, resources):
        api_gw = resources["OpenMeteoTarget"]["Properties"]["TargetConfiguration"]["Mcp"]["ApiGateway"]
        assert "RestApiId" in api_gw

    def test_target_references_stage(self, resources):
        api_gw = resources["OpenMeteoTarget"]["Properties"]["TargetConfiguration"]["Mcp"]["ApiGateway"]
        assert "Stage" in api_gw

    def test_target_has_tool_configuration(self, resources):
        api_gw = resources["OpenMeteoTarget"]["Properties"]["TargetConfiguration"]["Mcp"]["ApiGateway"]
        assert "ApiGatewayToolConfiguration" in api_gw
        tool_config = api_gw["ApiGatewayToolConfiguration"]
        assert "ToolFilters" in tool_config
        assert len(tool_config["ToolFilters"]) >= 1


class TestCognito:
    def test_user_pool_exists(self, resources):
        assert "CognitoUserPool" in resources
        assert resources["CognitoUserPool"]["Type"] == "AWS::Cognito::UserPool"

    def test_user_pool_client_exists(self, resources):
        assert "CognitoUserPoolClient" in resources
        assert resources["CognitoUserPoolClient"]["Type"] == "AWS::Cognito::UserPoolClient"

    def test_client_auth_flows(self, resources):
        auth_flows = resources["CognitoUserPoolClient"]["Properties"]["ExplicitAuthFlows"]
        assert "ALLOW_USER_PASSWORD_AUTH" in auth_flows
        assert "ALLOW_REFRESH_TOKEN_AUTH" in auth_flows


# ============================================================
# 5.3 — Lambda Configuration
# ============================================================


class TestLambdaConfig:
    def test_lambda_exists(self, resources):
        assert "AgentLambdaFunction" in resources
        assert resources["AgentLambdaFunction"]["Type"] == "AWS::Serverless::Function"

    def test_runtime_python312(self, resources):
        props = resources["AgentLambdaFunction"]["Properties"]
        assert props["Runtime"] == "python3.12"

    def test_architecture_x86_64(self, resources):
        props = resources["AgentLambdaFunction"]["Properties"]
        assert "x86_64" in props["Architectures"]

    def test_timeout_at_least_120(self, resources):
        props = resources["AgentLambdaFunction"]["Properties"]
        assert props["Timeout"] >= 120

    def test_memory_at_least_1024(self, resources):
        props = resources["AgentLambdaFunction"]["Properties"]
        assert props["MemorySize"] >= 1024

    def test_code_uri_present(self, resources):
        # SAM packages the code from CodeUri (the execution role and log
        # group are generated automatically by the AWS::Serverless::Function
        # transform).
        props = resources["AgentLambdaFunction"]["Properties"]
        assert "CodeUri" in props

    def test_env_var_gateway_id(self, resources):
        env_vars = resources["AgentLambdaFunction"]["Properties"]["Environment"]["Variables"]
        assert "GATEWAY_ID" in env_vars

    def test_env_var_cognito_jwks_url(self, resources):
        env_vars = resources["AgentLambdaFunction"]["Properties"]["Environment"]["Variables"]
        assert "COGNITO_JWKS_URL" in env_vars

    def test_env_var_bedrock_model_id(self, resources):
        env_vars = resources["AgentLambdaFunction"]["Properties"]["Environment"]["Variables"]
        assert "BEDROCK_MODEL_ID" in env_vars


# ============================================================
# 5.4 — IAM Roles
# ============================================================


def _collect_actions_from_policies(role_resource):
    """Extract all actions from all policy statements in a role."""
    actions = []
    for policy in role_resource["Properties"].get("Policies", []):
        for stmt in policy["PolicyDocument"]["Statement"]:
            stmt_actions = stmt.get("Action", [])
            if isinstance(stmt_actions, str):
                stmt_actions = [stmt_actions]
            actions.extend(stmt_actions)
    return actions


def _collect_resources_from_policies(role_resource):
    """Extract all resource ARNs (as strings) from all policy statements in a role.

    CloudFormation intrinsic functions like !Sub are parsed as dicts, e.g.
    {"Sub": "arn:aws:..."}. We stringify everything so pattern matching works.
    """
    arns = []
    for policy in role_resource["Properties"].get("Policies", []):
        for stmt in policy["PolicyDocument"]["Statement"]:
            stmt_resources = stmt.get("Resource", [])
            if isinstance(stmt_resources, str):
                stmt_resources = [stmt_resources]
            elif isinstance(stmt_resources, dict):
                # e.g. {"Sub": "arn:aws:bedrock-agentcore:..."}
                stmt_resources = [str(stmt_resources)]
            else:
                stmt_resources = [str(r) for r in stmt_resources]
            arns.extend(stmt_resources)
    return arns


def _collect_actions_from_sam_function_policies(function_resource):
    """Extract all actions from the Policies list of an AWS::Serverless::Function.

    SAM function Policies are a list of policy documents or statement blocks;
    here each entry is a {"Statement": [...]} block.
    """
    actions = []
    for policy in function_resource["Properties"].get("Policies", []):
        statements = policy.get("Statement", []) if isinstance(policy, dict) else []
        for stmt in statements:
            stmt_actions = stmt.get("Action", [])
            if isinstance(stmt_actions, str):
                stmt_actions = [stmt_actions]
            actions.extend(stmt_actions)
    return actions


class TestAgentLambdaPermissions:
    """The Agent Lambda execution role is generated by SAM from the
    function's Policies property; CloudWatch Logs permissions are provided
    automatically by the AWS::Serverless::Function transform via the managed
    basic execution policy."""

    def test_bedrock_invoke_model(self, resources):
        actions = _collect_actions_from_sam_function_policies(resources["AgentLambdaFunction"])
        assert "bedrock:InvokeModel" in actions

    def test_bedrock_invoke_model_with_response_stream(self, resources):
        actions = _collect_actions_from_sam_function_policies(resources["AgentLambdaFunction"])
        assert "bedrock:InvokeModelWithResponseStream" in actions

    def test_bedrock_converse(self, resources):
        actions = _collect_actions_from_sam_function_policies(resources["AgentLambdaFunction"])
        assert "bedrock:Converse" in actions

    def test_bedrock_converse_stream(self, resources):
        actions = _collect_actions_from_sam_function_policies(resources["AgentLambdaFunction"])
        assert "bedrock:ConverseStream" in actions

    def test_get_gateway(self, resources):
        actions = _collect_actions_from_sam_function_policies(resources["AgentLambdaFunction"])
        assert "bedrock-agentcore:GetGateway" in actions


class TestGatewayExecutionRole:
    def test_role_exists(self, resources):
        assert "GatewayExecutionRole" in resources
        assert resources["GatewayExecutionRole"]["Type"] == "AWS::IAM::Role"

    def test_get_workload_access_token(self, resources):
        actions = _collect_actions_from_policies(resources["GatewayExecutionRole"])
        assert "bedrock-agentcore:GetWorkloadAccessToken" in actions

    def test_get_resource_api_key(self, resources):
        actions = _collect_actions_from_policies(resources["GatewayExecutionRole"])
        assert "bedrock-agentcore:GetResourceApiKey" in actions

    def test_get_resource_api_key_has_token_vault_default(self, resources):
        arns = _collect_resources_from_policies(resources["GatewayExecutionRole"])
        arn_str = " ".join(arns)
        assert "token-vault/default" in arn_str

    def test_get_resource_api_key_has_token_vault_provider_wildcard(self, resources):
        arns = _collect_resources_from_policies(resources["GatewayExecutionRole"])
        arn_str = " ".join(arns)
        assert "token-vault/default/apikeycredentialprovider/*" in arn_str

    def test_get_resource_api_key_has_workload_identity_default(self, resources):
        arns = _collect_resources_from_policies(resources["GatewayExecutionRole"])
        arn_str = " ".join(arns)
        assert "workload-identity-directory/default" in arn_str

    def test_get_resource_api_key_has_workload_identity_gateway_wildcard(self, resources):
        arns = _collect_resources_from_policies(resources["GatewayExecutionRole"])
        arn_str = " ".join(arns)
        assert "workload-identity-directory/default/workload-identity/" in arn_str

    def test_secrets_manager_get_secret_value(self, resources):
        actions = _collect_actions_from_policies(resources["GatewayExecutionRole"])
        assert "secretsmanager:GetSecretValue" in actions

    def test_apigateway_get(self, resources):
        actions = _collect_actions_from_policies(resources["GatewayExecutionRole"])
        assert "apigateway:GET" in actions

    def test_four_get_resource_api_key_arn_patterns(self, resources):
        """Verify all 4 required ARN patterns exist for GetResourceApiKey."""
        role = resources["GatewayExecutionRole"]
        api_key_resources = []
        for policy in role["Properties"]["Policies"]:
            for stmt in policy["PolicyDocument"]["Statement"]:
                stmt_actions = stmt.get("Action", [])
                if isinstance(stmt_actions, str):
                    stmt_actions = [stmt_actions]
                if "bedrock-agentcore:GetResourceApiKey" in stmt_actions:
                    res = stmt.get("Resource", [])
                    if isinstance(res, list):
                        api_key_resources.extend([str(r) for r in res])
                    else:
                        api_key_resources.append(str(res))

        arn_str = " ".join(api_key_resources)
        assert "token-vault/default" in arn_str
        assert "apikeycredentialprovider/*" in arn_str
        assert "workload-identity-directory/default" in arn_str
        assert "workload-identity/" in arn_str
        assert len(api_key_resources) >= 4


# ============================================================
# 5.5 — Template Parameters and Outputs
# ============================================================


class TestParameters:
    def test_environment_name_param(self, parameters):
        assert "EnvironmentName" in parameters
        assert parameters["EnvironmentName"]["Type"] == "String"

    def test_no_weather_api_key_param(self, parameters):
        # Open-Meteo needs no key, so the WeatherAPI secret param was removed.
        assert "WeatherApiKeySecretArn" not in parameters

    def test_credential_provider_arn_param(self, parameters):
        assert "CredentialProviderArn" in parameters
        assert parameters["CredentialProviderArn"]["Type"] == "String"


class TestOutputs:
    REQUIRED_OUTPUTS = [
        "GatewayId",
        "RestApiId",
        "ApiKeyId",
        "UserPoolId",
        "UserPoolClientId",
        "CognitoJwksUrl",
        "AgentLambdaArn",
        "ApiEndpointUrl",
    ]

    @pytest.mark.parametrize("output_name", REQUIRED_OUTPUTS)
    def test_required_output_exists(self, outputs, output_name):
        assert output_name in outputs, f"Missing required output: {output_name}"

    def test_all_eight_outputs_present(self, outputs):
        for name in self.REQUIRED_OUTPUTS:
            assert name in outputs
        assert len(self.REQUIRED_OUTPUTS) == 8

    def test_gateway_id_references_gateway(self, outputs):
        value = outputs["GatewayId"]["Value"]
        assert value == {"Ref": "AgentCoreGateway"}

    def test_rest_api_id_references_rest_api(self, outputs):
        value = outputs["RestApiId"]["Value"]
        assert value == {"Ref": "RestApi"}

    def test_api_key_id_references_api_key(self, outputs):
        value = outputs["ApiKeyId"]["Value"]
        assert value == {"Ref": "ApiKey"}

    def test_user_pool_id_references_cognito(self, outputs):
        value = outputs["UserPoolId"]["Value"]
        assert value == {"Ref": "CognitoUserPool"}

    def test_user_pool_client_id_references_client(self, outputs):
        value = outputs["UserPoolClientId"]["Value"]
        assert value == {"Ref": "CognitoUserPoolClient"}

    def test_agent_lambda_arn_uses_getatt(self, outputs):
        value = outputs["AgentLambdaArn"]["Value"]
        assert value == {"GetAtt": "AgentLambdaFunction.Arn"}
