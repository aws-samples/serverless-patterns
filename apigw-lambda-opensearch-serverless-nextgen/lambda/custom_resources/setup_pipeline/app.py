"""Custom Resource handler to set up ML model and pipelines at deploy time.

Creates:
- An Amazon Bedrock Titan V2 ML connector
- A registered and deployed ML model
- An ingest pipeline with text_embedding processor
- A hybrid search pipeline with min-max normalization

Properties:
    CollectionEndpoint: The AOSS collection endpoint URL
    ModelRoleArn: IAM role ARN for OpenSearch ML to call Bedrock
    EmbeddingModelId: Bedrock model ID (e.g. amazon.titan-embed-text-v2:0)
    EmbeddingDimension: Vector dimension (e.g. 1024)
"""

from __future__ import annotations

import logging
import os
import time

from opensearch_client import get_client
from crhelper import CfnResource

logger = logging.getLogger(__name__)

helper = CfnResource(json_logging=True, log_level="INFO", sleep_on_delete=30)

SEARCH_PIPELINE_NAME = "hybrid-search-pipeline"
INGEST_PIPELINE_NAME = "embedding-ingest-pipeline"
REGION = os.environ.get("AWS_REGION")


def _wait_for_model_deployed(client, model_id, max_attempts=30, delay=5):
    """Poll model status until deployed or timeout."""
    for _ in range(max_attempts):
        resp = client.transport.perform_request(
            "GET", f"/_plugins/_ml/models/{model_id}"
        )
        status = resp.get("model_state")
        if status == "DEPLOYED":
            return True
        if status in ("DEPLOY_FAILED", "REGISTER_FAILED"):
            raise RuntimeError(f"Model {model_id} failed with state: {status}")
        time.sleep(delay)
    raise TimeoutError(f"Model {model_id} did not reach DEPLOYED state")


def _retry_with_backoff(func, max_attempts=6, initial_delay=10):
    """Retry a function with exponential backoff for auth propagation."""
    delay = initial_delay
    last_error = None
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            last_error = e
            error_str = str(e)
            # Only retry on authorization/forbidden errors (policy propagation)
            if "403" in error_str or "Forbidden" in error_str or "Authorization" in error_str:
                logger.warning(
                    "Authorization error on attempt %d/%d, retrying in %ds: %s",
                    attempt + 1, max_attempts, delay, error_str,
                )
                time.sleep(delay)
                delay = min(delay * 2, 60)
            else:
                raise
    raise last_error


