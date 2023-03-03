from aws_cdk import (
    CfnOutput,
    RemovalPolicy,
    Stack,
    aws_dynamodb as ddb,
    aws_iam as iam,
    aws_pipes as pipes,
    aws_sqs as sqs,
)
from constructs import Construct
import json

class EventbridgePipesDynamodbstreamToSqsCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ddb_table = ddb.Table(self, "Table",
            partition_key=ddb.Attribute(name="pk", type=ddb.AttributeType.STRING),
            stream=ddb.StreamViewType.NEW_IMAGE,
            removal_policy=RemovalPolicy.DESTROY
        )

        sqs_queue = sqs.Queue(self, 'sqs-queue')

        # Create Pipe policies and role
        pipe_source_policy = iam.PolicyStatement(
                actions=[
                    'dynamodb:DescribeStream',
                    'dynamodb:GetRecords',
                    'dynamodb:GetShardIterator',
                    'dynamodb:ListStreams'
                    ],
                resources=[ddb_table.table_stream_arn],
                effect=iam.Effect.ALLOW,
        )

        pipe_target_policy = iam.PolicyStatement(
                actions=['sqs:SendMessage'],
                resources=[sqs_queue.queue_arn],
                effect=iam.Effect.ALLOW,
        )

        pipe_role = iam.Role(self, 'pipe-role',
            assumed_by=iam.ServicePrincipal('pipes.amazonaws.com'),
        )

        pipe_role.add_to_policy(pipe_source_policy)
        pipe_role.add_to_policy(pipe_target_policy)

        # Create Pipe
        pipe = pipes.CfnPipe(self, "pipe",
            role_arn=pipe_role.role_arn,
            source=ddb_table.table_stream_arn,
            source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                dynamo_db_stream_parameters=pipes.CfnPipe.PipeSourceDynamoDBStreamParametersProperty(
                    starting_position="LATEST",
                ),
                filter_criteria=pipes.CfnPipe.FilterCriteriaProperty(
                    filters=[pipes.CfnPipe.FilterProperty(
                        pattern=json.dumps({"dynamodb.NewImage.entity.S":["user"]})
                    )]
                ),
            ),
            target=sqs_queue.queue_arn,
        )

        # Output
        CfnOutput(self, "QueueName", value=sqs_queue.queue_name)
        CfnOutput(self, "DynamoDBTableName", value=ddb_table.table_name)
        CfnOutput(self, "PipeARN", value=pipe.attr_arn)