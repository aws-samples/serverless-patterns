package com.myorg;

import software.amazon.awscdk.*;
import software.amazon.awscdk.services.events.EventBus;
import software.amazon.awscdk.services.events.EventPattern;
import software.amazon.awscdk.services.events.Rule;
import software.amazon.awscdk.services.events.targets.CloudWatchLogGroup;
import software.amazon.awscdk.services.logs.LogGroup;
import software.amazon.awscdk.services.logs.RetentionDays;
import software.amazon.awscdk.services.s3.BlockPublicAccess;
import software.amazon.awscdk.services.s3.Bucket;
import software.amazon.awscdk.services.s3.EventType;
import software.amazon.awscdk.services.s3.notifications.SqsDestination;
import software.amazon.awscdk.services.sqs.Queue;
import software.constructs.Construct;

import java.util.Collections;

public class S3ToSqsStack extends Stack {
    public S3ToSqsStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public S3ToSqsStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        // Create an S3 bucket
        Bucket bucket = Bucket.Builder.create(this, "MyBucket")
                .removalPolicy(RemovalPolicy.DESTROY)
                .blockPublicAccess(BlockPublicAccess.BLOCK_ALL)
                .build();

        // Create an SQS queue
        Queue queue = Queue.Builder.create(this, "MyQueue")
                .visibilityTimeout(Duration.seconds(300))
                .build();

        // Add an S3 bucket notification to the queue
        bucket.addEventNotification(EventType.OBJECT_CREATED, new SqsDestination(queue));
    }
}