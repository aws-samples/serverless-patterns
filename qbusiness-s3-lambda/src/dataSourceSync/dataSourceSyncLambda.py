
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import logging
import boto3
import cfnresponse
import random
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

INDEX_ID = os.environ['INDEX_ID']
DS_ID = os.environ['DS_ID']
AWS_REGION = os.environ['AWS_REGION']
QBUSINESS = boto3.client('qbusiness')
APP_ID = os.environ['APP_ID']

def start_data_source_sync(dsId, indexId, appID):
    logger.info(f"start_data_source_sync(dsId={dsId}, indexId={indexId})")
    resp = QBUSINESS.start_data_source_sync_job(dataSourceId=dsId, indexId=indexId, applicationId=appID)
    logger.info(f"response:" + json.dumps(resp))

def lambda_handler(event, context):
    logger.info("Received event: %s" % json.dumps(event))
    start_data_source_sync(DS_ID, INDEX_ID, APP_ID)
    status = cfnresponse.SUCCESS
    cfnresponse.send(event, context, status, {}, None)
    return status
