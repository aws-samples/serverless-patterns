from aws_cdk import (
    Stack, Duration,
    aws_iam as iam,
    aws_ssm as ssm,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)

from constructs import Construct
from util.sagemaker_endpoint_construct import SageMakerEndpointConstruct
from datetime import datetime

class ApigwLambdaSagemakerJumpstartendpointStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, model_info, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get the instance count parameter from the context or use a default value
        instance_count_param = self.node.try_get_context("instance_count_param")
        instance_count = int(instance_count_param) if instance_count_param else 1

        role = iam.Role(self, "SageMaker-Policy", assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"))

        sts_policy = iam.Policy(self, "sm-deploy-policy-sts",
                                statements=[iam.PolicyStatement(
                                    effect=iam.Effect.ALLOW,
                                    actions=[
                                        "sts:AssumeRole"
                                    ],
                                    resources=["*"]
                                )]
                                )

        logs_policy = iam.Policy(self, "sm-deploy-policy-logs",
                                 statements=[iam.PolicyStatement(
                                     effect=iam.Effect.ALLOW,
                                     actions=[
                                         "cloudwatch:PutMetricData",
                                         "logs:CreateLogStream",
                                         "logs:PutLogEvents",
                                         "logs:CreateLogGroup",
                                         "logs:DescribeLogStreams",
                                         "ecr:GetAuthorizationToken"
                                     ],
                                     resources=["*"]
                                 )]
                                 )

        ecr_policy = iam.Policy(self, "sm-deploy-policy-ecr",
                                statements=[iam.PolicyStatement(
                                    effect=iam.Effect.ALLOW,
                                    actions=[
                                        "ecr:*",
                                    ],
                                    resources=["*"]
                                )]
                                )

        role.attach_inline_policy(sts_policy)
        role.attach_inline_policy(logs_policy)
        role.attach_inline_policy(ecr_policy)

        # Generate a unique model name
        model_name = f"JumpstartModel-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Create a SageMaker endpoint that can be used to generate images from text
        endpoint = SageMakerEndpointConstruct(self, "Jumpstart",
                                              project_prefix=f"Jumpstart-{instance_count}",
                                              role_arn=role.role_arn,
                                              model_name=model_name,
                                              model_bucket_name=model_info["model_bucket_name"],
                                              model_bucket_key=model_info["model_bucket_key"],
                                              model_docker_image=model_info["model_docker_image"],
                                              variant_name="AllTraffic",
                                              variant_weight=1,
                                              instance_count=instance_count,
                                              instance_type=model_info["instance_type"],
                                              environment={
                                                  "MMS_MAX_RESPONSE_SIZE": "20000000",
                                                  "SAGEMAKER_CONTAINER_LOG_LEVEL": "20",
                                                  "SAGEMAKER_PROGRAM": "inference.py",
                                                  "SAGEMAKER_REGION": model_info["region_name"],
                                                  "SAGEMAKER_SUBMIT_DIRECTORY": "/opt/ml/model/code",
                                              },

                                              deploy_enable=True
                                              )

        endpoint.node.add_dependency(sts_policy)
        endpoint.node.add_dependency(logs_policy)
        endpoint.node.add_dependency(ecr_policy)

        ssm.StringParameter(self, "Jumpstart_endpoint", parameter_name="Jumpstart_endpoint",
                            string_value=endpoint.endpoint_name)

        # Create a Lambda function to invoke the SageMaker endpoint
        lambda_function = _lambda.Function( 
        self,
        "InvokeSagemakerEndpointLambda",
        function_name="InvokeSagemakerEndpointLambda",
        runtime=_lambda.Runtime.PYTHON_3_9,
        handler="InvokeSagemakerEndpointLambda.lambda_handler",
        code=_lambda.Code.from_asset("lambda"),
        environment={
            "SAGEMAKER_ENDPOINT_NAME": endpoint.endpoint_name,
        },
        timeout=Duration.seconds(500)
        )

        # Add the necessary IAM permissions to the Lambda function to invoke the SageMaker endpoint
        lambda_function.add_to_role_policy(iam.PolicyStatement(
        effect=iam.Effect.ALLOW,
        actions=["sagemaker:InvokeEndpoint"],
        resources=[endpoint.endpoint_arn]
        ))

        # Add the SageMaker endpoint as a dependency of the Lambda function
        lambda_function.node.add_dependency(endpoint)

        # Create the REST API Gateway
        api = apigateway.RestApi(
            self,
            "APIForSagemakerEndpoint",
            rest_api_name="APIForSagemakerEndpoint"
        )

        # Store the API Gateway URL in an SSM Parameter
        ssm.StringParameter(
            self,
            "api_gateway_url",
            parameter_name="/SagemakerAPI/URL",
            string_value=api.url,
        )

        # Add the usage plan
        usage_plan = api.add_usage_plan(
            "APIForSagemakerUsagePlan",
            name="APIForSagemakerUsagePlan",
            throttle=apigateway.ThrottleSettings(
                rate_limit=1000,
                burst_limit=2000
            )
        )
        # Create the API key
        api_key = api.add_api_key("SagemakerAPIKey")

        # Associate the API key with the usage plan
        usage_plan.add_api_key(api_key)

        # Store the API key in an SSM Parameter
        ssm.StringParameter(
            self,
            "api_gateway_key",
            parameter_name="/SagemakerAPI/APIKey",
            string_value=api_key.key_id,  # Store the API key value
        )

        # Create the API Gateway integration with the Lambda function
        integration = apigateway.LambdaIntegration(
            lambda_function,
            proxy=True,
        )

        # Create a resource and attach the integration
        resource = api.root.add_resource("generateimage")
        method = resource.add_method(
            http_method="POST",
            integration=integration,
            api_key_required=True
        )
        # Add the API stage and associate it with the usage plan
        stage = api.deployment_stage
        usage_plan.add_api_stage(
            api=api,
            stage=api.deployment_stage
        )

        # Add dependency between Lambda function and API Gateway
        api.node.add_dependency(lambda_function)

