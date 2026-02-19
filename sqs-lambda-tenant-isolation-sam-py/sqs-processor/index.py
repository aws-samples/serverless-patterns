import json
import boto3
import os

lambda_client = boto3.client('lambda')
TENANT_ISOLATED_FUNCTION = os.environ['TENANT_ISOLATED_FUNCTION_NAME']

def handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        
        # Get message group ID from SQS attributes
        attributes = record.get('attributes') or {}
        message_group_id = attributes.get('MessageGroupId')
        
        if not message_group_id:
            print(f"Missing MessageGroupId in SQS record: {record}")
            message_group_id = "default"
        
        lambda_client.invoke(
            FunctionName=TENANT_ISOLATED_FUNCTION,
            InvocationType='Event',
            Payload=json.dumps(body),
            TenantId=message_group_id
        )
        
        print(f"Invoked tenant-isolated function for message group: {message_group_id}")
    
    return {'statusCode': 200}
