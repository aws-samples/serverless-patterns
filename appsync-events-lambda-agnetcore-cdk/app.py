#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import CdkStack


app = cdk.App()

stack_name = app.node.try_get_context("stack_name") or "AppsyncLambdaAgentcore"

region = os.environ.get("AWS_REGION")
if not region:
    raise EnvironmentError("AWS_REGION environment variable must be set")

CdkStack(
    app,
    stack_name,
    env=cdk.Environment(region=region),
)

app.synth()
