import json
import boto3
import os
from datetime import datetime

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Tracer

tracer = Tracer()
sns_topic = os.environ['SNS_TOPIC']
sns = boto3.client('sns')

@tracer.capture_lambda_handler
def lambda_handler(event, context):

    now = datetime.now()                                        
    date = "%m/%d/%Y"                                           
    time = "%H:%M"                                          
    current_time = now.strftime(date+" "+time)
    message = "This message was sent: " + current_time

    sns.publish(
        TopicArn=sns_topic,
        Message=message
    )


    return {
        'statusCode': 200,
        'body': json.dumps(message)
    } 

