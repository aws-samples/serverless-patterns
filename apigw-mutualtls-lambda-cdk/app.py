#!/usr/bin/env python3
import os

from aws_cdk import (
    core as cdk,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_s3 as s3,
    aws_certificatemanager as acm,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_iam as iam
)

DIRNAME = os.path.dirname(__file__)

class MutualTLSAPIGatewayStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Lambda function
        # Code in ./src directory
        lambda_fn = lambda_.Function(
            self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src"))
        )
        #Input parameter for custom domain name created for API Gateway, ex: apis.example.com
        custom_domain_name = cdk.CfnParameter(self, "customdomainname", type="String",
        description="The custom domain name for AWS REST API Gateway")

        #Input parameter for ACM certificate arn
        certificate_arn = cdk.CfnParameter(self, "certificatearn", type="String",
        description="The ACM certificate ARN for custom domain name")

        #Input parameter for s3 bucket name that has truststore pem file
        truststore_bucket = cdk.CfnParameter(self, "truststorebucket", type="String",
        description="The S3 trustsore uri for custom domain name")

        #Input parameter for public hosted zone id
        public_zone_id = cdk.CfnParameter(self, "publiczoneid", type="String",
        description="The public hosted zone id to create a record for custom domain name")

        #Input parameter for public hosted zone id
        public_zone_name = cdk.CfnParameter(self, "publiczonename", type="String",
        description="The public hosted zone name to create a record for custom domain name")

        # Create the Rest API
        rest_api = apigateway.RestApi(
            self, "TLSRestAPI",
            endpoint_types=[apigateway.EndpointType.REGIONAL],
            description="RestAPI Gateway to verify mutual TLS",
            deploy=False,
            retain_deployments=False,
            disable_execute_api_endpoint=True
        )

        # Create the custom domain
        api_domain = apigateway.DomainName(
            self, "MyDomainName",
            domain_name=custom_domain_name.value_as_string,
            certificate=acm.Certificate.from_certificate_arn(self, "cert", certificate_arn.value_as_string),
            mtls=apigateway.MTLSConfig(
                bucket=s3.Bucket.from_bucket_name(self, "Bucket", truststore_bucket.value_as_string),
                key="/truststore.pem"
            ),
            security_policy=apigateway.SecurityPolicy.TLS_1_2
        )

        # Create API deployment
        deployment = apigateway.Deployment(
            self, "Deployment",
            api=rest_api,
            retain_deployments=False
        )

        # Create prod Stage for deployment
        stage = apigateway.Stage(
            self, "prod",
            deployment=deployment,
        )

        # Create API mapping to custom domain
        base_path_mapping = apigateway.BasePathMapping(self, "MyBasePathMapping",
            domain_name=api_domain,
            rest_api=rest_api,
            stage=stage
        )

        #Get public hosted zone object
        public_zone = route53.HostedZone.from_hosted_zone_attributes(self, "publiczone", hosted_zone_id=public_zone_id.value_as_string,zone_name=public_zone_name.value_as_string)

        #Create A record for custom domain name in public hosted zone
        #Record name will be taken from custom domain name, ex: for apis.example.com, record name will be apis
        record = route53.ARecord(self, 'MyAliasRecord',
            zone=public_zone,
            record_name=cdk.Fn.select(0,cdk.Fn.split('.',custom_domain_name.value_as_string)),
            target=route53.RecordTarget.from_alias(targets.ApiGatewayDomain(api_domain))
        )

        rest_api.deployment_stage = stage

        # Create URI for lambda function
        stage_uri = f"arn:aws:apigateway:{cdk.Aws.REGION}:lambda:path/2015-03-31/functions/{lambda_fn.function_arn}/invocations"

        # Create Lambda Integration
        integration = apigateway.Integration(
            type=apigateway.IntegrationType.AWS_PROXY,
            integration_http_method="POST",
            uri=stage_uri
        )

        # Create APIGW Method
        method = rest_api.root.add_method("GET", integration)

        # Add Lambda permissions
        lambda_fn.add_permission(
            "lambdaPermission",
            action="lambda:InvokeFunction",
            principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
            source_arn=method.method_arn.replace(
                rest_api.deployment_stage.stage_name, "*"
            )
        )

        # OUTPUTS
        cdk.CfnOutput(self, "LambdaFunction", export_name="MyLambdaFunction", value=lambda_fn.function_arn)
        cdk.CfnOutput(self, "ApigwId", export_name="MyAPIGWID", value=rest_api.rest_api_id)
        cdk.CfnOutput(self, "CustomDomainName", export_name="MyCustomDomain", value=api_domain.domain_name)
        cdk.CfnOutput(self, "CustomDomainHostedZone", export_name="MyCustomeZone", value=api_domain.domain_name_alias_hosted_zone_id)
        cdk.CfnOutput(self, "CustomDomainAlias", export_name="MyCustomAlias", value=api_domain.domain_name_alias_domain_name)

app = cdk.App()
MutualTLSAPIGatewayStack(app, "MutualTLSAPIGatewayStack")
app.synth()
