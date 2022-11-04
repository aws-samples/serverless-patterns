#!/usr/bin/env python3
import aws_cdk as cdk

from glue_eventbridge_lambda_cdk.glue_eventbridge_lambda_cdk_stack import GlueEventBridgeLambda


app = cdk.App()
GlueEventBridgeLambda(app, "GlueEventBridgeLambda")

app.synth()
