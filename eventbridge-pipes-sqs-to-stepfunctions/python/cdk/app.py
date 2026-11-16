#!/usr/bin/env python3
import os

import aws_cdk as cdk

from eventbridge_pipes_sqs_to_stepfunctions_cdk_python.eventbridge_pipes_sqs_to_stepfunctions_cdk_python_stack import EventbridgePipesSqsToStepfunctionsCdkPythonStack


app = cdk.App()
EventbridgePipesSqsToStepfunctionsCdkPythonStack(app, "EventbridgePipesSqsToStepfunctionsCdkPythonStack")

app.synth()
