import json
import boto3
import decimal
import os

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('dynamoDBTableName'))

def lambda_handler(event, context):
    message = json.loads(json.loads(event['Records'][0]['body'])['Message'])
    if message.get('Status'):
        if message.get('Status') == 'SUCCEEDED':
            job_id = message.get('JobId')
            rekognition_response = rekognition.get_label_detection(
                JobId=job_id
            )
            key = message.get('Video').get('S3ObjectName')
            bucket = message.get('Video').get('S3Bucket')
            dynamodb_response = table.put_item(Item=json.loads(json.dumps({'Video': key, 'Bucket': bucket, 'Metadata': rekognition_response.get('VideoMetadata'), 'Labels': rekognition_response.get('Labels') }), parse_float=decimal.Decimal))
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully stored video tags.')
    }
