#!/usr/bin/env python3
import os

import aws_cdk as cdk

from src.cdkstack import SqsToStepfunctionsFilterTransformStack


app = cdk.App()
SqsToStepfunctionsFilterTransformStack(app, "SqsToStepfunctionsFilterTransformStack")

app.synth()
