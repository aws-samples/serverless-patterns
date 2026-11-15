package com.myorg;

import software.amazon.awscdk.*;
import software.amazon.awscdk.services.iam.*;
import software.amazon.awscdk.services.sns.*;
import software.amazon.awscdk.services.sns.subscriptions.EmailSubscription;
import software.amazon.awscdk.services.scheduler.*;
import software.constructs.Construct;

import java.util.List;

public class EventbridgeScheduleToSnsCdkJavaStack extends Stack {
    public EventbridgeScheduleToSnsCdkJavaStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public EventbridgeScheduleToSnsCdkJavaStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        // get email address from parameters or use a fake email address
        String email = (String)this.getNode().tryGetContext("email");
        if (email == null || email.isEmpty())
            email = "sample@example.com";

        // create topic
        Topic topic = Topic.Builder.create(this, "Scheduler Topic")
         .displayName("Scheduler topic")
         .build();

        // subscribe to the created topic, the provided email address should receive subscription confirmation email
        topic.addSubscription(new EmailSubscription(email));
        
        // create scheduler role
        Role scheduler_role = Role.Builder.create(this, "scheduler-role")
         .assumedBy(new ServicePrincipal("scheduler.amazonaws.com"))
         .description("Scheduler role for Scheduler Topic")
         .build();

        // create IAM policy for scheduler
        PolicyStatement scheduler_events_policy = PolicyStatement.Builder.create() 
         .actions(List.of("sns:Publish"))
         .resources(List.of(topic.getTopicArn()))
         .effect(Effect.ALLOW)
         .build();

        // Add IAM policy to scheduler role
        scheduler_role.addToPolicy(scheduler_events_policy);

        // Create schedule to publish a message to SNS topic every 5 minutes, 
        // the provided email should start receiving notification every 5 minutes if the above subscription is confirmed.
        CfnSchedule scheduler = CfnSchedule.Builder.create(this, "demo-schedule")
          .flexibleTimeWindow(CfnSchedule.FlexibleTimeWindowProperty.builder().mode("OFF").build())
          .scheduleExpression("rate(5 minute)")
          .target(CfnSchedule.TargetProperty.builder()
                    .arn(topic.getTopicArn())
                    .roleArn(scheduler_role.getRoleArn())
                    .input("This message was sent using EventBridge Scheduler!").build())
          .build();

        // Output
        CfnOutput.Builder.create(this,"Scheduler_ARN").value(scheduler.getAttrArn()).build();
        CfnOutput.Builder.create(this,"SNS_Topic_ARN").value(topic.getTopicArn()).build();
        
    }
}
