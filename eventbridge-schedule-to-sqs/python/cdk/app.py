#!/usr/bin/env python3
import aws_cdk as cdk

from eventbridge_schedule_to_sqs_cdk_python.eventbridge_schedule_to_sqs_cdk_python_stack import EventbridgeScheduleToSqsCdkPythonStack


app = cdk.App()
EventbridgeScheduleToSqsCdkPythonStack(app, "EventbridgeScheduleToSqsCdkPythonStack")

app.synth()
