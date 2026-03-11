#!/usr/bin/env python3
"""CDK app entrypoint for the AppSync Events + Lambda + AgentCore stack."""
import os

import aws_cdk as cdk
from cdk_nag import AwsSolutionsChecks

from cdk.stack import ChatStack


app = cdk.App()

stack_name = app.node.try_get_context("stack_name") or "AppsyncLambdaAgentcore"

region = os.environ.get("AWS_REGION")
if not region:
    raise EnvironmentError("AWS_REGION environment variable must be set")

ChatStack(
    app,
    stack_name,
    env=cdk.Environment(region=region),
)

cdk.Aspects.of(app).add(AwsSolutionsChecks(verbose=True))

app.synth()
