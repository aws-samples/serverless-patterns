#!/usr/bin/env python3
import os

import aws_cdk as cdk

from eventbridge_schedule_to_step_function_cdk_python.eventbridge_schedule_to_step_function_cdk_python_stack import EventbridgeScheduleToStepFunctionCdkPythonStack


app = cdk.App()
EventbridgeScheduleToStepFunctionCdkPythonStack(app, "EventbridgeScheduleToStepFunctionCdkPythonStack")

app.synth()
