"""Property-based tests for CloudFormation template compliance.

Uses hypothesis to verify universal properties hold across all valid inputs.
Each property test runs 100 iterations with generated inputs.
"""

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st


# ---------------------------------------------------------------------------
# Helpers to extract data from the parsed CloudFormation template
# ---------------------------------------------------------------------------


def _get_method_logical_ids(resources):
    """Return the set of logical IDs for all API Gateway Method resources."""
    return {
        lid for lid, res in resources.items()
        if res.get("Type") == "AWS::ApiGateway::Method"
    }


def _get_deployment_depends_on(resources):
    """Return the DependsOn list for the ApiDeployment resource."""
    depends = resources["ApiDeployment"].get("DependsOn", [])
    if isinstance(depends, str):
        depends = [depends]
    return set(depends)


def _collect_actions_from_policies(role_resource):
    """Extract all actions from all policy statements in a role."""
    actions = set()
    for policy in role_resource["Properties"].get("Policies", []):
        for stmt in policy["PolicyDocument"]["Statement"]:
            stmt_actions = stmt.get("Action", [])
            if isinstance(stmt_actions, str):
                stmt_actions = [stmt_actions]
            actions.update(stmt_actions)
    return actions


def _collect_actions_from_sam_function_policies(function_resource):
    """Extract all actions from the Policies list of an AWS::Serverless::Function.

    SAM function Policies are a list of {"Statement": [...]} blocks rather than
    the {"PolicyName", "PolicyDocument"} shape used by AWS::IAM::Role.
    """
    actions = set()
    for policy in function_resource["Properties"].get("Policies", []):
        statements = policy.get("Statement", []) if isinstance(policy, dict) else []
        for stmt in statements:
            stmt_actions = stmt.get("Action", [])
            if isinstance(stmt_actions, str):
                stmt_actions = [stmt_actions]
            actions.update(stmt_actions)
    return actions


def _collect_resources_from_policies(role_resource):
    """Extract all resource ARNs (as strings) from all policy statements."""
    arns = []
    for policy in role_resource["Properties"].get("Policies", []):
        for stmt in policy["PolicyDocument"]["Statement"]:
            stmt_resources = stmt.get("Resource", [])
            if isinstance(stmt_resources, str):
                stmt_resources = [stmt_resources]
            elif isinstance(stmt_resources, dict):
                stmt_resources = [str(stmt_resources)]
            else:
                stmt_resources = [str(r) for r in stmt_resources]
            arns.extend(stmt_resources)
    return arns


def _get_get_resource_api_key_arns(role_resource):
    """Extract resource ARNs specifically from GetResourceApiKey statements."""
    arns = []
    for policy in role_resource["Properties"].get("Policies", []):
        for stmt in policy["PolicyDocument"]["Statement"]:
            stmt_actions = stmt.get("Action", [])
            if isinstance(stmt_actions, str):
                stmt_actions = [stmt_actions]
            if "bedrock-agentcore:GetResourceApiKey" in stmt_actions:
                res = stmt.get("Resource", [])
                if isinstance(res, list):
                    arns.extend([str(r) for r in res])
                elif isinstance(res, dict):
                    arns.append(str(res))
                else:
                    arns.append(str(res))
    return arns


def _get_named_resources(resources):
    """Return resources that have a Name property (or equivalent naming field)."""
    named = {}
    # Fields that represent a resource name in CloudFormation
    name_fields = [
        "Name", "FunctionName", "RoleName", "UserPoolName",
        "ClientName", "UsagePlanName", "StageName",
    ]
    for lid, res in resources.items():
        props = res.get("Properties", {})
        for field in name_fields:
            if field in props:
                named[lid] = (field, props[field])
                break
    return named


# ---------------------------------------------------------------------------
# Compliance functions — these encode what "correct" looks like
# ---------------------------------------------------------------------------


def deployment_depends_on_all_methods(method_ids, depends_on):
    """A compliant deployment's DependsOn must include every method logical ID."""
    return method_ids.issubset(depends_on)


def role_includes_all_bedrock_actions(role_actions, required_actions):
    """A compliant Lambda role must include all required Bedrock actions."""
    return required_actions.issubset(role_actions)


def gateway_role_includes_all_arn_patterns(arn_strings, required_patterns):
    """A compliant Gateway role must include all required ARN patterns."""
    combined = " ".join(arn_strings)
    return all(pattern in combined for pattern in required_patterns)


def resource_name_uses_environment(name_value):
    """A compliant resource name must reference EnvironmentName."""
    name_str = str(name_value)
    return "EnvironmentName" in name_str


def outputs_include_all_required(output_keys, required_outputs):
    """A compliant template must define all required outputs."""
    return required_outputs.issubset(output_keys)


# ---------------------------------------------------------------------------
# Property-Based Tests
# ---------------------------------------------------------------------------


# Feature: agentcore-apigw-weather-agent, Property 1: Deployment DependsOn includes all method logical IDs
class TestProperty1DeploymentDependsOn:
    """**Validates: Requirements 1.7**"""

    @given(
        subset_indices=st.lists(
            st.integers(min_value=0, max_value=99),
            min_size=1,
            max_size=10,
        )
    )
    @settings(max_examples=100)
    def test_deployment_depends_on_all_methods(self, resources, subset_indices):
        """For any random set of method logical IDs, verify the deployment's
        DependsOn includes all actual method logical IDs from the template."""
        actual_method_ids = _get_method_logical_ids(resources)
        actual_depends_on = _get_deployment_depends_on(resources)

        # Generate a random subset of the actual method IDs to query about
        method_list = sorted(actual_method_ids)
        assume(len(method_list) > 0)
        selected = {method_list[i % len(method_list)] for i in subset_indices}

        # The compliance function must hold: every selected method is in DependsOn
        assert deployment_depends_on_all_methods(selected, actual_depends_on), (
            f"Deployment DependsOn {actual_depends_on} is missing methods: "
            f"{selected - actual_depends_on}"
        )


