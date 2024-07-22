from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_cloudwatch as cloudwatch,
    aws_cloudwatch_actions as cloudwatch_actions,
    aws_dynamodb as dynamodb,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    CfnOutput as cfnoutput 
)
from constructs import Construct

class DelayFifoQueueTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)    
        
        # create a dead letter queue called primary_queue_dlq
        primary_queue_dlq = sqs.Queue(self, "DelayFifoQueueDlq",
                                      visibility_timeout=Duration.seconds(60),
                                      fifo=True,
                                      content_based_deduplication=True
                                      )

        # create an initial primary SQS FIFO queue with a visibility timeout of 60 seconds
        primary_queue = sqs.Queue(self, "DelayFifoQueue",
                          visibility_timeout=Duration.seconds(60),
                          fifo=True,
                          content_based_deduplication=True,
                          dead_letter_queue=sqs.DeadLetterQueue(
                            max_receive_count=5,
                            queue=primary_queue_dlq
                          )
        )
        
        # create a downstream SQS FIFO queue with a visibility timeout of 60 seconds
        downstream_queue = sqs.Queue(self, "DelayFifoQueueDownstream",
                          visibility_timeout=Duration.seconds(60),
                          fifo=True,
                          content_based_deduplication=True
                          )
        
        # create a dynamodb table to store customer id and created timestamp
        customer_table = dynamodb.Table(self, "CustomerTable",
                                        table_name="DelayFifoQueueCustomerTable",
                                        partition_key=dynamodb.Attribute(name="customer_id", type=dynamodb.AttributeType.STRING),
                                        time_to_live_attribute="ttl"
                                        )
        
        # create a Lambda function to process messages from the queue
        process_queue_function = lambda_.Function(self, "ProcessMessageLambda",
                                                    runtime=lambda_.Runtime.PYTHON_3_9,
                                                    code=lambda_.Code.from_asset("lambda"),
                                                    handler="process_message.handler",
                                                    environment={
                                                        "QUEUE_URL": downstream_queue.queue_url,
                                                        "TABLE_NAME": customer_table.table_name
                                                    })

        # create an SNS topic to send notifications when primary_queue_dlq is not empty
        dlq_size_sns_topic = sns.Topic(self, "PrimaryQueueDqlSizeAlertTopic")
        dlq_size_sns_topic.add_subscription(subscriptions.EmailSubscription("notification_address@email.com"))

        # create a CloudWatch alarm if primary_queue_dlq is not empty
        dlq_size_alarm = cloudwatch.Alarm(self, "PrimaryQueueDqlSizeAlert",
                                            metric=cloudwatch.Metric(metric_name="ApproximateNumberOfMessagesVisible",
                                                                    namespace="AWS/SQS",
                                                                    dimensions_map={
                                                                        "QueueName": primary_queue_dlq.queue_name
                                                                        },
                                                                    statistic="Sum",
                                                                    period=Duration.seconds(60)
                                                                    ),
                                            evaluation_periods=1,
                                            threshold=0,
                                            comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
                                            treat_missing_data=cloudwatch.TreatMissingData.NOT_BREACHING
                                            )
        dlq_size_alarm.add_alarm_action(
            cloudwatch_actions.SnsAction(
                topic = dlq_size_sns_topic
            )
        )


        # create Lambda execution role that has access to receive messages from primary_queue queue
        process_queue_function.add_to_role_policy(iam.PolicyStatement(
            actions=["sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueAttributes", "sqs:GetQueueUrl"],
            resources=[primary_queue.queue_arn]
        ))

        # add to Lambda execution role policy to send messages to the downstream_queue queue
        process_queue_function.add_to_role_policy(iam.PolicyStatement(
            actions=["sqs:SendMessage"],
            resources=[downstream_queue.queue_arn]
        ))
                
        lambda_.EventSourceMapping(self, "ProcessMessageLambdaEventSourceMapping",
                                    event_source_arn=primary_queue.queue_arn,
                                    target=process_queue_function,
                                    batch_size=10,
                                    report_batch_item_failures=True
        )
      
        # give permissions for the  function to read and write to the dynamodb table
        customer_table.grant_read_write_data(process_queue_function)

        cfnoutput(self, "DelayFifoQueueURL", value=primary_queue.queue_url)
