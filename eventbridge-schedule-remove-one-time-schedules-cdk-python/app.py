#!/usr/bin/env python3
import aws_cdk as cdk

from eventbridge_schedule_remove_onetime_schedules_cdk_python.eventbridge_schedule_remove_onetime_schedules_cdk_python_stack import EventBridgeRemoveOnetimeSchedulesCdkPythonStack

app = cdk.App()
EventBridgeRemoveOnetimeSchedulesCdkPythonStack(app, "EventBridgeRemoveOnetimeSchedulesCdkPythonStack")

app.synth()
