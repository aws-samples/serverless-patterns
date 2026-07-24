"""Unit tests for the index documents Lambda handler."""

import json
import sys
import os
import importlib.util
from unittest.mock import patch, MagicMock

_index_path = os.path.join(os.path.dirname(__file__), "..", "..", "lambda", "index_documents", "app.py")
_spec = importlib.util.spec_from_file_location("index_app", _index_path)
index_app = importlib.util.module_from_spec(_spec)
sys.modules["index_app"] = index_app
_spec.loader.exec_module(index_app)

handler = index_app.handler


@patch("index_app.get_client")
def test_index_single_document(mock_get_client, apigw_event, lambda_context):
    """Indexing a single document calls bulk with correct structure."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": False, "items": []}

    event = apigw_event(body={
        "documents": [{"id": "doc-1", "title": "Test", "content": "Content"}]
    })
    result = handler(event, lambda_context)

    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert "1 document" in body["message"]
    assert body["errors"] is False


@patch("index_app.get_client")
def test_index_multiple_documents(mock_get_client, apigw_event, lambda_context):
    """Indexing multiple documents sends all in a single bulk request."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": False, "items": []}

    docs = [
        {"id": f"doc-{i}", "title": f"Title {i}", "content": f"Content {i}"}
        for i in range(5)
    ]
    event = apigw_event(body={"documents": docs})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert "5 document" in body["message"]

    # Verify bulk was called with 10 items (action + source for each doc)
    bulk_body = mock_client.bulk.call_args[1]["body"]
    assert len(bulk_body) == 10


@patch("index_app.get_client")
def test_index_uses_ingest_pipeline(mock_get_client, apigw_event, lambda_context):
    """Bulk index request specifies the ingest pipeline for embedding generation."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": False, "items": []}

    event = apigw_event(body={
        "documents": [{"id": "doc-1", "title": "Test", "content": "Content"}]
    })
    handler(event, lambda_context)

    call_kwargs = mock_client.bulk.call_args[1]
    assert call_kwargs["pipeline"] == "embedding-ingest-pipeline"


@patch("index_app.get_client")
def test_embedding_text_combines_title_and_content(mock_get_client, apigw_event, lambda_context):
    """The embedding_text field concatenates title and content."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": False, "items": []}

    event = apigw_event(body={
        "documents": [{"id": "doc-1", "title": "My Title", "content": "My content"}]
    })
    handler(event, lambda_context)

    bulk_body = mock_client.bulk.call_args[1]["body"]
    doc_body = bulk_body[1]
    assert doc_body["embedding_text"] == "My Title. My content"


@patch("index_app.get_client")
def test_embedding_text_without_title(mock_get_client, apigw_event, lambda_context):
    """When title is empty, embedding_text is just the content."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {"errors": False, "items": []}

    event = apigw_event(body={
        "documents": [{"id": "doc-1", "title": "", "content": "Only content"}]
    })
    handler(event, lambda_context)

    bulk_body = mock_client.bulk.call_args[1]["body"]
    doc_body = bulk_body[1]
    assert doc_body["embedding_text"] == "Only content"


@patch("index_app.get_client")
def test_empty_documents_returns_400(mock_get_client, apigw_event, lambda_context):
    """Empty documents array returns 400 without calling OpenSearch."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    event = apigw_event(body={"documents": []})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 400
    assert "no documents" in json.loads(result["body"])["error"].lower()
    mock_client.bulk.assert_not_called()


@patch("index_app.get_client")
def test_no_documents_key_returns_400(mock_get_client, apigw_event, lambda_context):
    """Missing documents key returns 400."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    event = apigw_event(body={"data": "something"})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 400
    mock_client.bulk.assert_not_called()


@patch("index_app.get_client")
def test_bulk_errors_reported_in_response(mock_get_client, apigw_event, lambda_context):
    """Bulk errors from OpenSearch are surfaced in the response."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.return_value = {
        "errors": True,
        "items": [
            {"index": {"_id": "doc-1", "error": {"type": "mapper_parsing_exception", "reason": "bad field"}}}
        ],
    }

    event = apigw_event(body={
        "documents": [{"id": "doc-1", "title": "Test", "content": "Content"}]
    })
    result = handler(event, lambda_context)

    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert body["errors"] is True
    assert len(body["item_errors"]) == 1
    assert body["item_errors"][0]["id"] == "doc-1"


@patch("index_app.get_client")
def test_opensearch_error_returns_500(mock_get_client, apigw_event, lambda_context):
    """OpenSearch client exception returns 500."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.bulk.side_effect = Exception("Connection refused")

    event = apigw_event(body={
        "documents": [{"id": "doc-1", "title": "Test", "content": "Content"}]
    })
    result = handler(event, lambda_context)

    assert result["statusCode"] == 500
    assert "Connection refused" in json.loads(result["body"])["error"]
