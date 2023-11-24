import json
import boto3
import os

sns_topic = os.environ.get('snsTopicARN')
client = boto3.client('rekognition')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = client.start_label_detection(
        Video={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        NotificationChannel={
            'SNSTopicArn': os.environ.get('snsTopicARN'),
            'RoleArn': os.environ.get('snsRole')
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Tagging video...')
    }
