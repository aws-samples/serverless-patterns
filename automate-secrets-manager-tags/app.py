#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.main import AutomateSecretsManagerTagsStack


app = cdk.App()
AutomateSecretsManagerTagsStack(app, "AutomateSecretsManagerTagsStack")

app.synth()
