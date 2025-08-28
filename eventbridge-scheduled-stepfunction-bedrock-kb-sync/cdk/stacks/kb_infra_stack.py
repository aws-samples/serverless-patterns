from aws_cdk import (
    RemovalPolicy,
    Stack,
)
from aws_cdk import aws_bedrock as bedrock
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_ssm as ssm
from constructs import Construct


class KbInfraStack(Stack):
    def __init__(
        self,
        scope: Construct,
        stack_id: str,
        params: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope=scope, id=stack_id, **kwargs)

        self.aws_partition = Stack.of(self).partition
        region = Stack.of(self).region
        account_id = Stack.of(self).account

        # Construct ARNs using the correct self.aws_partition
        self.embedding_model_id = params["embedding_model_id"]
        self.kb_role_name = params["kb_role_name"]
        self.embedding_model_arn = f"arn:{self.aws_partition}:bedrock:{region}::foundation-model/{self.embedding_model_id}"
        self.parser_model_arn = (
            f"arn:{self.aws_partition}:bedrock:{region}::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
        )

        self.index_name = "kb-index"
        self.kb_chunk_max_size = params["kb_chunk_max_size"]
        self.kb_chunk_overlap_percentage = params["kb_chunk_overlap_percentage"]
        self.kb_source_bucket = f"kb-data-source-{account_id}"
        self.intermediate_bucket_name = f"{params['intermediate_bucket_name']}-{account_id}"

        # Create knowledge base from OpenSearchService
        self.collection_arn = ssm.StringParameter.from_string_parameter_attributes(
            self, "KbCollectionArn", parameter_name="/collection-arn"
        ).string_value

        self.kb_role_arn = ssm.StringParameter.from_string_parameter_attributes(
            self, "KbRoleArn", parameter_name="/role-arn"
        ).string_value

        self.knowledge_base = self.create_knowledge_base_oss()

        # Store collection ARN in SSM
        self.knowledge_base_id = ssm.StringParameter(
            self,
            "KBId",
            parameter_name="/kb-id",
            string_value=self.knowledge_base.attr_knowledge_base_id,
        )

        self.create_data_source(self.knowledge_base, self.kb_source_bucket, "")

        self.guardrail = self.create_guardrail()
        # Store Guardrail ARN in SSM
        self.guardrail_arn = ssm.StringParameter(
            self,
            "GuardRailArn",
            parameter_name="guardrail-arn",
            string_value=self.guardrail.attr_guardrail_arn,
        )

    def create_knowledge_base_oss(self) -> bedrock.CfnKnowledgeBase:
        intermediate_bucket = s3.Bucket(
            self,
            "IntermediateS3Bucket",
            bucket_name=self.intermediate_bucket_name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            server_access_logs_prefix="access-logs",
        )

        supplemental_data_storage_configuration = bedrock.CfnKnowledgeBase.SupplementalDataStorageConfigurationProperty(
            supplemental_data_storage_locations=[
                bedrock.CfnKnowledgeBase.SupplementalDataStorageLocationProperty(
                    supplemental_data_storage_location_type="S3",
                    s3_location=bedrock.CfnKnowledgeBase.S3LocationProperty(uri=f"s3://{self.intermediate_bucket_name}"),
                )
            ]
        )
        knowledge_base = bedrock.CfnKnowledgeBase(
            self,
            "KnowledgeBase",
            knowledge_base_configuration=bedrock.CfnKnowledgeBase.KnowledgeBaseConfigurationProperty(
                type="VECTOR",
                vector_knowledge_base_configuration=bedrock.CfnKnowledgeBase.VectorKnowledgeBaseConfigurationProperty(
                    embedding_model_arn=self.embedding_model_arn,
                    supplemental_data_storage_configuration=supplemental_data_storage_configuration,
                ),
            ),
            name="KnowledgeBase",
            role_arn=self.kb_role_arn,
            description="Knowledge base with OSS",
            storage_configuration=bedrock.CfnKnowledgeBase.StorageConfigurationProperty(
                type="OPENSEARCH_SERVERLESS",
                opensearch_serverless_configuration=bedrock.CfnKnowledgeBase.OpenSearchServerlessConfigurationProperty(
                    collection_arn=self.collection_arn,
                    field_mapping=bedrock.CfnKnowledgeBase.OpenSearchServerlessFieldMappingProperty(
                        metadata_field="AMAZON_BEDROCK_METADATA",
                        text_field="AMAZON_BEDROCK_TEXT_CHUNK",
                        vector_field="bedrock-knowledge-base-default-vector",
                    ),
                    vector_index_name=self.index_name,
                ),
            ),
        )
        # Add the dependency
        knowledge_base.node.add_dependency(intermediate_bucket)

        return knowledge_base

    def create_data_source(self, knowledge_base, bucket, bucket_path) -> bedrock.CfnDataSource:
        source_bucket = s3.Bucket(
            self,
            "DataSourceS3Bucket",
            bucket_name=bucket,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            server_access_logs_prefix="access-logs",
        )

        kb_id = knowledge_base.attr_knowledge_base_id
        # source_s3_bucket_arn = f"arn:{self.aws_partition}:s3:::{bucket}"
        parsing_configuration = bedrock.CfnDataSource.ParsingConfigurationProperty(
            parsing_strategy="BEDROCK_DATA_AUTOMATION",
            bedrock_data_automation_configuration=bedrock.CfnDataSource.BedrockDataAutomationConfigurationProperty(
                parsing_modality="MULTIMODAL"
            ),
        )

        vector_ingestion_config = bedrock.CfnDataSource.VectorIngestionConfigurationProperty(
            chunking_configuration=bedrock.CfnDataSource.ChunkingConfigurationProperty(
                chunking_strategy="FIXED_SIZE",
                fixed_size_chunking_configuration=bedrock.CfnDataSource.FixedSizeChunkingConfigurationProperty(
                    max_tokens=self.kb_chunk_max_size, overlap_percentage=self.kb_chunk_overlap_percentage
                ),
            ),
            parsing_configuration=parsing_configuration,
        )

        if bucket_path:
            s3_config = bedrock.CfnDataSource.S3DataSourceConfigurationProperty(
                bucket_arn=source_bucket.bucket_arn,
                inclusion_prefixes=[f"{bucket_path}/"],
            )
        else:
            s3_config = bedrock.CfnDataSource.S3DataSourceConfigurationProperty(
                bucket_arn=source_bucket.bucket_arn,
            )
        datasource = bedrock.CfnDataSource(
            self,
            f"RagDataSource{bucket}",
            data_source_configuration=bedrock.CfnDataSource.DataSourceConfigurationProperty(
                s3_configuration=s3_config,
                type="S3",
            ),
            knowledge_base_id=kb_id,
            name=f"dataSource-{bucket}",
            description="Routing Rag DataSource",
            vector_ingestion_configuration=vector_ingestion_config,
        )
        datasource.node.add_dependency(source_bucket)

        return datasource

    def create_guardrail(self) -> bedrock.CfnGuardrail:
        return bedrock.CfnGuardrail(
            self,
            "RagGuardrail",
            blocked_input_messaging="Sorry, I cannot answer this question.",
            blocked_outputs_messaging="Sorry, I cannot answer this question.",
            name="guardrail",
            description="Guardrail with comprehensive content filtering",
            content_policy_config=bedrock.CfnGuardrail.ContentPolicyConfigProperty(
                filters_config=[
                    # Hate Speech Filter
                    bedrock.CfnGuardrail.ContentFilterConfigProperty(
                        type="HATE",
                        input_strength="HIGH",
                        output_strength="NONE",
                    ),
                    # Sexual Content Filter
                    bedrock.CfnGuardrail.ContentFilterConfigProperty(
                        type="SEXUAL",
                        input_strength="HIGH",
                        output_strength="NONE",
                    ),
                    # INSULTS Filter
                    bedrock.CfnGuardrail.ContentFilterConfigProperty(
                        type="INSULTS",
                        input_strength="HIGH",
                        output_strength="NONE",
                    ),
                    # Violent Filter
                    bedrock.CfnGuardrail.ContentFilterConfigProperty(
                        type="VIOLENCE",
                        input_strength="HIGH",
                        output_strength="NONE",
                    ),
                    # MISCONDUCT Filter
                    bedrock.CfnGuardrail.ContentFilterConfigProperty(
                        type="MISCONDUCT",
                        input_strength="HIGH",
                        output_strength="NONE",
                    ),
                    # PROMPT_ATTACK Filter
                    bedrock.CfnGuardrail.ContentFilterConfigProperty(
                        type="PROMPT_ATTACK",
                        input_strength="HIGH",
                        output_strength="NONE",
                    ),
                ]
            ),
        )
