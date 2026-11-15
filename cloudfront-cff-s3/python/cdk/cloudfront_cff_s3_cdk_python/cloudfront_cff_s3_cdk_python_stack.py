from aws_cdk import (
    Stack,
    CfnOutput,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment
)
from constructs import Construct

class CloudfrontCffS3CdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #create the Cloudfront Function used to change the uri
        cf_function = cloudfront.Function(self, "Function",
            code=cloudfront.FunctionCode.from_file(file_path="cff/ab_testing.js")
        )

        #the S3 bucket where the html files will be hosted
        hosting_bucket = s3.Bucket(self, "MyHostingBucket")

        #copy the html files at deployment to the hosting bucket
        s3_deployment.BucketDeployment(self, "myDeployment",
            sources = [s3_deployment.Source.asset("website")],
            destination_bucket = hosting_bucket,
        )

        #create a cloudfront distribution and associate the cloudfront Function to the Distribution
        my_distribution = cloudfront.Distribution(self, "MyDistribution",
        default_behavior=cloudfront.BehaviorOptions(
            origin=origins.S3Origin(hosting_bucket),
            function_associations=[cloudfront.FunctionAssociation(
                function=cf_function,
                event_type=cloudfront.FunctionEventType.VIEWER_REQUEST
                )]
            )

        )

        CfnOutput(self, "DomainName",
            value = my_distribution.domain_name,
            export_name = 'DomainName',
            description = 'CloudFront Domain Name')
