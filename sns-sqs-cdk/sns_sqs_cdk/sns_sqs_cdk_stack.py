from aws_cdk import (
    Stack,
    CfnOutput,
    aws_sns as sns,
    aws_sns_subscriptions as snssubs,
    aws_sqs as sqs
)
from constructs import Construct


class SnsSqsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the queue
        MySqsQueue = sqs.Queue(self, "MySqsQueue")

        # Create the Topic
        MySnsTopic = sns.Topic(self, "MySnsTopic")

        # Create an SQS topic subscription object
        sqsSubscription = snssubs.SqsSubscription(MySqsQueue)

        # Add the SQS subscription to the sns topic
        MySnsTopic.add_subscription(sqsSubscription)

        CfnOutput(self, "SQS queue name", description="SQS queue name", value=MySqsQueue.queue_name)
        CfnOutput(self, "SQS queue ARN", description="SQS queue arn", value=MySqsQueue.queue_arn)
        CfnOutput(self, "SQS queue URL", description="SQS queue URL", value=MySqsQueue.queue_url)
        CfnOutput(self, "SNS topic name", description="SNS topic name", value=MySnsTopic.topic_name)
        CfnOutput(self, "SNS topic ARN", description="SNS topic ARN", value=MySnsTopic.topic_arn)
