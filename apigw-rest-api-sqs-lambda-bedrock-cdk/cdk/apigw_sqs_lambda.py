from aws_cdk import (Stack, aws_sqs as sqs, aws_apigateway as apigateway,
                     aws_iam as iam, aws_lambda as lambdafun,
                     aws_lambda_event_sources as eventsources, Duration as duration
                     ,aws_logs as logs)
import os
import json
from constructs import Construct
import subprocess


class ApigwSqsLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_region = self.region

        params = self.node.try_get_context("params")

        SQS_ESM_CONCURRENCY = params["SQS_ESM_CONCURRENCY"]
        LAMBDA_TIMEOUT = duration.seconds(120)

        ##############################Create SQS queue ################################ 
        dead_letter_queue = sqs.Queue(
            self,
            'genai-simple-request-dlq',
            queue_name='genai-simple-request-dlq',
            encryption=sqs.QueueEncryption.KMS_MANAGED,
            retention_period=duration.days(14),
        )

        # Create a SQS queue for storing message that APIGateway will receive.
        sqs_queue = sqs.Queue(
            self,
            'genai-simple-request-queue',
            #queue_name = os.getenv("storage_sqs_queue_name","apigwstoragequeue"),
            queue_name="genai-simple-request-queue",
            encryption=sqs.QueueEncryption.KMS_MANAGED,
            dead_letter_queue=sqs.DeadLetterQueue(
                max_receive_count=3,  # max. number of times to retry processing a message before sending to the DLQ
                queue=dead_letter_queue,
            ),
            visibility_timeout=LAMBDA_TIMEOUT

            )

        # Create an inline Policy document that grants permission to access SQS queue
        sqs_inline_policy = iam.Policy(self,
                                       "sqs-policy-for-apigw",
                                       statements=[
                                           iam.PolicyStatement(
                                               actions=["sqs:SendMessage"],
                                               resources=[sqs_queue.queue_arn])
                                       ])
        
        ##############################Create API Gateway ################################ 

        # Create an IAM  apigateway execution role.

        apigw_role = iam.Role(
            self,
            "apigw_role",
            assumed_by=iam.CompositePrincipal(
                iam.ServicePrincipal("apigateway.amazonaws.com"),
                iam.ServicePrincipal("lambda.amazonaws.com")),
            description="This is the role for apigateway to access SQS queue.")
        # Attach policy to the role.
        apigw_role.attach_inline_policy(sqs_inline_policy)

        # Create new Integration Options that can for adding request paramaters and templates.
        integration_options = apigateway.IntegrationOptions(
            credentials_role=apigw_role,
            request_parameters={
                'integration.request.header.Content-Type':
                "'application/x-www-form-urlencoded'"
            },
            passthrough_behavior=apigateway.PassthroughBehavior.NEVER,
            request_templates={
                "application/json":
                "Action=SendMessage&MessageBody=$input.body"
            },
            integration_responses=[
                apigateway.IntegrationResponse(status_code="200")
            ],
        )
        # Create new apigateway rest api.
        apigw = apigateway.RestApi(
            self,
            'genai-scalable-api',
            description='This is genAI serverless API ',
            endpoint_types=[apigateway.EndpointType.REGIONAL])

        # Create a apigateway resource method with authorizer needed
        resource = apigw.root.add_resource('invokeModel')
        resource.add_method(
            'POST',
            apigateway.AwsIntegration(region=aws_region,
                                      service='sqs',
                                      integration_http_method='POST',
                                      path=sqs_queue.queue_name,
                                      options=integration_options),
            method_responses=[apigateway.MethodResponse(status_code="200")],
            authorization_type=apigateway.AuthorizationType.NONE,
        )
        ## Add CORS
        resource.add_method(
            'OPTIONS',
            apigateway.MockIntegration(integration_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Headers':
                    "'Content-Type,\
                      X-Amz-Date,\
                      Authorization,\
                      X-Api-Key,\
                      X-Amz-Security-Token,X-Amz-User-Agent'",
                    'method.response.header.Access-Control-Allow-Origin':
                    "'*'",
                    'method.response.header.Access-Control-Allow-Credentials':
                    "'false'",
                    'method.response.header.Access-Control-Allow-Methods':
                    "'OPTIONS,\
                      GET,\
                      PUT,\
                      POST,\
                      DELETE'",
                }
            }],
            passthrough_behavior=apigateway.
            PassthroughBehavior.NEVER,
            request_templates={
                "application/json":
                "{\"statusCode\": 200}"
            }),
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_parameters={
                        'method.response.header.Access-Control-Allow-Headers':
                        True,
                        'method.response.header.Access-Control-Allow-Methods':
                        True,
                        'method.response.header.Access-Control-Allow-Credentials':
                        True,
                        'method.response.header.Access-Control-Allow-Origin':
                        True
                    })
            ],
            authorization_type=apigateway.AuthorizationType.NONE,
        )
        ##############################Create Lambda function and Role ################################ 

        SqsHandlerLambdaExecutionRole = iam.Role(
            self,
            'SqsHandlerLambdaExecutionRole',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            role_name="SqsHandlerLambdaExecutionRole",
        )

        SqsHandlerLambdaExecutionRole.attach_inline_policy(
            iam.Policy(self,
                       'SqsHandlerInlinePolicy',
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
                                   'bedrock:InvokeModel',
                                   'bedrock:InvokeModelWithResponseStream'
                               ],
                               resources=['*'],
                           ),
                           iam.PolicyStatement(
                               actions=["iot:DescribeEndpoint", "iot:Publish"],
                               resources=['*'],
                           ),
                           iam.PolicyStatement(
                               actions=[
                                   'sqs:ReceiveMessage',
                                   'sqs:DeleteMessage',
                                   'sqs:GetQueueAttributes',
                               ],
                               resources=[sqs_queue.queue_arn],
                           ),
                           iam.PolicyStatement(
                               actions=[
                                   'sqs:SendMessage',
                               ],
                               resources=[sqs_queue.queue_arn],
                           ),
                       ]))

        fnSqsHandler = lambdafun.Function(
            self,
            "SqsHandlerFunction",
            
            runtime=lambdafun.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=lambdafun.Code.from_asset("../src/invoke-model"
                                          ),
            role=SqsHandlerLambdaExecutionRole,
            function_name="invoke-bedrock-sqs",
            timeout=LAMBDA_TIMEOUT,
            layers=[
                self.create_dependencies_layer(self.stack_name, "invoke-model")
            ],
            log_retention= logs.RetentionDays.FIVE_DAYS

        )

        # Add SQS as event source to trigger Lambda
        fnSqsHandler.add_event_source(eventsources.SqsEventSource(
            sqs_queue,max_concurrency=SQS_ESM_CONCURRENCY))


##### Create Layer for boto3 that supports Bedrock #####

    def create_dependencies_layer(self, project_name, function_name: str) -> lambdafun.LayerVersion:
        requirements_file = f'../src/{function_name}/requirements.txt'
        output_dir = f'../src/build/{function_name}'

        if not os.environ.get('SKIP_PIP'):
            subprocess.check_call(
                f'pip3 install -r {requirements_file} -t {output_dir}/python'.split()
            )

        layer_id = f'{project_name}-{function_name}-dependencies'
        layer_code = lambdafun.Code.from_asset(output_dir)

        return lambdafun.LayerVersion(self, layer_id, code=layer_code)