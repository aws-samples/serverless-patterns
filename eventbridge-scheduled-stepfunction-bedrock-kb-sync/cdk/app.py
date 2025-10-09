#!/usr/bin/env python3
import json
import logging
import os

import aws_cdk as cdk
import yaml
from cdk_nag import AwsSolutionsChecks, NagSuppressions

from stacks.common_lambda_layer_stack import CommonLambdaLayerStack
from stacks.kb_infra_stack import KbInfraStack
from stacks.kb_role_stack import KbRoleStack
from stacks.kb_sync_pipeline_stack import KbSyncPipelineStack
from stacks.vector_store_stacks.oss_infra_stack import OpenSearchServerlessStack

# Set up logging
logger = logging.getLogger(__name__)

app = cdk.App()

config: dict = {}

# Load Config Files in to Dict
for file_path in (
    "config/config.global",
):

    current_file_path = __file__
    project_dir = os.path.dirname(current_file_path)
    config_file_path = os.path.join(project_dir, file_path.format(**os.environ))
    print(f"Reading config file: {config_file_path}")
    for extension in (".yml", ".yaml"):
        formatted_file_path = f"{config_file_path}{extension}"
        if os.path.exists(formatted_file_path):
            print(f"Reading Config File: {formatted_file_path}")
            with open(formatted_file_path, encoding="utf-8") as yaml_file:
                print("Detected Config File: ", config_file_path)
                config.update(yaml.safe_load(yaml_file))
            break

logger.info(json.dumps(config, indent=4))

account = os.environ["CDK_DEFAULT_ACCOUNT"]
region = os.environ["CDK_DEFAULT_REGION"]

# create IAM role for e2e RAG
kb_role_stack = KbRoleStack(
    app,
    "KbRoleStack",
    stack_name="KbRoleStack",
    env=cdk.Environment(
        account=account,
        region=region,
    ),
    params=config,
)

# setup vector store OSS
vector_infra_stack = OpenSearchServerlessStack(
    app,
    "OSSStack",
    stack_name="OSSStack",
    env=cdk.Environment(
        account=account,
        region=region,
    ),
    params=config,
)

# create Knowledgebase and datasource
kb_infra_stack = KbInfraStack(
    app,
    "KbInfraStack",
    stack_name="KbInfraStack",
    env=cdk.Environment(
        account=account,
        region=region,
    ),
    params=config,
)

# set up dependencies
vector_infra_stack.add_dependency(kb_role_stack)
kb_infra_stack.add_dependency(vector_infra_stack)

common_lambda_layer_stack = CommonLambdaLayerStack(
    app,
    "CommonLambdaLayerStack",
    stack_name="CommonLambdaLayerStack",
)


kb_sync_pipeline_stack = KbSyncPipelineStack(
    app,
    "KbSyncPipelineStack",
    stack_name="KbSyncPipelineStack",
    env=cdk.Environment(
        account=account,
        region=region,
    ),
    params=config,
)

kb_sync_pipeline_stack.add_dependency(kb_infra_stack)
kb_sync_pipeline_stack.add_dependency(common_lambda_layer_stack)


cdk.Aspects.of(app).add(AwsSolutionsChecks())
# Suppress the AwsSolutions-* where remediation is already applied and recommendation is out of use case scope

NagSuppressions.add_stack_suppressions(
    kb_role_stack,
    [
        {
            "id": "AwsSolutions-IAM5",
            "reason": "The IAM user, role, or group uses AWS managed policies",
        },
    ],
    apply_to_nested_stacks=True,
)

NagSuppressions.add_stack_suppressions(
    kb_infra_stack,
    [
        {
            "id": "AwsSolutions-IAM5",
            "reason": "The IAM user, role, or group uses AWS managed policies",
        },
    ],
    apply_to_nested_stacks=True,
)

NagSuppressions.add_stack_suppressions(
    vector_infra_stack,
    [
        {
            "id": "AwsSolutions-IAM4",
            "reason": "The IAM user, role, or group uses AWS managed policies",
        },
        {
            "id": "AwsSolutions-IAM5",
            "reason": "The IAM user, role, or group uses AWS managed policies",
        },
        {
            "id": "AwsSolutions-L1",
            "reason": "The non-container Lambda function is not configured to use the latest runtime version",
        },
    ],
    apply_to_nested_stacks=True,
)

NagSuppressions.add_stack_suppressions(
    kb_sync_pipeline_stack,
    [
        {
            "id": "AwsSolutions-IAM4",
            "reason": "The IAM user, role, or group uses AWS managed policies",
        },
        {
            "id": "AwsSolutions-IAM5",
            "reason": "The IAM user, role, or group uses AWS managed policies",
        },
        {
            "id": "AwsSolutions-L1",
            "reason": "The non-container Lambda function is not configured to use the latest runtime version",
        },
        {
            "id": "AwsSolutions-APIG4",
            "reason": "APIGW Methods will use IAM Authorizor eventually",
        },
        {
            "id": "AwsSolutions-COG4",
            "reason": "APIGW Methods will use IAM Authorizor eventually",
        },
        {
            "id": "AwsSolutions-APIG6",
            "reason": "Logging will be added eventually eventually",
        },
        {
            "id": "AwsSolutions-APIG2",
            "reason": "Fast API will validate the requests",
        },
    ],
    apply_to_nested_stacks=True,
)
app.synth()
