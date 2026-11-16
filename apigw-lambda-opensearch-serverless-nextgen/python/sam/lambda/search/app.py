"""Lambda handler for search against OpenSearch Serverless NextGen.

Supports three search modes:
- semantic: neural search using OpenSearch ML model (Bedrock Titan V2)
- lexical: BM25 full-text match query with fuzzy matching
- hybrid: combines both with score normalization pipeline

Embeddings are generated server-side by the OpenSearch ML model — no
client-side embedding generation is needed.
"""

import json
import os

from aws_lambda_powertools import Logger, Tracer
from opensearch_client import get_client

logger = Logger()
tracer = Tracer()

INDEX_NAME = os.environ.get("INDEX_NAME", "documents")
COLLECTION_ENDPOINT = os.environ["COLLECTION_ENDPOINT"]
MODEL_ID = os.environ["MODEL_ID"]
REGION = os.environ.get("AWS_REGION", "eu-west-1")


@tracer.capture_lambda_handler
@logger.inject_lambda_context
def handler(event, context):
    """Perform search in the specified mode.

    Expected request body:
    {
        "query": "search terms",
        "mode": "semantic" | "lexical" | "hybrid",  // optional, default "semantic"
        "size": 5  // optional, default 5
    }
    """
    try:
        body = json.loads(event.get("body", "{}"))
        query_text = body.get("query")
        mode = body.get("mode", "semantic")
        size = body.get("size", 5)

        if not query_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "'query' is required"}),
            }

        if mode not in ("semantic", "lexical", "hybrid"):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "mode must be 'semantic', 'lexical', or 'hybrid'"}),
            }

        client = get_client(COLLECTION_ENDPOINT, REGION)
        search_body = _build_query(query_text, mode, size)

        params = {}
        if mode == "hybrid":
            params["search_pipeline"] = "hybrid-search-pipeline"

        response = client.search(index=INDEX_NAME, body=search_body, params=params)

        hits = [
            {
                "id": hit["_id"],
                "score": hit["_score"],
                "title": hit["_source"].get("title"),
                "content": hit["_source"].get("content"),
            }
            for hit in response["hits"]["hits"]
        ]

        logger.info("Search completed", extra={
            "mode": mode,
            "total_hits": response["hits"]["total"]["value"],
        })

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {
                    "results": hits,
                    "total": response["hits"]["total"]["value"],
                    "mode": mode,
                }
            ),
        }

    except Exception as e:
        logger.exception("Error performing search")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }


def _build_query(query_text, mode, size):
    """Build the OpenSearch query body based on mode."""
    if mode == "hybrid":
        return _build_hybrid_query(query_text, size)

    if mode == "lexical":
        return {
            "size": size,
            "query": {
                "multi_match": {
                    "query": query_text,
                    "fields": ["title^2", "content"],
                    "fuzziness": 1,
                }
            },
        }

    # semantic — uses neural query (OpenSearch generates embedding server-side)
    return {
        "size": size,
        "min_score": 0.55,
        "query": {
            "neural": {
                "embedding": {
                    "query_text": query_text,
                    "model_id": MODEL_ID,
                    "k": size,
                }
            }
        },
    }


def _build_hybrid_query(query_text, size):
    """Build a hybrid query combining lexical and neural search."""
    return {
        "size": size,
        "query": {
            "hybrid": {
                "queries": [
                    {
                        "multi_match": {
                            "query": query_text,
                            "fields": ["title^2", "content"],
                        }
                    },
                    {
                        "neural": {
                            "embedding": {
                                "query_text": query_text,
                                "model_id": MODEL_ID,
                                "k": size,
                            }
                        }
                    },
                ]
            }
        },
    }
