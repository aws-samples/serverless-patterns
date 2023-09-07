# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import os
import boto3
from aws_lambda_powertools.utilities.data_classes import KinesisStreamEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

def lambda_handler(event: KinesisStreamEvent, context: LambdaContext):
  records = event["Records"]
  print(records)
