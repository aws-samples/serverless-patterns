import os
import json
import boto3

def lambda_handler(event, context):
    # Initialize SNS client
    sns_client = boto3.client('sns')

    # Get the SNS topic ARN from the environment variable
    sns_topic_arn = os.environ['TOPIC_ARN']

    # Log the received message from SQS
    for record in event['Records']:
        body = json.loads(record['body'])
        print(f"Received message: {json.dumps(body)}")

        # Send notification to SNS topic
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=json.dumps(body),
            Subject='SQS Event Notification'
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
