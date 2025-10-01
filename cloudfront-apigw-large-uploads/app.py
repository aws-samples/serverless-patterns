import aws_cdk as cdk
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_iam as iam

class CloudFrontApigwLargeUploadsStack(cdk.Stack):
    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create an API Gateway HTTP endpoint that will return a mock response 
        nonUploadApi = apigw.RestApi(
            self,
            "nonUploadApi",
            endpoint_types=[apigw.EndpointType.REGIONAL],
            deploy_options=apigw.StageOptions(
                stage_name="mock",
                throttling_rate_limit=100,
                throttling_burst_limit=1000,
            ),
            cloud_watch_role=True,
            deploy=True,
        )

        # Create a mock integration for the nonUploadApi / path that returns status 200 for GET requests
        nonUploadApi.root.add_method(
            "GET",
            apigw.MockIntegration(
                integration_responses=[
                    apigw.IntegrationResponse(
                        status_code="200",
                        response_templates={
                            "application/json": '{"message": "GET request processed by API Gateway!"}'
                        },
                    )
                ],
                passthrough_behavior=apigw.PassthroughBehavior.NEVER,
                request_templates={"application/json": '{"statusCode": 200}'},
            ),
            method_responses=[apigw.MethodResponse(status_code="200")],
        )

        # Create a mock integration for the nonUploadApi / path that returns status 200 for POST requests
        nonUploadApi.root.add_method(
            "POST",
            apigw.MockIntegration(
                integration_responses=[
                    apigw.IntegrationResponse(
                        status_code="201",
                        response_templates={
                            "application/json": '{"message": "POST request processed by API Gateway!"}'
                        },
                    )
                ],
                passthrough_behavior=apigw.PassthroughBehavior.NEVER,
                request_templates={"application/json": '{"statusCode": 200}'},
            ),
            method_responses=[apigw.MethodResponse(status_code="201")],
        )

        # Create Lamdba@edge function
        edge_function = lambda_.Function(
            self,
            "OriginRequestFunction",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            handler="lambda.handler",
            code=lambda_.Code.from_asset("lambda.zip")
        )

        # Add Lambda@Edge permission
        edge_function.add_permission(
            "EdgeFunctionPermission",
            principal=iam.ServicePrincipal("edgelambda.amazonaws.com"),
            action="lambda:InvokeFunction"
        )

        # Add execution role permissions for Lambda@Edge
        edge_function.role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                resources=["arn:aws:logs:*:*:*"]
            )
        )

        # Create a CloudFront distribution with custom origin
        distribution = cloudfront.Distribution(
            self, 
            "testLargeUploadDistribution",
            price_class=cloudfront.PriceClass.PRICE_CLASS_100, # Change this if you need more regions enabled in CloudFront
            # Default behavior now points to API Gateway
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.RestApiOrigin(
                    nonUploadApi,
                    origin_path="/mock"
                ),
                edge_lambdas=[
                    cloudfront.EdgeLambda(
                        function_version=edge_function.current_version,
                        event_type=cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST
                    )
                ],
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                origin_request_policy=cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER,
                cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
            ),
            # Additional behavior for /upload/* paths to hit a test endpoint httpbin which will provide a generic response.
            additional_behaviors={
                "/upload/*": cloudfront.BehaviorOptions(
                    origin=origins.HttpOrigin(
                        "echo.free.beeceptor.com", # This is the URL of a mock file server.
                        protocol_policy=cloudfront.OriginProtocolPolicy.HTTPS_ONLY,
                        https_port=443,
                        origin_path="/" # The origin path is set to / for the example endpoint. It will need to be modified to the correct URI for real world use-cases.
                    ),
                    viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                    cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                    allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,  # Allow all HTTP methods for uploads
                    origin_request_policy=cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER  # Forward all headers and query strings
                )
            },
            comment="Distribution to test alternative origin for large uploads"
        )

app = cdk.App()
CloudFrontApigwLargeUploadsStack(app, "CloudFrontApiGatewayLargeUploads")
app.synth()
