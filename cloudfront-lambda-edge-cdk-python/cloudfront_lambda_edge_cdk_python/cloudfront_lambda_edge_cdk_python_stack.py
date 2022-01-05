from aws_cdk import (
    Stack,
    CfnOutput,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3 as s3,
    aws_lambda as _lambda
)
from constructs import Construct

class CloudfrontLambdaEdgeCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_edge = _lambda.Function(self, 'LambdaEdge',
            runtime = _lambda.Runtime.PYTHON_3_7,
            handler = 'index.handler',
            code = _lambda.Code.from_asset('lambda'),
        )

        #create an S3 bucket used as origin for Cloudfront, not used but origin is a required field
        hosting_bucket = s3.Bucket(self, "MyHostingBucket")

        my_distribution = cloudfront.Distribution(self, "MyDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(hosting_bucket),
                edge_lambdas=[cloudfront.EdgeLambda(
                    function_version=lambda_edge.current_version,
                    event_type=cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST
                )
                ]
            ),
            comment = 'Dynamic content generation using Lambda@Edge'
        )


        CfnOutput(self, "DomainName",
            value = my_distribution.domain_name,
            export_name = 'DomainName',
            description = 'CloudFront Domain Name')
