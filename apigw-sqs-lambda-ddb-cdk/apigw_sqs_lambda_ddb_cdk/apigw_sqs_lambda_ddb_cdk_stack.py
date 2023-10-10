from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigatewayv2 as apigwv2,
    aws_iam as iam,
    aws_lambda_event_sources as eventsources,
    aws_secretsmanager as secretsmanager,
    aws_logs as logs,
    SecretValue as SecretValue,
    CfnOutput as CfnOutput,
)
from constructs import Construct
import json
import os

class ApigwSqsLambdaDdbCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        ##########################################################################
        #   Getting Accound ID and Region as variables                           #
        ##########################################################################
        
        self._accountId = os.environ["CDK_DEFAULT_ACCOUNT"]
        self._region = os.environ["CDK_DEFAULT_REGION"]

        ##########################################################################
        #   SQS Queues                                                           #
        ##########################################################################

        # SQS DLQ
        queueDlq = sqs.Queue(
            self, "DeadLetterQueue",
            queue_name="DeadLetterQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # SQS queue for request buffering
        queueBufferingQueue = sqs.Queue(
            self, "BufferingQueue",
            queue_name="BufferingQueue",
            visibility_timeout=Duration.seconds(300),
            dead_letter_queue=sqs.DeadLetterQueue(
                max_receive_count=1,
                queue=queueDlq,
                ),
        )
        ##########################################################################
        #   Log Group                                                           #
        ##########################################################################  
        
        # Configure log group for short retention
        logGroup = logs.CfnLogGroup(self, "LogGroup",
            log_group_name="logGroup",
            retention_in_days=14,
        )

        ##########################################################################
        #   Dynamo DB                                                            #
        ##########################################################################  
        
        # Dynamo DB
        table = dynamodb.Table(self, "EventTable",
        partition_key=dynamodb.Attribute(name="eventId", type=dynamodb.AttributeType.STRING),
        billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        table_name="EventTable",
        )

        ##########################################################################
        #   Secrets - Generated for Endpoint Auth                                #
        ##########################################################################  

        # Secret for username
        secretUsername = secretsmanager.Secret(self, "authUsername",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template=json.dumps({}),
                generate_string_key="username",
                exclude_characters='@"',
                ),
        )

        # Secret for password
        secretPassword = secretsmanager.Secret(self, "authPassword",
        generate_secret_string=secretsmanager.SecretStringGenerator(
            secret_string_template=json.dumps({}),
            generate_string_key="password",
            exclude_characters='@|;"',
            ),
        )

        ##########################################################################
        #   Roles                                                                #
        ##########################################################################   

        # API GW to SQS Role
        ApiGwToSqsRole = iam.Role(
            self, 'ApiGwV2ToSqsRole',
            assumed_by=iam.ServicePrincipal('apigateway.amazonaws.com'),
            role_name="ApiGwV2ToSqsRole",
        )

        ApiGwToSqsRole.add_managed_policy(
            iam.ManagedPolicy.from_managed_policy_arn(
                self, 'ApiGwPushCwPolicy',
                'arn:aws:iam::aws:policy/service-role/'\
                'AmazonAPIGatewayPushToCloudWatchLogs'
            ),
        )
        ApiGwToSqsRole.attach_inline_policy(
            iam.Policy(
                self,
                'ApiGwV2ToSqsInlinePolicy',
                statements=[
                    iam.PolicyStatement(
                        actions=[
                            'sqs:SendMessage',
                            'sqs:ReceiveMessage',
                            'sqs:PurgeQueue',
                            'sqs:DeleteMessage',
                        ],
                        resources=[queueBufferingQueue.queue_arn]
                    ),
                ]
            ),
        )

        # Lambda SQS Handler to Dynamo DB Role
        SqsHandlerLambdaExecutionRole = iam.Role(
            self, 'SqsHandlerLambdaExecutionRole',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            role_name="SqsHandlerLambdaExecutionRole",
        )

        SqsHandlerLambdaExecutionRole.attach_inline_policy(
            iam.Policy(
                self,
                'SqsHandlerInlinePolicy',
                statements=[
                    iam.PolicyStatement(
                        actions=[
                            'dynamodb:List*',
                            'dynamodb:DescribeReservedCapacity*',
                            'dynamodb:DescribeLimits',
                            'dynamodb:DescribeTimeToLive',
                            'dynamodb:Get*',
                            'dynamodb:PutItem',               
                        ],
                        resources=[table.table_arn],
                    ),
                    iam.PolicyStatement(
                        actions=[
                            'logs:CreateLogGroup',
                            'logs:CreateLogStream',
                            'logs:PutLogEvents',             
                        ],
                        resources=['*'],
                    ),
                    iam.PolicyStatement(
                        actions=[
                            'sqs:ReceiveMessage',
                            'sqs:DeleteMessage',
                            'sqs:GetQueueAttributes',             
                        ],
                        resources=[queueBufferingQueue.queue_arn],
                    ),
                    iam.PolicyStatement(
                        actions=[
                            'sqs:SendMessage',        
                        ],
                        resources=[queueDlq.queue_arn],
                    ),
                ]
            )
        )

        # Authorization Lambda Role
        AuthorizationLambdaRole = iam.Role(
            self, 'AuthorizationLambdaRole',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            role_name="AuthorizationLambdaRole",
        )

        AuthorizationLambdaRole.attach_inline_policy(
            iam.Policy(
                self,
                'AuthorizationInlinePolicy',
                statements=[
                    iam.PolicyStatement(
                        actions=[
                            'logs:CreateLogGroup',
                            'logs:CreateLogStream',
                            'logs:PutLogEvents',             
                        ],
                        resources=['*'],
                    ),
                    iam.PolicyStatement(
                        actions=[
                            'secretsmanager:GetSecretValue',           
                        ],
                        resources=[
                            secretUsername.secret_arn,
                            secretPassword.secret_arn,
                            ],
                    ),
                ]
            )
        )

        ##########################################################################
        #   Lambda Functions                                                     #
        ##########################################################################

        # Lambda - SqsHandlerFunction
        pwrToolsLayer = lambda_.LayerVersion.from_layer_version_arn(self, 'powertools-layer', 'arn:aws:lambda:' + self._region + ':017000801446:layer:AWSLambdaPowertoolsPythonV2:32')

        fnSqsHandler = lambda_.Function(self, "SqsHandlerFunction",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="index.lambda_handler",
            code=lambda_.Code.from_asset("lambda/sqs-handler/"),
            role=SqsHandlerLambdaExecutionRole,
            layers  = [pwrToolsLayer],
            environment={ 
                "dynamo_db_name": table.table_name,
             },
            function_name="SqsHandlerFunction",
            )
        
        # Add SQS as event source to trigger Lambda
        fnSqsHandler.add_event_source(eventsources.SqsEventSource(queueBufferingQueue))
        
        # Lambda - AuthorizerFunction
        fnAuthorizer = lambda_.Function(self, "AuthorizerFunction",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="index.lambda_handler",
            code=lambda_.Code.from_asset("lambda/authorizer/"),
            role=AuthorizationLambdaRole,
            layers  = [pwrToolsLayer],
            environment={ 
                "usernameSecretArn": secretUsername.secret_arn,
                "passwordSecretArn": secretPassword.secret_arn,
             },
            function_name="AuthorizerFunction",
            )
        principal = iam.ServicePrincipal("apigateway.amazonaws.com")

        ##########################################################################
        #   API GW                                                               #
        ##########################################################################  
               
        # API GW v2 HTTP API
        Apigwv2 =  apigwv2.CfnApi(
            self,'HttpToSqs',
            cors_configuration=apigwv2.CfnApi.CorsProperty(
                allow_credentials=False,
                allow_headers=["*"],
                allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
                allow_origins=["*"],
                max_age=43200,
            ),
            name='HttpToSqs',
            protocol_type='HTTP',
        )
       
        # API GW v2 Stage
        stage = apigwv2.CfnStage(self, 'HttpToSqsStage',
            api_id=Apigwv2.ref,
            stage_name='$default',
            auto_deploy=True,
            access_log_settings=apigwv2.CfnStage.AccessLogSettingsProperty(
                destination_arn=logGroup.attr_arn,
                format='{ "requestId":"$context.requestId", "ip": "$context.identity.sourceIp", "requestTime":"$context.requestTime", "httpMethod":"$context.httpMethod","routeKey":"$context.routeKey", "status":"$context.status","protocol":"$context.protocol", "responseLength":"$context.responseLength" }'
            ),
        )
    
        # API GW v2 Integration
        httpApiIntegSqsSendMessage =apigwv2.CfnIntegration(
            self, 'httpApiIntegSqsSendMessage',
            api_id=Apigwv2.ref,
            integration_type='AWS_PROXY',
            integration_subtype='SQS-SendMessage',
            payload_format_version='1.0',
            request_parameters={
                'QueueUrl': queueBufferingQueue.queue_url,
                'MessageBody': '$request.body',
            },
            credentials_arn=ApiGwToSqsRole.role_arn,
        )
        
        # API GW v2 Authorizer
        authorizer = apigwv2.CfnAuthorizer(self, "ApiGwAuthorizer",
            api_id=Apigwv2.ref,
            authorizer_type="REQUEST",
            name="AuthorizerFunction", 
            authorizer_uri = "arn:aws:apigateway:" + self._region + ":lambda:path/2015-03-31/functions/" + fnAuthorizer.function_arn + "/invocations",
            authorizer_payload_format_version = "2.0",
            authorizer_result_ttl_in_seconds = 0,
            enable_simple_responses = True,
            )

        # API GW v2 Route
        HttpApiRoute =apigwv2.CfnRoute(
            self, 'HttpApiRouteSqsSendMsg',
            api_id=Apigwv2.ref,
            route_key='POST /submit',
            target='/'.join(['integrations',httpApiIntegSqsSendMessage.ref]),
            authorization_type="CUSTOM",
            authorizer_id=authorizer.attr_authorizer_id,
        )

        # Create Resource policy for SQS Handler Lambda, which only allows access from the created API GW
        fnAuthorizer.add_permission("apigateway.amazonaws.com",
            principal=principal,
            source_arn =  "arn:aws:execute-api:" + self._region + ":" + self._accountId + ":" + Apigwv2.attr_api_id + "/authorizers/*",
        )      

        ##########################################################################
        #   Output                                                               #
        ##########################################################################  

        CfnOutput(self, "HttpApiEndpoint",
        description="API Endpoint", 
            value=Apigwv2.attr_api_endpoint,
        )