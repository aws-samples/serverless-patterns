from constructs import Construct
from aws_cdk import (
    Duration,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_lambda_event_sources as eventsources,
    aws_s3 as s3
)


class TriggerTranscribe(Construct):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Input Bucket
        self.input_bucket = s3.Bucket(self, 'input-bucket',
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
        trigger_transcription_trigger = lambda_.Function(self, 'file-upload-trigger', **python_lambda_kwargs,
                                                         code=lambda_.Code.from_asset(
                                                             './assets/file-uploaded-trigger'),
                                                         function_name="start-transcription",
                                                         initial_policy=[
                                                             iam.PolicyStatement(
                                                                 actions=['transcribe:StartTranscriptionJob'],
                                                                 resources=['*']),
                                                             iam.PolicyStatement(actions=['s3:PutObject'],
                                                                                 resources=[
                                                                                     self.destination_bucket.bucket_arn+'/*']
                                                                                 ),
                                                             iam.PolicyStatement(actions=['s3:GetObject',
                                                                                          's3:ListBucket'],
                                                                                 resources=[
                                                                                     self.input_bucket.bucket_arn,
                                                                                     self.input_bucket.bucket_arn + '/*'
                                                                                 ]
                                                                                 )
                                                         ]
                                                         )
        
        # Add Trigger and Environment Variable
        trigger_transcription_trigger.add_event_source(eventsources.S3EventSource(self.input_bucket, events=[s3.EventType.OBJECT_CREATED]))
        trigger_transcription_trigger.add_environment('DESTINATION_BUCKET', self.destination_bucket.bucket_name)
