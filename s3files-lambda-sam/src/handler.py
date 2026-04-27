"""
Amazon S3 Files + AWS Lambda

Demonstrates accessing an Amazon S3 bucket as a file system from AWS Lambda using
Amazon S3 Files. Files are read and written via standard Python file I/O
at the local mount path.

The Amazon S3 bucket is mounted at /mnt/s3data via the Amazon S3 Files file system.
"""

import csv
import json
import logging
import os

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
    with open(input_path, newline="") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames or []
        rows = list(reader)

    logger.info("Read %s: %d rows, %d columns", input_path, len(rows), len(columns))

    return {
        "statusCode": 200,
        "body": {
            "file": input_path,
            "rows": len(rows),
            "columns": columns,
            "preview": rows[:5],
        },
    }
