#!/usr/bin/env python3
import aws_cdk as cdk
import boto3
from stack.ApigwLambdaSagemakerJumpstartendpointStack import ApigwLambdaSagemakerJumpstartendpointStack
from util.sagemaker_util import *

region_name = boto3.Session().region_name
env = {"region": region_name}


# Obtain the model ID from: https://sagemaker.readthedocs.io/en/v2.173.0/doc_utils/pretrainedmodels.html
# Here we are using Flan T5 XL Model
MODEL_ID = "huggingface-text2text-flan-t5-xl"

# Change the instance type to match your model. 
# For GPU Service Quota related issues, please raise a quota request from AWS console
INFERENCE_INSTANCE_TYPE = "ml.g5.2xlarge"

# Name of the stack:
STACK_NAME = "apigw-lambda-sagemaker-jumpstartendpoint-stack"



MODEL_INFO = get_sagemaker_uris(model_id=MODEL_ID,
                                        instance_type=INFERENCE_INSTANCE_TYPE,
                                        region_name=region_name)

app = cdk.App()

stack = ApigwLambdaSagemakerJumpstartendpointStack(
    app,
    STACK_NAME,
    model_info=MODEL_INFO,
    env=env
)

app.synth()
