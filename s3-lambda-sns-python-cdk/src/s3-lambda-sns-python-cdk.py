import aws_cdk as cdk
from aws_cdk import (
    aws_lambda as lambda_,
    aws_lambda_event_sources as eventsources,
    aws_s3 as s3
)
            
class CdkS3LambdaSnsPythonStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.email = cdk.CfnParameter(
            self,
            "Email",
            type="String",
            description="Email address for subscription"
        )

        #create a S3 bucket
        bucket = s3.Bucket(self, "cdk-s3-lambda-sns", versioned=True, block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,)

        # Define SNS topic
        topic = cdk.aws_sns.Topic(self, "S3LambdaSNSTopic")

        # add SNS subscription to SNS topic
        topic.add_subscription(cdk.aws_sns_subscriptions.EmailSubscription(self.email.value_as_string))

        # Define Lambda function
        my_function = lambda_.Function(
            self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("src"),
            handler="lambda_function.lambda_handler"
        )
        # Add environment variable to Lambda function
        my_function.add_environment("TOPIC_ARN", topic.topic_arn)

        # Grant Lambda permission to access S3
        bucket.grant_put(my_function) 

        # Grant Lambda permission to publish to SNS topic
        topic.grant_publish(my_function)

        # add event source to lambda function
        my_function.add_event_source(eventsources.S3EventSource(bucket, events=[s3.EventType.OBJECT_CREATED]))
