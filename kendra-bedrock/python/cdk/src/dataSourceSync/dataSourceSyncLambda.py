
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

INDEX_ID = os.environ['INDEX_ID']
DS_ID = os.environ['DS_ID']
AWS_REGION = os.environ['AWS_REGION']
KENDRA = boto3.client('kendra')

def start_data_source_sync(dsId, indexId):
    logger.info(f"start_data_source_sync(dsId={dsId}, indexId={indexId})")
    resp = KENDRA.start_data_source_sync_job(Id=dsId, IndexId=indexId)
    logger.info(f"response:" + json.dumps(resp))

def lambda_handler(event, context):
    logger.info("Received event: %s" % json.dumps(event))
    start_data_source_sync(DS_ID, INDEX_ID)
    return 
