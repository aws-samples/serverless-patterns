package com.myorg;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.CfnOutputProps;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.events.EventBus;
import software.amazon.awscdk.services.iam.Effect;
import software.amazon.awscdk.services.iam.PolicyDocument;
import software.amazon.awscdk.services.iam.PolicyStatement;
import software.amazon.awscdk.services.iam.Role;
import software.amazon.awscdk.services.iam.ServicePrincipal;
import software.amazon.awscdk.services.pipes.CfnPipe;
import software.amazon.awscdk.services.pipes.CfnPipe.PipeSourceParametersProperty;
import software.amazon.awscdk.services.pipes.CfnPipe.PipeSourceSqsQueueParametersProperty;
import software.amazon.awscdk.services.pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty;
import software.amazon.awscdk.services.pipes.CfnPipe.PipeTargetParametersProperty;
import software.amazon.awscdk.services.sqs.Queue;
import software.constructs.Construct;

import java.util.List;
import java.util.Map;

public class SqsToEventBridgeStack extends Stack {
    public SqsToEventBridgeStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public SqsToEventBridgeStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        Queue source = Queue.Builder.create(this, "SourceSQSQueue").build();
        EventBus target = EventBus.Builder.create(this, "TargetEventBus").build();


        PolicyDocument sourcePolicy = PolicyDocument.Builder.create()
                .statements(List.of(
                        PolicyStatement.Builder.create()
                                .resources(List.of(source.getQueueArn()))
                                .actions(List.of(
                                        "sqs:ReceiveMessage",
                                        "sqs:DeleteMessage",
                                        "sqs:GetQueueAttributes"))
                                .effect(Effect.ALLOW)
                                .build()
                ))
                .build();

        PolicyDocument targetPolicy = PolicyDocument.Builder.create()
                .statements(List.of(
                        PolicyStatement.Builder.create()
                                .resources(List.of(target.getEventBusArn()))
                                .actions(List.of("events:PutEvents"))
                                .effect(Effect.ALLOW)
                                .build()
                ))
                .build();

        Role pipeRole = Role.Builder.create(this, "PipeRole")
                .assumedBy(ServicePrincipal.Builder.create("pipes.amazonaws.com").build())
                .inlinePolicies(Map.of(
                        "SourcePolicy", sourcePolicy,
                        "TargetPolicy", targetPolicy
                ))
                .build();

        PipeSourceSqsQueueParametersProperty sqsQueueParameters = PipeSourceSqsQueueParametersProperty.builder()
                .batchSize(5)
                .maximumBatchingWindowInSeconds(120)
                .build();

        PipeSourceParametersProperty sourceParameters = PipeSourceParametersProperty.builder()
                        .sqsQueueParameters(sqsQueueParameters)
                        .build();

        PipeTargetEventBridgeEventBusParametersProperty eventBridgeParams =
                PipeTargetEventBridgeEventBusParametersProperty.builder()
                        .source("myapp.orders")
                        .detailType("OrderCreated")
                        .build();

        PipeTargetParametersProperty targetParameters =
                PipeTargetParametersProperty.builder()
                        .eventBridgeEventBusParameters(eventBridgeParams)
                        .inputTemplate("{\"message\": \"<$.body>\"}")
                        .build();

        CfnPipe pipe = CfnPipe.Builder.create(this, "Pipe")
                .roleArn(pipeRole.getRoleArn())
                .source(source.getQueueArn())
                .sourceParameters(sourceParameters)
                .target(target.getEventBusArn())
                .targetParameters(targetParameters)
                .build();

        Map<String, String> outputProps = Map.of(
                "ExportName", "QueueName",
                "Value", source.getQueueUrl()
        );

        new CfnOutput(this, "QueueNameOutput", CfnOutputProps.builder()
                .key("QueueUrl")
                .value(source.getQueueUrl())
                .build());
    }
}