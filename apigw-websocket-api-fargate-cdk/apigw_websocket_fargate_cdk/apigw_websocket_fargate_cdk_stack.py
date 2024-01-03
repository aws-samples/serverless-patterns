from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_apigatewayv2 as apigw,
    aws_ec2 as ec2,
    CfnOutput,
    aws_ecs as ecs,
    aws_logs as logs,
    aws_ecs_patterns as ecs_patterns,
    aws_iam as iam,
)
import aws_cdk as core
from constructs import Construct
from aws_cdk.aws_logs import RetentionDays


class ApigwWebsocketFargateCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create cloudwatch log group - ApiGW
        api_log_group = logs.LogGroup(
            self,
            "apigw-websocket-log-group",
            removal_policy=RemovalPolicy.DESTROY,
            retention=RetentionDays.FIVE_DAYS,
        )

        # create api gateway websocket api
        websockets_api = apigw.WebSocketApi(self, "apigw-websocket-fargate-api")

        stage = apigw.CfnStage(
            scope=self,
            id="DEV-WS-API-STAGE",
            api_id=websockets_api.api_id,
            stage_name="dev",
            auto_deploy=True,
            default_route_settings=apigw.CfnStage.RouteSettingsProperty(
                data_trace_enabled=True,
                detailed_metrics_enabled=True,
                logging_level="INFO",
            ),
            access_log_settings=apigw.CfnStage.AccessLogSettingsProperty(
                destination_arn=api_log_group.log_group_arn,
                format='{ "requestId":"$context.requestId", "ip": "$context.identity.sourceIp", "requestTime":"$context.requestTime", "routeKey":"$context.routeKey", "status":"$context.status","responseLength":"$context.responseLength"}',
            ),
        )

        # create VPC for fargate cluster
        vpc = ec2.Vpc(self, "apigw-websocket-fargate-vpc", max_azs=2)

        # create cloudwatch log group - FARGATE
        log_group = logs.LogGroup(
            self,
            "apigw-websocket-fargate-log-group",
            removal_policy=RemovalPolicy.DESTROY,
            retention=RetentionDays.FIVE_DAYS,
        )

        # create Fargate task definition
        task_definition = ecs.FargateTaskDefinition(
            self,
            "apigw-websocket-fargate-task-definition",
            cpu=1024,
            memory_limit_mib=2048,
            runtime_platform=ecs.RuntimePlatform(
                cpu_architecture=ecs.CpuArchitecture.ARM64
            ),
        )

        # add container to task definition
        task_definition.add_container(
            "apigw-websocket-fargate-container",
            image=ecs.ContainerImage.from_asset("./src/api"),
            memory_reservation_mib=2048,
            cpu=512,
            logging=ecs.LogDriver.aws_logs(
                stream_prefix="apigw-websocket-fargate", log_group=log_group
            ),
            port_mappings=[ecs.PortMapping(container_port=8000)],
            # add web socket api endpoint as env variable
            environment={
                "WEBSOCKET_API_ENDPOINT": f"https://{websockets_api.api_id}.execute-api.{core.Aws.REGION}.amazonaws.com/{stage.stage_name}"
            },
        )

        # add task role policy for cloud watch
        task_definition.add_to_task_role_policy(
            statement=iam.PolicyStatement(
                actions=[
                    "logs:PutLogEvents",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:DescribeLogStreams",
                    "logs:DescribeLogGroups",
                    "xray:*",
                ],
                resources=["*"],
                effect=iam.Effect.ALLOW,
            )
        )

        # add task role policy for websockets api
        task_definition.add_to_task_role_policy(
            statement=iam.PolicyStatement(
                actions=["execute-api:ManageConnections"],
                resources=[
                    f"arn:aws:execute-api:{core.Aws.REGION}:{core.Aws.ACCOUNT_ID}:{websockets_api.api_id}/{stage.stage_name}/*/*"
                ],
                effect=iam.Effect.ALLOW,
            )
        )

        # create security group to allow inbound traffic on port 8000
        security_group = ec2.SecurityGroup(
            self,
            "apigw-websocket-fargate-security-group",
            vpc=vpc,
            allow_all_outbound=True,
        )
        security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(8000))

        # create application balanced Fargate service
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "apigw-websocket-fargate-service",
            task_definition=task_definition,
            cpu=1024,
            memory_limit_mib=2048,
            desired_count=1,
            public_load_balancer=True,
            security_groups=[security_group],
            assign_public_ip=True,
            vpc=vpc,
        )

        # setup auto scaling for the Fargate service
        fargate_service.service.auto_scale_task_count(max_capacity=2)

        template = """{"connectionId": "$context.connectionId", "body": $input.body}"""

        # http integration
        http_api_integration = apigw.CfnIntegration(
            self,
            "http_api_integration",
            api_id=websockets_api.api_id,
            integration_type="HTTP",
            integration_method="POST",
            integration_uri=f"http://{fargate_service.load_balancer.load_balancer_dns_name}",
            template_selection_expression="\\$default",
            request_templates={"\\$default": template},
        )

        # create default route for api and associate http integration
        apigw.CfnRoute(
            self,
            "default_route",
            api_id=websockets_api.api_id,
            route_key="$default",
            target=f"integrations/{http_api_integration.ref}",
        )

        CfnOutput(self, "websockets_api_endpoint", value=websockets_api.api_endpoint)
        CfnOutput(
            self,
            "alb_endpoint",
            value=fargate_service.load_balancer.load_balancer_dns_name,
        )
