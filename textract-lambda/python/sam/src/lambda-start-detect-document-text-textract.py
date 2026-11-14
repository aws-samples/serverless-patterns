import json
import boto3
import os
import decimal

client = boto3.client('textract')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('dynamoDBTableName'))

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    record = {'Image': key, 'Bucket': bucket}
    response = client.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        }
    )
    record['DetectedText'] = response
    dynamodb_response = table.put_item(Item=json.loads(json.dumps(record), parse_float=decimal.Decimal))
    return {
        'statusCode': 200,
        'body': json.dumps('Textract complete.')
    }