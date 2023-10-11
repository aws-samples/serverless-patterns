from aws_cdk import (Stack, aws_sqs as sqs, aws_apigateway as apigateway,
                     aws_iam as iam, aws_lambda as lambdafun,
                     aws_lambda_event_sources as eventsources, Duration as duration
                     ,aws_logs as logs)
import os
import json
from constructs import Construct
import subprocess


class ApigwLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ##############################Create Lambda function and Role ################################ 

        LambdaRole = iam.Role(
            self,
            'LambdaBedrockExecutionRole',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            role_name="LambdaBedrockExecutionRole",
        )

        LambdaRole.attach_inline_policy(
            iam.Policy(self,
                       'BedrockHandlerInlinePolicy',
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
                           )
                       ]))

        fnHandler = lambdafun.Function(
            self,
            "BedrockHandlerFunction",
            
            runtime=lambdafun.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=lambdafun.Code.from_asset("../src/invoke-model"
                                          ),
            role=LambdaRole,
            function_name="invoke-bedrock",
            timeout=duration.seconds(30),
            layers=[
                self.create_dependencies_layer(self.stack_name, "invoke-model")
            ],
            log_retention= logs.RetentionDays.FIVE_DAYS

        )
        ##############################Create API Gateway ################################ 

        # Create new apigateway rest api.
        apigw = apigateway.RestApi(
            self,
            'genai-simple-api',
            description='This is genAI serverless API with Lambda ',
            endpoint_types=[apigateway.EndpointType.REGIONAL])

        # Create a apigateway resource method with authorizer needed
        resource = apigw.root.add_resource('invokeModel')
        resource.add_method(
            'POST',
            apigateway.LambdaIntegration(fnHandler,
                request_templates={"application/json": '{ "statusCode": "200" }'}),            
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