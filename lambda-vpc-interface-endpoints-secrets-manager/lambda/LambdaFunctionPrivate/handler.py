import json
import boto3
from botocore.config import Config


def lambda_handler(event, context):
    client = boto3.client('secretsmanager', 
        config=Config(
            connect_timeout=2, 
            read_timeout=2,
            retries = {
                'max_attempts': 2,
            }
        )
    )

    list_secrets = client.list_secrets()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'api_response': json.dumps(list_secrets, default=str)
    }
