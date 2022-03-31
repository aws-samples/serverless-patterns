"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""


import boto3
import os
from aws_lambda_powertools import Logger
import traceback
import json


logger = Logger()


def lambdaFirehoseLogger(event, context):
    logger.info(f"event={json.dumps(event)}")

    try:
        stream_name = os.environ.get(
            "FIREHOSE_STREAM_NAME"
        )
    except Exception:
        var = traceback.format_exc()
        logger.error(
            f"ERROR :  {var} \nEnvironment variable FIREHOSE_STREAM_NAME not set"
        )
        return

    firehose = boto3.client('firehose')

    response = firehose.put_record(
        DeliveryStreamName=stream_name,
        Record={'Data': json.dumps(event)}
    )

    logger.info(f"firehose.put_record.response={json.dumps(response)}")
