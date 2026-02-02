
#!/usr/bin/env python3
import os

import aws_cdk as cdk

from apigw_sqs_lambda import ApigwSqsLambdaStack
import aws_cdk as cdk

app = cdk.App()
ApigwSqsLambdaStack(app, "genai-simple-scalable-api")
app.synth()