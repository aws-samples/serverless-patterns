#!/usr/bin/env python3
import os

import aws_cdk as cdk

from apigw_bedrock_cognito_cdk.apigw_bedrock_cognito_cdk_stack import (
    ApigwBedrockCognitoCdkStack,
)


app = cdk.App()

organization_domain = app.node.try_get_context("ORGANIZATION_DOMAIN")
api_throttle_rate_limit = app.node.try_get_context("API_THROTTLE_RATE_LIMIT") or 1
api_throttle_burst_limit = app.node.try_get_context("API_THROTTLE_BURST_LIMIT") or 2
api_throttle_settings = {
    "rate_limit": int(api_throttle_rate_limit),
    "burst_limit": int(api_throttle_burst_limit),
}
api_quota_limit = app.node.try_get_context("API_QUOTA_LIMIT") or 25
api_quota_period = app.node.try_get_context("API_QUOTA_PERIOD") or "DAY"
api_quota_settings = {"limit": int(api_quota_limit), "period": api_quota_period}

ApigwBedrockCognitoCdkStack(
    app,
    "ApigwBedrockCognitoCdkStack",
    organization_domain=organization_domain,
    api_throttle_settings=api_throttle_settings,
    api_quota_settings=api_quota_settings,
)

app.synth()
