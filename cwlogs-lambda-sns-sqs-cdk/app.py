#!/usr/bin/env python3

import aws_cdk as cdk

from src.cwlogs_lambda_sns_sqs.cwlogs_lambda_sns_sqs_stack import CwlogsLambdaSnsSqsStack


app = cdk.App()
CwlogsLambdaSnsSqsStack(app, "cwlogs-lambda-sns-sqs")

app.synth()
