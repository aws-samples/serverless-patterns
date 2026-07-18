"""Unit test configuration — sets up isolated environment before any imports."""

import os
import sys
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

# Lambda function env vars
os.environ["COLLECTION_ENDPOINT"] = "https://test-collection.eu-west-1.aoss.amazonaws.com"
os.environ["COLLECTION_NAME"] = "semantic-search"
os.environ["INDEX_NAME"] = "documents"
os.environ["MODEL_ID"] = "test-model-id"
os.environ["INGEST_PIPELINE"] = "embedding-ingest-pipeline"

# Add the layer source to the path so Lambda functions can import opensearch_client
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "layers", "opensearch_client"))


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


@pytest.fixture
def apigw_event():
    """Build a minimal API Gateway proxy event."""
    def _make(body=None, method="POST", path="/"):
        return {
            "body": body if isinstance(body, str) else __import__("json").dumps(body or {}),
            "httpMethod": method,
            "path": path,
            "requestContext": {
                "requestId": "test-request-id",
                "stage": "Prod",
            },
            "headers": {"Content-Type": "application/json"},
        }
    return _make
