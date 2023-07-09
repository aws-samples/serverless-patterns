from constructs import Construct
from aws_cdk import (
    Aspects,
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
import cdk_nag


class CwlogsLambdaSnsSqsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Create KMS Customer managed key for SNS server side encryption
        key = kms.Key(self, "Key",
            enable_key_rotation=True,
            pending_window=Duration.days(7)
        )
        alias = key.add_alias("alias/queuecustomkey")

        #Create an SNS topic
        topic = sns.Topic(self, 'LambdaTopic',
            master_key=alias
        )
        
        #Create a Lambda function and Lambda execution role 
        lambda_execution_role = iam.Role(self, "Custom Lambda Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )
        subscribed_lambda = _lambda.Function(self, "SubscribedFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("src/lambda"),
            handler="index.lambda_handler",
            timeout=Duration.seconds(2),
            environment={'TOPIC_ARN': topic.topic_arn},
            role=lambda_execution_role
        )

        #Create a CloudWatch Log group and stream
        log_group = logs.LogGroup(self, "LogGroup")
        
        log_stream = logs.LogStream(self, "LogStream",
            log_group=log_group,
        )
        
        
        #IAM role to access CloudWatch logs
        subscribed_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            resources=["*"],
        ))
        
        #CDK Nag rule suppression for wildcard permission 
        cdk_nag.NagSuppressions.add_resource_suppressions(lambda_execution_role, [{
                "id":"AwsSolutions-IAM5", 
                "reason":"To create custom Lambda execution role to write to CloudWatch.",
                "applies_to": [{
                    "regex": "Resource::arn:aws:logs:(.*):\\*$/g"
                }]
            }],
            apply_to_children=True
            )
        

        #IAM role to invoke Lambda 
        subscribed_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "logs:PutLogEvents"
            ],
            resources=[log_group.log_group_arn],
        ))

        #IAM Role to publish to SNS
        subscribed_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "sns:Publish"
            ],
            resources=[topic.topic_arn],
        ))

        #IAM Role to access KMS key
        subscribed_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            resources=[key.key_arn],
        ))
        
        #Add Lambda as a destination for log subscription
        log_group.add_subscription_filter(
            id="lambdaSubscription",
            destination=log_destinations.LambdaDestination(fn=subscribed_lambda),
            filter_pattern=logs.FilterPattern.all_terms("ERROR")
        )
        #Create an SQS dead letter queue
        dead_letter_queue = sqs.Queue(self, "DeadLetterQueue",
            enforce_ssl=True
        )
        
        #CDK Nag rule suppression for dlq 
        cdk_nag.NagSuppressions.add_resource_suppressions(dead_letter_queue, 
        [{"id":"AwsSolutions-SQS3", "reason":"This is a dead letter queue for the main queue."}])
        
        #Create an SQS queue
        main_queue = sqs.Queue(self, "MainQueue",
            enforce_ssl=True,
            dead_letter_queue = sqs.DeadLetterQueue(
                max_receive_count=2,
                queue=dead_letter_queue
        ))

        
        #Subscribe SQS queue to SNS topic
        topic.add_subscription(sns_sub.SqsSubscription(
            main_queue, 
            raw_message_delivery=True
        ))
        
        Aspects.of(self).add(cdk_nag.AwsSolutionsChecks())

        #Stack Outputs
        CfnOutput(self, "LOG GROUP NAME", 
            value=log_group.log_group_name
            )
        CfnOutput(self, "LOG STREAM NAME", 
            value=log_stream.log_stream_name
            )
        CfnOutput(self, "QUEUE URL", 
            value=main_queue.queue_url
            )

        

         
