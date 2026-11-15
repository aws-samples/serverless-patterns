#!/usr/bin/env python3

import aws_cdk as cdk

from iot_sns_sqs_cdk.iot_sns_sqs_cdk_stack import IotSnsSqsCdkStack


app = cdk.App()
IotSnsSqsCdkStack(app, "iot-sns-sqs-cdk")

app.synth()
