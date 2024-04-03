#!/usr/bin/env python3

import aws_cdk as cdk

from cdk.cdk import PreSignedURLStack


app = cdk.App()
PreSignedURLStack(app, "PreSignedURLStack")

app.synth()
