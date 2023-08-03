from aws_cdk import (
    aws_iam as iam,
    aws_iot as iot,
    aws_kinesisfirehose as kfh,
    aws_s3 as s3,
    aws_lambda as _lambda,
    Stack,
    CfnParameter,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions
)
from constructs import Construct
from aws_cdk.aws_s3_notifications import LambdaDestination

class PredictiveMaintenanceAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket for kinesis
        kinesis_bucket = s3.Bucket(self, 'kinesis_data')
        
        # Create an input S3 Bucket
        input_bucket = s3.Bucket(self, 'input_data')
        
        # Create an output S3 Bucket
        output_bucket = s3.Bucket(self, 'output_data')
        
        # Create a parameter for the SNS email
        email_parameter = CfnParameter(
            self,
            "EmailParameter",
            type="String",
            description="The email to subscribe to the SNS topic"
        )
        
    
        # Create IAM Role for Kinesis Firehose
        firehose_role = iam.Role(self, 'FirehoseRole', assumed_by=iam.ServicePrincipal('firehose.amazonaws.com'))
        kinesis_bucket.grant_write(firehose_role)
        kinesis_bucket.grant_read(firehose_role)

        # Create IAM Role for IoT Core Rule
        iot_role = iam.Role(self, 'IoTRuleRole', assumed_by=iam.ServicePrincipal('iot.amazonaws.com'))

        # Create a Kinesis Firehose Delivery Stream
        firehose = kfh.CfnDeliveryStream(
            self, 'MyFirehose',
            delivery_stream_name=f'{self.stack_name}FirehoseStream',  # Set the stream name explicitly
            delivery_stream_type='DirectPut',
            s3_destination_configuration={
                'bucketArn': kinesis_bucket.bucket_arn,
                'roleArn': firehose_role.role_arn,
            }
        )

        # Create an IoT Rule
        iot_rule = iot.CfnTopicRule(
            self, 'MyIoTRule',
            topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                actions=[
                    iot.CfnTopicRule.ActionProperty(
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name=firehose.delivery_stream_name,  # Use the stream name
                            role_arn=iot_role.role_arn
                        )
                    )
                ],
                sql =  "SELECT * from 'maintain_info'", # SQL query
                rule_disabled=False
            )
        )

        # Grant IoT Rule the necessary permissions to access the Kinesis Firehose
        iot_role.add_to_policy(iam.PolicyStatement(
            actions=['firehose:PutRecord', 'firehose:PutRecordBatch'],
            resources=[firehose.attr_arn]
        ))
        
        # Create the IAM role with the lambda execution policy
        lambda_role = iam.Role(
            self, "lambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
            ]
        )
        
        # Create a SNS Topic
        topic = sns.Topic(self, 'predictive_maintenance_app')
        
        # Create IAM Role for SNS
        sns_role = iam.Role(self, 'SNSRole', assumed_by=iam.ServicePrincipal('sns.amazonaws.com'))
        topic.grant_publish(sns_role)
        
        # Add the email subscription using the email parameter value
        topic.add_subscription(subscriptions.EmailSubscription(email_parameter.value_as_string))
        
        # Create a Lambda function for transformation 
        lambda_function1 = _lambda.Function(
            self, 'json2csv',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda_functions/lambda1'),  # load code from lambda1.py
            handler='lambda1.lambda_handler',
            role = lambda_role,
            environment={
            'S3_BUCKET_NAME': input_bucket.bucket_name,  # name of the S3 input_bucket as an environment variable
    }
        )
        
        # Create a Lambda function for SNS notification
        lambda_function2 = _lambda.Function(
            self, 'sns_notification',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda_functions/lambda2'),  # load code from lambda2.py
            handler='lambda2.lambda_handler',
            role = lambda_role,
            environment={
                'SNS_TOPIC_ARN': topic.topic_arn,  # name of the SNS topic as an environment variable
            } ) 

        
        # Set up the S3 kinesis_bucket to send an event to the Lambda function when a new object is created
        kinesis_bucket.add_event_notification(s3.EventType.OBJECT_CREATED, LambdaDestination(lambda_function1))

        # Set up the S3 output_bucket to send an event to the Lambda function when a new object is created
        output_bucket.add_event_notification(s3.EventType.OBJECT_CREATED, LambdaDestination(lambda_function2))
        
