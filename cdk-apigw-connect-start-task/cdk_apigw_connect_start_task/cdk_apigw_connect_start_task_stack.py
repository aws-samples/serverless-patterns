from aws_cdk import (
    core as cdk,
    aws_apigateway as apigw,
    aws_iam as iam

)

class CdkApigwConnectStartTaskStack(cdk.Stack):

        # The code that defines your stack goes here
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
            super().__init__(scope, construct_id, **kwargs)

            # Create Mapping template for APIGW integration request
            template_mapping = '''$input.json("$")'''
        
            # Create an inline Policy document that grants permission to access Amazon Connect
            apigw_connect_policy1 = iam.Policy(self, "apigw-policy-for-connect",
                statements=[iam.PolicyStatement(
                    actions=["connect:StartTaskContact"],
                    resources=["arn:aws:connect:"+self.region+":"+self.account+":instance/*/*/*"]
                )]
            )
        
            # Create an Execution role for API Gateway
            apigw_role = iam.Role(self, "apigw_role_for_connect",
                        assumed_by=iam.CompositePrincipal(
                                iam.ServicePrincipal("apigateway.amazonaws.com"), 
                                iam.ServicePrincipal("connect.amazonaws.com")
                        ),       
                        description="This is the role for apigateway to access Amazon Connect from APIGW."
            )
        

            # Attach inline policy to the Execution role
            apigw_role.attach_inline_policy(apigw_connect_policy1)

            # Create API Gateway integration Options
            integration_options = apigw.IntegrationOptions( 
                        credentials_role = apigw_role,
                        request_parameters={
                            'integration.request.header.Content-Type' : "'application/x-amz-json-1.1'",
                            'integration.request.header.X-Amz-Target' : "'StartTaskContact'"
                        },
                        passthrough_behavior=apigw.PassthroughBehavior.WHEN_NO_MATCH,
                        request_templates={"application/json": template_mapping},
                        integration_responses=[apigw.IntegrationResponse(status_code="200")],
            )
            
            #Create rest api
            api_gateway = apigw.RestApi(self, "APIGatewayForConnect",
                                            rest_api_name="apigateway-for-connect",
                                            description="API gateway for integration with Amazon Connect - Start Contact task.",
                                                endpoint_types =[apigw.EndpointType.REGIONAL]
                                            )
            
        # Create a resource for the API Gateway
            api_gateway_resource = api_gateway.root.add_resource("start-task-contact").add_method("POST",
                                    apigw.AwsIntegration(
                                        region=self.region,
                                        service="connect",
                                        path="contact/task",
                                        integration_http_method="PUT",
                                        options=integration_options
                                    ),
                                    method_responses=[apigw.MethodResponse(status_code="200")]
                                    )
