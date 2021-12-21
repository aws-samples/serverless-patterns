#!/usr/bin/env python3

from aws_cdk import core

from vsam_to_dynamo.vsam_to_dynamo_stack import VsamToDynamoStack


app = core.App()
VsamToDynamoStack(app, "vsam-to-dynamo")

app.synth()
