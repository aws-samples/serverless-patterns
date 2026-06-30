"""Unit tests for the setup pipeline custom resource handler."""

import sys
import os
import importlib.util
from unittest.mock import patch, MagicMock

import pytest

_setup_path = os.path.join(os.path.dirname(__file__), "..", "..", "lambda", "custom_resources", "setup_pipeline", "app.py")
_spec = importlib.util.spec_from_file_location("setup_app", _setup_path)
setup_app = importlib.util.module_from_spec(_spec)
sys.modules["setup_app"] = setup_app
_spec.loader.exec_module(setup_app)

on_create = setup_app.on_create
on_delete = setup_app.on_delete
_wait_for_model_deployed = setup_app._wait_for_model_deployed
_retry_with_backoff = setup_app._retry_with_backoff


def _make_event(physical_id=None):
    """Build a minimal CloudFormation custom resource event."""
    event = {
        "ResourceProperties": {
            "CollectionEndpoint": "https://test.eu-west-1.aoss.amazonaws.com",
            "ModelRoleArn": "arn:aws:iam::123456789012:role/MLRole",
            "EmbeddingModelId": "amazon.titan-embed-text-v2:0",
            "EmbeddingDimension": "1024",
        },
    }
    if physical_id:
        event["PhysicalResourceId"] = physical_id
    return event


@patch("setup_app.helper")
@patch("setup_app.get_client")
def test_create_registers_connector_and_model(mock_get_client, mock_helper, lambda_context):
    """Create handler creates connector, registers model, deploys, and creates pipelines."""
    mock_helper.Data = {}
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    mock_client.transport.perform_request.side_effect = [
        # Step 1: Create connector
        {"connector_id": "conn-123"},
        # Step 2: Register model
        {"model_id": "model-456"},
        # Step 3: Deploy model
        {},
        # Step 3b: Wait for deploy (poll)
        {"model_state": "DEPLOYED"},
        # Step 4: Create ingest pipeline
        {"acknowledged": True},
        # Step 5: Create search pipeline
        {"acknowledged": True},
    ]

    result = on_create(_make_event(), lambda_context)

    assert result == "conn-123/model-456"
    assert mock_helper.Data["ModelId"] == "model-456"
    assert mock_helper.Data["ConnectorId"] == "conn-123"
    assert mock_helper.Data["IngestPipeline"] == "embedding-ingest-pipeline"
    assert mock_helper.Data["SearchPipeline"] == "hybrid-search-pipeline"


@patch("setup_app.helper")
@patch("setup_app.get_client")
def test_create_connector_body_contains_bedrock_config(mock_get_client, mock_helper, lambda_context):
    """Connector body includes correct Bedrock model and role ARN."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    mock_client.transport.perform_request.side_effect = [
        {"connector_id": "conn-123"},
        {"model_id": "model-456"},
        {},
        {"model_state": "DEPLOYED"},
        {"acknowledged": True},
        {"acknowledged": True},
    ]

    on_create(_make_event(), lambda_context)

    # First call is the connector creation
    first_call = mock_client.transport.perform_request.call_args_list[0]
    assert first_call[0][0] == "POST"
    assert "/_plugins/_ml/connectors/_create" in first_call[0][1]
    connector_body = first_call[1]["body"]
    assert connector_body["credential"]["roleArn"] == "arn:aws:iam::123456789012:role/MLRole"


@patch("setup_app.helper")
@patch("setup_app.get_client")
def test_delete_cleans_up_resources(mock_get_client, mock_helper, lambda_context):
    """Delete handler removes pipelines, undeploys model, and deletes connector."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.transport.perform_request.return_value = {}

    event = _make_event(physical_id="conn-123/model-456")
    on_delete(event, lambda_context)

    calls = mock_client.transport.perform_request.call_args_list
    methods_and_paths = [(c[0][0], c[0][1]) for c in calls]

    assert ("DELETE", "/_ingest/pipeline/embedding-ingest-pipeline") in methods_and_paths
    assert ("DELETE", "/_search/pipeline/hybrid-search-pipeline") in methods_and_paths
    assert ("POST", "/_plugins/_ml/models/model-456/_undeploy") in methods_and_paths
    assert ("DELETE", "/_plugins/_ml/models/model-456") in methods_and_paths
    assert ("DELETE", "/_plugins/_ml/connectors/conn-123") in methods_and_paths


@patch("setup_app.helper")
@patch("setup_app.get_client")
def test_delete_handles_pipeline_errors_gracefully(mock_get_client, mock_helper, lambda_context):
    """Delete handler continues even if pipeline deletion fails."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.transport.perform_request.side_effect = Exception("Not found")

    event = _make_event(physical_id="conn-123/model-456")

    # Should not raise
    on_delete(event, lambda_context)


def test_wait_for_model_deployed_success():
    """_wait_for_model_deployed returns True when model reaches DEPLOYED."""
    mock_client = MagicMock()
    mock_client.transport.perform_request.side_effect = [
        {"model_state": "REGISTERING"},
        {"model_state": "DEPLOYING"},
        {"model_state": "DEPLOYED"},
    ]

    result = _wait_for_model_deployed(mock_client, "model-1", max_attempts=5, delay=0)
    assert result is True


def test_wait_for_model_deployed_failure():
    """_wait_for_model_deployed raises on DEPLOY_FAILED."""
    mock_client = MagicMock()
    mock_client.transport.perform_request.return_value = {"model_state": "DEPLOY_FAILED"}

    with pytest.raises(RuntimeError, match="DEPLOY_FAILED"):
        _wait_for_model_deployed(mock_client, "model-1", max_attempts=3, delay=0)


def test_wait_for_model_deployed_timeout():
    """_wait_for_model_deployed raises TimeoutError if model doesn't deploy."""
    mock_client = MagicMock()
    mock_client.transport.perform_request.return_value = {"model_state": "DEPLOYING"}

    with pytest.raises(TimeoutError):
        _wait_for_model_deployed(mock_client, "model-1", max_attempts=2, delay=0)


def test_retry_with_backoff_succeeds_on_first_try():
    """_retry_with_backoff returns immediately when function succeeds."""
    result = _retry_with_backoff(lambda: "success", max_attempts=3, initial_delay=0)
    assert result == "success"


def test_retry_with_backoff_retries_on_403():
    """_retry_with_backoff retries on 403 Forbidden errors."""
    attempts = {"count": 0}

    def flaky():
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise Exception("403 Forbidden")
        return "ok"

    result = _retry_with_backoff(flaky, max_attempts=5, initial_delay=0)
    assert result == "ok"
    assert attempts["count"] == 3


def test_retry_with_backoff_raises_non_auth_errors():
    """_retry_with_backoff does not retry non-authorization errors."""
    def always_fails():
        raise ValueError("Something else broke")

    with pytest.raises(ValueError, match="Something else broke"):
        _retry_with_backoff(always_fails, max_attempts=3, initial_delay=0)
