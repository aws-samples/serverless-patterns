from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    aws_s3 as s3,
    aws_sqs as sqs,
    aws_s3_notifications as s3n
)
from constructs import Construct

class S3SQSStack(Stack):
    def __init__(self, app: App, id: str) -> None:
        super().__init__(app, id)

        
        # SQS queue
        queue = sqs.Queue(self, 's3-to-sqs-test')

        bucket = s3.Bucket(self, "MyBucket")
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.SqsDestination(queue))

        
        # Output information about the created resources
        CfnOutput(self, 'sqsQueueUrl',
                      value=queue.queue_url,
                      description='The URL of the SQS queue')
        CfnOutput(self, 'bucketName',
                      value=bucket.bucket_name,
                      description='The name of the bucket created')


app = App()
S3SQSStack(app, "S3SQSStackExample")
app.synth()
