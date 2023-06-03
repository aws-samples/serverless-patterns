package com.myorg;

import software.amazon.awscdk.*;
import software.amazon.awscdk.services.iam.*;
import software.amazon.awscdk.services.ecs.*;
import software.amazon.awscdk.services.ec2.*;
import software.amazon.awscdk.services.scheduler.*;
import software.amazon.awscdk.services.events.*;
import software.amazon.awscdk.services.events.targets.*;
import software.constructs.Construct;

import java.util.List;

public class EventbridgeScheduleEcsCdkJavaStack extends Stack {
    public EventbridgeScheduleEcsCdkJavaStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public EventbridgeScheduleEcsCdkJavaStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        // Create a VPC for ECS Cluster
        Vpc vpc = Vpc.Builder.create(this, "TheVPC")
         .cidr("10.10.0.0/24")
         .build();

        // Create ECS Cluster
        Cluster cluster = Cluster.Builder.create(this, "Cluster")
         .vpc(vpc)
         .build();

        // Create a Fargate Task Definition
        FargateTaskDefinition fargateTaskDefinition = FargateTaskDefinition.Builder.create(this, "TaskDef")
         .memoryLimitMiB(512)
         .cpu(256)
         .build();

         // Create a container definition with sample image
         ContainerDefinition container = fargateTaskDefinition.addContainer("WebContainer", ContainerDefinitionOptions.builder()
         .image(ContainerImage.fromRegistry("amazon/amazon-ecs-sample"))
         .build());

        // Create a scheduler role
        Role scheduler_role = Role.Builder.create(this, "scheduler-role")
         .assumedBy(new ServicePrincipal("scheduler.amazonaws.com"))
         .description("Scheduler role for ECS RunTask")
         .build();

        // Create IAM Policy for scheduler role
        PolicyStatement scheduler_events_policy = PolicyStatement.Builder.create() 
         .actions(List.of("ecs:RunTask", "iam:PassRole"))
         .effect(Effect.ALLOW)
         .resources(List.of("*"))
         .build();

        // Add the IAM policy to the scheduler role
        scheduler_role.addToPolicy(scheduler_events_policy);

        // Create an EventBridge Scheduler to run a task in ECS cluster and in private subnets every 5 minutes
        CfnSchedule scheduler = CfnSchedule.Builder.create(this, "demo-schedule")
          .flexibleTimeWindow(CfnSchedule.FlexibleTimeWindowProperty.builder().mode("OFF").build())
          .scheduleExpression("rate(15 minute)")
          .target(CfnSchedule.TargetProperty.builder()
                    .arn(cluster.getClusterArn())
                    .roleArn(scheduler_role.getRoleArn())
                    .ecsParameters(CfnSchedule.EcsParametersProperty.builder()
                                     .taskDefinitionArn(fargateTaskDefinition.getTaskDefinitionArn())
                                     .taskCount(1)
                                     .launchType("FARGATE")
                                     .networkConfiguration(CfnSchedule.NetworkConfigurationProperty.builder()
                                                             .awsvpcConfiguration(CfnSchedule.AwsVpcConfigurationProperty.builder()
                                                                                    .subnets(vpc.selectSubnets(SubnetSelection.builder().subnetType(SubnetType.PRIVATE_WITH_EGRESS).build()).getSubnetIds())
                                                                                    .build())      
                                                             .build())
                                     .build())
                    .build())
          .build();

        // Output
        CfnOutput.Builder.create(this,"Scheduler_ARN").value(scheduler.getAttrArn()).build();
        CfnOutput.Builder.create(this,"ECS_Cluster").value(cluster.getClusterArn()).build();
    }
}
