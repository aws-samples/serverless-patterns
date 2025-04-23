#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import CfnParameter

from bedrock_batch_inference_pattern.bedrock_batch_inference_pattern_stack import BedrockBatchInferencePatternStack

app = cdk.App()
stack = BedrockBatchInferencePatternStack(app, "BedrockBatchInferencePatternStack")

app.synth()
