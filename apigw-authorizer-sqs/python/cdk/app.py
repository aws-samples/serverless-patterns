#!/usr/bin/env python3
import os

import aws_cdk as cdk

from apigw_sqs.apigw_sqs_stack import ApigwSqsStack
from apigw_sqs.apigw_sqs_auth_stack import ApigwSqsAuthStack
app = cdk.App()
#ApigwSqsStack(app, "ApigwSqsStack")
ApigwSqsAuthStack(app,"ApigwSqsAuthStack")

app.synth()
