#!/usr/bin/env python3
import os

import aws_cdk as cdk

from iot_kinesis_lambda_cdk.iot_kinesis_lambda_cdk_stack import IotKinesisLambdaCdkStack


app = cdk.App()
IotKinesisLambdaCdkStack(app, "IotKinesisLambdaCdkStack")

app.synth()
