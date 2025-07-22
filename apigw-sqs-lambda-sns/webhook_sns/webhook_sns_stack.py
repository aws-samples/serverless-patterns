from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_lambda_event_sources as lambda_event_sources,
    CfnOutput,
    Duration
)
from constructs import Construct


class WebhookSnsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create SQS Queue
        queue = sqs.Queue(
            self, "WebhookQueue",
            queue_name="webhook-queue"
        )

        # Create Lambda function
        lambda_function = _lambda.Function(
            self, "EventProcessingFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="app.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            timeout=Duration.seconds(30)
        )

        # Grant Lambda permission to publish to SNS
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["sns:Publish"],
                resources=["*"]
            )
        )

        # Add SQS event source to Lambda
        lambda_function.add_event_source(
            lambda_event_sources.SqsEventSource(queue)
        )

        # Create API Gateway
        api = apigateway.RestApi(
            self, "WebhookApi",
            rest_api_name="webhook-api",
            description="API Gateway for webhook integration with SQS"
        )

        # Create IAM role for API Gateway to send messages to SQS
        api_role = iam.Role(
            self, "ApiGatewayRole",
            assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com"),
            inline_policies={
                "SqsSendMessagePolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            effect=iam.Effect.ALLOW,
                            actions=["sqs:SendMessage"],
                            resources=[queue.queue_arn]
                        )
                    ]
                )
            }
        )

        # Create API Gateway integration with SQS
        integration = apigateway.AwsIntegration(
            service="sqs",
            path=f"{self.account}/{queue.queue_name}",
            integration_http_method="POST",
            options=apigateway.IntegrationOptions(
                credentials_role=api_role,
                request_parameters={
                    "integration.request.header.Content-Type": "'application/x-www-form-urlencoded'"
                },
                request_templates={
                    "application/json": "Action=SendMessage&MessageBody=$util.urlEncode($input.body)"
                },
                integration_responses=[
                    apigateway.IntegrationResponse(
                        status_code="200"
                    )
                ]
            )
        )

        # Add POST method to root resource
        api.root.add_method(
            "POST",
            integration,
            api_key_required=True,
            method_responses=[
                apigateway.MethodResponse(status_code="200")
            ]
        )

        # Create API Key
        api_key = apigateway.ApiKey(
            self, "WebhookApiKey",
            enabled=True,
            description="API Key for webhook endpoint"
        )

        # Create Usage Plan
        usage_plan = apigateway.UsagePlan(
            self, "WebhookUsagePlan",
            name="webhook-usage-plan",
            description="Usage plan for webhook API",
            api_stages=[
                apigateway.UsagePlanPerApiStage(
                    api=api,
                    stage=api.deployment_stage
                )
            ]
        )

        # Associate API Key with Usage Plan
        usage_plan.add_api_key(api_key)

        # Outputs
        CfnOutput(
            self, "ApiEndpoint",
            value=api.url,
            description="API Gateway endpoint URL"
        )

        CfnOutput(
            self, "QueueName",
            value=queue.queue_name,
            description="SQS Queue name"
        )

        CfnOutput(
            self, "QueueUrl",
            value=queue.queue_url,
            description="SQS Queue URL"
        )

        CfnOutput(
            self, "ApiKeyId",
            value=api_key.key_id,
            description="API Key ID for webhook endpoint"
        )
