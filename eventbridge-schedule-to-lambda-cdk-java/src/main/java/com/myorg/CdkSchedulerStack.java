package com.myorg;

import software.amazon.awscdk.services.iam.*;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.scheduler.CfnSchedule;
import software.amazon.awscdk.services.scheduler.CfnScheduleGroup;
import software.constructs.Construct;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.Duration;
import software.amazon.awscdk.services.lambda.Runtime;
import java.util.*;

public class CdkSchedulerStack extends Stack {
    public CdkSchedulerStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public CdkSchedulerStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        // Create our basic function
        Function lambdaFn = Function.Builder.create(this,"ScheduledFunction")
                .runtime(Runtime.JAVA_11)
                .memorySize(256)
                .handler("com.myorg.SchedulerHandler")
                .timeout(Duration.seconds(30))
                .code(Code.fromAsset("target/cdk-scheduler-0.1.jar"))
                .build();

        // Create Role
        Role lambdaRole = Role.Builder.create(this, "Role")
                .assumedBy(new ServicePrincipal("scheduler.amazonaws.com"))
                .build();
        List<Role> roles = new ArrayList<Role>();
        roles.add(lambdaRole);

        // Create Policy
        PolicyStatement statement = PolicyStatement.Builder.create()
                .effect(Effect.ALLOW)
                .actions(Arrays.asList("lambda:InvokeFunction"))
                .resources(Arrays.asList(lambdaFn.getFunctionArn()))
                .build();
        Policy policy = Policy.Builder.create(this, "Policy")
                .roles(roles)
                .policyName("ScheduleToInvokeLambdas")
                .statements(Arrays.asList(statement))
                .build();

        CfnScheduleGroup scheduleGroup = CfnScheduleGroup.Builder.create(this, "scheduleGroup")
                .name("lambdaSchedules")
                .build();

        // Create rate based schedule every 5 minutes using custom group name
        CfnSchedule.Builder.create(this, "lambdaSchedule")
            // no flexible time window for this schedule
            .flexibleTimeWindow(CfnSchedule.FlexibleTimeWindowProperty.builder()
                .mode("OFF").build())
            .groupName(scheduleGroup.getName())
            .scheduleExpression("rate(5 minute)")
            //create target builder and set Lambda ARN and role created above ARN
            .target(CfnSchedule.TargetProperty.builder()
                .arn(lambdaFn.getFunctionArn())
                .roleArn(lambdaRole.getRoleArn())
                .build())
            .build();

    }

}
