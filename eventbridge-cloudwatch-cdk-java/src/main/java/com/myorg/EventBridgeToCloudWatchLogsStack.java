package com.myorg;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.RemovalPolicy;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.events.EventBus;
import software.amazon.awscdk.services.events.EventPattern;
import software.amazon.awscdk.services.events.Rule;
import software.amazon.awscdk.services.events.targets.CloudWatchLogGroup;
import software.amazon.awscdk.services.logs.LogGroup;
import software.amazon.awscdk.services.logs.RetentionDays;
import software.constructs.Construct;

import java.util.Collections;

public class EventBridgeToCloudWatchLogsStack extends Stack {
    public EventBridgeToCloudWatchLogsStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public EventBridgeToCloudWatchLogsStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        // CloudWatch Log Group
        LogGroup cloudWatchLogGroup = LogGroup.Builder.create(this, "EventBridgeCloudWatchLogs")
                .removalPolicy(RemovalPolicy.DESTROY)
                .retention(RetentionDays.ONE_DAY)
                .build();

        // EventBridge Event Bus
        EventBus eventBus = EventBus.Builder.create(this, "MyCloudWatchEventBus")
                .eventBusName("MyCloudWatchEventBus")
                .build();

        // EventBridge Rule
        Rule cloudWatchLogsRule = Rule.Builder.create(this, "cloudWatchLogsRule")
                .description("CloudWatch Logs Event Bus Rule")
                .eventPattern(EventPattern.builder()
                        .source(Collections.singletonList("cdk.myapp"))
                        .build())
                .eventBus(eventBus)
                .build();

        cloudWatchLogsRule.addTarget(new CloudWatchLogGroup(cloudWatchLogGroup));

        // CDK Outputs
        CfnOutput.Builder.create(this, "LogGroupName")
                .value(cloudWatchLogGroup.getLogGroupName())
                .description("CloudWatch Log Group Name")
                .build();
    }
}