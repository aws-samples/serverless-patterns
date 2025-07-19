#!/usr/bin/env python3
import os
import aws_cdk as cdk
from personalized_sms_briefing_bedrock.personalized_sms_briefing_bedrock_stack import PersonalizedSmsBriefingBedrockStack

app = cdk.App()

PersonalizedSmsBriefingBedrockStack(
    app, 
    "PersonalizedSmsBriefingBedrockStack",
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION')
    )
)

app.synth()