#!/usr/bin/env python3
from aws_cdk import App
from sns_sqs_cdk.sns_sqs_cdk_stack import SnsSqsCdkStack


app = App()
SnsSqsCdkStack(app, "SnsSqsCdkStack")

app.synth()
