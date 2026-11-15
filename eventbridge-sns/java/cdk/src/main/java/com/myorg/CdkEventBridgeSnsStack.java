package com.myorg;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.CfnOutputProps;
import software.amazon.awscdk.services.events.*;
import software.amazon.awscdk.services.events.targets.SnsTopic;
import software.amazon.awscdk.services.sns.Topic;
import software.constructs.Construct;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;

import java.util.List;

public class CdkEventBridgeSnsStack extends Stack {
    public CdkEventBridgeSnsStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public CdkEventBridgeSnsStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        Topic mySnsTopic = new Topic(this, "MySnsTopic");

        EventBus eventBus = new EventBus(this, "MySnsEventBus", EventBusProps.builder()
                .eventBusName("MySnsEventBus")
                .build());


        Rule rule = new Rule(this, "MySnsRule", RuleProps.builder()
                .description("SNS Event Bus Rule")
                .eventPattern(EventPattern.builder()
                        .source(List.of("cdk.myapp"))
                        .build())
                .eventBus(eventBus)
                .build());

        rule.addTarget(new SnsTopic(mySnsTopic));

        new CfnOutput(this, "SnsTopicName", CfnOutputProps.builder()
                .value(mySnsTopic.getTopicName())
                .description("SNS Topic name")
                .build());

        new CfnOutput(this, "SnsTopicArn", CfnOutputProps.builder()
                .value(mySnsTopic.getTopicName())
                .description("SNS Topic ARN")
                .build());
    }
}
