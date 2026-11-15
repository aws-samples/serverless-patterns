
   
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""Storage stack that defines the S3 bucket"""

from aws_cdk import (
    aws_s3 as s3,
)
import aws_cdk as cdk
from constructs import Construct
class StorageStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creation of Custom S3 Bucket

        s3_bucket_name = self.node.try_get_context("s3bucketname")

    
        s3_custom_bucket = s3.Bucket(
                self, 'DQBucket',
                block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                bucket_name=s3_bucket_name,
                encryption=s3.BucketEncryption.KMS_MANAGED,
                enforce_ssl=True,
                versioned=True,
                auto_delete_objects=True,
                removal_policy=cdk.RemovalPolicy.DESTROY
            )

        self.s3_custom_bucket = s3_custom_bucket

       

