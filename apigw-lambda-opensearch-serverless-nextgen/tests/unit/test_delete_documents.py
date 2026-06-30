"""Unit tests for the delete documents Lambda handler."""

import json
import sys
import os
import importlib.util
from unittest.mock import patch, MagicMock

_delete_path = os.path.join(os.path.dirname(__file__), "..", "..", "lambda", "delete_documents", "app.py")
_spec = importlib.util.spec_from_file_location("delete_app", _delete_path)
delete_app = importlib.util.module_from_spec(_spec)
sys.modules["delete_app"] = delete_app
_spec.loader.exec_module(delete_app)

handler = delete_app.handler


@patch("delete_app.get_client")
def test_delete_single_document(mock_get_client, apigw_event, lambda_context):
    """Deleting a single document calls bulk with correct delete action."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": False, "items": []}

    event = apigw_event(body={"ids": ["doc-1"]})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert "1 document" in body["message"]
    assert body["errors"] is False


@patch("delete_app.get_client")
def test_delete_multiple_documents(mock_get_client, apigw_event, lambda_context):
    """Deleting multiple documents sends all in a single bulk request."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": False, "items": []}

    event = apigw_event(body={"ids": ["doc-1", "doc-2", "doc-3"]})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert "3 document" in body["message"]

    bulk_body = mock_client.bulk.call_args[1]["body"]
    assert len(bulk_body) == 3
    assert all(item.get("delete") for item in bulk_body)


@patch("delete_app.get_client")
def test_delete_bulk_body_contains_correct_ids(mock_get_client, apigw_event, lambda_context):
    """Bulk request contains the correct document IDs and index."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": False, "items": []}

    event = apigw_event(body={"ids": ["doc-a", "doc-b"]})
    handler(event, lambda_context)

    bulk_body = mock_client.bulk.call_args[1]["body"]
    assert bulk_body[0] == {"delete": {"_index": "documents", "_id": "doc-a"}}
    assert bulk_body[1] == {"delete": {"_index": "documents", "_id": "doc-b"}}


@patch("delete_app.get_client")
def test_empty_ids_returns_400(mock_get_client, apigw_event, lambda_context):
    """Empty ids array returns 400 without calling OpenSearch."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    event = apigw_event(body={"ids": []})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 400
    assert "no document" in json.loads(result["body"])["error"].lower()
    mock_client.bulk.assert_not_called()


@patch("delete_app.get_client")
def test_missing_ids_key_returns_400(mock_get_client, apigw_event, lambda_context):
    """Missing ids key returns 400."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    event = apigw_event(body={"documents": ["doc-1"]})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 400
    mock_client.bulk.assert_not_called()


@patch("delete_app.get_client")
def test_bulk_errors_reported(mock_get_client, apigw_event, lambda_context):
    """Bulk errors from OpenSearch are surfaced in the response."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": True, "items": []}

    event = apigw_event(body={"ids": ["doc-1"]})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert body["errors"] is True


@patch("delete_app.get_client")
def test_opensearch_error_returns_500(mock_get_client, apigw_event, lambda_context):
    """OpenSearch client exception returns 500."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.side_effect = Exception("Service unavailable")

    event = apigw_event(body={"ids": ["doc-1"]})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 500
    assert "Service unavailable" in json.loads(result["body"])["error"]
