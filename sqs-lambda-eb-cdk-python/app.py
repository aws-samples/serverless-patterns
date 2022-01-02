#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sqs_lambda_eb_cdk.sqs_lambda_eb_cdk_stack import SqsLambdaEbCdkStack


app = cdk.App()
SqsLambdaEbCdkStack(app, "SqsLambdaEbCdkStack",)

app.synth()
