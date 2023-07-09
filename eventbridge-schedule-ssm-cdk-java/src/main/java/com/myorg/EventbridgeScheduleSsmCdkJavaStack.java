package com.myorg;

import software.amazon.awscdk.*;
import software.amazon.awscdk.services.iam.*;
import software.amazon.awscdk.services.ec2.*;
import software.amazon.awscdk.services.scheduler.*;
import software.amazon.awscdk.services.ssm.*;
import software.constructs.Construct;

import java.util.List;
import java.util.HashMap;
import java.util.Arrays;

public class EventbridgeScheduleSsmCdkJavaStack extends Stack {
    public EventbridgeScheduleSsmCdkJavaStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public EventbridgeScheduleSsmCdkJavaStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        // Create a VPC for Security Group
        Vpc vpc = Vpc.Builder.create(this, "TheVPC")
         .cidr("10.10.0.0/24")
         .build();

        // Create Security Group with SSH and RDP public access 
        CfnSecurityGroup securityGroup = CfnSecurityGroup.Builder.create(this, "TestingSecurityGroup")
         .groupDescription("Security Group for State Manager Association Demo")
         .groupName("TestingSecurityGroup")
         .securityGroupEgress(List.of(CfnSecurityGroup.EgressProperty.builder()
                 .ipProtocol("-1")
                 .cidrIp("0.0.0.0/0")
                 .build()))
         .securityGroupIngress(List.of(CfnSecurityGroup.IngressProperty.builder()
                 .ipProtocol("TCP")
                 .cidrIp("0.0.0.0/0")
                 .fromPort(3389)
                 .toPort(3389)
                 .build(),
                  CfnSecurityGroup.IngressProperty.builder()
                 .ipProtocol("TCP")
                 .cidrIp("0.0.0.0/0")
                 .fromPort(22)
                 .toPort(22)
                 .build()))
         .vpcId(vpc.getVpcId())
         .build();

        // Create IAM role for Systems Manager Automation
        Role automationRole = Role.Builder.create(this, "AutomationRole")
         .assumedBy(new ServicePrincipal("ssm.amazonaws.com"))
         .description("Scheduler role for Systems Manager Automation")
         .build();

        // Create IAM Policy for the role of Systems Manager Automation
        PolicyStatement automationPolicy = PolicyStatement.Builder.create() 
         .actions(List.of("ec2:RevokeSecurityGroupIngress"))
         .effect(Effect.ALLOW)
         .resources(List.of("arn:aws:ec2:*:"+ Aws.ACCOUNT_ID + ":security-group/"+securityGroup.getAttrGroupId()))
         .build();

        // Attach IAM Policy to the Automation IAM Role
        automationRole.addToPolicy(automationPolicy);

        // Prepare State Manager Association parameters
        HashMap<String, Object> associationParam = new HashMap<>();
        associationParam.put("AutomationAssumeRole", Arrays.asList(automationRole.getRoleArn()));
        associationParam.put("GroupId", Arrays.asList(securityGroup.getAttrGroupId()));

        // Create a State Manager Association 
        CfnAssociation association = CfnAssociation.Builder.create(this, "DemoAssociation")
         .name("AWS-DisablePublicAccessForSecurityGroup")
         .associationName("DemoAssociation")
         .parameters(associationParam)
         .build();

        // Create IAM Role for EventBridge Scheduler
        Role schedulerRole = Role.Builder.create(this, "SchedulerRole")
         .assumedBy(new ServicePrincipal("scheduler.amazonaws.com"))
         .description("Role for EventBridge Scheduler")
         .build();

        // Create IAM Policy for EventBridge Scheduler role
        PolicyStatement schedulerPolicy = PolicyStatement.Builder.create() 
         .actions(List.of("ssm:StartAssociationsOnce"))
         .effect(Effect.ALLOW)
         .resources(List.of("arn:aws:ssm:*:"+ Aws.ACCOUNT_ID + ":association/" + association.getAttrAssociationId()))
         .build();

        // Attach IAM Policy to Scheduler Role
        schedulerRole.addToPolicy(schedulerPolicy);

        // Create an EventBridge Scheduler with Universal Target
        CfnSchedule scheduler = CfnSchedule.Builder.create(this, "DemoSchedule")
          .flexibleTimeWindow(CfnSchedule.FlexibleTimeWindowProperty.builder().mode("OFF").build())
          .scheduleExpression("rate(5 minute)")
          .target(CfnSchedule.TargetProperty.builder()
                    .arn("arn:aws:scheduler:::aws-sdk:ssm:startAssociationsOnce")
                    .roleArn(schedulerRole.getRoleArn())
                    .input("{\"AssociationIds\": [\""+association.getAttrAssociationId()+"\"]}").build())
          .build();

        // Output
        CfnOutput.Builder.create(this,"Association_ID").value(association.getAttrAssociationId()).build();
        CfnOutput.Builder.create(this,"Scheduler_Role").value(schedulerRole.getRoleArn()).build();
    }
}
