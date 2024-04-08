import json
import boto3
import os
import decimal
import os

client = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('dynamoDBTableName'))

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    record = {'Image': key, 'Bucket': bucket}
    response = client.detect_moderation_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        }
    )
    record['ModerationLabels'] = response['ModerationLabels']
    dynamodb_response = table.put_item(Item=json.loads(json.dumps(record), parse_float=decimal.Decimal))
    return {
        'statusCode': 200,
        'body': json.dumps('Tagging complete.')
    }