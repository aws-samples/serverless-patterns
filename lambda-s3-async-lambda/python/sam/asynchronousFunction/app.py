import boto3
import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client_s3 = boto3.client('s3')

def get_payload_from_event(event):
    data = None

    # S3 file upload trigger event
    if is_event_from_s3(event):
        logger.info("S3 trigger event")
        data = get_payload_from_s3(event)

    # async invoke from SendPayloadFunction
    else:
        logger.info('Async invoke event')
        data = json.loads(event)

    return data

def is_event_from_s3(event):
    return type(event) == type({}) and event.get('Records') and event.get('Records')[0].get('eventSource') == 'aws:s3' and event.get('Records')[0].get('eventName') == 'ObjectCreated:Put'

def get_payload_from_s3(record):
    bucketname = record.get('Records')[0].get('s3').get('bucket').get('name')
    filename = record.get('Records')[0].get('s3').get('object').get('key')

    response = client_s3.get_object(Bucket=bucketname, Key=filename)
    payload = json.loads(response['Body'].read().decode('utf-8'))
    return payload

def lambda_handler(event, context):
    payload = get_payload_from_event(event)

    logger.info(len(payload))