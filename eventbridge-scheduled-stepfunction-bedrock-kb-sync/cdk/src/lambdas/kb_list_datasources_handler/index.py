import logging

import boto3
from botocore.exceptions import ClientError

log = logging.getLogger()
log.setLevel(logging.INFO)

bedrock = boto3.client("bedrock-agent", "us-west-2")


def handler(event, context):
    log.info("Event: %s", event)
    try:
        # Validate input
        if "knowledgeBaseId" not in event:
            error_msg = "Missing required field: knowledgeBaseId"
            log.error(error_msg)
            raise ValueError(error_msg)

        knowledge_base_id = event["knowledgeBaseId"]

        # List data sources without pagination since it"s not supported
        try:
            response = bedrock.list_data_sources(knowledgeBaseId=knowledge_base_id)
            data_sources = response.get("dataSourceSummaries", [])
            log.info("Data sources: %s", data_sources)

            return {
                "dataSources": [
                    {
                        "knowledgeBaseId": knowledge_base_id,
                        "dataSourceId": ds["dataSourceId"],
                        "name": ds.get("name", ""),
                        "status": ds.get("status", ""),
                    }
                    for ds in data_sources
                ]
            }
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            error_message = e.response["Error"]["Message"]
            log.error("Bedrock API error: %s - %s", error_code, error_message)
            raise

    except Exception as e:
        log.error("Error processing request: %s", str(e))
        raise
