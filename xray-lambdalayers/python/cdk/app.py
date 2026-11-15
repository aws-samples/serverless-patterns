#!/usr/bin/env python3
from aws_cdk import App
from lambda_layer_x_ray_stack.lambda_layer_x_ray_stack_stack import LambdaLayerXRayStackStack

app = App()
LambdaLayerXRayStackStack(app, "LambdaLayerXRayStackStack")

app.synth()
