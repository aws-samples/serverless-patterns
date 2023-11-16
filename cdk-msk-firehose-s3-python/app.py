#!/usr/bin/env python3

import aws_cdk as cdk
import os

from cdk_msk_kdf_s3.MSKKdfS3Stack import CdkMSKKdfS3Stack
from cdk_msk_serverless.MSKServerlessStack import CdkMSKServerlessVpcStack


app = cdk.App()

env_USA = cdk.Environment(account="816085599212", region="us-east-1")

os.environ['ACCOUNT_ID'] = env_USA.account
os.environ['AWS_REGION'] = env_USA.region
os.environ['TOPIC_NAME'] = 'msk-kdf-s3-topic'
os.environ['S3_NAME'] = 'kinesisdatafirehose-dest-msk-demo-192837128937'

CdkMSKServerlessVpcStack(app, "MSKServerLessStack",env=env_USA)
CdkMSKKdfS3Stack(app, "MSKKdfS3Stack",env=env_USA)

app.synth()
