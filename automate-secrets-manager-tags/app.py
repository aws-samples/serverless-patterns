#!/usr/bin/env python3
import os

import aws_cdk as cdk

from automate_secrets_manager_tags.automate_secrets_manager_tags_stack import AutomateSecretsManagerTagsStack


app = cdk.App()
AutomateSecretsManagerTagsStack(app, "AutomateSecretsManagerTagsStack")

app.synth()
