from aws_cdk import (
    core as cdk,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigateway,
    aws_iam as iam,
    aws_lambda as lambdafun
)
import json

class CdkApigwMarketplaceMeteringRecordsStack(cdk.Stack):

     def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get config values from cdk.out.context
        params = self.node.try_get_context("params")

        aws_region_name =params["aws_region_name"]
        metering_table_name = params["metering_table_name"]


        apigw_request_template_customeridentifier = '''{
            "TableName": "''' + metering_table_name +'''",
            "Item": {
                "create_timestamp": {
                    "N": "$context.requestTimeEpoch"
                    },
                "customerIdentifier": {
                    "S": "$method.request.path.customerIdentifier"
                    },
                "metering_pending": {
                    "S": "true"
                    },
                "dimension_usage": { "L": [
                #foreach($dimension in $input.path('$.metered_dimensions'))
                {"M":{
                        "dimension": { "S": "$dimension.dimension_name" },
                        "value": { "N": "$dimension.dimension_value" }
                    }
                }#if($foreach.hasNext),#end
                #end
                ]
                }
            }
        }'''

        apigw_request_template_batchinserts = '''{
            "RequestItems": {"''' + metering_table_name + '''": [
                    #foreach($buyer in $input.path('$.buyers')){
                        "PutRequest" : {
                            "Item" : {
                                "create_timestamp": {
                                    "N": "$context.requestTimeEpoch"
                                    },
                                "customerIdentifier": {
                                    "S": "$buyer.customerIdentifier"
                                    },
                                "metering_pending": {
                                    "S": "true"
                                    },
                                "dimension_usage": { "L": [
                                    #foreach($dimension in $buyer.metered_dimensions)
                                    {"M":{
                                            "dimension": { "S": "$dimension.dimension_name" },
                                            "value": { "N": "$dimension.dimension_value" }
                                        }
                                    }#if($foreach.hasNext),#end
                                    #end
                                ]
                                }
                            }
                        }
                    }#if($foreach.hasNext),#end
                    #end
                ]
            } 
        }'''

        apigw_request_template_query = '''{
            "TableName": "''' + metering_table_name +'''",
            "KeyConditionExpression": "customerIdentifier = :v1",
            "ExpressionAttributeValues": {
                ":v1": {
                    "S": "$input.params('customerIdentifier')"
                }
            }
        }'''

 # Create an inline Policy document that grants permission to access SQS queue
        apigw_policy_dyanmodb = iam.Policy(self, "apigw-policy-for-dyanmodb",
            statements=[iam.PolicyStatement(
                actions=["dynamodb:PutItem", "dynamodb:List*","dynamodb:BatchWriteItem","dynamodb:Query"],
                resources=["arn:aws:dynamodb:*:*:table/"+metering_table_name]
            )]
        )
# Create an IAM  apigateway execution role.
        apigw_role = iam.Role(self, "apigw_role_for_dynamodb",
                    assumed_by=iam.CompositePrincipal(
                            iam.ServicePrincipal("apigateway.amazonaws.com"), 
                            iam.ServicePrincipal("lambda.amazonaws.com")
                    ),       
                    description="This is the role for apigateway to access Dynamodb tables."
        )
# Attach policy to the role.       
        apigw_role.attach_inline_policy(apigw_policy_dyanmodb)

# Create new Integration Options that can for adding request paramaters and templates.
        customeridentifier_integration_options = apigateway.IntegrationOptions(
                    credentials_role = apigw_role,
                    request_parameters={
                        'integration.request.header.Content-Type' : "'application/x-www-form-urlencoded'"
                    },
                    passthrough_behavior=apigateway.PassthroughBehavior.NEVER,
                    request_templates={"application/json": apigw_request_template_customeridentifier},
                    integration_responses=[apigateway.IntegrationResponse(status_code="200")],
        )
# Create new Integration Options for batch inserts.
        batch_insert_integration_options = apigateway.IntegrationOptions(
                    credentials_role = apigw_role,
                    request_parameters={
                        'integration.request.header.Content-Type' : "'application/x-www-form-urlencoded'"
                    },
                    passthrough_behavior=apigateway.PassthroughBehavior.NEVER,
                    request_templates={"application/json": apigw_request_template_batchinserts},
                    integration_responses=[apigateway.IntegrationResponse(status_code="200")],
        )

        query_integration_options = apigateway.IntegrationOptions(
                    credentials_role = apigw_role,
                    request_parameters={
                        'integration.request.header.Content-Type' : "'application/x-www-form-urlencoded'"
                    },
                    passthrough_behavior=apigateway.PassthroughBehavior.NEVER,
                    request_templates={"application/json": apigw_request_template_query},
                    integration_responses=[apigateway.IntegrationResponse(status_code="200")],
        )

        

# Create new apigateway rest api.      
        apigw = apigateway.RestApi(self, 'marketplace-metering-records',
                description ='This api will insert metering records into dynamodb table : AWSMarketplaceMeteringRecords',
                endpoint_types =[apigateway.EndpointType.REGIONAL]
        )
        
# Create a apigateway resource method with authorizer needed   

        apigw.root.add_resource('insertMeteringRecord').add_resource('{customerIdentifier}').add_method('POST',
            apigateway.AwsIntegration(
                region = aws_region_name,
                service = 'dynamodb',
                integration_http_method = 'POST',
                action = 'PutItem', 
                options = customeridentifier_integration_options
            ),
            method_responses=[apigateway.MethodResponse(status_code="200")],

        )
# create a resource for batch entry of metered records
        apigw.root.add_resource('insertMeteringRecords').add_method('POST',
            apigateway.AwsIntegration(
                region = aws_region_name,
                service = 'dynamodb',
                integration_http_method = 'POST',
                action = 'BatchWriteItem', 
                options = batch_insert_integration_options
            ),
            method_responses=[apigateway.MethodResponse(status_code="200")],

        ) 
# create a resource for querying metered records
        apigw.root.add_resource('listMeteringRecords').add_resource('{customerIdentifier}').add_method('GET',
            apigateway.AwsIntegration(
                region = aws_region_name,
                service = 'dynamodb',
                integration_http_method = 'POST',
                action = 'Query', 
                options = query_integration_options
            ),
            method_responses=[apigateway.MethodResponse(status_code="200")],

        ) 