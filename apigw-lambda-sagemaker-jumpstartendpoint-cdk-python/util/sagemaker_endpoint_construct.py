from aws_cdk import (
    aws_sagemaker as sagemaker,
    aws_ssm as ssm,
    CfnOutput
)
from constructs import Construct


class SageMakerEndpointConstruct(Construct):

    def __init__(self, scope: Construct, construct_id: str,
                 project_prefix: str,
                 role_arn: str,
                 model_name: str,
                 model_bucket_name: str,
                 model_bucket_key: str,
                 model_docker_image: str,
                 variant_name: str,
                 variant_weight: int,
                 instance_count: int,
                 instance_type: str,
                 environment: dict,
                 deploy_enable: bool) -> None:
        super().__init__(scope, construct_id)

        model = sagemaker.CfnModel(self, f"{model_name}-Model",
                                   execution_role_arn=role_arn,
                                   containers=[
                                       sagemaker.CfnModel.ContainerDefinitionProperty(
                                           image=model_docker_image,
                                           model_data_url=f"s3://{model_bucket_name}/{model_bucket_key}",
                                           environment=environment
                                       )
                                   ],
                                   model_name=f"{project_prefix}-{model_name}-Model"
                                   )

        config = sagemaker.CfnEndpointConfig(self, f"{model_name}-Config",
                                             endpoint_config_name=f"{project_prefix}-{model_name}-Config",
                                             production_variants=[
                                                 sagemaker.CfnEndpointConfig.ProductionVariantProperty(
                                                     model_name=model.attr_model_name,
                                                     variant_name=variant_name,
                                                     initial_variant_weight=variant_weight,
                                                     initial_instance_count=instance_count,
                                                     instance_type=instance_type
                                                 )
                                             ]
                                             )

        self.deploy_enable = deploy_enable
        if deploy_enable:
            self.endpoint = sagemaker.CfnEndpoint(self, f"{model_name}-Endpoint",
                                                  endpoint_name=f"{project_prefix}-{model_name}-Endpoint",
                                                  endpoint_config_name=config.attr_endpoint_config_name
                                                  )

            CfnOutput(scope=self, id=f"{model_name}EndpointName", value=self.endpoint.endpoint_name)

    @property
    def endpoint_name(self) -> str:
        return self.endpoint.attr_endpoint_name if self.deploy_enable else "not_yet_deployed"

    @property
    def endpoint_arn(self) -> str:
        return self.endpoint.ref if self.deploy_enable else "not_yet_deployed"
