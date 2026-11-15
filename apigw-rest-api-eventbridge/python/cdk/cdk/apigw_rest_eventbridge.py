from aws_cdk import (
    Stack,
    aws_apigateway as api_gateway,
    aws_events as events
)

from aws_cdk.aws_iam import(
    PolicyStatement,
    Role,
    ServicePrincipal,
    Effect
)

from constructs import Construct

class ApigwRestEventBridgeStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        ##############################Create EventBridge Bus ################################ 

        ### The event bus ###
        event_bus = events.EventBus(
            scope=self,
            id= "EventBus",
            event_bus_name="apigw-event-bus"

        )
        

        ##############################Create IAM Policies & Roles ################################ 

        ### IAM Role which is assumed by the API Gateway ###
        api_gw_service_role = Role(
            scope=self,
            id= "ApiGWRole",
            assumed_by = ServicePrincipal("apigateway.amazonaws.com")
        )

        ### IAM Policy which allows the API Gateway to publish to the event bus  ###
        api_gw_service_role.add_to_policy(
            PolicyStatement(
                effect=Effect.ALLOW,
                actions=["events:PutEvents"],
                resources=[event_bus.event_bus_arn]
            )
        )

        ##############################Create REST API Gateway ################################ 

        ### The REST API Gateway ###
        rest_api = api_gateway.RestApi(
            scope = self,
            id = "RestAPIGw",
        )

        ### The REST API Integration which points to the event bus ###
        event_bridge_rest_api_integration = api_gateway.AwsIntegration(
            action="PutEvents",
            service="events",
            options=api_gateway.IntegrationOptions(
                integration_responses=[
                    api_gateway.IntegrationResponse(
                        status_code="200",
                        response_templates={
                            "application/json": (
                                """
                                #set($inputRoot = $input.path('$'))
                                    {
                                        $util.escapeJavaScript($input.body)
                                    }
                                """
                            )
                        }
                    )
                ],
                credentials_role=api_gw_service_role,
                passthrough_behavior=api_gateway.PassthroughBehavior.WHEN_NO_TEMPLATES,
                request_templates={
                    "application/json": 
                        """
                        #set($context.requestOverride.header.X-Amz-Target = "AWSEvents.PutEvents")
                        #set($context.requestOverride.header.Content-Type = "application/x-amz-json-1.1")
                        #set($inputRoot = $input.path('$'))
                        {
                            "Entries": [
                                {
                                    "Detail": "$util.escapeJavaScript($input.body)",
                                    "DetailType": "POST-Request",
                                    "EventBusName": "apigw-event-bus",
                                    "Source": "WebClient"
                                }
                            ]
                        }
                        """
                }
            )
        )
        
        ### A POST method added to the REST API which points to the integration  ###
        rest_api.root.add_method("POST", event_bridge_rest_api_integration,
                             request_parameters={
                                "method.request.header.X-Amz-Target": False,
                                "method.request.header.Content-Type": False
                             },
                             method_responses=[
                                api_gateway.MethodResponse(
                                    # Successful response from the integration
                                    status_code="200"
                                    # Validate the schema on the response
                                )
                            ]
        )
