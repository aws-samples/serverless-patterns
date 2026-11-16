import json
import os
import boto3

def lambda_handler(event, context):
    
    bedrock_agent_client = boto3.client('bedrock-agent')

    # Specify the Knowledge Base ID
    knowledge_base_id = os.environ['KNOWLEDGE_BASE_ID']
    data_source_id = os.environ['DATA_SOURCE_ID']

    response = bedrock_agent_client.start_ingestion_job(
        dataSourceId=data_source_id,
        description=f"Scheduled Knowledge Base Sync - {event['time']}",
        knowledgeBaseId=knowledge_base_id
    )
    message = f"Ingestion job with ID: {response['ingestionJob']['ingestionJobId']} started at {response['ingestionJob']['startedAt'] } with current status:{response['ingestionJob']['status']}"
    # Print the sync job ID
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': message
        })
    }   