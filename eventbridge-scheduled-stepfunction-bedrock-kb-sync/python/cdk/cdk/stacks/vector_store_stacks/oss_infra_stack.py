import json

from aws_cdk import (
    Stack,
)
from aws_cdk import aws_opensearchserverless as aoss
from aws_cdk import aws_ssm as ssm
from aws_cdk import (
    custom_resources,
)
from constructs import Construct


class SecurityPolicyType(str):
    ENCRYPTION = "encryption"
    NETWORK = "network"


class OpenSearchServerlessStack(Stack):
    def __init__(
        self,
        scope: Construct,
        stack_id: str,
        params: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope=scope, id=stack_id, **kwargs)

        self.account_id = Stack.of(self).account
        self.aws_partition = Stack.of(self).partition

        self.collection_name = params["oss_vector_collection_name"]
        self.index_name = params["oss_vector_index_name"]
        self.embedding_model_id = params["embedding_model_id"]

        # Create policies and collection
        self.encryption_policy = self.create_encryption_policy()
        self.network_policy = self.create_network_policy()
        self.collection = self.create_collection()

        # Wait for encryption and network policies to be created
        self.network_policy.node.add_dependency(self.encryption_policy)
        self.collection.node.add_dependency(self.network_policy)

        # Create data access policy after collection is created
        self.data_access_policy = self.create_data_access_policy()
        self.data_access_policy.node.add_dependency(self.collection)

        self.base_model_mapping = params[self.embedding_model_id]

        # Store collection ARN in SSM
        self.collection_arn_param = ssm.StringParameter(
            self,
            "CollectionArn",
            parameter_name="/collection-arn",
            string_value=self.collection.attr_arn,
        )

        # Create index after all other resources
        self.create_oss_index()

    def create_encryption_policy(self) -> aoss.CfnSecurityPolicy:
        return aoss.CfnSecurityPolicy(
            self,
            "EncryptionPolicy",
            name=f"{self.collection_name}-enc",
            type=SecurityPolicyType.ENCRYPTION,
            policy=json.dumps(
                {
                    "Rules": [{"ResourceType": "collection", "Resource": [f"collection/{self.collection_name}"]}],
                    "AWSOwnedKey": True,
                }
            ),
        )

    def create_network_policy(self) -> aoss.CfnSecurityPolicy:
        return aoss.CfnSecurityPolicy(
            self,
            "NetworkPolicy",
            name=f"{self.collection_name}-net",
            type=SecurityPolicyType.NETWORK,
            policy=json.dumps(
                [
                    {
                        "Description": f"Private access for {self.collection_name} collection",
                        "Rules": [
                            {"ResourceType": "collection", "Resource": [f"collection/{self.collection_name}"]},
                            {"ResourceType": "dashboard", "Resource": [f"collection/{self.collection_name}"]},
                        ],
                        "AllowFromPublic": True,
                    }
                ]
            ),
        )

    def create_collection(self) -> aoss.CfnCollection:
        return aoss.CfnCollection(
            self,
            "Collection",
            name=self.collection_name,
            description=f"{self.collection_name}-RAG-collection",
            type="VECTORSEARCH",
        )

    def create_data_access_policy(self) -> aoss.CfnAccessPolicy:
        kb_role_arn = ssm.StringParameter.from_string_parameter_attributes(
            self, "RoleArn", parameter_name="/role-arn"
        ).string_value

        return aoss.CfnAccessPolicy(
            self,
            "DataAccessPolicy",
            name="kb-data-access",
            type="data",
            policy=json.dumps(
                [
                    {
                        "Rules": [
                            {
                                "Resource": [f"collection/{self.collection_name}"],
                                "Permission": [
                                    "aoss:CreateCollectionItems",
                                    "aoss:DeleteCollectionItems",
                                    "aoss:UpdateCollectionItems",
                                    "aoss:DescribeCollectionItems",
                                ],
                                "ResourceType": "collection",
                            },
                            {
                                "Resource": [f"index/{self.collection_name}/*"],
                                "Permission": [
                                    "aoss:ReadDocument",
                                    "aoss:WriteDocument",
                                    "aoss:CreateIndex",
                                    "aoss:DeleteIndex",
                                    "aoss:UpdateIndex",
                                    "aoss:DescribeIndex",
                                ],
                                "ResourceType": "index",
                            },
                        ],
                        "Principal": [kb_role_arn, f"arn:{self.aws_partition}:iam::{self.account_id}:root"],
                    }
                ]
            ),
        )

    def create_oss_index(self):
        # Add a wait condition to ensure collection is active
        wait_condition = custom_resources.AwsCustomResource(
            self,
            "WaitForCollection",
            on_create=custom_resources.AwsSdkCall(
                service="OpenSearchServerless",
                action="listCollections",
                parameters={},
                physical_resource_id=custom_resources.PhysicalResourceId.of("WaitForCollection"),
            ),
            policy=custom_resources.AwsCustomResourcePolicy.from_sdk_calls(
                resources=custom_resources.AwsCustomResourcePolicy.ANY_RESOURCE
            ),
        )
        wait_condition.node.add_dependency(self.collection)
        wait_condition.node.add_dependency(self.data_access_policy)

        cdk_mapping = {
            "mappings": aoss.CfnIndex.MappingsProperty(
                properties={
                    "bedrock-knowledge-base-default-vector": aoss.CfnIndex.PropertyMappingProperty(
                        type=self.base_model_mapping["mappings"]["properties"]["bedrock-knowledge-base-default-vector"][
                            "type"
                        ],
                        dimension=self.base_model_mapping["mappings"]["properties"][
                            "bedrock-knowledge-base-default-vector"
                        ]["dimension"],
                        method=aoss.CfnIndex.MethodProperty(
                            engine=self.base_model_mapping["mappings"]["properties"][
                                "bedrock-knowledge-base-default-vector"
                            ]["method"]["engine"],
                            name=self.base_model_mapping["mappings"]["properties"]["bedrock-knowledge-base-default-vector"][
                                "method"
                            ]["name"],
                            parameters=aoss.CfnIndex.ParametersProperty(
                                ef_construction=self.base_model_mapping["mappings"]["properties"][
                                    "bedrock-knowledge-base-default-vector"
                                ]["method"]["parameters"]["ef_construction"],
                                m=self.base_model_mapping["mappings"]["properties"][
                                    "bedrock-knowledge-base-default-vector"
                                ]["method"]["parameters"]["m"],
                            ),
                            space_type=self.base_model_mapping["mappings"]["properties"][
                                "bedrock-knowledge-base-default-vector"
                            ]["method"]["space_type"],
                        ),
                    ),
                    "AMAZON_BEDROCK_METADATA": aoss.CfnIndex.PropertyMappingProperty(
                        type=self.base_model_mapping["mappings"]["properties"]["AMAZON_BEDROCK_METADATA"]["type"],
                        index=self.base_model_mapping["mappings"]["properties"]["AMAZON_BEDROCK_METADATA"]["index"],
                    ),
                    "AMAZON_BEDROCK_TEXT_CHUNK": aoss.CfnIndex.PropertyMappingProperty(
                        type=self.base_model_mapping["mappings"]["properties"]["AMAZON_BEDROCK_TEXT_CHUNK"]["type"],
                        index=self.base_model_mapping["mappings"]["properties"]["AMAZON_BEDROCK_TEXT_CHUNK"]["index"],
                    ),
                }
            ),
            "settings": aoss.CfnIndex.IndexSettingsProperty(
                index=aoss.CfnIndex.IndexProperty(
                    knn=self.base_model_mapping["settings"]["index"]["knn"],
                    knn_algo_param_ef_search=self.base_model_mapping["settings"]["index"]["knn.algo_param.ef_search"],
                )
            ),
        }

        oss_index = aoss.CfnIndex(
            self,
            "OSSCfnIndex",
            collection_endpoint=self.collection.attr_collection_endpoint,
            index_name=self.index_name,
            mappings=cdk_mapping["mappings"],
            settings=cdk_mapping["settings"],
        )
        oss_index.node.add_dependency(self.data_access_policy)
        oss_index.node.add_dependency(self.collection)
