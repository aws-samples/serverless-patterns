"""Unit test configuration — sets up isolated environment before any imports."""

import os
from dataclasses import dataclass

import pytest

# Prevent any real AWS service calls — fake credentials and region
_REGION = os.environ.get("AWS_REGION", "eu-west-1")

os.environ["AWS_ACCESS_KEY_ID"] = "testing"
os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
os.environ["AWS_SECURITY_TOKEN"] = "testing"
os.environ["AWS_SESSION_TOKEN"] = "testing"
os.environ.setdefault("AWS_DEFAULT_REGION", _REGION)
os.environ.setdefault("AWS_REGION", _REGION)

# Disable X-Ray tracing so Tracer uses a no-op provider
os.environ["POWERTOOLS_TRACE_DISABLED"] = "true"
os.environ["POWERTOOLS_SERVICE_NAME"] = "test"

# Agent invoker Lambda env vars
os.environ["STREAM_RELAY_ARN"] = f"arn:aws:lambda:{_REGION}:123456789012:function:stream-relay"

# Stream relay Lambda env vars
os.environ["APPSYNC_HTTP_ENDPOINT"] = f"test.appsync-api.{_REGION}.amazonaws.com"
os.environ["APPSYNC_API_KEY"] = "test-api-key"
os.environ["AGENT_RUNTIME_ARN"] = f"arn:aws:bedrock-agentcore:{_REGION}:123456789012:runtime/test"


@dataclass
class FakeLambdaContext:
    """Minimal Lambda context for Powertools inject_lambda_context."""

    function_name: str = "test-function"
    memory_limit_in_mb: int = 256
    invoked_function_arn: str = f"arn:aws:lambda:{_REGION}:123456789012:function:test"
    aws_request_id: str = "test-request-id"


@pytest.fixture
def lambda_context():
    """Provide a fake Lambda context for Powertools."""
    return FakeLambdaContext()