# Feature: agentcore-apigw-weather-agent, Property 2: Lambda role includes all 4 required Bedrock actions
class TestProperty2BedrockActions:
    """**Validates: Requirements 6.1**"""

    REQUIRED_BEDROCK_ACTIONS = frozenset({
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:Converse",
        "bedrock:ConverseStream",
    })

    @given(
        subset=st.frozensets(
            st.sampled_from([
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:Converse",
                "bedrock:ConverseStream",
            ]),
            min_size=1,
            max_size=4,
        )
    )
    @settings(max_examples=100)
    def test_lambda_role_includes_all_bedrock_actions(self, resources, subset):
        """For any random subset of the 4 required Bedrock actions, verify the
        Lambda function's inline policies always contain the full required set
        (not just the subset). SAM generates the execution role from these."""
        role_actions = _collect_actions_from_sam_function_policies(resources["AgentLambdaFunction"])

        # Regardless of which subset we picked, the full set must be present
        assert role_includes_all_bedrock_actions(role_actions, self.REQUIRED_BEDROCK_ACTIONS), (
            f"Lambda role is missing Bedrock actions: "
            f"{self.REQUIRED_BEDROCK_ACTIONS - role_actions}"
        )

        # Additionally, the queried subset must also be present
        assert subset.issubset(role_actions), (
            f"Lambda role is missing queried actions: {subset - role_actions}"
        )


# Feature: agentcore-apigw-weather-agent, Property 3: Gateway role includes all 4 GetResourceApiKey ARN patterns
class TestProperty3GatewayArnPatterns:
    """**Validates: Requirements 6.4**"""

    REQUIRED_ARN_PATTERNS = [
        "token-vault/default",
        "token-vault/default/apikeycredentialprovider/*",
        "workload-identity-directory/default",
        "workload-identity-directory/default/workload-identity/",
    ]

    @given(
        subset=st.frozensets(
            st.sampled_from([
                "token-vault/default",
                "token-vault/default/apikeycredentialprovider/*",
                "workload-identity-directory/default",
                "workload-identity-directory/default/workload-identity/",
            ]),
            min_size=1,
            max_size=4,
        )
    )
    @settings(max_examples=100)
    def test_gateway_role_includes_all_arn_patterns(self, resources, subset):
        """For any random subset of the 4 required ARN patterns, verify the
        Gateway role always contains all 4 patterns (not just the subset)."""
        arn_strings = _get_get_resource_api_key_arns(resources["GatewayExecutionRole"])

        # All 4 patterns must always be present regardless of which subset we queried
        assert gateway_role_includes_all_arn_patterns(
            arn_strings, self.REQUIRED_ARN_PATTERNS
        ), (
            f"Gateway role GetResourceApiKey ARNs missing patterns. "
            f"ARNs: {arn_strings}"
        )

        # The queried subset must also be present
        combined = " ".join(arn_strings)
        for pattern in subset:
            assert pattern in combined, (
                f"Gateway role missing queried ARN pattern: {pattern}"
            )


# Feature: agentcore-apigw-weather-agent, Property 4: All named resources use EnvironmentName for namespacing
class TestProperty4EnvironmentNameNamespacing:
    """**Validates: Requirements 8.2**"""

    @given(
        resource_index=st.integers(min_value=0, max_value=99)
    )
    @settings(max_examples=100)
    def test_named_resources_use_environment_name(self, resources, resource_index):
        """For any named resource in the template, verify its name value
        references the EnvironmentName parameter."""
        named_resources = _get_named_resources(resources)
        assume(len(named_resources) > 0)

        resource_ids = sorted(named_resources.keys())
        selected_id = resource_ids[resource_index % len(resource_ids)]
        field_name, name_value = named_resources[selected_id]

        assert resource_name_uses_environment(name_value), (
            f"Resource {selected_id}.{field_name} = {name_value} "
            f"does not reference EnvironmentName parameter"
        )


# Feature: agentcore-apigw-weather-agent, Property 5: All 8 required outputs are defined
class TestProperty5RequiredOutputs:
    """**Validates: Requirements 8.4**"""

    REQUIRED_OUTPUTS = frozenset({
        "GatewayId",
        "RestApiId",
        "ApiKeyId",
        "UserPoolId",
        "UserPoolClientId",
        "CognitoJwksUrl",
        "AgentLambdaArn",
        "ApiEndpointUrl",
    })

    @given(
        subset=st.frozensets(
            st.sampled_from([
                "GatewayId",
                "RestApiId",
                "ApiKeyId",
                "UserPoolId",
                "UserPoolClientId",
                "CognitoJwksUrl",
                "AgentLambdaArn",
                "ApiEndpointUrl",
            ]),
            min_size=1,
            max_size=8,
        )
    )
    @settings(max_examples=100)
    def test_all_required_outputs_defined(self, outputs, subset):
        """For any random subset of the 8 required output names, verify the
        template's Outputs section always contains the full required set."""
        output_keys = set(outputs.keys())

        # All 8 must always be present regardless of which subset we queried
        assert outputs_include_all_required(output_keys, self.REQUIRED_OUTPUTS), (
            f"Template outputs missing: {self.REQUIRED_OUTPUTS - output_keys}"
        )

        # The queried subset must also be present
        assert subset.issubset(output_keys), (
            f"Template outputs missing queried outputs: {subset - output_keys}"
        )
