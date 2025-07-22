#!/usr/bin/env python3
import aws_cdk as cdk
from translate_api.translate_api_stack import TranslateApiStack

app = cdk.App()
TranslateApiStack(app, "TranslateApiStack")
app.synth()
