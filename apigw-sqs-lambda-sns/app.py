#!/usr/bin/env python3
import aws_cdk as cdk
from webhook_sns.webhook_sns_stack import WebhookSnsStack

app = cdk.App()
WebhookSnsStack(app, "WebhookSnsStack")

app.synth()
