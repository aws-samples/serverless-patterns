#!/usr/bin/env python3
import os

import aws_cdk as cdk

from step_function_callback.step_function_callback_stack import StepFunctionCallbackStack


app = cdk.App()
StepFunctionCallbackStack(app, "StepFunctionCallbackStack")

app.synth()
