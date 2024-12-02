import json
from aws_cdk import (
    Duration,
    Names,
    RemovalPolicy,
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_opensearchserverless as aoss,
    custom_resources,
    CustomResource
)
from constructs import Construct

class OpenSearchServerlessStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,
            bedrock_kb_service_role_arn,
            **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        #retrieve the context parameters that would be used in creating the resources
        OPENSEARCH_SERVERLESS_PARAMS = self.node.try_get_context('opensearch_serverless_params')
        collection_name = OPENSEARCH_SERVERLESS_PARAMS['collection_name']
        index_name = f"{OPENSEARCH_SERVERLESS_PARAMS['index_name']}"

        # Index Creation Lambda Role
        create_aoss_index_lambda_role = iam.Role(self, "create-index-lambda-role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            description="Role for the CreateAOSSIndex Lambda",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ],
            inline_policies={
                "aoss-policy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["aoss:*"],
                            resources=["*"]
                        )
                    ]
                )
            }
        )
                
        #Create the neccessary network policy, encryption policy and data access policy for the OpenSearch serverless collection
        network_policy  = json.dumps([{
            "Description":f"Public access for {collection_name} collection",
            "Rules":[{
                "ResourceType":"dashboard",
                "Resource":[
                f"collection/{collection_name}"
            ]},
            {
                "ResourceType":"collection",
                "Resource":[
                    f"collection/{collection_name}"
                ]
            }],
            "AllowFromPublic":True
        }], indent=2)
        encryption_policy  = json.dumps({
            "Rules":[
                {
                    "ResourceType":"collection",
                    "Resource":[
                        f"collection/{collection_name}"
                    ]
                }
            ],
            "AWSOwnedKey":True
        }, indent=2)
        data_access_policy  = json.dumps([{
            "Rules": [{
                "Resource": [
                    f"collection/{collection_name}"
                ],
                "Permission": [
                    "aoss:CreateCollectionItems",
                    "aoss:DeleteCollectionItems",
                    "aoss:UpdateCollectionItems",
                    "aoss:DescribeCollectionItems"
                ],
                "ResourceType": "collection"
            },
            {
                "Resource": [
                    f"index/{collection_name}/*"
                ],
                "Permission": [
                    "aoss:CreateIndex",
                    "aoss:DeleteIndex",
                    "aoss:UpdateIndex",
                    "aoss:DescribeIndex",
                    "aoss:ReadDocument",
                    "aoss:WriteDocument"
                ],
                "ResourceType": "index"
            }],
            "Principal": [
                create_aoss_index_lambda_role.role_arn,
                bedrock_kb_service_role_arn
            ]
        }], indent=2)

        #Create the CFN resources for the security and access policies
        cfn_data_access_policy = aoss.CfnAccessPolicy(self,
            "BedrockKBDataAccessPolicy",
            name=f"{collection_name}-ap",
            description="Access policy for Admin and Create Index Function",
            policy= data_access_policy,
            type="data"
        )  
        cfn_network_access_policy = aoss.CfnSecurityPolicy(self,
            "BedrockKBDataSecurityPolicy",
            name=f"{collection_name}-np",
            description="Security policy for RAG Knowledge Base",
            policy= network_policy,
            type="network"
        )
        cfn_encryption_policy = aoss.CfnSecurityPolicy (self,
            "BedrockKBDataEncryptionPolicy",
            name=f"{collection_name}-ep",
            description="Encryption policy for RAG Knowledge Base",
            policy= encryption_policy,
            type="encryption"
        )

        #Create the AOSS Collection
        cfn_aoss_collection = aoss.CfnCollection(self,
            "BedrockKBDataCollection",
            name=collection_name,
            type="VECTORSEARCH",
            description="Collection for Bedrock Knowledge Base"
        )

        # Create layer
        layer = _lambda.LayerVersion(self, 'lambda_layer',
            description='Dependencies for the lambda functions',
            code= _lambda.Code.from_asset( 'layers/'), # required
            compatible_runtimes=[
                _lambda.Runtime.PYTHON_3_11
            ],
        )
        
        # Define the Lambda function resource and give the associated Execution role the permission to call the relevant Bedrock service api to start ingestion job
        create_aoss_index_function = _lambda.Function(
            self, 'CreateAOSSIndex',
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset('functions'),
            handler='index_creation.on_event',
            timeout=Duration.seconds(30),
            role=iam.Role.from_role_arn(self, "LambdaRole", create_aoss_index_lambda_role.role_arn),
            layers=[layer]
        ) 
        create_aoss_index_function.node.add_dependency(layer)
        
        #Create the Custom Resource Provider backed by Lambda Function
        crProvider = custom_resources.Provider(
            self, 'CreateAOSSIndexCustomResourceProvider',
            on_event_handler=create_aoss_index_function,
            provider_function_name="create-aoss-index-provider"
        )
        
        #Creates the custom Resource
        create_aoss_index_custom_resource = CustomResource(
            self, 'CreateAOSSIndexCustomResource',
            service_token=crProvider.service_token,
            properties={
                "AOSSIndexName": index_name,
                "AOSSHost": cfn_aoss_collection.attr_collection_endpoint
            } 
        )
        
        #Add resource dependencies
        cfn_aoss_collection.add_dependency (cfn_data_access_policy)
        cfn_aoss_collection.add_dependency (cfn_network_access_policy)
        cfn_aoss_collection.add_dependency (cfn_encryption_policy)
        create_aoss_index_custom_resource.node.add_dependency(cfn_aoss_collection)
        
        self.index_name = index_name
        self.collection_name = collection_name
        self.cfn_aoss_collection_arn = cfn_aoss_collection.attr_arn
