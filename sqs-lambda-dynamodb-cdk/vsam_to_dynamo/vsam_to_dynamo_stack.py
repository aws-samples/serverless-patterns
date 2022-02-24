from aws_cdk import (
    Stack,
    Duration,
    RemovalPolicy,
    CfnOutput,
    aws_iam as _iam,
    aws_sqs as _sqs,
    aws_dynamodb as _dyn,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _event
)
from constructs import Construct

class VsamToDynamoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = _sqs.Queue(
            self, "VsamToDynamoQueue",
            visibility_timeout=Duration.seconds(300),
            queue_name='VsamToDynamoQueue')


        dynamoTable = _dyn.Table(
            self, "CLIENT",
            partition_key=_dyn.Attribute(
                name="CLIENT-KEY",
                type=_dyn.AttributeType.STRING
            ),
            table_name = "CLIENT",

        )

        # Create the Lambda function to subscribe to SQS and store the record in DynamoDB
        # The source code is in './src' directory
        lambda_fn = _lambda.Function(
            self, "SQSToDynamoFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="insertRecord.handler",
            code=_lambda.Code.from_asset("lambda_fns"),
        )

        dynamoTable.grant_write_data(lambda_fn)
        
        queue.grant_consume_messages(lambda_fn)
        lambda_fn.add_event_source(_event.SqsEventSource(queue))