#!/usr/bin/env python3

import aws_cdk as cdk

# from cdk_msk_firehose_s3_python.cdk_msk_firehose_s3_python_stack import CdkMskFirehoseS3PythonStack

from cdk_msk_kdf_s3.MSKKdfS3Stack import CdkMSKKdfS3Stack
from cdk_msk_serverless.MSKServerlessStack import CdkMSKServerlessVpcStack

app = cdk.App()


CdkMSKServerlessVpcStack(app, "MSKServerLessStack")
CdkMSKKdfS3Stack(app, "MSKKdfS3Stack")

app.synth()
