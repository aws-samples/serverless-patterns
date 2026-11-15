#!/usr/bin/env python3
from aws_cdk import App

from lambda_sqs_cdk.lambda_sqs_cdk_stack import LambdaSqsCdkStack


app = App()
LambdaSqsCdkStack(app, "LambdaSqsCdkStack")

app.synth()
