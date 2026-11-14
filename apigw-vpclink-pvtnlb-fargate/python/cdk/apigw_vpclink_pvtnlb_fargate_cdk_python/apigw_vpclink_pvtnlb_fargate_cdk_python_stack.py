import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)


from constructs import Construct

class ApigwVpclinkPvtnlbFargateCdkPyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "Vpc",
         max_azs=2,
         cidr="10.1.0.0/16",
         subnet_configuration=[
             ec2.SubnetConfiguration(name="private-snet",
                                     subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                                     cidr_mask=24),
            ec2.SubnetConfiguration(name="public-snet",
                                     subnet_type=ec2.SubnetType.PUBLIC,
                                     cidr_mask=24)]

        )

        # Create a Fargate cluster
        cluster = ecs.Cluster(self, "Cluster",
            vpc=vpc
        )

        # Create a task definition
        task_def = ecs.FargateTaskDefinition(
            self, 'TaskDef',
            cpu=512, 
            memory_limit_mib=1024,
        )

        # create container with amazon ecs sample image
        container = task_def.add_container(
            'Container',
            image=ecs.ContainerImage.from_registry('amazon/amazon-ecs-sample'),
            memory_limit_mib=512,
        )

        # Add port mappings
        container.add_port_mappings(
            ecs.PortMapping(
                container_port=80,
                host_port=80
            )
        )
        
        # security group for the service
        service_sg = ec2.SecurityGroup(self, "Service_SG", vpc=vpc)

        service_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4(vpc.vpc_cidr_block),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP from NLB"
        )

        # Create a service
        service = ecs_patterns.NetworkLoadBalancedFargateService(self, "Service",
            cluster=cluster,
            task_definition=task_def,
            public_load_balancer=False,
            security_groups=[service_sg]
        )

        # Create an NLB
        nlb = service.load_balancer

        # nlb.load_balancer_security_groups[0] = ec2.SecurityGroup(self, 'LoadBalancerSG', vpc=vpc, allow_all_outbound=False)
        


        # Create an API
        apigateway = apigw.RestApi(self, "serverless-pattern-api")

        # Create a VPC link targeting the NLB
        link = apigw.VpcLink(self, "Link", targets=[nlb])

        # API gw proxy resource
        root = apigateway.root.add_resource("{proxy+}")

        vpc_integration = apigw.Integration(
            type=apigw.IntegrationType.HTTP,
            integration_http_method= "ANY",
            uri="http://" + nlb.load_balancer_dns_name + "/{proxy}",
            options=apigw.IntegrationOptions(
                connection_type=apigw.ConnectionType.VPC_LINK,
                vpc_link=link,
                request_parameters =  { 'integration.request.path.proxy': 'method.request.path.proxy' },
                integration_responses=[
                    apigw.IntegrationResponse(
                        status_code="200",
                        response_templates={
                            "application/json": ""
                        },
                    )
                ]
            ),
        )

        # Integrate the method with the VPC link
        root.add_method("ANY", vpc_integration,
                        request_parameters= { 'method.request.path.proxy': True },
                        method_responses=[
                                apigw.MethodResponse(
                                    # Successful response from the integration
                                    status_code="200"
                                    # Validate the schema on the response
                                )
                            ])
