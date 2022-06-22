#!/usr/bin/env python3
import os

import aws_cdk as cdk

from iot_s3_lambda_cdk.iot_s3_lambda_cdk_stack import IotS3LambdaCdkStack


app = cdk.App()
IotS3LambdaCdkStack(app, "IotS3LambdaCdkStack")

app.synth()
