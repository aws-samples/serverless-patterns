"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import os.path
from os import path
from typing import Mapping
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput, AssetType, TerraformAsset
from cdktf_cdktf_provider_aws import (
    AwsProvider,
    lambdafunction,
    iam,
    s3,
    cloudwatch,
    datasources
)
from cdktf_cdktf_provider_random import (
    RandomProvider,
    Id
)
from helpers.hash import getB64FileSha256Hash
from helpers.config import getDeploymentConfig
from helpers.layers import downloadPillowLayerFile


class S3LambdaTextractStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str, config: Mapping[str, any]):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region=config.get("region"))

        RandomProvider(self, "random_provider")

        deploymentId = Id(self, "random_id", byte_length=4).hex

        inputBucket = s3.S3Bucket(
            self,
            id="s3_bucket_input",
            bucket=f"s3-lambda-textract-"
                   f"input-bucket-{deploymentId}",
            tags=config.get("tags", {}),
            force_destroy=True
        )

        s3.S3BucketPublicAccessBlock(
            self,
            id="s3_bucket_input_public_access_blocked",
            bucket=inputBucket.id,
            block_public_acls=True,
            block_public_policy=True,
            restrict_public_buckets=True,
            ignore_public_acls=True
        )

        TerraformOutput(self, id="s3_bucket_input_arn", value=inputBucket.arn)

        outputBucket = s3.S3Bucket(
            self,
            id="s3_bucket_output",
            bucket=f"s3-lambda-textract-"
                   f"output-bucket-{deploymentId}",
            tags=config.get("tags", {}),
            force_destroy=True
        )

        s3.S3BucketPublicAccessBlock(
            self,
            id="s3_bucket_output_public_access_blocked",
            bucket=outputBucket.id,
            block_public_acls=True,
            block_public_policy=True,
            restrict_public_buckets=True,
            ignore_public_acls=True
        )

        TerraformOutput(self, id="s3_bucket_output_arn", value=outputBucket.arn)

        logGroup = cloudwatch.CloudwatchLogGroup(
            self,
            id="lambda_cloudwatch_log_group",
            name=f"/aws/lambda/s3-lambda-textract-lambda-{deploymentId}",
            retention_in_days=3,
            tags=config.get("tags", {})
        )

        TerraformOutput(self, id="lambda_cloudwatch_log_group_arn",
                        value=logGroup.arn)

        if not os.path.exists(path.abspath("assets/lambda/layers/python/PIL")):
            downloadPillowLayerFile(directory=path.abspath("assets/lambda/layers"),
                                    url=config["layers"]["pillow"].get("url"),
                                    file_hash=config["layers"]["pillow"].get("hash"))
        else:
            if config["layers"]["pillow"].get("always_refresh", False) is True:
                downloadPillowLayerFile(directory=path.abspath("assets/lambda/layers"),
                                        url=config["layers"]["pillow"].get("url"),
                                        file_hash=config["layers"]["pillow"].get("hash"))

        pillowLayerAsset = TerraformAsset(
            self,
            id="python_pillow_layer",
            path=path.abspath("assets/lambda/layers"),
            type=AssetType(AssetType.ARCHIVE)
        )

        pillowLayer = lambdafunction.LambdaLayerVersion(
            self,
            id="lambda_pillow_Layer",
            layer_name=f"pythonPillowLayer-{deploymentId}",
            compatible_runtimes=["python3.9"],
            filename=pillowLayerAsset.path
        )

        TerraformOutput(self, id="lambda_pillow_mayer_arn", value=pillowLayer.arn)

        textractStatement = iam.DataAwsIamPolicyDocumentStatement(
            sid="AllowTextractServiceToAnalyseExpenseDocument",
            actions=[
                "textract:AnalyzeExpense",
                "textract:GetExpenseAnalysis",
                "textract:StartExpenseAnalysis"
            ],
            effect="Allow",
            # Amazon Textract does not support resource-based policies
            # https://docs.aws.amazon.com/textract/latest/dg/security_iam_service-with-iam.html
            resources=["*"]
        )

        InputBucketStatement = iam.DataAwsIamPolicyDocumentStatement(
            sid="AllowLambdaToAccessS3ToReadObjects",
            actions=[
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            effect="Allow",
            resources=[inputBucket.arn,
                       f"{inputBucket.arn}/*"]
        )

        outputBucketStatement = iam.DataAwsIamPolicyDocumentStatement(
            sid="AllowLambdaToAccessS3ToPutObjects",
            actions=[
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            effect="Allow",
            resources=[outputBucket.arn,
                       f"{outputBucket.arn}/*"]
        )

        cloudwatchLogGroupStatement = iam.DataAwsIamPolicyDocumentStatement(
            sid="AllowLambdaToAccessCloudWatchToWriteLogs",
            actions=[
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            effect="Allow",
            resources=[logGroup.arn,
                       f"{logGroup.arn}:*"]
        )

        lambdaPrincipals = iam.DataAwsIamPolicyDocumentStatementPrincipals(
            identifiers=["lambda.amazonaws.com"],
            type="Service"
        )

        lambdaAssumeRoleStatement = iam.DataAwsIamPolicyDocumentStatement(
            sid="AllowLambdaServiceToAssumeThisRole",
            actions=["sts:AssumeRole"],
            effect="Allow",
            principals=[lambdaPrincipals]
        )

        lambdaPolicyDocument = iam.DataAwsIamPolicyDocument(
            self,
            id="lambda_policy_document",
            statement=[textractStatement, InputBucketStatement,
                       outputBucketStatement, cloudwatchLogGroupStatement]
        )

        lambdaRoleDocument = iam.DataAwsIamPolicyDocument(
            self,
            id="lambda_role_document",
            statement=[lambdaAssumeRoleStatement]
        )

        lambdaPolicy = iam.IamPolicy(
            self,
            id="s3-lambda-textract-policy",
            name=f"s3-lambda-textract-policy-{deploymentId}",
            tags=config.get("tags", {}),
            policy=lambdaPolicyDocument.json
        )

        lambdaRole = iam.IamRole(
            self,
            id="s3-lambda-textract-role",
            name=f"s3-lambda-textract-role-{deploymentId}",
            tags=config.get("tags", {}),
            assume_role_policy=lambdaRoleDocument.json
        )

        iam.IamRolePolicyAttachment(
            self,
            id="s3-lambda-textract-policy-role-attachment",
            policy_arn=lambdaPolicy.arn,
            role=lambdaRole.name
        )

        TerraformOutput(self, id="lambda_policy_arn", value=lambdaPolicy.arn)
        TerraformOutput(self, id="lambda_role_arn", value=lambdaRole.arn)

        lambdaAsset = TerraformAsset(
            self,
            id="python_lambda_asset",
            path=path.abspath("assets/lambda/src"),
            type=AssetType(AssetType.ARCHIVE)
        )

        lambdaFunction = lambdafunction.LambdaFunction(
            self,
            id="lambda_function",
            function_name=f"s3-lambda-textract-lambda-{deploymentId}",
            filename=lambdaAsset.path,
            handler="lambdaTextract.lambdaTextract",
            runtime="python3.9",
            role=lambdaRole.arn,
            publish=True,
            memory_size=128,
            timeout=30,
            tags=config.get("tags", {}),
            environment=lambdafunction.LambdaFunctionEnvironment(
                variables={
                    "SAVE_OUTPUT_IMAGE": "True",
                    "OUTPUT_BUCKET_NAME": outputBucket.id
                }
            ),
            layers=[
                f"arn:aws:lambda:{config.get('region')}:"
                f"017000801446:layer:AWSLambdaPowertoolsPython:13",
                pillowLayer.arn
            ]
        )

        TerraformOutput(self, id="lambda_function_arn",
                        value=lambdaFunction.arn)

        callerIdentity = datasources.DataAwsCallerIdentity(
            self,
            id='caller_identity'
        )

        lambdafunction.LambdaPermission(
            self,
            id="s3_bucket_permission_to_invoke_lambda",
            action="lambda:InvokeFunction",
            function_name=lambdaFunction.arn,
            principal="s3.amazonaws.com",
            source_account=callerIdentity.account_id,
            source_arn=inputBucket.arn
        )

        notificationLambda = s3.S3BucketNotificationLambdaFunction(
            id="s3_bucket_lambda_notification_events",
            events=["s3:ObjectCreated:*"],
            lambda_function_arn=lambdaFunction.arn,
            filter_suffix=".png"
        )

        s3.S3BucketNotification(
            self,
            id="s3_bucket_lambda_notification",
            bucket=inputBucket.id,
            lambda_function=[notificationLambda]
        )


def main():
    """
    build resources via CDK-TF
    """

    CONFIG_FILE = "config.json"

    config = getDeploymentConfig(CONFIG_FILE)

    # region = config.get("region")
    # tags = config.get("tags", {})
    # pillow_layer_refresh = config["layers"]["pillow"].get("always_refresh", False)
    # pillow_layer_version = config["layers"]["pillow"].get("version", "latest")

    app = App()
    S3LambdaTextractStack(app, "s3-lambda-textract-stack", config=config)
    app.synth()


if __name__ == "__main__":
    main()
