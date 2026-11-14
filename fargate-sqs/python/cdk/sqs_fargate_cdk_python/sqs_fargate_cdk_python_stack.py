from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_autoscaling as autoscaling
)


class SqsFargateCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "SqsFargateCdkPythonQueue",
            visibility_timeout=Duration.seconds(300)
        )

        nat_provider = ec2.NatProvider.instance(
            instance_type=ec2.InstanceType("t3.small")
        )

        vpc = ec2.Vpc(self, "SqsFargateCdkPythonVpc", nat_gateway_provider=nat_provider, nat_gateways=1)

        cluster = ecs.Cluster(self, "SqsFargateCdkPythonCluster", vpc=vpc)

        role = iam.Role(self, "SqsFargateCdkPythonRole", assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"))

        queue.grant_consume_messages(role)

        fargate_task_definition = ecs.FargateTaskDefinition(self, "SqsFargateCdkPythonFargateTaskDefinition",
                                                            memory_limit_mib=512, cpu=256,
                                                            task_role=role)

        aws_log_drive = ecs.AwsLogDriver(stream_prefix="sqs_fargate_cdk_python")

        fargate_task_definition.add_container("SqsFargateCdkPythonContainer",
                                              image=ecs.ContainerImage.from_asset("./docker"),
                                              environment={"QUEUE_URL": queue.queue_url}, logging=aws_log_drive)

        fargate_service = ecs.FargateService(self, "SqsFargateCdkPythonFargateService", cluster=cluster,
                                             task_definition=fargate_task_definition, desired_count=0)

        auto_scale_task_count = fargate_service.auto_scale_task_count(min_capacity=0, max_capacity=1)
        auto_scale_task_count.scale_on_metric("SqsFargateCdkPythonScaleOnMetric",
                                              metric=queue.metric_approximate_number_of_messages_visible(),
                                              adjustment_type=autoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
                                              cooldown=Duration.seconds(300),
                                              scaling_steps=[{"upper": 0, "change": -1}, {"lower": 1, "change": +1}])
