from aws_cdk import RemovalPolicy, aws_s3 as s3
from constructs import Construct


class DocumentBucket(Construct):
    """Private Amazon S3 bucket for the files that the agent analyzes. Versioning is
    on because Amazon S3 Files requires it:
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html
    Stack deletion empties and removes the bucket."""

    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        self.bucket = s3.Bucket(
            self,
            "Bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
