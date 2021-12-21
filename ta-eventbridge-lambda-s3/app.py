#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3_bucket_privatizer.s3_bucket_privatizer_stack import S3BucketPrivatizerStack


app = cdk.App()
S3BucketPrivatizerStack(app, "S3BucketPrivatizerStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    # env=cdk.Environment(account='<accountID>', region='us-east-1'),
    )

app.synth()
