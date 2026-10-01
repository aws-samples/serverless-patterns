"""End-to-end integration tests for the strands-agentcore-mcp stack.

These tests exercise the full deployed system:
  - Test A (happy path): Cognito auth → Agent Lambda → AgentCore Gateway →
    MCP Server Lambda → DynamoDB, asserting a conversational answer that
    references seeded product data.
  - Test B (unauthorized): Agent Lambda invoked without a JWT, asserting
    an auth-error response shape (no CloudWatch assertion needed).
  - Test C (MCP discovery): Agent Lambda invoked with a product-detail
    prompt; CloudWatch Logs Insights confirms both ``tools/list`` and at
    least one ``tools/call`` appear in the MCP Server Lambda's log stream
    during the invocation window.

Requirements: a deployed CloudFormation stack named ``agentcore-mcp`` in
``us-east-1``.  All tests are skipped (not failed) when the stack is absent
or its outputs are unavailable.
"""

import json
import subprocess
import time
from datetime import datetime, timedelta, timezone

import boto3
import pytest

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

STACK_NAME = "agentcore-mcp"
REGION = "us-east-1"

TEST_USERNAME = "testuser"
TEST_PASSWORD = "TestPassword123!"

# Seeded product identifiers — at least one must appear in a happy-path answer.
SEEDED_PRODUCT_TOKENS = [
    "ELEC-001",
    "ELEC-002",
    "BOOK-001",
    "Headphones",
    "Electronics",
    "Books",
]


