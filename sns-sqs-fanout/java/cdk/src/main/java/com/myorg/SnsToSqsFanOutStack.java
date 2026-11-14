package com.myorg;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.sns.Filter;
import software.amazon.awscdk.services.sns.StringConditions;
import software.amazon.awscdk.services.sns.SubscriptionFilter;
import software.amazon.awscdk.services.sns.Topic;
import software.amazon.awscdk.services.sns.subscriptions.SqsSubscription;
import software.amazon.awscdk.services.sns.subscriptions.SqsSubscriptionProps;
import software.amazon.awscdk.services.sqs.Queue;
import software.constructs.Construct;

import java.util.List;
import java.util.Map;

public class SnsToSqsFanOutStack extends Stack {
    public SnsToSqsFanOutStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public SnsToSqsFanOutStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        Topic topic = Topic.Builder.create(this, "MyTopic")
                .topicName("my-topic")
                .build();

        Queue queue1 = Queue.Builder.create(this, "Queue1")
                .queueName("queue1")
                .build();

        Queue queue2 = Queue.Builder.create(this, "Queue2")
                .queueName("queue2")
                .build();

        Queue queue3 = Queue.Builder.create(this, "Queue3")
                .queueName("queue3")
                .build();

        filterByEventType("order_placed");

        topic.addSubscription(new SqsSubscription(queue1));
        topic.addSubscription(new SqsSubscription(queue2, filterByEventType("order_placed")));
        topic.addSubscription(new SqsSubscription(queue3, filterByEventType("order_shipped")));

        CfnOutput.Builder.create(this, "SnsArn")
                .key("SnsArn")
                .value(topic.getTopicArn())
                .build();
    }

    private static SqsSubscriptionProps filterByEventType(String type) {
        return SqsSubscriptionProps.builder()
                .filterPolicyWithMessageBody(Map.of(
                        "event", Filter.filter(SubscriptionFilter.stringFilter(StringConditions.builder()
                                .allowlist(List.of(type))
                                .build()))
                )).build();

    }
}
