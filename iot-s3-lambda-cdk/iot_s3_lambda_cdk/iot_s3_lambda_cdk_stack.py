from constructs import Construct
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda
)
import aws_cdk.aws_iot_alpha as iot
import aws_cdk.aws_iot_actions_alpha as actions
import aws_cdk.aws_lambda_event_sources as LambdaEventSources

class IotS3LambdaCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 bucket
        bucket = s3.Bucket(self, "IotS3LambdaCdkBucket")

        # IoT Rule with S3 action
        iot.TopicRule(self, "IotS3LambdaCdkRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/data'"),
            actions=[
                actions.S3PutObjectAction(bucket,
                    key="iot/${timestamp()}.json"
                )
            ]
        )

        # Lambda function
        iot_s3_lambda = _lambda.Function(
            self, 
            id='IotS3LambdaCdk',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('src'),
            handler='lambda_function.handler',
        )

        # Lambda S3 event source 
        iot_s3_lambda.add_event_source(LambdaEventSources.S3EventSource(bucket,
            events=[s3.EventType.OBJECT_CREATED],
            filters=[s3.NotificationKeyFilter(prefix="iot/")]
        ))