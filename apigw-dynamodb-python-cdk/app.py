#!/usr/bin/env python3
import os
import aws_cdk as cdk
from apigw_dynamodb_python_cdk.apigw_dynamodb_python_cdk_stack import ApigwDynamodbPythonStack


app = cdk.App()

vtl_dir = os.path.join(os.path.dirname(__file__), "vtl")
group_names = ["Group-FreeTier", "Group-BasicUsagePlan"]

app.node.set_context("group_names", group_names)
app.node.set_context("vtl_dir", vtl_dir)

usage_plans = {
    "FreeTier": {
        "quota": {
            "limit": 500,
            "period": "DAY"
        },
        "throttle": {
            "burst_limit": 10,
            "rate_limit": 5
        },
        "method": "GET"
    },
    "BasicUsagePlan": {
        "quota": {
            "limit": 10000,
            "period": "MONTH"
        },
        "throttle": {
            "burst_limit": 100,
            "rate_limit": 50
        },
        "method": "POST"
    }
}

app.node.set_context("usage_plans", usage_plans)

stack = ApigwDynamodbPythonStack(app, "ApigwDynamodbPythonStack")

app.synth()
