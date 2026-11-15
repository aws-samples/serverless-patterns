# Import Boto 3 for AWS Glue
import boto3
import os

client = boto3.client('glue')


def handler(event, context):
    glueJobName = os.environ['JOB_NAME']
    response = client.start_job_run(
        JobName=glueJobName,
        Timeout=10
    )
    return True
