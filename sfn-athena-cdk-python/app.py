#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sfn_athena_cdk_python.sfn_athena_cdk_python_stack import SfnAthenaCdkPythonStack


app = cdk.App()
SfnAthenaCdkPythonStack(app, "SfnAthenaCdkPythonStack",
    env=cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"])
    )

app.synth()
