from constructs import Construct
import os
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
)

class DemoWebsiteStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 bucket for static website hosting
        website_bucket = s3.Bucket(
            self, id="demo-website",
            versioned=True
        )

        # OAI for S3 bucket --> CloudFront
        bucket_origin_access_identity = cloudfront.OriginAccessIdentity(self, "OriginAccessIdentity")
        website_bucket.grant_read(bucket_origin_access_identity)

        # CloudFront distribution
        cloudfront_distribution = cloudfront.Distribution(self, "DemoDistribution",
            default_root_object="index.html",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(website_bucket, origin_access_identity=bucket_origin_access_identity)
            )
        )

        # S3 bucket deployment
        website_bucket_deployment = s3_deployment.BucketDeployment(
            self, "DeployDemoWebsite",
            sources=[s3_deployment.Source.asset("aws_serverless_pattern_cdk_crossaccount_deployment/static_site/dist")],
            destination_bucket=website_bucket,
            distribution=cloudfront_distribution
        )

        # Depend on S3 bucket for bucket deployment
        website_bucket_deployment.node.add_dependency(website_bucket)
