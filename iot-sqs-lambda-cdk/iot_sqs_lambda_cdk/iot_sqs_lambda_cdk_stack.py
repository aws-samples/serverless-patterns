# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 
# SPDX-License-Identifier: MIT-0

from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda
)

import aws_cdk.aws_iot_alpha as iot
import aws_cdk.aws_iot_actions_alpha as actions
import aws_cdk.aws_lambda_event_sources as LambdaEventSources

class IotSqsLambdaCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # SQS standard queue
        queue = sqs.Queue(
            self, "IotSqsLambdaCdkQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # IoT Rule with SQS action
        topic_rule = iot.TopicRule(self, "IotSqsLambdaCdkRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/data'"),
            actions=[
                actions.SqsQueueAction(queue,
                    use_base64=False
                )
            ]
        )

        # Lambda function 
        iot_sqs_lambda = _lambda.Function(
            self, 
            id='IotSqsLambdaCdk',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('src'),
            handler='lambda_function.handler',
        )

        # Lambda event source 
        iot_sqs_lambda.add_event_source(LambdaEventSources.SqsEventSource(queue,
            batch_size=10, 
            max_batching_window=Duration.minutes(5),
            report_batch_item_failures=True
        ))  