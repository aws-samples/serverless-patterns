#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_msk_kdf_s3.MSKKdfS3Stack import CdkMSKKdfS3Stack
from cdk_msk_serverless.MSKServerlessStack import CdkMSKServerlessVpcStack


app = cdk.App()

env_USA = cdk.Environment(account="816085599212", region="us-east-1")

CdkMSKServerlessVpcStack(app, "MSKServerLessStack", env=env_USA)
CdkMSKKdfS3Stack(app, "MSKKdfS3Stack", env=env_USA)

app.synth()
