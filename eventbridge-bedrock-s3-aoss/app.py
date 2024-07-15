#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.bedrock_knowledgebase_stack import BedrockKnowledgebaseStack
from stacks.opensearch_serverless_stack import OpenSearchServerlessStack
from stacks.ingestion_job_resources_stack import IngestionJobResourcesStack
from stacks.bedrock_service_role_stack import BedrockServiceRoleStack
from stacks.bedrock_knowledgebase_logging import KnowledgeBaseLoggingStack


app = cdk.App()

stack_suffix = app.node.try_get_context('stack_suffix')

bedrock_sr_ap_stack = BedrockServiceRoleStack(app,
    "BedrockServiceRoleAccessPolicyStack",
    env=cdk.Environment(
        region=os.getenv('us-west-2')
    ),
    stack_suffix=stack_suffix
)

opensearch_serverless_stack = OpenSearchServerlessStack(app, "OpenSearchServerlessStack",
    env=cdk.Environment(
        region=os.getenv('us-west-2')
    ),
    stack_suffix=stack_suffix,
    bedrock_kb_service_role_arn =  bedrock_sr_ap_stack.bedrock_kb_service_role_arn
)                   

bedrock_kb_stack = BedrockKnowledgebaseStack(app,
    "BedrockKnowledgebaseStack",
    env=cdk.Environment(
        region=os.getenv('us-west-2')
    ),
    stack_suffix=stack_suffix,
    cfn_aoss_collection_arn = opensearch_serverless_stack.cfn_aoss_collection_arn,
    index_name = opensearch_serverless_stack.index_name,
    bedrock_kb_service_role_arn = bedrock_sr_ap_stack.bedrock_kb_service_role_arn
)
ingestion_job_resources_stack = IngestionJobResourcesStack(app,
    "IngestionResourcesStack",
    env=cdk.Environment(
        region=os.getenv('us-west-2')
    ),
    stack_suffix=stack_suffix,
    knowledge_base_id=bedrock_kb_stack.knowledge_base_id,
    data_source_id=bedrock_kb_stack.knowledgebase_datasource_id
)

knowledge_base_logging_stack = KnowledgeBaseLoggingStack(app,
    "KnowledgeBaseLoggingStack",
    env=cdk.Environment(
        region=os.getenv('us-west-2')
    ),
    stack_suffix=stack_suffix,
    knowledge_base_id=bedrock_kb_stack.knowledge_base_id
)

app.synth()
