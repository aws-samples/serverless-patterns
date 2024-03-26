import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_lambda_event_sources as event_sources,
    aws_iam as iam,
    aws_bedrock as bedrock,
    # aws_sqs as sqs,
)
from constructs import Construct

class S3LambdaBedrockCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a S3 bucket
        bucket = s3.Bucket(self, "s3-lambda-bedrock-cdk-python-bucket", versioned=True, block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,)
            
        # defina Lambda function with timeout
        lambda_function = lambda_.Function(self, "s3-lambda-bedrock-cdk-python",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="lambda_function.lambda_handler",
            code=lambda_.Code.from_asset("src"),
            timeout=cdk.Duration.seconds(300),
        )

        # Grant Lambda permission to access S3 and get object
        bucket.grant_read(lambda_function) 

        # Grant Lambda permission to invoke bedrock-runtime
        lambda_function.add_to_role_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources=["*"]
            #comment above and uncomment below by replacing region and account id to make this permission specific toa  model rather than giving access to all resources
            # resources=["arn:aws:bedrock:region:account-id:model/amazon.titan-embed-text-v1"]
            )
        )

        # add event source to lambda function
        lambda_function.add_event_source(event_sources.S3EventSource(bucket, events=[s3.EventType.OBJECT_CREATED]))

       


        
