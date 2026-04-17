"""
Amazon S3 Files + AWS Lambda

Demonstrates accessing an S3 bucket as a file system from Lambda using
Amazon S3 Files. Files are read and written via standard Python file I/O
at the local mount path — no boto3 S3 calls needed.

The S3 bucket is mounted at /mnt/s3data via the S3 Files file system.
"""

import json
import logging
import os

import pandas as pd

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

MOUNT_PATH = os.environ.get("MOUNT_PATH", "/mnt/s3data")


def lambda_handler(event, context):
    """
    Expected event:
    {
        "file": "input/sample_sales.csv"  # path relative to the S3 Files mount root
    }
    """
    file_key = event.get("file")
    if not file_key:
        return {"statusCode": 400, "body": {"error": "Missing required field: 'file'"}}

    input_path = os.path.join(MOUNT_PATH, file_key)

    if not os.path.exists(input_path):
        return {"statusCode": 404, "body": {"error": f"File not found: {input_path}"}}

    # Read the CSV directly from the S3 Files mount using standard file I/O
    df = pd.read_csv(input_path)
    logger.info("Read %s: %d rows, %d columns", input_path, len(df), len(df.columns))

    return {
        "statusCode": 200,
        "body": {
            "file": input_path,
            "rows": len(df),
            "columns": list(df.columns),
            "preview": df.head(5).to_dict(orient="records"),
        },
    }
