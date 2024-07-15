import json
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_bedrock as bedrock,
    aws_s3 as s3,
    aws_opensearchserverless as aoss,
    aws_iam as iam,
)
from constructs import Construct

class BedrockKnowledgebaseStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,
                 stack_suffix,
                 cfn_aoss_collection_arn,
                 index_name,
                 bedrock_kb_service_role_arn,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #setup variables for use in constructs
        BEDROCK_KNOWLEDGEBASE_PARAMS = self.node.try_get_context('bedrock_knowledgebase_params')
        embedding_model_id = BEDROCK_KNOWLEDGEBASE_PARAMS['embedding_model_id']
        embedding_model_arn = f"arn:aws:bedrock:{self.region}::foundation-model/{embedding_model_id}"
        metadata_field = BEDROCK_KNOWLEDGEBASE_PARAMS['vector_index_metadata_field']
        text_field = BEDROCK_KNOWLEDGEBASE_PARAMS['vector_index_text_field']
        vector_field = BEDROCK_KNOWLEDGEBASE_PARAMS['vector_index_vector_field']
        s3_bucket_name = f"{BEDROCK_KNOWLEDGEBASE_PARAMS['s3_bucket_name_prefix']}-{stack_suffix.lower()}"

        #Create an S3 bucket to store the data files needed for RAG Knowledge Base
        knowledgebase_datasource_bucket = s3.Bucket(
            self,
            "KBDataSourceS3Bucket",
            bucket_name=s3_bucket_name,
            public_read_access=False
        )
                                  
        #Create the Bedrock Knowledge Base with the s3 bucket as knowledge base
        bedrock_knowledgebase = bedrock.CfnKnowledgeBase(self, "BedrockKB",
            name=f"knowledge-base-{stack_suffix}",
            knowledge_base_configuration=bedrock.CfnKnowledgeBase.KnowledgeBaseConfigurationProperty(
                type="VECTOR",
                vector_knowledge_base_configuration=bedrock.CfnKnowledgeBase.VectorKnowledgeBaseConfigurationProperty(
                    embedding_model_arn=f"{embedding_model_arn}"
                )
            ),
            role_arn=bedrock_kb_service_role_arn,            
            storage_configuration=bedrock.CfnKnowledgeBase.StorageConfigurationProperty(
                type="OPENSEARCH_SERVERLESS",
                # the properties below are optional
                opensearch_serverless_configuration=bedrock.CfnKnowledgeBase.OpenSearchServerlessConfigurationProperty(
                    collection_arn=cfn_aoss_collection_arn,
                    vector_index_name=index_name,
                    field_mapping=bedrock.CfnKnowledgeBase.OpenSearchServerlessFieldMappingProperty(
                        metadata_field=metadata_field,
                        text_field=text_field,
                        vector_field=vector_field
                    )
                )
            ),
            description="RAG Knowledge Base for Amazon Bedrock"
        )
        
        #Add a KB datasource with S3 datasource configuration
        knowledgebase_datasource = bedrock.CfnDataSource(self, "BedrockKBDataSource",
            name=f"bedrock_kb_datasource-{stack_suffix}",
            description="Bedrock Knowledgebase DataSource Configuration",
            data_source_configuration=bedrock.CfnDataSource.DataSourceConfigurationProperty(
                s3_configuration=bedrock.CfnDataSource.S3DataSourceConfigurationProperty(
                    bucket_arn=knowledgebase_datasource_bucket.bucket_arn,
                ),
                type="S3"
            ),
            vector_ingestion_configuration=bedrock.CfnDataSource.VectorIngestionConfigurationProperty (
                chunking_configuration=bedrock.CfnDataSource.ChunkingConfigurationProperty(
                    chunking_strategy="FIXED_SIZE",
                    fixed_size_chunking_configuration=bedrock.CfnDataSource.FixedSizeChunkingConfigurationProperty(
                        max_tokens=1024,
                        overlap_percentage=30
                    )
                )
            ),
            knowledge_base_id=bedrock_knowledgebase.attr_knowledge_base_id,
        )
        self.knowledge_base_id = bedrock_knowledgebase.attr_knowledge_base_id
        self.knowledgebase_datasource_id = knowledgebase_datasource.attr_data_source_id
        CfnOutput(
            self, "knowledge_base_id", value=self.knowledge_base_id,export_name="knowledgeBaseId")
        CfnOutput(self, "data_source_id", value=self.knowledgebase_datasource_id, export_name="DataSourceId")