#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.bedrock_knowledgebase_stack import BedrockKnowledgebaseStack
from stacks.opensearch_serverless_stack import OpenSearchServerlessStack
from stacks.ingestion_job_resources_stack import IngestionJobResourcesStack
from stacks.bedrock_service_role_stack import BedrockServiceRoleStack


app = cdk.App()

bedrock_sr_ap_stack = BedrockServiceRoleStack(app,
    "BedrockServiceRoleStack",
)

opensearch_serverless_stack = OpenSearchServerlessStack(app, "AOSSStack",
    bedrock_kb_service_role_arn =  bedrock_sr_ap_stack.bedrock_kb_service_role_arn
)                   

bedrock_kb_stack = BedrockKnowledgebaseStack(app,
    "BedrockKBStack",
    cfn_aoss_collection_arn = opensearch_serverless_stack.cfn_aoss_collection_arn,
    index_name = opensearch_serverless_stack.index_name,
    bedrock_kb_service_role_arn = bedrock_sr_ap_stack.bedrock_kb_service_role_arn
)
ingestion_job_resources_stack = IngestionJobResourcesStack(app,
    "SchedulerStack",
    knowledge_base_id=bedrock_kb_stack.knowledge_base_id,
    data_source_id=bedrock_kb_stack.knowledgebase_datasource_id
)

app.synth()
