#!/usr/bin/env python3
import aws_cdk as cdk

from eventbridge_schedule_to_sns_cdk_python.eventbridge_schedule_to_sns_cdk_python_stack import EventbridgeScheduleToSnsCdkPythonStack


app = cdk.App()
EventbridgeScheduleToSnsCdkPythonStack(app, "EventbridgeScheduleToSnsCdkPythonStack")

app.synth()