package com.myorg;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.Duration;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.iam.Effect;
import software.amazon.awscdk.services.iam.PolicyDocument;
import software.amazon.awscdk.services.iam.PolicyStatement;
import software.amazon.awscdk.services.iam.Role;
import software.amazon.awscdk.services.iam.ServicePrincipal;
import software.amazon.awscdk.services.pipes.CfnPipe;
import software.amazon.awscdk.services.sqs.Queue;
import software.amazon.awscdk.services.stepfunctions.*;
import software.constructs.Construct;

import java.util.Arrays;
import java.util.List;

public class SqsSfnStack extends Stack {
    public SqsSfnStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public SqsSfnStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        Queue source = Queue.Builder.create(this, "SourceSQSQueue").build();


        var mapState = Map.Builder.create(this, "TargetStepFunctionDefintion")
                .stateName("LoopMessages")
                .inputPath(JsonPath.getEntirePayload())
                .build();

        mapState.itemProcessor(Wait.Builder.create(this, "WaitState")
                        .time(WaitTime.duration(Duration.seconds(10)))
                        .build());

        StateMachine stepFunction = StateMachine.Builder.create(this, "TargetStepFunction")
                .definition(mapState)
                .stateMachineType(StateMachineType.STANDARD)
                .build();

        PolicyStatement sourcePolicy = PolicyStatement.Builder.create()
                .resources(List.of(source.getQueueArn()))
                .actions(Arrays.asList("sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueAttributes"))
                .effect(Effect.ALLOW)
                .build();

        PolicyStatement targetPolicy = PolicyStatement.Builder.create()
                .resources(List.of(stepFunction.getStateMachineArn()))
                .actions(List.of("states:StartExecution"))
                .effect(Effect.ALLOW)
                .build();

        java.util.Map<String, PolicyDocument> policies = java.util.Map.of(
                "SourcePolicy", PolicyDocument.Builder.create().statements(List.of(sourcePolicy)).build(),
                "TargetPolicy", PolicyDocument.Builder.create().statements(List.of(targetPolicy)).build()
        );

        Role pipeRole = Role.Builder.create(this, "PipeRole")
                .assumedBy(ServicePrincipal.Builder.create("pipes.amazonaws.com").build())
                .inlinePolicies(policies)
                .build();

        CfnPipe.PipeSourceSqsQueueParametersProperty sqsQueueParameters = CfnPipe.PipeSourceSqsQueueParametersProperty.builder()
                .batchSize(5)
                .maximumBatchingWindowInSeconds(120)
                .build();

        CfnPipe.PipeSourceParametersProperty sourceParameters = CfnPipe.PipeSourceParametersProperty.builder()
                .sqsQueueParameters(sqsQueueParameters)
                .build();

        CfnPipe.PipeTargetStateMachineParametersProperty stateMachineParameters = CfnPipe.PipeTargetStateMachineParametersProperty.builder()
                .invocationType("FIRE_AND_FORGET")
                .build();

        CfnPipe.PipeTargetParametersProperty targetParameters = CfnPipe.PipeTargetParametersProperty.builder()
                .stepFunctionStateMachineParameters(stateMachineParameters)
                .build();

        CfnPipe.Builder.create(this, "Pipe")
                .roleArn(pipeRole.getRoleArn())
                .source(source.getQueueArn())
                .sourceParameters(sourceParameters)
                .target(stepFunction.getStateMachineArn())
                .targetParameters(targetParameters)
                .build();

        // Add output for the queue name
        CfnOutput outputQueueName = CfnOutput.Builder.create(this, "QueueUrlOutput")
                .exportName("QueueUrlOutput")
                .value(source.getQueueName())
                .build();
    }
}
