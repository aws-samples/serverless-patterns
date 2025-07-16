import boto3
import json
import os
from urllib.parse import quote

def lambda_handler(event, context):
    task_token = quote(event['taskToken'])  # URL encode the task token
    execution_id = event['execution']
    
    api_endpoint = os.environ['API_ENDPOINT']
    approve_url = f"{api_endpoint}?taskToken={task_token}&decision=approve"
    reject_url = f"{api_endpoint}?taskToken={task_token}&decision=reject"
    
    # Create message in SNS message format
    message_data = {
        'default': 'Workflow Approval Required',
        'email': f"""
Workflow Approval Required - {execution_id}

A new approval is required for workflow execution {execution_id}

To approve: {approve_url}

To reject: {reject_url}
        """
    }
    
    sns = boto3.client('sns')
    try:
        # Publish message with MessageStructure as 'json'
        response = sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Message=json.dumps(message_data),
            MessageStructure='json'
        )
        return {
            'statusCode': 200,
            'body': 'Approval notification sent successfully'
        }
    except Exception as e:
        print(str(e))
        raise
