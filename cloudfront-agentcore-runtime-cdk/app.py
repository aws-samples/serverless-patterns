#!/usr/bin/env python3

import aws_cdk as cdk
import os

from infra.agentcore_stack import AgentcoreStack
from infra.cloudfront_stack import CloudFrontStack

app = cdk.App()

region = os.environ.get("CDK_DEFAULT_REGION")
if not region:
    raise ValueError("CDK_DEFAULT_REGION environment variable must be set. Run: export CDK_DEFAULT_REGION=<your-region>")

agentcore_stack = AgentcoreStack(app, "AgentCoreAgentsStack",
    env=cdk.Environment(region=region),
    cross_region_references=True
)

cloudfront_stack = CloudFrontStack(app, "CloudFrontToAgentCoreStack",
    env=cdk.Environment(region=region),
    cross_region_references=True,
    a2a_agent_runtime_arn=agentcore_stack.a2a_agent_runtime_arn,
    http_agent_runtime_arn=agentcore_stack.http_agent_runtime_arn,
    mcp_agent_runtime_arn=agentcore_stack.mcp_agent_runtime_arn
)
cloudfront_stack.add_dependency(agentcore_stack)

app.synth()
