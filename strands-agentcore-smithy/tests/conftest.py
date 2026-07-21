"""Shared test fixtures for the agentcore-smithy-bedrock project."""

import json
import os
import sys
import time

import pytest
import jwt
import yaml

# Add src to path so shared modules are importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

_ROOT = os.path.join(os.path.dirname(__file__), "..")

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
# CloudFormation template fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def cfn_template():
    """Load and return the parsed CloudFormation template."""
    path = os.path.join(_ROOT, "infrastructure", "cloudformation-template.yaml")
    with open(path) as fh:
        return yaml.load(fh, Loader=_CfnLoader)


@pytest.fixture(scope="session")
def cfn_resources(cfn_template):
    """Return the Resources section of the CloudFormation template."""
    return cfn_template["Resources"]


@pytest.fixture(scope="session")
def cfn_outputs(cfn_template):
    """Return the Outputs section of the CloudFormation template."""
    return cfn_template.get("Outputs", {})


# ---------------------------------------------------------------------------
# Smithy model fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def smithy_model(cfn_resources):
    """Parse and return the official AWS Smithy model."""
    model_path = os.path.join(
        os.path.dirname(__file__), "..", "infrastructure", "bedrock-runtime-2023-09-30.json"
    )
    if not os.path.exists(model_path):
        model_path = "/tmp/bedrock-runtime-2023-09-30.json"
    with open(model_path) as f:
        return json.load(f)


@pytest.fixture(scope="session")
def smithy_shapes(smithy_model):
    """Return the shapes dict from the Smithy model."""
    return smithy_model["shapes"]


# ---------------------------------------------------------------------------
# Deploy script fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def deploy_script_content():
    """Return the raw content of scripts/deploy.sh."""
    path = os.path.join(_ROOT, "scripts", "deploy.sh")
    with open(path) as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# JWT / user context fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def make_jwt_token():
    """Factory fixture that creates JWT tokens with given claims."""

    def _make(claims: dict, exp_offset: int = 3600) -> str:
        payload = {
            "iat": int(time.time()),
            "exp": int(time.time()) + exp_offset,
            **claims,
        }
        return jwt.encode(payload, "test-secret", algorithm="HS256")

    return _make


@pytest.fixture
def sample_id_token(make_jwt_token):
    """A sample Cognito ID token with cognito:username claim."""
    return make_jwt_token({
        "token_use": "id",
        "cognito:username": "testuser",
        "sub": "abc-123",
    })


@pytest.fixture
def sample_access_token(make_jwt_token):
    """A sample Cognito access token."""
    return make_jwt_token({
        "token_use": "access",
        "username": "testuser",
        "sub": "abc-123",
    })


@pytest.fixture
def sample_user_context(sample_id_token):
    """A sample UserContext dict."""
    return {
        "username": "testuser",
        "token": sample_id_token,
    }
