package com.myorg;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.events.EventBus;
import software.amazon.awscdk.services.events.EventPattern;
import software.amazon.awscdk.services.events.Rule;
import software.amazon.awscdk.services.events.RuleTargetInput;
import software.amazon.awscdk.services.events.targets.KinesisFirehoseStream;
import software.amazon.awscdk.services.iam.Role;
import software.amazon.awscdk.services.iam.ServicePrincipal;
import software.amazon.awscdk.services.kinesisfirehose.CfnDeliveryStream;
import software.amazon.awscdk.services.kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty;
import software.amazon.awscdk.services.kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty;
import software.amazon.awscdk.services.kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty;
import software.amazon.awscdk.services.kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty;
import software.amazon.awscdk.services.kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty;
import software.amazon.awscdk.services.kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty;
import software.amazon.awscdk.services.kinesisfirehose.CfnDeliveryStream.ProcessorProperty;
import software.amazon.awscdk.services.s3.BlockPublicAccess;
import software.amazon.awscdk.services.s3.Bucket;
import software.constructs.Construct;

import java.util.Arrays;
import java.util.List;

public class EventBridgeFirehoseS3Stack extends Stack {
    public EventBridgeFirehoseS3Stack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public EventBridgeFirehoseS3Stack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        // Create EventBridge Bus
        EventBus eventBridgeBus = EventBus.Builder.create(this, "EventBridgeBus")
                .eventBusName("EventBridgeBus")
                .build();

        // Create EventBridge rule
        Rule eventBridgeRule = Rule.Builder.create(this, "EventBridgeRule")
                .eventPattern(EventPattern.builder()
                        .detailType(List.of("SaveToS3"))
                        .build())
                .eventBus(eventBridgeBus)
                .build();

        // Create target S3 bucket
        Bucket targetBucket = Bucket.Builder.create(this, "TargetBucket")
                .bucketName("your-bucket-name-897887") // Replace with your desired bucket name
                .versioned(true)
                .blockPublicAccess(BlockPublicAccess.BLOCK_ALL)
                .build();

        // Create role for Firehose Delivery Stream
        Role firehoseDeliveryStreamRole = Role.Builder.create(this, "FirehoseDeliveryStreamRole")
                .assumedBy(ServicePrincipal.Builder.create("firehose.amazonaws.com").build())
                .build();

        // Grant access to S3 bucket
        targetBucket.grantWrite(firehoseDeliveryStreamRole);

        // S3 Destination configuration
        var extendedS3DestinationConfiguration = ExtendedS3DestinationConfigurationProperty.builder()
                .bucketArn(targetBucket.getBucketArn())
                .roleArn(firehoseDeliveryStreamRole.getRoleArn())
                .dynamicPartitioningConfiguration(DynamicPartitioningConfigurationProperty.builder()
                        .enabled(true)
                        .build())
                .processingConfiguration(buildProcessingConfig())
                .prefix("!{partitionKeyFromQuery:DEPARTMENT}/")
                .bufferingHints(BufferingHintsProperty.builder()
                        .intervalInSeconds(60)
                        .sizeInMBs(64)
                        .build())
                .cloudWatchLoggingOptions(CloudWatchLoggingOptionsProperty.builder()
                        .enabled(true)
                        .logGroupName("FirehoseLogs")
                        .logStreamName("DliveryStreamLogs")
                        .build())
                .errorOutputPrefix("FirehoseFailures/")
                .build();

        // Create Firehose delivery stream
        CfnDeliveryStream cfnDeliveryStream = CfnDeliveryStream.Builder.create(this, "DeliveryStream")
                .deliveryStreamName("DeliveryStream")
                .deliveryStreamType("DirectPut")
                .extendedS3DestinationConfiguration(extendedS3DestinationConfiguration)
                .build();

        // Filter Detail field from EventBridge event
        eventBridgeRule.addTarget(KinesisFirehoseStream.Builder.create(cfnDeliveryStream)
                .message(RuleTargetInput.fromEventPath("$.detail"))
                .build());

        CfnOutput.Builder.create(this, "S3BucketName")
                .value(targetBucket.getBucketName())
                .build();
    }

    private ProcessingConfigurationProperty buildProcessingConfig() {
        return ProcessingConfigurationProperty.builder()
                .enabled(true)
                .processors(Arrays.asList(
                        metaDataExtractor(),
                        appendDelimiter()
                        ))
                .build();
    }

    private static ProcessorProperty appendDelimiter() {
        return ProcessorProperty.builder()
                .type("AppendDelimiterToRecord")
                .parameters(List.of(
                        ProcessorParameterProperty.builder()
                                .parameterName("Delimiter")
                                .parameterValue("\\n")
                                .build()))
                .build();
    }

    private static ProcessorProperty metaDataExtractor() {
        return ProcessorProperty.builder()
                .type("MetadataExtraction")
                .parameters(Arrays.asList(
                        ProcessorParameterProperty.builder()
                                .parameterName("MetadataExtractionQuery")
                                .parameterValue("{DEPARTMENT: with_entries(.key|=ascii_upcase) .DEPARTMENT|ascii_upcase}")
                                .build(),
                        ProcessorParameterProperty.builder()
                                .parameterName("JsonParsingEngine")
                                .parameterValue("JQ-1.6")
                                .build()))
                .build();
    }
}