import aws_cdk as cdk
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_lambda_event_sources as lambda_event_sources,
    aws_iam as iam,
)
from constructs import Construct

class S3SqsLambdaBedrockS3CdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

         #create a S3 bucket source
        bucket = s3.Bucket(self, "input-bucket", versioned=True, block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,)
        
        #create a S3 bucket source
        bucket_summary = s3.Bucket(self, "summary-bucket", versioned=True, block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,)

        # Define dead letter queue
        dead_letter_queue = sqs.Queue(
        self, "S3EventQueueDLQ",
        retention_period=Duration.days(14)
        )

        queue = sqs.Queue(
            self, "S3EventQueue",
            visibility_timeout=Duration.seconds(360),
            dead_letter_queue=sqs.DeadLetterQueue (
                    max_receive_count= 3,
                    queue= dead_letter_queue,
                )
        )

        

        #queue_arn = queue.queue_arn 

         # Add S3 notification to send events to queue
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED, 
            # s3.NotificationKeyFilter(prefix="uploads/") Use this is you want to filter the object with a certain prefix
            # add notification destination
            s3n.SqsDestination(queue)

        )

        # Create Lambda function
        function = lambda_.Function(
        self, "lambda_function",
        runtime=lambda_.Runtime.PYTHON_3_9,
        handler="index.lambda_handler",
        code=lambda_.Code.from_asset("lambda"),
        timeout=cdk.Duration.seconds(300),
        )

        # Configure queue as event source
        function.add_event_source(lambda_event_sources.SqsEventSource(queue, batch_size=10))    

        # Grant Lambda permission to invoke bedrock-runtime
        function.add_to_role_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources=["*"]
            #comment above and uncomment below by replacing region and account id to make this permission specific toa  model rather than giving access to all resources
            # resources=["arn:aws:bedrock:region:account-id:model/amazon.titan-embed-text-v1"]
            )
        )  

        # Get queue URL
        queue_url = queue.queue_url

        # Add environment variable
        function.add_environment("SQS_QUEUE_URL", queue_url)

        # Add bucket_summary to environment variable
        function.add_environment("BUCKET_SUMMARY", bucket_summary.bucket_name)

        bucket_summary.grant_put(function)
        bucket.grant_read(function)


        
