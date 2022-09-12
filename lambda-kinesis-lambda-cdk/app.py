#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_kinesis_lambda_cdk.lambda_kinesis_lambda_cdk_stack import LambdaKinesisLambdaCdkStack

app = cdk.App()
LambdaKinesisLambdaCdkStack(app, "LambdaKinesisLambdaCdkStack")

app.synth()