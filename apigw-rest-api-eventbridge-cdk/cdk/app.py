#!/usr/bin/env python3
import os

from apigw_rest_eventbridge import ApigwRestEventBridgeStack
import aws_cdk as cdk

app = cdk.App()
ApigwRestEventBridgeStack(app, "ApigwRestEventBridgeStack")

app.synth()
