#!/usr/bin/env python3
import aws_cdk as cdk
from sqs_lambda_cdk.sqs_lambda_cdk_stack import SqsLambdaCdkStack


app = cdk.App()
SqsLambdaCdkStack(app, "SqsLambdaCdkStack")

app.synth()
