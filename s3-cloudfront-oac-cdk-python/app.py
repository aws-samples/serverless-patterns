import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    CfnOutput,
    RemovalPolicy,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins
)

class S3CloudFrontOAC(Construct):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        website_bucket = s3.Bucket(
            self,
            "My-Website-Bucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            versioned=True
        )
        
        website_bucket.add_cors_rule(
            allowed_methods=[s3.HttpMethods.GET],
            allowed_origins=["*"],
            allowed_headers=["*"],
            exposed_headers=["Access-Control-Allow-Origin"]
        )

        distribution = cloudfront.Distribution(self, "myCloudFrontDistribution",
            default_root_object='index.html',
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(website_bucket),
                origin_request_policy=cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                response_headers_policy=cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL
            )
        )

        s3deploy.BucketDeployment(
            self,
            "DeployWebsite",
            sources=[s3deploy.Source.asset("./website")],
            destination_bucket=website_bucket,
            distribution=distribution,
            distribution_paths=["/*"]
        )

        CfnOutput(self, "DistributionId", value=distribution.distribution_id)
        CfnOutput(self, "DistributionDomainName", value=distribution.distribution_domain_name)

app = cdk.App()
stack = cdk.Stack(app, "S3CloudFrontOACStack")
S3CloudFrontOAC(stack, "s3-hosted-website")
app.synth()
