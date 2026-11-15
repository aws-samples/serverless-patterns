import json
import re
import sys
import boto3
import os
from botocore.exceptions import ClientError

lambda_client = boto3.client('lambda')
TENANT_ISOLATED_FUNCTION = os.environ['TENANT_ISOLATED_FUNCTION_NAME']

TENANT_ID_PATTERN = re.compile(r'^[a-zA-Z0-9-]{1,64}$')
MAX_BODY_SIZE_BYTES = 262144  # 256 KB

def handler(event, context):
    for record in event['Records']:
        try:
            body = json.loads(record['body'])
        except json.JSONDecodeError as e:
            print(f"Failed to parse message body: {e}")
            continue

        body_size = sys.getsizeof(record['body'])
        if body_size > MAX_BODY_SIZE_BYTES:
            print(f"Message body exceeds max size ({body_size} > {MAX_BODY_SIZE_BYTES}), skipping")
            continue

        if not isinstance(body, dict):
            print(f"Message body is not a JSON object, skipping")
            continue

        attributes = record.get('attributes') or {}
        message_group_id = attributes.get('MessageGroupId')

        if not message_group_id:
            raise ValueError("MessageGroupId is required for tenant isolation")

        if not TENANT_ID_PATTERN.match(message_group_id):
            raise ValueError(f"Invalid tenant ID format: {message_group_id}")

        try:
            lambda_client.invoke(
                FunctionName=TENANT_ISOLATED_FUNCTION,
                InvocationType='Event',
                Payload=json.dumps(body),
                TenantId=message_group_id
            )
        except ClientError as e:
            print(f"Lambda invocation failed for tenant {message_group_id}: {e}")
            raise  # Let SQS retry

        print(f"Invoked tenant-isolated function for messagegroup: {message_group_id}")

    return {'statusCode': 200}
