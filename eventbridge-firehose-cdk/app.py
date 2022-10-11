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
    aws_logs as logs
)
from constructs import Construct


class EventBridgeKinesisFirehoseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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

        
        #add KMS permission to role
        firehose_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=[firehose_kms_key.key_arn],
            actions=["kms:Decrypt",
               "kms:GenerateDataKey"],
        ))

        #Kinesis Firehose
        firehose_delivery_stream = firehose.CfnDeliveryStream(
            self, "firehose-delivery-stream",
            s3_destination_configuration=firehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
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
                role_arn=firehose_role_arn
            )
        )

        # Custom EventBridge Bus
        custom_bus = events.EventBus(
            self, "bus",
            event_bus_name="test-bus-cdk"
        )

        # EventBridge Rule
        rule = events.Rule(
            self, "rule",
            event_bus=custom_bus,

        )

        # Event Pattern to filter events
        rule.add_event_pattern(
            source=["my-application"],
            detail_type=["message"]
        )

        # Kinesis Firehose as target for Eventbridge Rue
        rule.add_target(targets.KinesisFirehoseStream(firehose_delivery_stream))

        #Output
        CfnOutput(self, "S3 Destination Bucket Name", description="S3 Destination Bucket Name", value=destination_bucket.bucket_name)


       
app = App()
EventBridgeKinesisFirehoseStack(app, "EventBridgeKinesisFirehoseExample")
app.synth()

