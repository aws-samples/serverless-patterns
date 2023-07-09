from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_lambda as lambda_,
    Duration,
    aws_iam as iam,
    aws_lambda_event_sources as eventsources
)
from constructs import Construct

class LambdaS3TranslateCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Input Bucket
        self.input_bucket = s3.Bucket(self, "input-bucket",
                            versioned=True,
                            encryption=s3.BucketEncryption.S3_MANAGED,
                            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                            enforce_ssl=True)

        # Destination Bucket
        self.destination_bucket = s3.Bucket(self, 'destination-bucket',
                                versioned=True,
                                encryption=s3.BucketEncryption.S3_MANAGED,
                                block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                                enforce_ssl=True)
        
        python_lambda_kwargs = {
            'handler': 'lambda_function.lambda_handler',
            'runtime': lambda_.Runtime.PYTHON_3_9,
            'timeout': Duration.minutes(2)
        }

        # Trigger Transcription Lambda
        trigger_translate_lambda = lambda_.Function(self, "file-upload-trigger", **python_lambda_kwargs,
                                                        code=lambda_.Code.from_asset(
                                                            './pattern/assets'),
                                                        function_name="start-translate",
                                                        initial_policy=[
                                                            iam.PolicyStatement(
                                                                actions=['translate:TranslateText',
                                                                         'comprehend:DetectDominantLanguage'
                                                                         ],
                                                                resources=['*']),
                                                            iam.PolicyStatement(actions=['s3:PutObject'],
                                                                                resources=[
                                                                                    self.destination_bucket.bucket_arn+'/*']
                                                                                ),
                                                            iam.PolicyStatement(actions=['s3:GetObject',
                                                                                        's3:ListBucket'],
                                                                                resources=[
                                                                                    self.input_bucket.bucket_arn,
                                                                                    self.input_bucket.bucket_arn+'/*'
                                                                                ]
                                                                        )
                                                        ]
                                                        )

        # Add Trigger and Environment Variable
        trigger_translate_lambda.add_event_source(eventsources.S3EventSource(self.input_bucket, events=[s3.EventType.OBJECT_CREATED]))
        trigger_translate_lambda.add_environment('DESTINATION_BUCKET', self.destination_bucket.bucket_name)
