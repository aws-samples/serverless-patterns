#!/usr/bin/env python3
import aws_cdk as cdk
from private_api_gateway.private_api_gateway_stack import PrivateApiGatewayStack

app = cdk.App()

# Get required context parameters
domain_name = app.node.try_get_context("domain_name")
certificate_arn = app.node.try_get_context("certificate_arn")

if not domain_name:
    raise ValueError("domain_name context parameter is required. Use: cdk deploy -c domain_name=api.example.com")

if not certificate_arn:
    raise ValueError("certificate_arn context parameter is required. Use: cdk deploy -c certificate_arn=arn:aws:acm:...")

PrivateApiGatewayStack(
    app, 
    "PrivateApiGatewayStack",
    domain_name=domain_name,
    certificate_arn=certificate_arn,
    env=cdk.Environment(
        account=app.account,
        region=app.region
    )
)

app.synth()
