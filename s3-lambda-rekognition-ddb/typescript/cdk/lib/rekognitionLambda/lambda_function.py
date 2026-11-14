# lambda handler
import boto3
import json
import os



def callRekognition(bucket_name,file_name):
    rekognition_client = boto3.client('rekognition')
    response = rekognition_client.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':file_name}})
    return response


def writeDynamoDB(file_name, labels):
    dynamodb_client = boto3.client('dynamodb')
    return dynamodb_client.put_item(TableName=os.environ['TABLE_NAME'], Item={'file_name': {'S':file_name}, 'labels': {'S':json.dumps(labels)}})


def lambda_handler(event, context):
    # S3 event
    s3_event = event['Records'][0]['s3']
    bucket_name = s3_event['bucket']['name']
    file_name = s3_event['object']['key']
    response = callRekognition(bucket_name,file_name)
    writeDynamoDB(file_name, response)

