#!/usr/bin/env python3

import aws_cdk as cdk

from bedrock_batch_inference.bedrock_batch_inference_pattern_stack import BedrockBatchInferencePatternStack

app = cdk.App()
stack = BedrockBatchInferencePatternStack(app, "BedrockBatchInferencePatternStack")

app.synth()
