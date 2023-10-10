#!/usr/bin/env python3
import os

import aws_cdk as cdk

from eventbridge_pipes_sqs_to_multiple_sqs.eventbridge_pipes_sqs_to_multiple_sqs_stack import EventbridgePipesSqsToMultipleSqsStack


app = cdk.App()
EventbridgePipesSqsToMultipleSqsStack(app, "EventbridgePipesSqsToMultipleSqsStack")

app.synth()
