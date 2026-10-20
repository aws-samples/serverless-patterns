#!/usr/bin/env python3

import os

import aws_cdk as cdk

from infra.agentcore_identity_stack import AgentCoreIdentityStack

app = cdk.App()

region = os.environ.get("CDK_DEFAULT_REGION")
if not region:
    raise ValueError(
        "CDK_DEFAULT_REGION environment variable must be set. "
        "Run: export CDK_DEFAULT_REGION=<your-region>"
    )

AgentCoreIdentityStack(
    app,
    "AgentCoreIdentityCognitoMultiTenantStack",
    env=cdk.Environment(region=region),
)

app.synth()
