#!/usr/bin/env python3
import aws_cdk as cdk

from stack.agentcore_runtime_code_interpreter_s3_stack import AgentCoreRuntimeCodeInterpreterS3Stack

app = cdk.App()
AgentCoreRuntimeCodeInterpreterS3Stack(app, "AgentCoreRuntimeCodeInterpreterS3Stack")
app.synth()
