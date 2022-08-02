from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins
)

class S3CloudFrontOAI(Construct):
            
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        website_bucket = s3.Bucket(
            self,
            "My-Website-Bucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            encryption=s3.BucketEncryption.KMS,
            enforce_ssl=True,
            versioned=True
        )
        
        website_bucket.add_cors_rule(
            allowed_methods=[s3.HttpMethods.GET],
            allowed_origins=["*"],
            allowed_headers=["*"],
            exposed_headers=["Access-Control-Allow-Origin"]
        )

        oai = cloudfront.OriginAccessIdentity(
            self,
            "My-OAI",
            comment="My OAI for the S3 Website"
        )

        website_bucket.grant_read(oai)


        cd = cloudfront.Distribution(self, "myCloudFrontDistribution",
            default_root_object='index.html',
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(website_bucket, origin_access_identity=oai),
                origin_request_policy=cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN, 
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                response_headers_policy=cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL
                )
        )

        