def _setup_ml_and_pipelines(event):
    """Core logic shared by create and update handlers."""
    props = event["ResourceProperties"]
    endpoint = props["CollectionEndpoint"]
    model_role_arn = props["ModelRoleArn"]
    embedding_model_id = props.get("EmbeddingModelId", "amazon.titan-embed-text-v2:0")
    embedding_dimension = int(props.get("EmbeddingDimension", "1024"))

    client = get_client(endpoint, REGION)

    # Step 1: Create the Bedrock connector (with retry for policy propagation)
    connector_body = {
        "name": "Amazon Bedrock Titan Embeddings V2",
        "description": "Connector for Amazon Bedrock Titan Text Embeddings V2",
        "version": "1.0",
        "protocol": "aws_sigv4",
        "credential": {
            "roleArn": model_role_arn,
        },
        "parameters": {
            "region": REGION,
            "service_name": "bedrock",
            "model": embedding_model_id,
        },
        "actions": [
            {
                "action_type": "predict",
                "method": "POST",
                "headers": {"content-type": "application/json"},
                "url": f"https://bedrock-runtime.{REGION}.amazonaws.com/model/{embedding_model_id}/invoke",
                "request_body": '{"inputText": "${parameters.inputText}", "dimensions": '
                + str(embedding_dimension)
                + ', "normalize": true}',
                "pre_process_function": "connector.pre_process.bedrock.embedding",
                "post_process_function": "connector.post_process.bedrock.embedding",
            }
        ],
    }

    connector_resp = _retry_with_backoff(
        lambda: client.transport.perform_request(
            "POST", "/_plugins/_ml/connectors/_create", body=connector_body
        )
    )
    connector_id = connector_resp["connector_id"]
    logger.info("Created connector: %s", connector_id)

    # Step 2: Register the model
    register_body = {
        "name": "Bedrock Titan Embed V2",
        "function_name": "remote",
        "description": "Titan Text Embeddings V2 via Bedrock connector",
        "connector_id": connector_id,
    }

    register_resp = client.transport.perform_request(
        "POST", "/_plugins/_ml/models/_register", body=register_body
    )
    model_id = register_resp["model_id"]
    logger.info("Registered model: %s", model_id)

    # Step 3: Deploy the model
    client.transport.perform_request(
        "POST", f"/_plugins/_ml/models/{model_id}/_deploy"
    )
    logger.info("Deploy initiated for model: %s", model_id)

    # Wait for deployment
    _wait_for_model_deployed(client, model_id)
    logger.info("Model deployed successfully: %s", model_id)

    # Step 4: Create the ingest pipeline with text_embedding processor
    ingest_pipeline_body = {
        "description": "Ingest pipeline that generates embeddings via Bedrock Titan V2",
        "processors": [
            {
                "text_embedding": {
                    "model_id": model_id,
                    "field_map": {
                        "embedding_text": "embedding",
                    },
                }
            }
        ],
    }

    client.transport.perform_request(
        "PUT",
        f"/_ingest/pipeline/{INGEST_PIPELINE_NAME}",
        body=ingest_pipeline_body,
    )
    logger.info("Created ingest pipeline: %s", INGEST_PIPELINE_NAME)

    # Step 5: Create/update the search pipeline with normalization
    search_pipeline_body = {
        "description": "Normalization pipeline for hybrid search",
        "phase_results_processors": [
            {
                "normalization-processor": {
                    "normalization": {"technique": "min_max"},
                    "combination": {
                        "technique": "arithmetic_mean",
                        "parameters": {"weights": [0.3, 0.7]},
                    },
                }
            }
        ],
    }

    client.transport.perform_request(
        "PUT",
        f"/_search/pipeline/{SEARCH_PIPELINE_NAME}",
        body=search_pipeline_body,
    )
    logger.info("Created search pipeline: %s", SEARCH_PIPELINE_NAME)

    # Store outputs for !GetAtt
    helper.Data["SearchPipeline"] = SEARCH_PIPELINE_NAME
    helper.Data["IngestPipeline"] = INGEST_PIPELINE_NAME
    helper.Data["ModelId"] = model_id
    helper.Data["ConnectorId"] = connector_id

    return f"{connector_id}/{model_id}"


@helper.create
def on_create(event, _context):
    """Create ML connector, model, ingest pipeline, and search pipeline."""
    return _setup_ml_and_pipelines(event)


@helper.update
def on_update(event, _context):
    """Update recreates all ML resources and pipelines."""
    return _setup_ml_and_pipelines(event)


@helper.delete
def on_delete(event, _context):
    """Delete pipelines and ML resources on stack deletion."""
    props = event["ResourceProperties"]
    endpoint = props["CollectionEndpoint"]

    client = get_client(endpoint, REGION)

    # Delete ingest pipeline
    try:
        client.transport.perform_request(
            "DELETE", f"/_ingest/pipeline/{INGEST_PIPELINE_NAME}"
        )
    except Exception:
        logger.warning("Failed to delete ingest pipeline", exc_info=True)

    # Delete search pipeline
    try:
        client.transport.perform_request(
            "DELETE", f"/_search/pipeline/{SEARCH_PIPELINE_NAME}"
        )
    except Exception:
        logger.warning("Failed to delete search pipeline", exc_info=True)

    # Undeploy and delete model (best effort from physical resource ID)
    physical_id = event.get("PhysicalResourceId", "")
    if "/" in physical_id:
        connector_id, model_id = physical_id.split("/", 1)
        try:
            client.transport.perform_request(
                "POST", f"/_plugins/_ml/models/{model_id}/_undeploy"
            )
            time.sleep(5)
            client.transport.perform_request(
                "DELETE", f"/_plugins/_ml/models/{model_id}"
            )
        except Exception:
            logger.warning("Failed to delete model %s", model_id, exc_info=True)

        try:
            client.transport.perform_request(
                "DELETE", f"/_plugins/_ml/connectors/{connector_id}"
            )
        except Exception:
            logger.warning(
                "Failed to delete connector %s", connector_id, exc_info=True
            )


def lambda_handler(event, context):
    """Main Lambda handler — delegates to crhelper."""
    helper(event, context)
