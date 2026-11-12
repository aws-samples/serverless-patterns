"""Reads the uploaded text document so the workflow can pass it to the agents.

The document text travels in the state payload, and Step Functions limits a
state's input and output to 256 KiB. Larger files fail here with a clear error
instead of failing later with States.DataLimitExceeded.
"""
import os

import boto3

MAX_BYTES = int(os.environ.get("MAX_DOCUMENT_BYTES", "200000"))
s3 = boto3.client("s3")


class DocumentTooLarge(Exception):
    pass


def handler(event, context):
    bucket, key = event["bucket"], event["key"]
    obj = s3.get_object(Bucket=bucket, Key=key)
    if obj["ContentLength"] > MAX_BYTES:
        raise DocumentTooLarge(f"{key} is {obj['ContentLength']} bytes. The limit is {MAX_BYTES} bytes.")
    return {"key": key, "body": obj["Body"].read().decode("utf-8", errors="replace")}
