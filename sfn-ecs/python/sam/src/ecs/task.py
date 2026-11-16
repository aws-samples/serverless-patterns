import boto3
import sys
import os
import json
import csv
from datetime import datetime
from datetime import date
from botocore.exceptions import ClientError

def convert_to_json_string(t):
    return f'{t}'


now = date.today()
processing_date = now.strftime("%m-%d-%Y")


s3Client = boto3.client('s3')
sfnClient = boto3.client('stepfunctions')

bucket = os.environ["S3_BUCKET"]
task_token = os.environ['TASK_TOKEN']

response = s3Client.list_objects_v2(Bucket=bucket)
file_list = response['Contents']


try:
    for fileObject in file_list:
        obj = s3Client.get_object(Bucket=bucket, Key=fileObject['Key'])
        data = obj['Body'].read().decode('utf-8').splitlines(True)
        reader = csv.reader(data)
        print("File Found: " + fileObject['Key'])
        
        print("File content:")
        for row in reader:
            print(row)

    # Create response to send to Step Function
    result = {
        "bucket": bucket,  
        "result": "pass",
        "processing_date": processing_date,
    }
    print("Sending pass output to Step Functions with task token " + task_token)
    #print(result)

    sfnClient.send_task_success(
        taskToken=task_token,
        output=json.dumps(result, default=convert_to_json_string)
    )

except Exception as e:
    result = {
        "files": file_list,
        "result": "fail",
        "cause": e.__class__,
        "processing_date": processing_date,
    }
    print("Sending fail output to Step Functions with task token " + task_token)
    print(result)
    sfnClient.send_task_failure(
        taskToken=task_token,
        error="TaskException",
        cause=json.dumps(result, default=convert_to_json_string)
    )
