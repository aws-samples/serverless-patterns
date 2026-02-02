import json
import boto3
import os

lambda_client = boto3.client('lambda')
TENANT_ISOLATED_FUNCTION = os.environ['TENANT_ISOLATED_FUNCTION_NAME']

def handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        customer_id = body.get('customer-id')
        
        if not customer_id:
            print(f"Missing customer-id in message: {body}")
            continue
        
        lambda_client.invoke(
            FunctionName=TENANT_ISOLATED_FUNCTION,
            InvocationType='Event',
            Payload=json.dumps(body),
            TenantId=customer_id
        )
        
        print(f"Invoked tenant-isolated function for customer: {customer_id}")
    
    return {'statusCode': 200}
