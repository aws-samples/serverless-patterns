import logging

import boto3
from botocore.exceptions import ClientError

log = logging.getLogger()
log.setLevel(logging.INFO)

bedrock = boto3.client("bedrock-agent", "us-west-2")


def handler(event, context):
    log.info("Event: %s", event)
    log.info("Context: %s", context)
    try:
        knowledge_base_id = event["knowledgeBaseId"]
        ingestion_job_id = event["ingestionJobId"]
        data_source_id = event["dataSourceId"]

        if knowledge_base_id is None or ingestion_job_id is None or data_source_id is None:
            log.error("Missing required field(s): knowledgeBaseId, ingestionJobId, dataSourceId")
            raise TypeError("knowledgeBaseId, data_source_id and ingestionJobId cannot be None")

        try:
            response = bedrock.get_ingestion_job(
                knowledgeBaseId=knowledge_base_id,
                ingestionJobId=ingestion_job_id,
                dataSourceId=data_source_id,
            )

            ingestion_job = response.get("ingestionJob", [])
            log.info("Ingestion Job response: %s", ingestion_job)

            # Validate response
            if "status" not in ingestion_job:
                raise KeyError("Missing status in response")

            # Log additional information if available
            if "statistics" in ingestion_job:
                log.info("Job statistics: %s", ingestion_job["statistics"])
            if "failureReason" in ingestion_job and ingestion_job["status"] == "FAILED":
                log.error("Job failed: %s", ingestion_job["failureReason"])

            return {
                "knowledgeBaseId": knowledge_base_id,
                "ingestionJobId": ingestion_job["ingestionJobId"],
                "dataSourceId": data_source_id,
                "status": ingestion_job["status"],
            }
        # Validate response
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            error_message = e.response["Error"]["Message"]
            log.error("Bedrock API error: %s - %s", error_code, error_message)
            raise
    except Exception as e:
        log.error("Error processing the request: %s", str(e))
        raise
