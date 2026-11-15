#!/usr/bin/env python3
import os

import aws_cdk as cdk

from eventbridge_schedule_to_eventbridge_cdk_python.eventbridge_schedule_to_eventbridge_cdk_python_stack import EventbridgeScheduleToEventbridgeCdkPythonStack


app = cdk.App()
EventbridgeScheduleToEventbridgeCdkPythonStack(app, "EventbridgeScheduleToEventbridgeCdkPythonStack")

app.synth()
