package com.myorg;

import software.constructs.Construct;

import java.util.Arrays;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.sqs.Queue;
import software.amazon.awscdk.services.iam.*;
import software.amazon.awscdk.services.scheduler.CfnSchedule;

public class EventBridgeScheduleToSqsCdkStack extends Stack {
        public EventBridgeScheduleToSqsCdkStack(final Construct scope, final String id) {
                this(scope, id, null);
        }

        public EventBridgeScheduleToSqsCdkStack(final Construct scope, final String id, final StackProps props) {
                super(scope, id, props);

                // Create the SQS queue
                Queue SqsQueue = Queue.Builder.create(this, "SQS-Queue")
                                .build();

                // Create IAM role for the scheduler to assume
                Role schedulerRole = Role.Builder.create(this, "Scheduler-Role")
                                .assumedBy(new ServicePrincipal("scheduler.amazonaws.com"))
                                .build();

                // Create IAM statement
                PolicyStatement sqsSendMessageStatement = PolicyStatement.Builder.create()
                                .effect(Effect.ALLOW)
                                .actions(Arrays.asList("sqs:SendMessage"))
                                .resources(Arrays.asList(SqsQueue.getQueueArn()))
                                .build();

                // Add statement to IAM role
                schedulerRole.addToPolicy(sqsSendMessageStatement);

                // Creates target for Schedule
                CfnSchedule.TargetProperty sqsTarget = CfnSchedule.TargetProperty.builder()
                                .arn(SqsQueue.getQueueArn())
                                .roleArn(schedulerRole.getRoleArn())
                                .input("This message was sent using EventBridge Scheduler!")
                                .build();

                // Creates EventBridge Schedule to send a message to SQS every 5 minutes
                CfnSchedule sqsSchedule = CfnSchedule.Builder.create(this, "SQS-Scheduler")
                                .flexibleTimeWindow(CfnSchedule.FlexibleTimeWindowProperty.builder()
                                                .mode("OFF")
                                                .build())
                                .scheduleExpression("rate(5 minute)")
                                .target(sqsTarget)
                                .build();

                // Outputs
                CfnOutput.Builder.create(this, "ScheduleName")
                                .description("Name of the EventBridge schedule")
                                .value(sqsSchedule.getRef())
                                .build();

                CfnOutput.Builder.create(this, "SqsQueueName")
                                .description("Name of the SQS Queue")
                                .value(SqsQueue.getQueueName())
                                .build();
        }
}
