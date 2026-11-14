from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
    aws_logs as logs,
    aws_pipes as pipes,
    aws_sqs as sqs,
    aws_iam as iam,
    RemovalPolicy,
    CfnOutput
)
from constructs import Construct
import aws_cdk as cdk

class EventbridgePipesSqsToDynamodb(Stack):

    def __init__(self, scope: Construct, construct_id: str, env: cdk.Environment = None, **kwargs) -> None:
        super().__init__(scope, construct_id, env=env, **kwargs)

        # SQS queue for decoupling and buffering events
        source_queue = sqs.Queue(
            self, "EntryPointToEventbridgePipe",
            visibility_timeout=cdk.Duration.seconds(60),
            retention_period=cdk.Duration.days(4),
            enforce_ssl=True
        )

        # DynamoDB table
        self.table = dynamodb.Table(
            self, "EventTableNew",
            table_name="Audit-Table",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
            point_in_time_recovery_specification=dynamodb.PointInTimeRecoverySpecification(
                point_in_time_recovery_enabled=True
            )
        )
                
        # IAM role for API Gateway to access DynamoDB
        api_gateway_role = iam.Role(
            self, "ApiGatewayDynamoDBRole",
            assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com"),
            inline_policies={
                "DynamoDBAccess": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=[
                                "dynamodb:PutItem",
                                "dynamodb:GetItem",
                                "dynamodb:UpdateItem",
                                "dynamodb:DeleteItem",
                                "dynamodb:Query",
                                "dynamodb:Scan"
                            ],
                            resources=[self.table.table_arn]
                        )
                    ]
                )
            }
        )
                
        # CloudWatch Log Group for API Gateway
        api_log_group = logs.LogGroup(
            self, "ApiGatewayLogGroup",
            removal_policy=RemovalPolicy.DESTROY
        )
        
        stage_name = "test"
        
        # API Gateway with Resource policy to be invoked only by Eventbridge Pipes
        self.api = apigateway.RestApi(
            self, "RegionalApi",
            rest_api_name="EventBridge-DynamoDB-API",
            endpoint_configuration=apigateway.EndpointConfiguration(
                types=[apigateway.EndpointType.REGIONAL]
            ),
            policy=iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        effect=iam.Effect.ALLOW,
                        principals=[iam.ServicePrincipal("pipes.amazonaws.com")],
                        actions=["execute-api:Invoke"],
                        resources=[f"execute-api:/{stage_name}/POST/events"]
                    )
                ]
            ),
            deploy_options=apigateway.StageOptions(
                stage_name=stage_name,
                access_log_destination=apigateway.LogGroupLogDestination(api_log_group),
                access_log_format=apigateway.AccessLogFormat.clf(),
                logging_level=apigateway.MethodLoggingLevel.INFO,
                data_trace_enabled=True
            )
        )
        
        # API Gateway integration with DynamoDB
        dynamodb_integration = apigateway.AwsIntegration(
            service="dynamodb",
            action="PutItem",
            options=apigateway.IntegrationOptions(
                credentials_role=api_gateway_role,
                request_templates={
                    "application/json": f'''#set($inputRoot = $input.path('$'))
#set($body = $util.parseJson($inputRoot.body))
#set($message = $util.parseJson($body.Message))
{{
    "TableName": "{self.table.table_name}",
    "Item": {{
        "id": {{
            "S": "$context.requestId"
        }},
        "createdAt": {{
            "S": "$context.requestTime"
        }},
        "name": {{
            "S": "$message.params.name"
        }},
        "surname": {{
            "S": "$message.params.surname"
        }},
        "content": {{
            "S": "$util.escapeJavaScript($message.content)"
        }}
    }}
}}'''
                },
                integration_responses=[
                    apigateway.IntegrationResponse(
                        status_code="200",
                        response_templates={
                            "application/json": '{"status": "success", "id": "$context.requestId"}'
                        }
                    )
                ]
            )
        )    
            
        # API Gateway resource and method with IAM authentication
        events_resource = self.api.root.add_resource("events")
        events_resource.add_method(
            "POST",
            dynamodb_integration,
            authorization_type=apigateway.AuthorizationType.IAM,
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_models={
                        "application/json": apigateway.Model.EMPTY_MODEL
                    }
                )
            ]
        )
                
        # IAM role for EventBridge Pipe
        pipe_role = iam.Role(
            self, "EventBridgePipeRole",
            assumed_by=iam.ServicePrincipal("pipes.amazonaws.com").with_conditions({
                "StringEquals": {
                    "aws:SourceAccount": cdk.Stack.of(self).account,
                    "aws:SourceArn": f"arn:aws:pipes:{cdk.Stack.of(self).region}:{cdk.Stack.of(self).account}:pipe/EventBridgePipe"
                }
            }),
            inline_policies={
                "SqsPipeSourceAccess": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=[
                                "sqs:ReceiveMessage",
                                "sqs:DeleteMessage",
                                "sqs:GetQueueAttributes"
                            ],
                            resources=[source_queue.queue_arn]
                        )
                    ]
                ),
                "ApiGatewayPipeTargetAccess": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=[
                                "execute-api:Invoke",
                                "execute-api:ManageConnections"
                            ],
                            resources=[f"arn:aws:execute-api:{cdk.Stack.of(self).region}:{cdk.Stack.of(self).account}:{self.api.rest_api_id}/{stage_name}/*"]
                        )
                    ]
                )
            }
        )
        
        # EventBridge Pipe: SQS → API Gateway
        self.pipe = pipes.CfnPipe(
            self, "SqsToApiGatewayPipe",
            role_arn=pipe_role.role_arn,
            name="EventBridgePipe",
            desired_state="RUNNING",
            source=source_queue.queue_arn,
            source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                    batch_size=1
                )
            ),
            target=f"arn:aws:execute-api:{cdk.Stack.of(self).region}:{cdk.Stack.of(self).account}:{self.api.rest_api_id}/{stage_name}/POST/events",
            target_parameters=pipes.CfnPipe.PipeTargetParametersProperty(
                http_parameters=pipes.CfnPipe.PipeTargetHttpParametersProperty(
                    header_parameters={
                        "Content-Type": "application/json"
                    }
                )
            )
        )

        # Output
        CfnOutput(self, "QueueName", value=source_queue.queue_name)

