#!/usr/bin/env python3

from aws_cdk import App

from vsam_to_dynamo.vsam_to_dynamo_stack import VsamToDynamoStack


app = App()
VsamToDynamoStack(app, "vsam-to-dynamo")

app.synth()
