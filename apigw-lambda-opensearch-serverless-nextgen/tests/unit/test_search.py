"""Unit tests for the search Lambda handler."""

import json
import sys
import os
import importlib.util
from unittest.mock import patch, MagicMock

# Import the search handler from its specific path
_search_path = os.path.join(os.path.dirname(__file__), "..", "..", "lambda", "search", "app.py")
_spec = importlib.util.spec_from_file_location("search_app", _search_path)
search_app = importlib.util.module_from_spec(_spec)
sys.modules["search_app"] = search_app
_spec.loader.exec_module(search_app)

handler = search_app.handler


def _opensearch_response(hits, total=None):
    """Build a mock OpenSearch search response."""
    if total is None:
        total = len(hits)
    return {
        "hits": {
            "total": {"value": total, "relation": "eq"},
            "hits": [
                {
                    "_id": h["id"],
                    "_score": h.get("score", 0.9),
                    "_source": {"title": h.get("title", ""), "content": h.get("content", "")},
                }
                for h in hits
            ],
        }
    }


@patch("search_app.get_client")
def test_semantic_search_returns_results(mock_get_client, apigw_event, lambda_context):
    """Semantic search with valid query returns formatted results."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.search.return_value = _opensearch_response(
        [{"id": "doc-1", "score": 0.92, "title": "Test Doc", "content": "Test content"}]
    )

    event = apigw_event(body={"query": "test query", "mode": "semantic"})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert body["mode"] == "semantic"
    assert len(body["results"]) == 1
    assert body["results"][0]["id"] == "doc-1"
    assert body["results"][0]["score"] == 0.92


@patch("search_app.get_client")
def test_semantic_is_default_mode(mock_get_client, apigw_event, lambda_context):
    """When no mode is specified, defaults to semantic."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.search.return_value = _opensearch_response([])

    event = apigw_event(body={"query": "test"})
    result = handler(event, lambda_context)

    body = json.loads(result["body"])
    assert body["mode"] == "semantic"


@patch("search_app.get_client")
def test_lexical_search_uses_multi_match(mock_get_client, apigw_event, lambda_context):
    """Lexical mode sends a multi_match query with fuzzy matching."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.search.return_value = _opensearch_response([])

    event = apigw_event(body={"query": "hiking boots", "mode": "lexical"})
    handler(event, lambda_context)

    call_kwargs = mock_client.search.call_args[1]
    assert "multi_match" in json.dumps(call_kwargs["body"])


@patch("search_app.get_client")
def test_hybrid_search_uses_search_pipeline(mock_get_client, apigw_event, lambda_context):
    """Hybrid mode passes search_pipeline param to OpenSearch."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.search.return_value = _opensearch_response([])

    event = apigw_event(body={"query": "waterproof bag", "mode": "hybrid"})
    handler(event, lambda_context)

    call_kwargs = mock_client.search.call_args[1]
    assert call_kwargs["params"]["search_pipeline"] == "hybrid-search-pipeline"


@patch("search_app.get_client")
def test_hybrid_search_combines_lexical_and_neural(mock_get_client, apigw_event, lambda_context):
    """Hybrid query body contains both multi_match and neural queries."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.search.return_value = _opensearch_response([])

    event = apigw_event(body={"query": "camping gear", "mode": "hybrid"})
    handler(event, lambda_context)

    search_body = mock_client.search.call_args[1]["body"]
    assert "hybrid" in search_body["query"]
    queries = search_body["query"]["hybrid"]["queries"]
    query_str = json.dumps(queries)
    assert "multi_match" in query_str
    assert "neural" in query_str


@patch("search_app.get_client")
def test_custom_size_parameter(mock_get_client, apigw_event, lambda_context):
    """Size parameter controls the number of results requested."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.search.return_value = _opensearch_response([])

    event = apigw_event(body={"query": "test", "size": 10})
    handler(event, lambda_context)

    search_body = mock_client.search.call_args[1]["body"]
    assert search_body["size"] == 10


@patch("search_app.get_client")
def test_missing_query_returns_400(mock_get_client, apigw_event, lambda_context):
    """Missing query field returns 400 without calling OpenSearch."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    event = apigw_event(body={"mode": "semantic"})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 400
    assert "query" in json.loads(result["body"])["error"].lower()
    mock_client.search.assert_not_called()


@patch("search_app.get_client")
def test_invalid_mode_returns_400(mock_get_client, apigw_event, lambda_context):
    """Invalid mode value returns 400."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    event = apigw_event(body={"query": "test", "mode": "invalid"})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 400
    assert "mode" in json.loads(result["body"])["error"].lower()
    mock_client.search.assert_not_called()


@patch("search_app.get_client")
def test_opensearch_error_returns_500(mock_get_client, apigw_event, lambda_context):
    """OpenSearch client exception returns 500 with error message."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.search.side_effect = Exception("Connection timeout")

    event = apigw_event(body={"query": "test"})
    result = handler(event, lambda_context)

    assert result["statusCode"] == 500
    assert "Connection timeout" in json.loads(result["body"])["error"]
