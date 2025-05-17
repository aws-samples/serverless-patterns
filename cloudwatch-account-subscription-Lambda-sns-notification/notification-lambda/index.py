import json
import boto3
import gzip
import base64
from io import BytesIO
import os
sns = boto3.client('sns')

def lambda_handler(event, context):
    topicArn = os.environ['SNS_TOPIC_ARN']

    compressed_log_data = event['awslogs']['data']
    uncompressed_log_data = gzip.decompress(base64.b64decode(compressed_log_data))
    print("Printing uncompressed_log_data :", uncompressed_log_data)

    log_events = json.loads(uncompressed_log_data)['logEvents']
    log_group = json.loads(uncompressed_log_data)['logGroup']
    log_stream = json.loads(uncompressed_log_data)['logStream']

    notification_message = f"*** An Exception has occurred within the specified log group. Please review the logs for detailed information and troubleshoot accordingly.***. \n Logdetails : \n Log events received from log group: {log_group}, log stream: {log_stream} \n log event: {log_events}"

    response = sns.publish(
        TopicArn=topicArn,
        Message=notification_message,
        Subject='Account Notification'
        )
    
    print(f"Notification published - messageID:", response['MessageId'])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }