from aws_cdk import aws_iam as iam
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as snssubs
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import aws_sqs as sqs
from aws_cdk import core as cdk


class SnsSqsCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the queue
        MySqsQueue = sqs.Queue(self, "MySqsQueue")

        # Create the Topic
        MySnsTopic = sns.Topic(self, "MySnsTopic")

        # Create an SQS topic subscription object
        sqsSubscription = snssubs.SqsSubscription(MySqsQueue)

        # Add the SQS subscription to the sns topic
        MySnsTopic.add_subscription(sqsSubscription)

        # Add policy statement to SQS Policy that is created as part of the new queue
        iam.PolicyStatement(actions=['SQS:SendMessage'],
                            effect=iam.Effect.ALLOW,
                            conditions={'ArnEquals': MySnsTopic.topic_arn},
                            resources=[MySqsQueue.queue_arn],
                            principals=[
                                iam.ServicePrincipal('sns.amazonaws.com')
                            ]
                            )

        cdk.CfnOutput(self, "SQS queue name", description="SQS queue name", value=MySqsQueue.queue_name)
        cdk.CfnOutput(self, "SQS queue ARN", description="SQS queue arn", value=MySqsQueue.queue_arn)
        cdk.CfnOutput(self, "SQS queue URL", description="SQS queue URL", value=MySqsQueue.queue_url)
        cdk.CfnOutput(self, "SNS topic name", description="SNS topic name", value=MySnsTopic.topic_name)
        cdk.CfnOutput(self, "SNS topic ARN", description="SNS topic ARN", value=MySnsTopic.topic_arn)
