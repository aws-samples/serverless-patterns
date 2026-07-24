"""Integration tests for the AgentCore API Gateway Weather Agent.

These tests run against a deployed stack and require the following
environment variables to be set:

  API_ENDPOINT_URL        – API Gateway stage URL (e.g. https://xxx.execute-api.us-east-1.amazonaws.com/dev)
  USER_POOL_ID            – Cognito User Pool ID
  USER_POOL_CLIENT_ID     – Cognito User Pool Client ID
  LAMBDA_FUNCTION_NAME    – Agent Lambda function name or ARN
  TEST_USERNAME           – Cognito test user username
  TEST_PASSWORD           – Cognito test user password
  AWS_REGION              – AWS region (default: us-east-1)

If any required variable is missing the test is skipped gracefully.
"""

import json
import os

import pytest

boto3 = pytest.importorskip("boto3", reason="boto3 is required for integration tests")
requests = pytest.importorskip("requests", reason="requests is required for integration tests")


# ---------------------------------------------------------------------------
# Environment helpers
# ---------------------------------------------------------------------------

def _env(name: str, default: str | None = None) -> str | None:
    return os.environ.get(name, default)


_REQUIRED_VARS = [
    "API_ENDPOINT_URL",
    "USER_POOL_ID",
    "USER_POOL_CLIENT_ID",
    "LAMBDA_FUNCTION_NAME",
    "TEST_USERNAME",
    "TEST_PASSWORD",
]


def _skip_if_missing() -> dict[str, str]:
    """Return a dict of env values or skip the test when any is absent."""
    values: dict[str, str] = {}
    missing: list[str] = []
    for var in _REQUIRED_VARS:
        val = _env(var)
        if val is None:
            missing.append(var)
        else:
            values[var] = val
    if missing:
        pytest.skip(
            f"Integration test skipped — missing env vars: {', '.join(missing)}"
        )
    values["AWS_REGION"] = _env("AWS_REGION", "us-east-1")
    return values


# ---------------------------------------------------------------------------
# 7.1 – API Gateway returns 403 without an API key
# ---------------------------------------------------------------------------

class TestApiGateway403:
    """Validates: Requirement 2.4 — requests without a valid x-api-key get 403."""

    def test_get_weather_without_api_key_returns_403(self):
        """Call /weather/current without an API key and expect 403 Forbidden."""
        env = _skip_if_missing()
        url = f"{env['API_ENDPOINT_URL'].rstrip('/')}/weather/current"

        response = requests.get(url, params={"q": "London"}, timeout=10)

        assert response.status_code == 403, (
            f"Expected 403 Forbidden but got {response.status_code}: {response.text}"
        )


# ---------------------------------------------------------------------------
# 7.2 – End-to-end: Cognito auth → JWT → Agent Lambda → weather response
# ---------------------------------------------------------------------------

class TestEndToEndAgent:
    """Validates: Requirement 9.4 — authenticate via Cognito, invoke Agent Lambda,
    verify weather data in response."""

    @pytest.fixture()
    def env(self):
        return _skip_if_missing()

    @pytest.fixture()
    def jwt_token(self, env):
        """Authenticate against Cognito and return an ID token (JWT)."""
        client = boto3.client("cognito-idp", region_name=env["AWS_REGION"])
        resp = client.admin_initiate_auth(
            UserPoolId=env["USER_POOL_ID"],
            ClientId=env["USER_POOL_CLIENT_ID"],
            AuthFlow="ADMIN_USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": env["TEST_USERNAME"],
                "PASSWORD": env["TEST_PASSWORD"],
            },
        )
        return resp["AuthenticationResult"]["IdToken"]

    def test_agent_returns_weather_data(self, env, jwt_token):
        """Invoke the Agent Lambda with a weather prompt and verify the response."""
        lambda_client = boto3.client("lambda", region_name=env["AWS_REGION"])

        payload = {
            "headers": {"Authorization": f"Bearer {jwt_token}"},
            "body": json.dumps({
                "prompt": "What is the current weather in London?",
                "session_id": "integration-test-session",
            }),
        }

        response = lambda_client.invoke(
            FunctionName=env["LAMBDA_FUNCTION_NAME"],
            InvocationType="RequestResponse",
            Payload=json.dumps(payload),
        )

        response_payload = json.loads(response["Payload"].read())

        # The Lambda should return a 200-level status
        status_code = response_payload.get("statusCode", response.get("StatusCode"))
        assert status_code == 200, (
            f"Expected 200 but got {status_code}: {json.dumps(response_payload, indent=2)}"
        )

        # Parse the body and verify it contains weather-related content
        body = response_payload.get("body")
        if isinstance(body, str):
            body = json.loads(body)

        agent_response = body.get("response", "") if isinstance(body, dict) else str(body)

        # The response should mention weather-related terms
        weather_terms = ["temperature", "weather", "degrees", "celsius", "fahrenheit", "wind", "humidity", "london"]
        response_lower = agent_response.lower()
        matches = [t for t in weather_terms if t in response_lower]

        assert len(matches) >= 1, (
            f"Expected weather data in response but found none of {weather_terms}. "
            f"Response: {agent_response[:500]}"
        )