# ---------------------------------------------------------------------------
# Session-scoped fixture: stack outputs
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def stack_outputs():
    """Return a dict mapping CloudFormation output key → value.

    Calls ``aws cloudformation describe-stacks`` once per test session.
    Skips the entire session if the stack is not deployed or the command
    fails for any reason.
    """
    result = subprocess.run(
        [
            "aws",
            "cloudformation",
            "describe-stacks",
            "--stack-name",
            STACK_NAME,
            "--region",
            REGION,
            "--output",
            "json",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        pytest.skip(
            f"Stack {STACK_NAME!r} not deployed — skipping integration tests "
            f"(aws cli error: {result.stderr.strip()!r})"
        )

    try:
        data = json.loads(result.stdout)
        raw_outputs = data["Stacks"][0].get("Outputs", [])
    except (json.JSONDecodeError, KeyError, IndexError) as exc:
        pytest.skip(
            f"Stack {STACK_NAME!r} outputs unavailable — skipping integration tests "
            f"(parse error: {exc})"
        )

    outputs = {item["OutputKey"]: item["OutputValue"] for item in raw_outputs}
    return outputs


# ---------------------------------------------------------------------------
# Helper: resolve MCP Server Lambda physical name from stack resources
# ---------------------------------------------------------------------------


def get_mcp_lambda_name(stack_name: str = STACK_NAME) -> str:
    """Return the physical resource ID for the ``McpServerLambda`` logical ID.

    Falls back to the conventional name ``agentcore-mcp-McpServerLambda``
    when the describe-stack-resources call fails.
    """
    result = subprocess.run(
        [
            "aws",
            "cloudformation",
            "describe-stack-resources",
            "--stack-name",
            stack_name,
            "--region",
            REGION,
            "--output",
            "json",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        try:
            data = json.loads(result.stdout)
            for resource in data.get("StackResources", []):
                if resource.get("LogicalResourceId") == "McpServerLambda":
                    return resource["PhysicalResourceId"]
        except (json.JSONDecodeError, KeyError):
            pass

    # Fallback: derive from stack name + logical ID
    return f"{stack_name}-McpServerLambda"


# ---------------------------------------------------------------------------
# Helper: Cognito authentication
# ---------------------------------------------------------------------------


def get_id_token(client_id: str, username: str, password: str) -> str:
    """Authenticate against Cognito and return the ID token.

    Args:
        client_id: The Cognito App Client ID.
        username: The Cognito username.
        password: The user's password.

    Returns:
        The ``IdToken`` string from the authentication result.
    """
    cognito = boto3.client("cognito-idp", region_name=REGION)
    response = cognito.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={"USERNAME": username, "PASSWORD": password},
        ClientId=client_id,
    )
    return response["AuthenticationResult"]["IdToken"]


# ---------------------------------------------------------------------------
# Helper: Lambda invocation
# ---------------------------------------------------------------------------


def invoke_lambda(function_name: str, payload: dict) -> dict:
    """Invoke a Lambda function synchronously and return the parsed response.

    Args:
        function_name: The Lambda function name or ARN.
        payload: The event payload dict to send.

    Returns:
        The parsed JSON response body returned by the Lambda function.
    """
    client = boto3.client("lambda", region_name=REGION)
    response = client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload).encode(),
    )
    raw = response["Payload"].read()
    return json.loads(raw)


# ---------------------------------------------------------------------------
# Test A — happy path
# ---------------------------------------------------------------------------


def test_happy_path(stack_outputs):
    """Authenticate via Cognito, invoke the Agent Lambda, assert a product answer.

    Validates: Requirements 1.2, 2.2, 2.3, 2.5, 4.4, 8.4, 14.1
    """
    agent_lambda_name = stack_outputs.get("AgentLambdaName")
    client_id = stack_outputs.get("CognitoClientId")

    if not agent_lambda_name or not client_id:
        pytest.skip("Required stack outputs (AgentLambdaName, CognitoClientId) not found")

    id_token = get_id_token(client_id, TEST_USERNAME, TEST_PASSWORD)

    result = invoke_lambda(
        agent_lambda_name,
        {"jwt": id_token, "prompt": "List all products."},
    )

    # The Agent Lambda returns either {"answer": "..."} or {"body": "..."}
    answer = result.get("answer") or result.get("body") or result.get("response", "")

    assert isinstance(answer, str) and len(answer) > 0, (
        f"Expected a non-empty string answer, got: {result!r}"
    )

    answer_lower = answer.lower()
    matched = any(token.lower() in answer_lower for token in SEEDED_PRODUCT_TOKENS)
    assert matched, (
        f"Answer does not reference any seeded product token "
        f"({SEEDED_PRODUCT_TOKENS!r}).\nAnswer: {answer!r}"
    )


# ---------------------------------------------------------------------------
# Test B — unauthorized (no JWT)
# ---------------------------------------------------------------------------


def test_unauthorized(stack_outputs):
    """Invoke the Agent Lambda without a JWT; assert an auth-error response.

    Only the return-payload shape is checked — no CloudWatch assertion.

    Validates: Requirements 1.7, 14.1
    """
    agent_lambda_name = stack_outputs.get("AgentLambdaName")

    if not agent_lambda_name:
        pytest.skip("Required stack output AgentLambdaName not found")

    # Omit the 'jwt' key entirely
    result = invoke_lambda(agent_lambda_name, {"prompt": "List all products."})

    result_str = json.dumps(result).lower()

    auth_error_tokens = ["error", "unauthorized", "401", "403", "missing", "invalid"]
    matched = any(token in result_str for token in auth_error_tokens)
    assert matched, (
        f"Expected an auth-error indicator in the response, but got: {result!r}"
    )


# ---------------------------------------------------------------------------
# Test C — MCP discovery via CloudWatch Logs Insights
# ---------------------------------------------------------------------------


def test_mcp_discovery(stack_outputs):
    """Invoke a product-detail prompt and verify MCP protocol traffic in logs.

    Confirms that both ``tools/list`` and at least one ``tools/call`` appear
    in the MCP Server Lambda's CloudWatch log stream during the invocation
    window.

    Validates: Requirements 2.2, 2.3, 2.5, 4.4, 14.2
    """
    agent_lambda_name = stack_outputs.get("AgentLambdaName")
    client_id = stack_outputs.get("CognitoClientId")

    if not agent_lambda_name or not client_id:
        pytest.skip("Required stack outputs (AgentLambdaName, CognitoClientId) not found")

    mcp_lambda_name = get_mcp_lambda_name()
    log_group = f"/aws/lambda/{mcp_lambda_name}"

    id_token = get_id_token(client_id, TEST_USERNAME, TEST_PASSWORD)

    # Record the window around the invocation
    start_time = datetime.now(tz=timezone.utc)

    invoke_lambda(
        agent_lambda_name,
        {"jwt": id_token, "prompt": "Get product ELEC-001 details"},
    )

    end_time = datetime.now(tz=timezone.utc)

    # Query CloudWatch Logs Insights for MCP protocol messages
    logs_client = boto3.client("logs", region_name=REGION)

    query_start = int((start_time - timedelta(seconds=30)).timestamp())
    query_end = int((end_time + timedelta(seconds=60)).timestamp())

    query_string = (
        "fields @message "
        "| filter @message like /tools\\/list/ or @message like /tools\\/call/"
    )

    query_response = logs_client.start_query(
        logGroupName=log_group,
        startTime=query_start,
        endTime=query_end,
        queryString=query_string,
    )
    query_id = query_response["queryId"]

    # Poll until the query completes (up to 60 seconds total)
    deadline = time.monotonic() + 60
    results = []
    while time.monotonic() < deadline:
        time.sleep(2)
        status_response = logs_client.get_query_results(queryId=query_id)
        status = status_response.get("status", "")
        if status == "Complete":
            results = status_response.get("results", [])
            break
        if status in ("Failed", "Cancelled", "Timeout"):
            pytest.fail(
                f"CloudWatch Logs Insights query ended with status {status!r}"
            )

    # Flatten results to a list of message strings
    messages = []
    for row in results:
        for field in row:
            if field.get("field") == "@message":
                messages.append(field.get("value", ""))

    # If no results yet, wait a bit more for log propagation (up to 60 s extra)
    if not messages:
        extra_deadline = time.monotonic() + 60
        while time.monotonic() < extra_deadline:
            time.sleep(5)
            status_response = logs_client.get_query_results(queryId=query_id)
            if status_response.get("status") == "Complete":
                results = status_response.get("results", [])
                for row in results:
                    for field in row:
                        if field.get("field") == "@message":
                            messages.append(field.get("value", ""))
                if messages:
                    break
            # Re-issue the query with a wider window if still empty
            if not messages and time.monotonic() > extra_deadline - 30:
                wider_end = int((end_time + timedelta(seconds=120)).timestamp())
                retry_response = logs_client.start_query(
                    logGroupName=log_group,
                    startTime=query_start,
                    endTime=wider_end,
                    queryString=query_string,
                )
                query_id = retry_response["queryId"]

    has_tools_list = any("tools/list" in msg for msg in messages)
    has_tools_call = any("tools/call" in msg for msg in messages)

    assert has_tools_list, (
        "Expected at least one 'tools/list' entry in MCP Server Lambda logs, "
        f"but found none. Messages captured: {messages!r}"
    )
    assert has_tools_call, (
        "Expected at least one 'tools/call' entry in MCP Server Lambda logs, "
        f"but found none. Messages captured: {messages!r}"
    )
