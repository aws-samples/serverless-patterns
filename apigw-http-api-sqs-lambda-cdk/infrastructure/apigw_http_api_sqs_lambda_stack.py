import os
from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    aws_sqs as _sqs,
    aws_apigatewayv2 as _apigwv2,
    aws_lambda as _lambda,
    aws_iam as _iam,
)

from aws_cdk.aws_lambda_event_sources import SqsEventSource

from constructs import Construct


class ApigwHttpApiSqsLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self._account_id = os.environ["CDK_DEFAULT_ACCOUNT"]
        self._region = os.environ["CDK_DEFAULT_REGION"]

        self._queue = _sqs.Queue(
            self, "ApigwV2SqsLambdaQueue",
            visibility_timeout=Duration.seconds(300),
        )

        self._sqs_event_source = SqsEventSource(self._queue)

        self._fn = _lambda.Function(self, 'SqsMessageHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='app.handler',
            code=_lambda.Code.from_asset(
                path='src'
            ),
            timeout=Duration.minutes(3),
            memory_size=128,
            environment={
                'REGION': self._region,
                'ACCOUNT_ID': self._account_id
            },
        )

        self._fn.add_event_source(self._sqs_event_source)

        self._http_api = self._create_apigw_v2()

        self._integration_role = self._create_apigw_to_sqs_role()

        self._send_msg_route = self._create_sqs_send_msg_route()

        # Enable Auto Deploy
        self._stage = self._create_stage()

        # Outputs
        CfnOutput(self, "API Endpoint", 
            description="API Endpoint", 
            value=self._http_api.attr_api_endpoint
        )
    
    def _create_apigw_to_sqs_role(self):
        _role = _iam.Role(
            self, 'ApiGwV2ToSqsRole',
            assumed_by=_iam.ServicePrincipal('apigateway.amazonaws.com')
        )

        _role.add_managed_policy(
            _iam.ManagedPolicy.from_managed_policy_arn(
                self, 'ApiGwPushCwPolicy',
                'arn:aws:iam::aws:policy/service-role/'\
                'AmazonAPIGatewayPushToCloudWatchLogs'
            )
        )
        _role.attach_inline_policy(
            _iam.Policy(
                self,
                'ApiGwV2ToSqsInlinePolicy',
                statements=[
                    _iam.PolicyStatement(
                        actions=[
                            'sqs:SendMessage',
                            'sqs:ReceiveMessage',
                            'sqs:PurgeQueue',
                            'sqs:DeleteMessage',
                        ],
                        resources=[self._queue.queue_arn]
                    )
                ]
            )
        )
        return _role

    def _create_apigw_v2(self):
        return _apigwv2.CfnApi(
            self,'HttpToSqs',
            cors_configuration=_apigwv2.CfnApi.CorsProperty(
                allow_credentials=False,
                allow_headers=["*"],
                allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
                allow_origins=["*"],
                max_age=43200,
            ),
            name='HttpToSqs',
            protocol_type='HTTP'
        )

    def _create_stage(self):
        _stage = _apigwv2.CfnStage(self, 'HttpToSqsStage',
            api_id=self._http_api.ref,
            stage_name='$default',
            auto_deploy=True
        )
        return _stage

    def _create_sqs_send_msg_route(self):
        _integ =_apigwv2.CfnIntegration(
            self, 'HttpApiIntegSqsSendMessage',
            api_id=self._http_api.ref,
            integration_type='AWS_PROXY',
            integration_subtype='SQS-SendMessage',
            payload_format_version='1.0',
            request_parameters={
                'QueueUrl': self._queue.queue_url,
                'MessageBody': '$request.body.MessageBody',
            },
            credentials_arn=self._integration_role.role_arn,
        )
        return _apigwv2.CfnRoute(
            self, 'HttpApiRouteSqsSendMsg',
            api_id=self._http_api.ref,
            route_key='POST /send',
            target='/'.join(['integrations',_integ.ref]),
        )

