import boto3
import json
from urllib.parse import unquote

def lambda_handler(event, context):
    query_params = event.get('queryStringParameters', {})
    # URL decode the task token
    task_token = unquote(query_params.get('taskToken', ''))
    decision = query_params.get('decision')
    
    sfn = boto3.client('stepfunctions')
    
    try:
        if decision == 'approve':
            sfn.send_task_success(
                taskToken=task_token,
                output=json.dumps({'approved': True})
            )
            message = "Workflow approved successfully"
        else:
            sfn.send_task_failure(
                taskToken=task_token,
                error='Rejected',
                cause='User rejected the workflow'
            )
            message = "Workflow rejected"
            
        return {
            'statusCode': 200,
            'body': json.dumps({'message': message}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
