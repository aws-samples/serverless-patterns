#!/usr/bin/env python3
import os

import aws_cdk as cdk

from apigw_rest_eventbridge_sqs import ApigwRestEventBridgeSQSStack


app = cdk.App()
ApigwRestEventBridgeSQSStack(app, "CdkStack",)

app.synth()
