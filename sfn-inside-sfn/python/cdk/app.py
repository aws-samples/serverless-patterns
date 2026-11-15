#!/usr/bin/env python3
import aws_cdk as cdk

from sfn_inside_sfn_cdk.sfn_inside_sfn_cdk_stack import SfnInsideSfnCdkStack


app = cdk.App()
SfnInsideSfnCdkStack(app, "SfnInsideSfnCdkStack")

app.synth()
