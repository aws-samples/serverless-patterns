from aws_cdk import (
    aws_lambda as lambda_,
    aws_kinesis as kinesis,
    aws_lambda_event_sources as event_sources,
    Stack, 
    Duration
)
from constructs import Construct

class SvlslandStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        with open("lambda_function.py", encoding="utf8") as fp:
            handler_code = fp.read()

        kinesis_stream = kinesis.Stream(self, "SampleStream")
        
        lambdaFn = lambda_.Function(
            self, 'sampleFn',
            handler='index.lambda_handler',
            code=lambda_.InlineCode(handler_code),
            runtime=lambda_.Runtime.PYTHON_3_8,
            timeout=Duration.seconds(30)
        )

        kinesis_stream.grant_read(lambdaFn)
        
        kinesis_event_source = event_sources.KinesisEventSource(
            stream=kinesis_stream,
            starting_position=lambda_.StartingPosition.LATEST,
            batch_size=1
        )
        
        lambdaFn.add_event_source(kinesis_event_source)
