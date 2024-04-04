from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_kinesis as kinesis,
    aws_lambda_event_sources as event_sources,
)
from constructs import Construct

class KinesisLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        kinesis_stream = kinesis.Stream(self, "stream-lambda-esm-filter", stream_name="stream-lambda-esm-filter")
        

        consumer_func_no_filter = lambda_.Function(
            self, 'LambdaConsumerNoFilter',
            handler='lambda_function.handler',
            code=lambda_.Code.from_asset('data_stream_processor/consumer'),
            runtime=lambda_.Runtime.PYTHON_3_11,
            timeout=Duration.seconds(30)
        )
        kinesis_stream.grant_read(consumer_func_no_filter)
        
        # Event Filter: None; receive all records from event source
        consumer_func_no_filter.add_event_source(
            event_sources.KinesisEventSource(
                stream=kinesis_stream,
                starting_position=lambda_.StartingPosition.LATEST,
                batch_size=1
            )
        )

        consumer_func_fail = lambda_.Function(
            self, 'LambdaConsumerFailStatus',
            handler='lambda_function.handler',
            code=lambda_.Code.from_asset('data_stream_processor/consumer'),
            runtime=lambda_.Runtime.PYTHON_3_11,
            timeout=Duration.seconds(30)
        )
        kinesis_stream.grant_read(consumer_func_fail)

        # Event Filter: records where "STATUS" attribute is "FAIL" only
        # Equals comparison
        consumer_func_fail.add_event_source(
            event_sources.KinesisEventSource(
                stream=kinesis_stream,
                starting_position=lambda_.StartingPosition.LATEST,
                batch_size=1,
                filters=[
                    lambda_.FilterCriteria.filter({"data": {
                        "STATUS": lambda_.FilterRule.is_equal("FAIL")
                    }
                    })
                ]
            )
        )

        consumer_func_not_ok = lambda_.Function(
            self, 'LambdaConsumerNotOkStatus',
            handler='lambda_function.handler',
            code=lambda_.Code.from_asset('data_stream_processor/consumer'),
            runtime=lambda_.Runtime.PYTHON_3_11,
            timeout=Duration.seconds(30)
        )
        kinesis_stream.grant_read(consumer_func_not_ok)

        # Event Filter: records where "STATUS" attribute is not "OK"
        # anything-but comparison
        consumer_func_not_ok.add_event_source(
            event_sources.KinesisEventSource(
                stream=kinesis_stream,
                starting_position=lambda_.StartingPosition.LATEST,
                batch_size=1,
                filters=[
                    lambda_.FilterCriteria.filter({"data": {
                        "STATUS": lambda_.FilterRule.not_equals("OK")
                    }
                    })
                ]
            )
        )

        consumer_func_warn_value = lambda_.Function(
            self, 'LambdaConsumerWarnValue',
            handler='lambda_function.handler',
            code=lambda_.Code.from_asset('data_stream_processor/consumer'),
            runtime=lambda_.Runtime.PYTHON_3_11,
            timeout=Duration.seconds(30)
        )
        kinesis_stream.grant_read(consumer_func_warn_value)

        # Event Filter: records where "STATUS" attribute is "WARN" and "VALUE" is between 0 and 80 (inclusive)
        # AND comparison
        consumer_func_warn_value.add_event_source(
            event_sources.KinesisEventSource(
                stream=kinesis_stream,
                starting_position=lambda_.StartingPosition.LATEST,
                batch_size=1,
                filters=[
                    lambda_.FilterCriteria.filter(
                        {"data": 
                            {
                            "STATUS": lambda_.FilterRule.is_equal("WARN"),
                            "VALUE": lambda_.FilterRule.between(0, 80)
                            }
                        }
                    )
                ]
            )
        )

        consumer_func_warn_less_than_value = lambda_.Function(
            self, 'LambdaConsumerWarnLessValue',
            handler='lambda_function.handler',
            code=lambda_.Code.from_asset('data_stream_processor/consumer'),
            runtime=lambda_.Runtime.PYTHON_3_11,
            timeout=Duration.seconds(30)
        )
        kinesis_stream.grant_read(consumer_func_warn_less_than_value)

        # Event Filter: records where "STATUS" attribute is "WARN" or "VALUE" less than 80
        # Defining filter rule without CDK FilterRule library
        # multiple fields, Or comparison
        consumer_func_warn_less_than_value.add_event_source(
            event_sources.KinesisEventSource(
                stream=kinesis_stream,
                starting_position=lambda_.StartingPosition.LATEST,
                batch_size=1,
                filters=[
                    lambda_.FilterCriteria.filter({"data": {"STATUS":["WARN"]}}),
                    lambda_.FilterCriteria.filter(
                        {"data": {"VALUE": [{"numeric": ["<", 80]}]}}
                    )
                ]
            )
        )