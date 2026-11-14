#!/usr/bin/env python3
import os

import aws_cdk as cdk

from data_stream_processor.kinesis_lambda import KinesisLambdaStack


app = cdk.App()
KinesisLambdaStack(
    app,
    "KinesisLambdaStack"
)

app.synth()
