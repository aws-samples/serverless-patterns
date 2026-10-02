"""Start an Amazon Bedrock Data Automation (BDA) job for each file uploaded to Amazon S3.

Triggered by an Amazon S3 ObjectCreated event on the input/ prefix. Calls the BDA
runtime invoke_data_automation_async API, which reads the uploaded file, runs the
managed extraction defined by the BDA project, and writes structured JSON to the
output/ prefix. The heavy lifting is done by BDA, so this function only starts the job.
"""
import os
import urllib.parse

import boto3
from botocore.exceptions import ClientError

bda = boto3.client("bedrock-data-automation-runtime")

PROJECT_ARN = os.environ["BDA_PROJECT_ARN"]
PROFILE_ARN = os.environ["BDA_PROFILE_ARN"]
OUTPUT_PREFIX = os.environ.get("OUTPUT_PREFIX", "output")


def handler(event, context):
    started = []
    failed = []

    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])
        size = record["s3"]["object"].get("size")

        # A key ending in "/" is the folder marker the Amazon S3 console creates, and a
        # zero byte object has nothing to extract. BDA rejects both with a
        # ValidationException, so skip them instead of starting a job that cannot work.
        if key.endswith("/") or size == 0:
            print("Skipping s3://" + bucket + "/" + key + ": folder marker or empty object")
            continue

        try:
            response = bda.invoke_data_automation_async(
                inputConfiguration={"s3Uri": "s3://" + bucket + "/" + key},
                outputConfiguration={"s3Uri": "s3://" + bucket + "/" + OUTPUT_PREFIX},
                dataAutomationConfiguration={
                    "dataAutomationProjectArn": PROJECT_ARN,
                    "stage": "LIVE",
                },
                dataAutomationProfileArn=PROFILE_ARN,
            )
        except ClientError as error:
            # One unusable file (for example an unsupported format) must not stop the
            # remaining records in the same event from being processed.
            code = error.response["Error"]["Code"]
            message = error.response["Error"]["Message"]
            print("ERROR starting BDA job for s3://" + bucket + "/" + key + ": " + code + ": " + message)
            failed.append(key)
            continue

        invocation_arn = response["invocationArn"]
        print("Started BDA job " + invocation_arn + " for s3://" + bucket + "/" + key)
        started.append(invocation_arn)

    if failed:
        # Amazon S3 invokes this function asynchronously. Raising keeps the Lambda
        # asynchronous retry behavior for the failed records and makes the failure
        # visible in the function Errors metric instead of hiding it.
        raise RuntimeError("Failed to start BDA jobs for: " + ", ".join(failed))

    return {"startedInvocations": started}
