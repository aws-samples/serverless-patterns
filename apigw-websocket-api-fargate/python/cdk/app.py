#!/usr/bin/env python3
import aws_cdk as cdk

from apigw_websocket_fargate_cdk.apigw_websocket_fargate_cdk_stack import (
    ApigwWebsocketFargateCdkStack,
)


app = cdk.App()
ApigwWebsocketFargateCdkStack(app, "ApigwWebsocketFargateCdkStack")

app.synth()
