#!/usr/bin/env python3
import os

import aws_cdk as cdk

from eventbridge_pipes_dynamodbstream_to_sqs_cdk_python.eventbridge_pipes_dynamodbstream_to_sqs_cdk_python_stack import EventbridgePipesDynamodbstreamToSqsCdkPythonStack


app = cdk.App()
EventbridgePipesDynamodbstreamToSqsCdkPythonStack(app, "EventbridgePipesDynamodbstreamToSqsCdkPythonStack")

app.synth()
