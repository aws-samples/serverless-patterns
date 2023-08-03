import boto3
import sys
import logging
import os
import datetime
import csv
import json

MY_SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
client = boto3.client('s3')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
sns_client = boto3.client('sns')
lambda_tmp_dir = '/tmp'

def lambda_handler(event, context):
    
    for r in event['Records']:
        s3 = r['s3']
        bucket = s3['bucket']['name']
        key = s3['object']['key']
    source = download_json(bucket, key)
    with open(source, 'r') as content_file:
        content = json.load(content_file)
        if content['prediction'] == 1 :
            timestamp = content['timestamp']
            Messages = 'Oh no! It seems that we have a problem.\n\n'
            Messages += f"At {timestamp}, our diagnostic systems detected an anomaly with the equipment.\n\n"
            Messages += 'Here are the details of the components and their anomaly values:\n\n'
   
            # Iterate through diagnostics and creatively append them to the Messages
            for diag in content['diagnostics']:
                component = diag['name'].split('\\')[1].replace('_', ' ').title()  # Format the component's name
                value = diag['value']
                Messages += f"- {component}: {value}\n"
   
            # Finalize the message
            Messages += "\nPlease take the necessary actions to prevent equipment failure."
   
            # Publish the message to SNS
            sns_client.publish(
                TopicArn = MY_SNS_TOPIC_ARN,
                Subject = '🚨 Equipment Failure Prediction Alert 🚨',
                Message = Messages
            )

def download_json(bucket, key):
    local_source_json = lambda_tmp_dir + "/" + key.split('/')[-1]
    directory = os.path.dirname(local_source_json)
    if not os.path.exists(directory):
        os.makedirs(directory)
    client.download_file(bucket, key.replace("%3A", ":"), local_source_json)
    return local_source_json

