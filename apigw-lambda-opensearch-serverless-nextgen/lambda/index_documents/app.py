"""Lambda handler for indexing documents into OpenSearch Serverless NextGen.

Documents are indexed with a text field that the OpenSearch ingest pipeline
automatically converts to embeddings via Bedrock Titan V2. No client-side
embedding generation is needed.
"""

import json
import os

from aws_lambda_powertools import Logger, Tracer
from opensearch_client import get_client

logger = Logger()
tracer = Tracer()

INDEX_NAME = os.environ.get("INDEX_NAME", "documents")
COLLECTION_ENDPOINT = os.environ["COLLECTION_ENDPOINT"]
INGEST_PIPELINE = os.environ.get("INGEST_PIPELINE", "embedding-ingest-pipeline")
REGION = os.environ.get("AWS_REGION", "eu-west-1")


@tracer.capture_lambda_handler
@logger.inject_lambda_context
def handler(event, context):
    """Index one or more documents.

    Expected request body:
    {
        "documents": [
            {
                "id": "doc-1",
                "title": "Example Document",
                "content": "Full text content..."
            }
        ]
    }

    Embeddings are generated automatically by the OpenSearch ingest pipeline.
    """
    try:
        body = json.loads(event.get("body", "{}"))
        documents = body.get("documents", [])

        if not documents:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No documents provided"}),
            }

        client = get_client(COLLECTION_ENDPOINT, REGION)

        # Build bulk request — the ingest pipeline handles embedding generation
        bulk_body = []
        for doc in documents:
            doc_id = doc.get("id")
            title = doc.get("title", "")
            content = doc.get("content", "")

            # Combine title and content for the embedding source field
            embedding_text = f"{title}. {content}" if title else content

            bulk_body.append({"index": {"_index": INDEX_NAME, "_id": doc_id}})
            bulk_body.append(
                {
                    "title": title,
                    "content": content,
                    "embedding_text": embedding_text,
                }
            )

        # Use the ingest pipeline to auto-generate embeddings
        response = client.bulk(body=bulk_body, pipeline=INGEST_PIPELINE)

        # Extract individual item errors for debugging
        item_errors = []
        if response.get("errors"):
            for item in response.get("items", []):
                for action, result in item.items():
                    if "error" in result:
                        item_errors.append({"id": result.get("_id"), "error": result["error"]})

        logger.info("Indexed documents", extra={
            "count": len(documents),
            "errors": response.get("errors", False),
        })

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {
                    "message": f"Indexed {len(documents)} document(s)",
                    "errors": response.get("errors", False),
                    "item_errors": item_errors[:5] if item_errors else [],
                }
            ),
        }

    except Exception as e:
        logger.exception("Error indexing documents")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }
