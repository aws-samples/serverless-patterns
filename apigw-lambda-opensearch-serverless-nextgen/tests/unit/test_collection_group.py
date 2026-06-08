"""Unit tests for the NextGen collection group custom resource handler."""

import sys
import os
import importlib.util
from unittest.mock import patch, MagicMock

_cg_path = os.path.join(os.path.dirname(__file__), "..", "..", "lambda", "custom_resources", "nextgen_collection_group", "app.py")
_spec = importlib.util.spec_from_file_location("cg_app", _cg_path)
cg_app = importlib.util.module_from_spec(_spec)
sys.modules["cg_app"] = cg_app
_spec.loader.exec_module(cg_app)

on_create = cg_app.on_create
on_update = cg_app.on_update
on_delete = cg_app.on_delete


def _make_event(props=None, physical_id=None):
    """Build a minimal CloudFormation custom resource event."""
    event = {
        "ResourceProperties": props or {
            "Name": "test-collection-group",
            "Description": "Test group",
            "MaxIndexingCapacityInOCU": "8",
            "MaxSearchCapacityInOCU": "8",
        },
    }
    if physical_id:
        event["PhysicalResourceId"] = physical_id
    return event


@patch("cg_app.helper")
@patch("cg_app.client")
def test_create_calls_api_with_correct_params(mock_client, mock_helper, lambda_context):
    """Create handler calls create_collection_group with NextGen generation."""
    mock_client.create_collection_group.return_value = {
        "createCollectionGroupDetail": {
            "id": "abc123def456",
            "arn": "arn:aws:aoss:eu-west-1:123456789012:collection-group/abc123def456",
            "name": "test-collection-group",
        }
    }

    result = on_create(_make_event(), lambda_context)

    mock_client.create_collection_group.assert_called_once_with(
        name="test-collection-group",
        standbyReplicas="ENABLED",
        generation="NEXTGEN",
        description="Test group",
        capacityLimits={
            "maxIndexingCapacityInOCU": 8,
            "maxSearchCapacityInOCU": 8,
        },
    )
    assert result == "abc123def456"


@patch("cg_app.helper")
@patch("cg_app.client")
def test_create_sets_helper_data(mock_client, mock_helper, lambda_context):
    """Create handler populates helper.Data with outputs."""
    mock_helper.Data = {}
    mock_client.create_collection_group.return_value = {
        "createCollectionGroupDetail": {
            "id": "abc123def456",
            "arn": "arn:aws:aoss:eu-west-1:123456789012:collection-group/abc123def456",
            "name": "test-collection-group",
        }
    }

    on_create(_make_event(), lambda_context)

    assert mock_helper.Data["Id"] == "abc123def456"
    assert mock_helper.Data["Generation"] == "NEXTGEN"
    assert mock_helper.Data["Name"] == "test-collection-group"


@patch("cg_app.helper")
@patch("cg_app.client")
def test_update_calls_api_with_physical_id(mock_client, mock_helper, lambda_context):
    """Update handler uses the physical resource ID to update."""
    event = _make_event(physical_id="abc123def456")

    on_update(event, lambda_context)

    mock_client.update_collection_group.assert_called_once_with(
        id="abc123def456",
        description="Test group",
        capacityLimits={
            "maxIndexingCapacityInOCU": 8,
            "maxSearchCapacityInOCU": 8,
        },
    )


@patch("cg_app.helper")
@patch("cg_app.client")
def test_delete_calls_api(mock_client, mock_helper, lambda_context):
    """Delete handler calls delete_collection_group."""
    event = _make_event(physical_id="abc123def456")

    on_delete(event, lambda_context)

    mock_client.delete_collection_group.assert_called_once_with(id="abc123def456")


@patch("cg_app.helper")
@patch("cg_app.client")
def test_delete_skips_invalid_physical_id(mock_client, mock_helper, lambda_context):
    """Delete handler skips deletion when physical ID looks like a CFN logical ID."""
    event = _make_event(physical_id="CollectionGroup-ABCDEF")

    on_delete(event, lambda_context)

    mock_client.delete_collection_group.assert_not_called()


@patch("cg_app.helper")
@patch("cg_app.client")
def test_delete_handles_not_found(mock_client, mock_helper, lambda_context):
    """Delete handler gracefully handles ResourceNotFoundException."""
    mock_client.exceptions.ResourceNotFoundException = type("ResourceNotFoundException", (Exception,), {})
    mock_client.delete_collection_group.side_effect = mock_client.exceptions.ResourceNotFoundException()

    event = _make_event(physical_id="abc123def456")

    # Should not raise
    on_delete(event, lambda_context)


@patch("cg_app.helper")
@patch("cg_app.client")
def test_create_default_capacity(mock_client, mock_helper, lambda_context):
    """Create uses default capacity of 2 when not specified."""
    mock_client.create_collection_group.return_value = {
        "createCollectionGroupDetail": {
            "id": "abc123",
            "arn": "arn:aws:aoss:eu-west-1:123456789012:collection-group/abc123",
            "name": "minimal",
        }
    }

    event = _make_event(props={"Name": "minimal"})
    on_create(event, lambda_context)

    call_kwargs = mock_client.create_collection_group.call_args[1]
    assert call_kwargs["capacityLimits"]["maxIndexingCapacityInOCU"] == 2
    assert call_kwargs["capacityLimits"]["maxSearchCapacityInOCU"] == 2
