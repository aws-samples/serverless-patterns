from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_certificatemanager as acm,
    aws_ec2 as ec2,
    aws_ecr_assets as assets,
    aws_ecs as ecs,
    aws_elasticloadbalancingv2 as elbv2,
    aws_elasticloadbalancingv2_targets as alb_targets,
    aws_lambda as lambda_,
    aws_route53 as r53,
    aws_s3 as s3,
    aws_autoscaling as autoscaling,
)

from constructs import Construct


class AlbPathBasedSessionStickinessStack(Stack):
    """
    This class represents the main CDK stack for the example application.
    It sets up the necessary AWS resources including S3 buckets, VPC, Lambda functions,
    and an Application Load Balancer.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC with public and private subnets
        vpc = ec2.Vpc(
            self,
            "VPC",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC, name="Public", cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name="Private",
                    cidr_mask=24,
                ),
            ],
            restrict_default_security_group=True,
            gateway_endpoints={
                "s3": ec2.GatewayVpcEndpointOptions(
                    service=ec2.GatewayVpcEndpointAwsService.S3
                ),
            },
        )

        for service in ["ssm", "ssmmessages", "ec2messages"]:
            endpoint = vpc.add_interface_endpoint(
                f"{service}-endpoint",
                service=ec2.InterfaceVpcEndpointAwsService(name=service),
                open=True,
            )

        requests_layer = lambda_.LayerVersion(
            self,
            "RequestsLayer",
            code=lambda_.Code.from_asset(
                "alb_path_based_session_stickiness/lambda_functions/requests_layer.zip"
            ),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_12],
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Create a Lambda function for handling cookies
        cookie_function = lambda_.Function(
            self,
            "CookieFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_asset(
                "alb_path_based_session_stickiness/lambda_functions/generate_cookie"
            ),
            handler="index.lambda_handler",
            # vpc=vpc,
            # vpc_subnets=ec2.SubnetSelection(
            #     subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            # ),
            # allow_public_subnet=False,
            layers=[requests_layer],
            tracing=lambda_.Tracing.ACTIVE,
        )

        lambda_tg = elbv2.ApplicationTargetGroup(
            self,
            "LambdaTargetGroup",
            vpc=vpc,
            target_type=elbv2.TargetType.LAMBDA,
            targets=[alb_targets.LambdaTarget(cookie_function)],
        )
        lambda_tg.set_attribute(
            key="lambda.multi_value_headers.enabled", 
            value="true"
        )

        alb_sg = ec2.SecurityGroup(
            self,
            "ALB-SG",
            vpc=vpc,
            allow_all_outbound=False,
            description="ALB Security Group",
        )

        alb = elbv2.ApplicationLoadBalancer(
            self,
            "LB",
            vpc=vpc,
            internet_facing=True,
            security_group=alb_sg,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

        with open("alb_path_based_session_stickiness/user_data/user_data.sh", "r") as f:
            web_user_data = ec2.UserData.custom(
                content=f.read()
            )

        web_asg = autoscaling.AutoScalingGroup(
            self,
            "WebASG",
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE4_GRAVITON, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023,
                cpu_type=ec2.AmazonLinuxCpuType.ARM_64,
            ),
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            min_capacity=2,
            max_capacity=4,
            ssm_session_permissions=True,
            user_data=web_user_data,
            block_devices=[
                autoscaling.BlockDevice(
                    device_name="/dev/xvda",
                    volume=autoscaling.BlockDeviceVolume.ebs(
                        volume_size=8,
                        volume_type=autoscaling.EbsDeviceVolumeType.GP3,
                        encrypted=True,
                    ),
                )
            ],
        )

        web_tg = elbv2.ApplicationTargetGroup(
            self,
            "WebTG",
            vpc=vpc,
            port=80,
            target_type=elbv2.TargetType.INSTANCE,
            stickiness_cookie_duration=Duration.hours(8),
        )

        web_asg.attach_to_application_target_group(web_tg)

        # Add HTTP listener to the ALB
        listener = alb.add_listener(
            "HTTP",
            port=80,
            open=True,
            default_action=elbv2.ListenerAction.forward(
                [lambda_tg],
            ),
        )

        listener.add_action(
            "WebServer",
            priority=1,
            action=elbv2.ListenerAction.forward(
                [web_tg],
            ),
            conditions=[
                elbv2.ListenerCondition.http_header(
                    name="Cookie", values=["AWSALBAPP=*"]
                )
            ],
        )
