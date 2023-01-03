from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
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

        #Create an SNS topic
        my_topic = sns.Topic(self, 'myLambdaTopic')
        
        #Create a Lambda function
        my_lambda = _lambda.Function(self, "LogsLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="index.lambda_handler",
            timeout=Duration.seconds(30),
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
        
        #Add Lambda as a destination for log subscription
        my_log_group.add_subscription_filter(
            id="lambdaSubscription",
            destination=log_destinations.LambdaDestination(fn=my_lambda),
            filter_pattern=logs.FilterPattern.all_terms("ERROR")
        )

        #Create an SQS queue
        my_queue = sqs.Queue(self, "myQueue")
        
        #Subscribe SQS queue to SNS topic
        my_topic.add_subscription(
            sns_sub.SqsSubscription(my_queue, raw_message_delivery=True)
        )

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

        

         