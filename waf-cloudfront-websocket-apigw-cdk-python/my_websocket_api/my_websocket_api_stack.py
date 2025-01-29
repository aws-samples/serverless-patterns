from aws_cdk import (
    Stack,
    aws_apigatewayv2 as apigatewayv2,
    aws_apigateway as apigateway,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_lambda as _lambda,
    custom_resources,
    aws_iam,
    aws_wafv2 as wafv2,
    CfnOutput 
)
from constructs import Construct

class MyWebsocketApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stage_value = "prod"


        # Create WebSocket API
        websocket_api = apigatewayv2.CfnApi(
            self, "WebSocketAPI",
            name="my-websocket-api",
            protocol_type="WEBSOCKET",
            route_selection_expression="$request.body.action",
            api_key_selection_expression="$request.header.x-api-key",
            disable_schema_validation=False
        )


        #Create a lambda execution role
        lambda_role = aws_iam.Role(
            self, "LambdaRole",
            assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )


        # Create Lambda function for WebSocket handler
        handler = _lambda.Function(
            self, "WebSocketHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=_lambda.Code.from_asset("lambda"),
            role=lambda_role,
            environment={
                "WEBSOCKET_API_ID": websocket_api.ref,
                "WEBSOCKET_API_ENDPOINT": websocket_api.attr_api_endpoint
            }
        )


        # add permission for apigateway websocket invokes
        handler.add_permission(
            "WebSocketInvoke",
            principal=aws_iam.ServicePrincipal("apigateway.amazonaws.com"),
            action="lambda:InvokeFunction"
        )



        # Create default route
        default_route = apigatewayv2.CfnRoute(
            self, "DefaultRoute",
            api_id=websocket_api.ref,
            route_key="$default",
            target="integrations/" + self.create_lambda_integration(websocket_api, handler, "$default").ref)
        
        # Create connect route
        connect_route = apigatewayv2.CfnRoute(
            self, "ConnectRoute",
            api_id=websocket_api.ref,
            route_key="$connect",
            api_key_required=True,
            target="integrations/" + self.create_lambda_integration(websocket_api, handler, "$connect").ref)

        # Create disconnect route
        disconnect_route = apigatewayv2.CfnRoute(
            self, "DisconnectRoute",
            api_id=websocket_api.ref,
            route_key="$disconnect",
            target="integrations/" + self.create_lambda_integration(websocket_api, handler, "$disconnect").ref)

        
        #create a deployment on api stage
        deployment = apigatewayv2.CfnDeployment(
            self, "WebSocketDeployment",
            api_id=websocket_api.ref,
        )
        deployment.node.add_dependency(default_route)
        deployment.node.add_dependency(connect_route)
        deployment.node.add_dependency(disconnect_route)

        # Create WebSocket Stage
        stage = apigatewayv2.CfnStage(
            self, "ProdStage",
            api_id=websocket_api.ref,
            stage_name=stage_value,
            deployment_id=deployment.ref
        )
        # add dependency on deployment
        stage.node.add_dependency(deployment)



        # Create API Key
        api_key = apigateway.CfnApiKey(
            self, "WebSocketApiKey",
            name="my-websocket-api-key",
            enabled=True
        )

        # fetch the apikey value and store it in a variable using custom resource
        api_key_details: custom_resources.AwsSdkCall = custom_resources.AwsSdkCall(
            service="APIGateway",
            action="getApiKey",
            parameters={
                "apiKey": api_key.ref,
                "includeValue": True,
            },
            physical_resource_id=custom_resources.PhysicalResourceId.of(
                f"APIKey:{api_key.ref}"
            ),
        )

        api_key_cr = custom_resources.AwsCustomResource(
            self,
            "api-key-cr",
            policy=custom_resources.AwsCustomResourcePolicy.from_statements(
                [
                    aws_iam.PolicyStatement(
                        effect=aws_iam.Effect.ALLOW,
                        resources=[
                            f"arn:aws:apigateway:{self.region}::/apikeys/{api_key.ref}"
                        ],
                        actions=["apigateway:GET"],
                    ),
                ]
            ),
            on_create=api_key_details,
            on_update=api_key_details,
        )
        api_key_cr.node.add_dependency(api_key)
        
        self.apikey_value = api_key_cr.get_response_field("value")

        # Create Usage Plan
        usage_plan = apigateway.CfnUsagePlan(
            self, "WebSocketUsagePlan",
            api_stages=[apigateway.CfnUsagePlan.ApiStageProperty(
                api_id=websocket_api.ref,
                stage="prod")],
            throttle=apigateway.CfnUsagePlan.ThrottleSettingsProperty(
                burst_limit=100,
                rate_limit=50
            )
        )
        usage_plan.node.add_dependency(stage)
        

        # Associate API Key with Usage Plan
        apigateway.CfnUsagePlanKey(
            self, "WebSocketUsagePlanKey",
            key_id=api_key.ref,
            key_type="API_KEY",
            usage_plan_id=usage_plan.ref
        )
        usage_plan.node.add_dependency(api_key)
        


        # Create WAF Web ACL
        waf_acl = wafv2.CfnWebACL(
            self, "WebSocketWafAcl",
            default_action=wafv2.CfnWebACL.DefaultActionProperty(allow={}),
            scope="CLOUDFRONT",
            visibility_config=wafv2.CfnWebACL.VisibilityConfigProperty(
                cloud_watch_metrics_enabled=True,
                metric_name="WebSocketWafAcl",
                sampled_requests_enabled=True
            ),
            rules=[
                wafv2.CfnWebACL.RuleProperty(
                    name="LimitRequests",
                    priority=1,
                    statement=wafv2.CfnWebACL.StatementProperty(
                        rate_based_statement=wafv2.CfnWebACL.RateBasedStatementProperty(
                            limit=2000,
                            aggregate_key_type="IP"
                        )
                    ),
                    action=wafv2.CfnWebACL.RuleActionProperty(
                        block={}
                    ),
                    visibility_config=wafv2.CfnWebACL.VisibilityConfigProperty(
                        cloud_watch_metrics_enabled=True,
                        metric_name="LimitRequestsRule",
                        sampled_requests_enabled=True
                    )
                )
            ]
        )

        # Create CloudFront distribution
        distribution = cloudfront.Distribution(
            self, "Distribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.HttpOrigin(
                    f"{websocket_api.ref}.execute-api.{self.region}.amazonaws.com",
                    origin_path=f"/{stage_value}",
                    custom_headers={
                        "x-api-key": self.apikey_value
                    }
                ),

                allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                origin_request_policy=cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER
            ),
            web_acl_id=waf_acl.attr_arn
        )
        distribution.node.add_dependency(waf_acl)
        distribution.node.add_dependency(websocket_api)
        distribution.node.add_dependency(api_key_cr)

        # Output the CloudFront distribution URL with wss://
        CfnOutput(self, "DistributionURL", value=f"wss://{distribution.domain_name}")

       
    def create_lambda_integration(self, websocket_api: apigatewayv2.CfnApi, handler: _lambda.Function, route_key: str = "") -> apigatewayv2.CfnIntegration:
        return apigatewayv2.CfnIntegration(
            self, f"Integration{handler.node.id}{route_key}",
            api_id=websocket_api.ref,
            integration_type="AWS_PROXY",
            integration_uri=f"arn:aws:apigateway:{Stack.of(self).region}:lambda:path/2015-03-31/functions/{handler.function_arn}/invocations"
        )

