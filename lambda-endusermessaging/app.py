#!/usr/bin/env python3
import os
import aws_cdk as cdk
from simple_sms_messaging.simple_sms_messaging_stack import SimpleSmSMessagingStack

app = cdk.App()

SimpleSmSMessagingStack(
    app, 
    "SimpleSmSMessagingStack",
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION')
    )
)

app.synth()