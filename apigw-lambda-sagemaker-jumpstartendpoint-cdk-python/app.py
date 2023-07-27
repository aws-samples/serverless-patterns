#!/usr/bin/env python3
import aws_cdk as cdk
import boto3
from cdk_stablediffusion_python.cdk_stablediffusion_python_stack import CdkStablediffusionPythonStack
from util.sagemaker_util import *

region_name = boto3.Session().region_name
env = {"region": region_name}

# Text to Image model parameters
TXT2IMG_MODEL_ID = "model-txt2img-stabilityai-stable-diffusion-v2-1-base"

# For Development
TXT2IMG_INFERENCE_INSTANCE_TYPE = "ml.g5.2xlarge"

# For Production
#TXT2IMG_INFERENCE_INSTANCE_TYPE = "ml.g5.12xlarge"

TXT2IMG_MODEL_INFO = get_sagemaker_uris(model_id=TXT2IMG_MODEL_ID,
                                        instance_type=TXT2IMG_INFERENCE_INSTANCE_TYPE,
                                        region_name=region_name)

app = cdk.App()

stack = CdkStablediffusionPythonStack(
    app,
    "Web3WorkshopStableDiffusionStack",
    model_info=TXT2IMG_MODEL_INFO,
    env=env
)

app.synth()
