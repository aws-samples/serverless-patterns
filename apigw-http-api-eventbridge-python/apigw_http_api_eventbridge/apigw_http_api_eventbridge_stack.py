from aws_cdk import (
    Stack,
    aws_events as events,
    aws_logs as logs,
    aws_events_targets as cloudw,
    aws_apigatewayv2_alpha as apigw,
    CfnOutput
)
from aws_cdk.aws_apigateway import (
    IntegrationType
)
from aws_cdk.aws_apigatewayv2 import (
    CfnIntegration,
    CfnRoute,
)
from aws_cdk.aws_iam import (
    Role,
    ServicePrincipal,
    PolicyStatement,
    Effect
)
from constructs import Construct


class ApigwHttpApiEventbridgeStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creating an event bus. Change `event_bus_name` with your own name
        event_bus = events.EventBus(
            scope=self,
            id='MyEventBus',
            event_bus_name='MyEventBus'
        )

        # Match the events to log to certain region
        event_logger_rule = events.Rule(
            scope=self,
            id="EventLoggerRule",
            description="Log all events",
            event_pattern=events.EventPattern(
                region=['app-southeast-2']
            ),
            event_bus=event_bus
        )

        # Creating log group
        log_group = logs.LogGroup(
            scope=self,
            id='EventLogGroup',
            log_group_name=f'/aws/events/{event_bus.event_bus_name}'
        )

        event_logger_rule.add_target(
            cloudw.CloudWatchLogGroup(log_group=log_group)
        )

        # Creating the HTTP Api. Change `api_name` with your own name
        http_api = apigw.HttpApi(
            scope=self,
            id='MyRestApi',
            api_name='MyRestApi'
        )

        api_role = Role(
            scope=self,
            id='EventBridgeIntegrationRole',
            assumed_by=ServicePrincipal('apigateway.amazonaws.com')
        )

        api_role.add_to_policy(
            PolicyStatement(
                effect=Effect.ALLOW,
                resources=[event_bus.event_bus_arn],
                actions=['events:PutEvents']
            )
        )

        event_bridge_integration = CfnIntegration(
            scope=self,
            id='EventBridgeIntegration',
            integration_type=str(IntegrationType.AWS_PROXY),
            integration_subtype='EventBridge-PutEvents',
            credentials_arn=api_role.role_arn,
            api_id=http_api.http_api_id,
            request_parameters={
                'Source': 'WebApp',
                'DetailType': 'MyDetailType',
                'Detail': '$request.body',
                'EventBusName': event_bus.event_bus_arn
            },
            payload_format_version='1.0',
            timeout_in_millis=10000
        )

        CfnRoute(
            scope=self,
            id='EventRoute',
            api_id=http_api.http_api_id,
            route_key='POST /',
            target=f'integrations/{event_bridge_integration.ref}'
        )

        CfnOutput(
            scope=self,
            id='apiUrl',
            value=http_api.url,
            description='HTTP API endpoint URL'
        )