#!/usr/bin/env python3
import os

import aws_cdk as cdk

from eventbridge_pipes_sqs_to_stepfunctions_python.eventbridge_pipes_sqs_to_stepfunctions_python_stack import SqsToStepfunctionsFilterTransformStack


app = cdk.App()
SqsToStepfunctionsFilterTransformStack(app, "SqsToStepfunctionsFilterTransformStack")

app.synth()
