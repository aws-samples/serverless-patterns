#!/usr/bin/env python3
import os

import aws_cdk as cdk

from apigw_lambda import ApigwLambdaStack
import aws_cdk as cdk

app = cdk.App()
ApigwLambdaStack(app, "genai-simple-api")
app.synth()


