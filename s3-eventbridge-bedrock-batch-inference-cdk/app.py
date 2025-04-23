#!/usr/bin/env python3
import os

import aws_cdk as cdk

from bedrock_batch_inference_pattern.bedrock_batch_inference_pattern_stack import BedrockBatchInferencePatternStack

app = cdk.App()
BedrockBatchInferencePatternStack(app, "BedrockBatchInferencePatternStack")

app.synth()
