
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0


"""Support S3 Large Deployments using Custom Resource and Assets Bucket"""

import os
import aws_cdk as cdk
from aws_cdk import (
    aws_logs as logs,
    aws_s3 as s3,
    aws_iam as _iam,
    aws_s3_assets as s3assets,
    aws_s3_deployment as s3_deploy
)
from aws_cdk.custom_resources import(
    AwsCustomResource, AwsCustomResourcePolicy, AwsSdkCall, PhysicalResourceId
)

from constructs import Construct


class S3LargeDeploymentStack(cdk.Stack):

    # The code that defines your stack goes here

    def __init__(self, scope: Construct, construct_id: str, s3_custom_bucket, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        file_name = self.node.try_get_context("filename")
        print(file_name)

        asset_bucket = self.upload_to_assets_bucket(
            construct_id, file_name)

        custom_resource_created = self.copy_from_assests_bucket_to_custom_bucket(
            construct_id, asset_bucket, file_name, s3_custom_bucket)

    # Function to Upload the File to Assets Bucket
    def upload_to_assets_bucket(self, construct_id, file_name):
           
            file_path = './assets'
            file_name = file_name
            asset_bucket = s3assets.Asset(self, id=f'{construct_id}-AssetBucket',
            path=os.path.join(file_path,file_name))
            return asset_bucket

    # Custom Function to Copy the File from Assets Bucket to Custom S3 Bucket
    def copy_from_assests_bucket_to_custom_bucket(self, construct_id, asset_bucket, file_name, s3_custom_bucket):
            asset_bucket_object = s3.Bucket.from_bucket_name(
                self, "AssetBucketObject", asset_bucket.s3_bucket_name)

            # Custom Resource Creation to Copy from Asset Bucket to Custom Bucket
            custom_resource_policy = AwsCustomResourcePolicy.from_sdk_calls(
            resources=[f"{asset_bucket_object.bucket_arn}/*",
                f"{s3_custom_bucket.bucket_arn}/*"]
            )

            custom_resource_lambda_role = _iam.Role(scope=self,
                                                id=f'{construct_id}-CustomResourceLambdaRole',
                                                assumed_by=_iam.ServicePrincipal(
                                                    'lambda.amazonaws.com'),
                                                managed_policies=[_iam.ManagedPolicy.from_aws_managed_policy_name(
                                                    "service-role/AWSLambdaBasicExecutionRole"),
                                                    _iam.ManagedPolicy(scope=self,
                                                                       id=f'{construct_id}-CustomResourceLambdaPolicy',
                                                                       managed_policy_name="AssetsBucketAccessPolicy",
                                                                       statements=[_iam.PolicyStatement(
                                                                           resources=[
                                                                               f"{asset_bucket_object.bucket_arn}/*",
                                                                               f"{s3_custom_bucket.bucket_arn}/*"
                                                                            ],
                                                                           actions=[
                                                                               "s3:List*",
                                                                               "s3:PutObject",
                                                                               "s3:GetObject"]
                                                                       )])])

            on_create = AwsSdkCall(action='copyObject',
                               service='S3',
                               physical_resource_id=PhysicalResourceId.of(
                                   f'{asset_bucket.s3_bucket_name}'),
                                parameters={
                                   "Bucket": s3_custom_bucket.bucket_name,
                                   "CopySource": asset_bucket.s3_bucket_name + '/' + asset_bucket.s3_object_key,
                                   "Key": file_name
                                   }
                               )
            custom_resource_creation = AwsCustomResource(scope=self,
                                                     id='CustomResourceSyncWithS3',
                                                     policy=custom_resource_policy,
                                                     log_retention=logs.RetentionDays.ONE_WEEK,
                                                     on_create=on_create,
                                                     on_update=on_create,
                                                     role=custom_resource_lambda_role,
                                                     timeout=cdk.Duration.seconds(300))
            return custom_resource_creation
