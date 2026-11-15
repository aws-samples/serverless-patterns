"""Lambda handler for deleting documents from OpenSearch Serverless NextGen."""

import json
import os

from aws_lambda_powertools import Logger, Tracer
from opensearch_client import get_client

logger = Logger()
tracer = Tracer()

INDEX_NAME = os.environ.get("INDEX_NAME", "documents")
COLLECTION_ENDPOINT = os.environ["COLLECTION_ENDPOINT"]
REGION = os.environ.get("AWS_REGION", "eu-west-1")


@tracer.capture_lambda_handler
@logger.inject_lambda_context
def handler(event, context):
    """Delete one or more documents by ID.

    Expected request body:
    {
        "ids": ["doc-1", "doc-2", ...]
    }
    """
    try:
        body = json.loads(event.get("body", "{}"))
        doc_ids = body.get("ids", [])

        if not doc_ids:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No document IDs provided"}),
            }

        client = get_client(COLLECTION_ENDPOINT, REGION)

        bulk_body = []
        for doc_id in doc_ids:
            bulk_body.append({"delete": {"_index": INDEX_NAME, "_id": doc_id}})

        response = client.bulk(body=bulk_body)

        logger.info("Deleted documents", extra={"count": len(doc_ids), "errors": response.get("errors", False)})

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {
                    "message": f"Deleted {len(doc_ids)} document(s)",
                    "errors": response.get("errors", False),
                }
            ),
        }

    except Exception as e:
        logger.exception("Error deleting documents")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }
