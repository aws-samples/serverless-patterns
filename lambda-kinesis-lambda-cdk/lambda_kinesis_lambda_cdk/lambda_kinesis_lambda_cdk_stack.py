from constructs import Construct
from aws_cdk import (
    Stack,
    #core,
    aws_kinesis as kinesis,
    aws_lambda as _lambda
)

import aws_cdk.aws_lambda_event_sources as LambdaEventSources

class LambdaKinesisLambdaCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Kinesis Data Stream
        stream = kinesis.Stream(self, "LambdaKinesisLambdaCdkStream")

        # Producer Lambda function 
        producer_lambda = _lambda.Function(
            self, 
            id='ProducerLambdaCdk',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('src/producer'),
            handler='lambda_function.handler',
            environment={
                "KINESIS_STREAM": stream.stream_name
            }
        )
        
        # Add permission for producer lambda to stream
        stream.grant_write(producer_lambda)
        
        # Consumer Lambda function 
        consumer_lambda = _lambda.Function(
            self, 
            id='ConsumerLambdaCdk',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('src/consumer'),
            handler='lambda_function.handler',
        )

        # Lambda Kinesis event source
        consumer_lambda.add_event_source(LambdaEventSources.KinesisEventSource(stream,
            batch_size=100, 
            starting_position=_lambda.StartingPosition.TRIM_HORIZON
        ))        