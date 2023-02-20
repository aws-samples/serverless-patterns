from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    aws_kms as kms,
    aws_lambda as _lambda,
    aws_logs as logs,
    aws_sns as sns,
    aws_sqs as sqs,
    aws_sns_subscriptions as sns_sub,
    aws_iam as iam,
    aws_logs_destinations as log_destinations
)


class CwlogsLambdaSnsSqsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Create KMS Customer managed key for SNS server side encryption
        key = kms.Key(self, "MyKey",
            enable_key_rotation=True,
            pending_window=Duration.days(7)
        )
        alias = key.add_alias("alias/custom")

        #Create an SNS topic
        my_topic = sns.Topic(self, 'myLambdaTopic',
            master_key=alias
        )
        
        #Create a Lambda function
        my_lambda = _lambda.Function(self, "LogsLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("src/lambda"),
            handler="index.lambda_handler",
            timeout=Duration.seconds(2),
            environment={'TOPIC_ARN': my_topic.topic_arn}
        )

        #Create a CloudWatch Log group and stream
        my_log_group = logs.LogGroup(self, "myLogGroup")
        
        my_log_stream = logs.LogStream(self, "myLogStream",
            log_group=my_log_group,
        )

        #IAM role to invoke Lambda 
        my_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "logs:PutLogEvents"
            ],
            resources=[my_log_group.log_group_arn],
        ))

        #IAM Role to publish to SNS
        my_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "sns:Publish"
            ],
            resources=[my_topic.topic_arn],
        ))

        my_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "kms:GenerateDataKey*",
                "kms:Decrypt"
            ],
            resources=[key.key_arn],
        ))
        
        #Add Lambda as a destination for log subscription
        my_log_group.add_subscription_filter(
            id="lambdaSubscription",
            destination=log_destinations.LambdaDestination(fn=my_lambda),
            filter_pattern=logs.FilterPattern.all_terms("ERROR")
        )
        #Create an SQS dead letter queue
        my_dead_letter_queue = sqs.Queue(self, "myDeadLetterQueue",
            enforce_ssl=True
        )
        #Create an SQS queue
        my_queue = sqs.Queue(self, "myQueue",
            enforce_ssl=True,
            dead_letter_queue = sqs.DeadLetterQueue(
                max_receive_count=2,
                queue=my_dead_letter_queue
        ))

        
        #Subscribe SQS queue to SNS topic
        my_topic.add_subscription(sns_sub.SqsSubscription(
            my_queue, 
            raw_message_delivery=True
        ))

        #Stack Outputs
        CfnOutput(self, "LOG GROUP NAME", 
            value=my_log_group.log_group_name
            )
        CfnOutput(self, "LOG STREAM NAME", 
            value=my_log_stream.log_stream_name
            )
        CfnOutput(self, "QUEUE URL", 
            value=my_queue.queue_url
            )

        

         