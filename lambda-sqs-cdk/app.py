#!/usr/bin/env python3
import os

from aws_cdk import core

from lambda_sqs_cdk.lambda_sqs_cdk_stack import LambdaSqsCdkStack


app = core.App()
LambdaSqsCdkStack(app, "LambdaSqsCdkStack")

app.synth()
