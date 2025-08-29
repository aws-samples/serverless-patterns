import json
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_apigateway as apigateway,
    aws_elasticloadbalancingv2 as elbv2,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_certificatemanager as acm,
    custom_resources as cr,
    CfnOutput,
    Duration
)
from constructs import Construct

class PrivateApiGatewayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, domain_name: str, certificate_arn: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC Configuration
        self.vpc = ec2.Vpc(
            self, "PrivateAPI-VPC",
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ],
            enable_dns_hostnames=True,
            enable_dns_support=True
        )

        # Security Group for VPC Endpoint
        vpc_endpoint_sg = ec2.SecurityGroup(
            self, "VPCEndpoint-SG",
            vpc=self.vpc,
            description="Security group for API Gateway VPC endpoint",
            allow_all_outbound=False
        )
        
        vpc_endpoint_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.0.0.0/16"),
            connection=ec2.Port.tcp(443),
            description="HTTPS from VPC"
        )
        

        # VPC Endpoint for API Gateway
        self.vpc_endpoint = ec2.InterfaceVpcEndpoint(
            self, "APIGateway-VPCEndpoint",
            vpc=self.vpc,
            service=ec2.InterfaceVpcEndpointAwsService.APIGATEWAY,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
            security_groups=[vpc_endpoint_sg],
            private_dns_enabled=True
        )

        # Private API Gateway
        self.api = apigateway.RestApi(
            self, "PrivateAPI",
            rest_api_name="PrivateAPI-PetStore",
            description="Private API Gateway for PetStore demo",
            endpoint_configuration=apigateway.EndpointConfiguration(
                types=[apigateway.EndpointType.PRIVATE],
                vpc_endpoints=[self.vpc_endpoint]
            ),
            policy=iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        effect=iam.Effect.ALLOW,
                        principals=[iam.AnyPrincipal()],
                        actions=["execute-api:Invoke"],
                        resources=["*"],
                        conditions={
                            "StringEquals": {
                                "aws:sourceVpce": self.vpc_endpoint.vpc_endpoint_id
                            }
                        }
                    )
                ]
            )
        )

        # Create API Gateway models
        pet_type_model = self.api.add_model(
            "PetTypeModel",
            content_type="application/json",
            model_name="PetType",
            schema=apigateway.JsonSchema(
                schema=apigateway.JsonSchemaVersion.DRAFT4,
                type=apigateway.JsonSchemaType.STRING,
                enum=["dog", "cat", "fish", "bird", "gecko"]
            )
        )

        pet_model = self.api.add_model(
            "PetModel",
            content_type="application/json",
            model_name="Pet",
            schema=apigateway.JsonSchema(
                schema=apigateway.JsonSchemaVersion.DRAFT4,
                type=apigateway.JsonSchemaType.OBJECT,
                properties={
                    "id": apigateway.JsonSchema(type=apigateway.JsonSchemaType.INTEGER),
                    "type": apigateway.JsonSchema(type=apigateway.JsonSchemaType.STRING),
                    "price": apigateway.JsonSchema(type=apigateway.JsonSchemaType.NUMBER)
                }
            )
        )

        pets_model = self.api.add_model(
            "PetsModel",
            content_type="application/json",
            model_name="Pets",
            schema=apigateway.JsonSchema(
                schema=apigateway.JsonSchemaVersion.DRAFT4,
                type=apigateway.JsonSchemaType.ARRAY,
                items=apigateway.JsonSchema(
                    type=apigateway.JsonSchemaType.OBJECT,
                    properties={
                        "id": apigateway.JsonSchema(type=apigateway.JsonSchemaType.INTEGER),
                        "type": apigateway.JsonSchema(type=apigateway.JsonSchemaType.STRING),
                        "price": apigateway.JsonSchema(type=apigateway.JsonSchemaType.NUMBER)
                    }
                )
            )
        )

        new_pet_model = self.api.add_model(
            "NewPetModel",
            content_type="application/json",
            model_name="NewPet",
            schema=apigateway.JsonSchema(
                schema=apigateway.JsonSchemaVersion.DRAFT4,
                type=apigateway.JsonSchemaType.OBJECT,
                properties={
                    "type": apigateway.JsonSchema(type=apigateway.JsonSchemaType.STRING),
                    "price": apigateway.JsonSchema(type=apigateway.JsonSchemaType.NUMBER)
                }
            )
        )

        new_pet_response_model = self.api.add_model(
            "NewPetResponseModel",
            content_type="application/json",
            model_name="NewPetResponse",
            schema=apigateway.JsonSchema(
                schema=apigateway.JsonSchemaVersion.DRAFT4,
                type=apigateway.JsonSchemaType.OBJECT,
                properties={
                    "pet": apigateway.JsonSchema(
                        type=apigateway.JsonSchemaType.OBJECT,
                        properties={
                            "id": apigateway.JsonSchema(type=apigateway.JsonSchemaType.INTEGER),
                            "type": apigateway.JsonSchema(type=apigateway.JsonSchemaType.STRING),
                            "price": apigateway.JsonSchema(type=apigateway.JsonSchemaType.NUMBER)
                        }
                    ),
                    "message": apigateway.JsonSchema(type=apigateway.JsonSchemaType.STRING)
                }
            )
        )

        # Create pets resource
        pets_resource = self.api.root.add_resource("pets")
        
        # Add GET method to pets resource
        pets_resource.add_method(
            "GET",
            apigateway.HttpIntegration(
                "http://petstore.execute-api.eu-west-1.amazonaws.com/petstore/pets",
                http_method="GET",
                options=apigateway.IntegrationOptions(
                    request_parameters={
                        "integration.request.querystring.page": "method.request.querystring.page",
                        "integration.request.querystring.type": "method.request.querystring.type"
                    },
                    integration_responses=[
                        apigateway.IntegrationResponse(
                            status_code="200",
                            response_parameters={
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        )
                    ]
                )
            ),
            request_parameters={
                "method.request.querystring.page": False,
                "method.request.querystring.type": False
            },
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_parameters={
                        "method.response.header.Access-Control-Allow-Origin": False
                    },
                    response_models={
                        "application/json": pets_model
                    }
                )
            ]
        )

        # Add POST method to pets resource
        pets_resource.add_method(
            "POST",
            apigateway.HttpIntegration(
                "http://petstore.execute-api.eu-west-1.amazonaws.com/petstore/pets",
                http_method="POST",
                options=apigateway.IntegrationOptions(
                    integration_responses=[
                        apigateway.IntegrationResponse(
                            status_code="200",
                            response_parameters={
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        )
                    ]
                )
            ),
            request_models={
                "application/json": new_pet_model
            },
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_parameters={
                        "method.response.header.Access-Control-Allow-Origin": False
                    },
                    response_models={
                        "application/json": new_pet_response_model
                    }
                )
            ]
        )

        # Add OPTIONS method for CORS
        pets_resource.add_method(
            "OPTIONS",
            apigateway.MockIntegration(
                integration_responses=[
                    apigateway.IntegrationResponse(
                        status_code="200",
                        response_parameters={
                            "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                            "method.response.header.Access-Control-Allow-Methods": "'GET,POST,OPTIONS'",
                            "method.response.header.Access-Control-Allow-Origin": "'*'"
                        }
                    )
                ],
                request_templates={
                    "application/json": '{"statusCode": 200}'
                }
            ),
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_parameters={
                        "method.response.header.Access-Control-Allow-Headers": False,
                        "method.response.header.Access-Control-Allow-Methods": False,
                        "method.response.header.Access-Control-Allow-Origin": False
                    }
                )
            ]
        )

        # Create pets/{petId} resource
        pet_id_resource = pets_resource.add_resource("{petId}")
        
        # Add GET method to pets/{petId} resource
        pet_id_resource.add_method(
            "GET",
            apigateway.HttpIntegration(
                "http://petstore.execute-api.eu-west-1.amazonaws.com/petstore/pets/{petId}",
                http_method="GET",
                options=apigateway.IntegrationOptions(
                    request_parameters={
                        "integration.request.path.petId": "method.request.path.petId"
                    },
                    integration_responses=[
                        apigateway.IntegrationResponse(
                            status_code="200",
                            response_parameters={
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        )
                    ]
                )
            ),
            request_parameters={
                "method.request.path.petId": True
            },
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_parameters={
                        "method.response.header.Access-Control-Allow-Origin": False
                    },
                    response_models={
                        "application/json": pet_model
                    }
                )
            ]
        )

        # Add OPTIONS method for CORS on pets/{petId}
        pet_id_resource.add_method(
            "OPTIONS",
            apigateway.MockIntegration(
                integration_responses=[
                    apigateway.IntegrationResponse(
                        status_code="200",
                        response_parameters={
                            "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                            "method.response.header.Access-Control-Allow-Methods": "'GET,OPTIONS'",
                            "method.response.header.Access-Control-Allow-Origin": "'*'"
                        }
                    )
                ],
                request_templates={
                    "application/json": '{"statusCode": 200}'
                }
            ),
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_parameters={
                        "method.response.header.Access-Control-Allow-Headers": False,
                        "method.response.header.Access-Control-Allow-Methods": False,
                        "method.response.header.Access-Control-Allow-Origin": False
                    }
                )
            ]
        )

        # Custom Domain Name
        certificate = acm.Certificate.from_certificate_arn(
            self, "Certificate",
            certificate_arn=certificate_arn
        )

        self.domain_name = apigateway.DomainName(
            self, "APIDomainName",
            domain_name=domain_name,
            certificate=certificate,
            endpoint_type=apigateway.EndpointType.REGIONAL,
            security_policy=apigateway.SecurityPolicy.TLS_1_2
        )

        # Base Path Mapping
        apigateway.BasePathMapping(
            self, "BasePathMapping",
            domain_name=self.domain_name,
            rest_api=self.api,
            stage=self.api.deployment_stage
        )

        # Security Group for ALB
        alb_sg = ec2.SecurityGroup(
            self, "ALB-SG",
            vpc=self.vpc,
            description="Security group for Application Load Balancer"
        )
        
        alb_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="HTTPS from anywhere"
        )
        
        alb_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="HTTP from anywhere"
        )

        # Application Load Balancer
        self.alb = elbv2.ApplicationLoadBalancer(
            self, "PrivateAPI-ALB",
            vpc=self.vpc,
            internet_facing=False,
            security_group=alb_sg,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
        )

        # Target Group for VPC Endpoint
        self.target_group = elbv2.ApplicationTargetGroup(
            self, "VPCEndpoint-TG",
            port=443,
            protocol=elbv2.ApplicationProtocol.HTTPS,
            target_type=elbv2.TargetType.IP,
            vpc=self.vpc,
            health_check=elbv2.HealthCheck(
                protocol=elbv2.Protocol.HTTPS,
                path="/",
                interval=Duration.seconds(30),
                timeout=Duration.seconds(5),
                healthy_threshold_count=2,
                unhealthy_threshold_count=3,
                healthy_http_codes="200,403"
            )
        )

        # HTTPS Listener
        self.alb.add_listener(
            "HTTPS-Listener",
            port=443,
            protocol=elbv2.ApplicationProtocol.HTTPS,
            certificates=[certificate],
            default_target_groups=[self.target_group]
        )

        # HTTP Listener (redirect to HTTPS)
        self.alb.add_listener(
            "HTTP-Listener",
            port=80,
            protocol=elbv2.ApplicationProtocol.HTTP,
            default_action=elbv2.ListenerAction.redirect(
                protocol="HTTPS",
                port="443",
                permanent=True
            )
        )

        # Lambda function to register VPC endpoint IPs as targets
        register_targets_function = _lambda.Function(
            self, "RegisterVPCEndpointTargets",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.handler",
            timeout=Duration.seconds(60),
            code=_lambda.Code.from_inline('''
import boto3
import json
import urllib3

def send_response(event, context, response_status, response_data=None):
    if response_data is None:
        response_data = {}
    
    response_body = {
        'Status': response_status,
        'Reason': f'See CloudWatch Log Stream: {context.log_stream_name}',
        'PhysicalResourceId': context.log_stream_name,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'Data': response_data
    }
    
    json_response_body = json.dumps(response_body)
    headers = {
        'content-type': '',
        'content-length': str(len(json_response_body))
    }
    
    try:
        http = urllib3.PoolManager()
        response = http.request('PUT', event['ResponseURL'], body=json_response_body, headers=headers)
        print(f"Status code: {response.status}")
    except Exception as e:
        print(f"Failed to send response: {str(e)}")

def handler(event, context):
    print(f"Event: {json.dumps(event)}")
    
    try:
        ec2 = boto3.client('ec2')
        elbv2 = boto3.client('elbv2')
        
        vpc_endpoint_id = event['ResourceProperties']['VpcEndpointId']
        target_group_arn = event['ResourceProperties']['TargetGroupArn']
        
        if event['RequestType'] == 'Delete':
            print("Processing DELETE request")
            try:
                response = elbv2.describe_target_health(TargetGroupArn=target_group_arn)
                targets = [{'Id': target['Target']['Id']} for target in response['TargetHealthDescriptions']]
                if targets:
                    print(f"Deregistering targets: {targets}")
                    elbv2.deregister_targets(TargetGroupArn=target_group_arn, Targets=targets)
            except Exception as e:
                print(f"Error during delete: {str(e)}")
            send_response(event, context, 'SUCCESS', {})
            return
        
        print("Processing CREATE/UPDATE request")
        
        # Get VPC endpoint network interfaces
        print(f"Getting VPC endpoint details for: {vpc_endpoint_id}")
        response = ec2.describe_vpc_endpoints(VpcEndpointIds=[vpc_endpoint_id])
        network_interface_ids = response['VpcEndpoints'][0]['NetworkInterfaceIds']
        print(f"Network interface IDs: {network_interface_ids}")
        
        # Get private IPs
        targets = []
        for eni_id in network_interface_ids:
            eni_response = ec2.describe_network_interfaces(NetworkInterfaceIds=[eni_id])
            private_ip = eni_response['NetworkInterfaces'][0]['PrivateIpAddress']
            targets.append({'Id': private_ip, 'Port': 443})
            print(f"Found target: {private_ip}")
        
        # Register targets
        print(f"Registering targets: {targets}")
        elbv2.register_targets(TargetGroupArn=target_group_arn, Targets=targets)
        
        send_response(event, context, 'SUCCESS', {'Targets': [t['Id'] for t in targets]})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        send_response(event, context, 'FAILED', {'Error': str(e)})
''')
        )

        # Grant permissions to Lambda
        register_targets_function.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "ec2:DescribeVpcEndpoints",
                    "ec2:DescribeNetworkInterfaces",
                    "elasticloadbalancing:RegisterTargets",
                    "elasticloadbalancing:DeregisterTargets",
                    "elasticloadbalancing:DescribeTargetHealth"
                ],
                resources=["*"]
            )
        )

        # Custom Resource to register VPC endpoint IPs
        cr.AwsCustomResource(
            self, "RegisterTargets",
            on_create=cr.AwsSdkCall(
                service="Lambda",
                action="invoke",
                parameters={
                    "FunctionName": register_targets_function.function_name,
                    "Payload": json.dumps({
                        "RequestType": "Create",
                        "ResourceProperties": {
                            "VpcEndpointId": self.vpc_endpoint.vpc_endpoint_id,
                            "TargetGroupArn": self.target_group.target_group_arn
                        }
                    })
                },
                physical_resource_id=cr.PhysicalResourceId.of("RegisterTargets")
            ),
            on_delete=cr.AwsSdkCall(
                service="Lambda",
                action="invoke",
                parameters={
                    "FunctionName": register_targets_function.function_name,
                    "Payload": json.dumps({
                        "RequestType": "Delete",
                        "ResourceProperties": {
                            "VpcEndpointId": self.vpc_endpoint.vpc_endpoint_id,
                            "TargetGroupArn": self.target_group.target_group_arn
                        }
                    })
                }
            ),
            policy=cr.AwsCustomResourcePolicy.from_statements([
                iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    actions=["lambda:InvokeFunction"],
                    resources=[register_targets_function.function_arn]
                )
            ])
        )

        # Outputs
        CfnOutput(self, "VPCId", value=self.vpc.vpc_id)
        CfnOutput(self, "ALBDNSName", value=self.alb.load_balancer_dns_name)
        CfnOutput(self, "ALBHostedZoneId", value=self.alb.load_balancer_canonical_hosted_zone_id)
        CfnOutput(self, "VPCEndpointId", value=self.vpc_endpoint.vpc_endpoint_id)
        CfnOutput(self, "APIGatewayId", value=self.api.rest_api_id)
        CfnOutput(self, "CustomDomainName", value=domain_name)
        CfnOutput(self, "APIEndpoint", value=f"https://{domain_name}/pets")
        CfnOutput(self, "PublicDNSInstructions", value=f"CNAME: {domain_name} -> {self.alb.load_balancer_dns_name}")
