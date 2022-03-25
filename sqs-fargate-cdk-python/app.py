#!/usr/bin/env python3

import aws_cdk as cdk
import os

from sqs_fargate_cdk_python.sqs_fargate_cdk_python_stack import SqsFargateCdkPythonStack

app = cdk.App()
SqsFargateCdkPythonStack(app, "sqs-fargate-cdk-python", env=cdk.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"],
                                                                            region=os.environ["CDK_DEFAULT_REGION"]))

app.synth()
