#!/usr/bin/env python3
import os
import aws_cdk as cdk
from eventbridge_pipes_sqs_to_dynamodb.eventbridge_pipes_sqs_to_dynamodb import EventbridgePipesSqsToDynamodb

app = cdk.App()
stack = EventbridgePipesSqsToDynamodb(app, "EventbridgePipesSqsToDynamodb")

app.synth()