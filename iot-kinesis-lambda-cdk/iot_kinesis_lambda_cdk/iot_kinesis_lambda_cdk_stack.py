from constructs import Construct
from aws_cdk import (
    Stack,
    aws_kinesis as kinesis,
    aws_lambda as _lambda
)

import aws_cdk.aws_iot_alpha as iot
import aws_cdk.aws_iot_actions_alpha as actions
import aws_cdk.aws_lambda_event_sources as LambdaEventSources

class IotKinesisLambdaCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Kinesis Data Stream
        stream = kinesis.Stream(self, "IotKinesisLambdaCdkStream")

        # IoT Rule with Kinesis Data Stream action
        topic_rule = iot.TopicRule(self, "IotKinesisLambdaCdkRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/data'"),
            actions=[
                actions.KinesisPutRecordAction(stream,
                    partition_key="${newuuid()}"
                )
            ]
        )
        
        # Lambda function 
        iot_kinesis_lambda = _lambda.Function(
            self, 
            id='IotKinesisLambdaCdk',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('src'),
            handler='lambda_function.handler',
        )

        # Lambda Kinesis event source
        iot_kinesis_lambda.add_event_source(LambdaEventSources.KinesisEventSource(stream,
            batch_size=100, 
            starting_position=_lambda.StartingPosition.TRIM_HORIZON
        ))        