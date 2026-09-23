"""Start an Amazon Bedrock Data Automation (BDA) job for each file uploaded to S3.

Triggered by an S3 ObjectCreated event on the input/ prefix. Calls the BDA runtime
invoke_data_automation_async API, which reads the uploaded file, runs the managed
extraction defined by the BDA project, and writes structured JSON to the output/ prefix.
The heavy lifting is done by BDA - this function only starts the job.
"""
import os
import urllib.parse
import boto3

bda = boto3.client("bedrock-data-automation-runtime")

PROJECT_ARN = os.environ["BDA_PROJECT_ARN"]
PROFILE_ARN = os.environ["BDA_PROFILE_ARN"]
OUTPUT_PREFIX = os.environ.get("OUTPUT_PREFIX", "output")


def handler(event, context):
    started = []
    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])
        response = bda.invoke_data_automation_async(
            inputConfiguration={"s3Uri": "s3://" + bucket + "/" + key},
            outputConfiguration={"s3Uri": "s3://" + bucket + "/" + OUTPUT_PREFIX},
            dataAutomationConfiguration={
                "dataAutomationProjectArn": PROJECT_ARN,
                "stage": "LIVE",
            },
            dataAutomationProfileArn=PROFILE_ARN,
        )
        invocation_arn = response["invocationArn"]
        print("Started BDA job " + invocation_arn + " for s3://" + bucket + "/" + key)
        started.append(invocation_arn)
    return {"startedInvocations": started}
