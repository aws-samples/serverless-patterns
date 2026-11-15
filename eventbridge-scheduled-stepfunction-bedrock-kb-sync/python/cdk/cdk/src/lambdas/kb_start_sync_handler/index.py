import logging
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

log = logging.getLogger()
log.setLevel(logging.INFO)
bedrock = boto3.client("bedrock-agent")


def handler(event, context):
    log.info("Event: %s", event)
    try:
        knowledge_base_id = event["knowledgeBaseId"]
        data_source_id = event["dataSourceId"]
        if knowledge_base_id is None or data_source_id is None:
            raise TypeError("knowledgeBaseId and dataSourceId cannot be None")
        try:
            response = bedrock.start_ingestion_job(
                knowledgeBaseId=knowledge_base_id,
                dataSourceId=data_source_id,
                description=f"Scheduled sync started at {datetime.now().isoformat()}",
            )

            ingestion_job = response.get("ingestionJob", [])
            log.info("Ingestion Job response: %s", ingestion_job)

            # Validate response
            if "ingestionJobId" not in ingestion_job:
                raise KeyError("Missing ingestionJobId in response")

            return {
                "knowledgeBaseId": knowledge_base_id,
                "dataSourceId": data_source_id,
                "ingestionJobId": ingestion_job["ingestionJobId"],
            }
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            error_message = e.response["Error"]["Message"]
            log.error("Bedrock API error: %s - %s", error_code, error_message)
            raise
    except KeyError as e:
        log.error("Missing required field:: %s", {str(e)})
        raise
    except TypeError as e:
        log.error("Invalid parameter type: %s", {str(e)})
        raise
    except Exception as e:
        log.error("Error processing request: %s", {str(e)})
        raise
