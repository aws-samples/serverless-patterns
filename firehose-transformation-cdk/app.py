from xml.etree.ElementTree import ProcessingInstruction
from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_iam as iam,
    aws_s3 as s3,
    aws_kms as kms,
    aws_events as events,
    aws_kinesisfirehose as firehose,
    aws_events_targets as targets,
    aws_lambda as lambda_,
    Duration
)
from constructs import Construct

class FirehoseTransformationCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = iam.Role(scope=self, id='cdk-lambda-role',
            assumed_by =iam.ServicePrincipal('lambda.amazonaws.com'),
            role_name='cdk-lambda-role',
            managed_policies=[
            iam.ManagedPolicy.from_aws_managed_policy_name(
                'service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        lambda_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=[
                "firehose:DescribeDeliveryStream",
                "firehose:PutRecord",
                "firehose:StartDeliveryStreamEncryption",
                "firehose:PutRecordBatch",
                "firehose:ListDeliveryStreams"
            ]
        ))

        #tranformation Lambda function
        transformation_lambda = lambda_.Function(
            self, 
            id='TransformationLambdaCdk',
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset('src'),
            handler='lambda_function.lambda_handler',
            role=lambda_role,
            timeout=Duration.seconds(90)
        )

        #KMS Key to encrypt firehose delivery stream
        firehose_kms_key = kms.Key(self, 'FirehoseKMSKey')

        #S3 bucket to be used as firehose destination
        destination_bucket = s3.Bucket(
            self,
            "Destination-Bucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            encryption=s3.BucketEncryption.KMS
        )

        #firehose role
        firehose_role = iam.Role(self, "firehose-role", assumed_by=iam.ServicePrincipal("firehose.amazonaws.com"))
        firehose_role_arn = firehose_role.role_arn

        #add s3 permissions to role
        firehose_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[destination_bucket.bucket_arn, destination_bucket.bucket_arn + "/*"],
            actions=["s3:AbortMultipartUpload",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:PutObject"],
        ))
        
        #add KMS permission to Firehose role 
        firehose_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[firehose_kms_key.key_arn],
            actions=["kms:Decrypt",
               "kms:GenerateDataKey"],
        ))

        #add Lambda permission to Firehose role 
        firehose_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[transformation_lambda.function_arn],
            actions=["lambda:InvokeFunction", 
               "lambda:GetFunctionConfiguration"],
        ))

        #Kinesis Firehose
        firehose_delivery_stream = firehose.CfnDeliveryStream(
            self, "firehose-delivery-stream",
            extended_s3_destination_configuration=firehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(
                bucket_arn=destination_bucket.bucket_arn,
                buffering_hints=firehose.CfnDeliveryStream.BufferingHintsProperty(
                    interval_in_seconds=60
                ),
                encryption_configuration=firehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                    kms_encryption_config=firehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                        awskms_key_arn=firehose_kms_key.key_arn
                    )
                ),
                compression_format="UNCOMPRESSED",
                role_arn=firehose_role_arn,
                processing_configuration=firehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                    enabled=True,
                    processors=[firehose.CfnDeliveryStream.ProcessorProperty(
                        type="Lambda",

                        # the properties below are optional
                        parameters=[firehose.CfnDeliveryStream.ProcessorParameterProperty(
                        parameter_name="LambdaArn",
                        parameter_value=transformation_lambda.function_arn
                        )]
                    )]
                )   
            )
        )

        #Output
        CfnOutput(self, "S3 Destination Bucket Name", description="S3 Destination Bucket Name", value=destination_bucket.bucket_name)
        CfnOutput(self, "Kinesis Firehose Delivery Stream Name", description="Kinesis Firehose Delivery Stream Name", value=firehose_delivery_stream.delivery_stream_name)


app = App()
FirehoseTransformationCdkStack(app, "FirehoseTransformationCdkStack")
app.synth()

