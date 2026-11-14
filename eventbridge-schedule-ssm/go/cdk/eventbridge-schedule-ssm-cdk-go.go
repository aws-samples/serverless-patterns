package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsec2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsiam"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsscheduler"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsssm"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type EventbridgeScheduleSsmCdkGoStackProps struct {
	awscdk.StackProps
}

func NewEventbridgeScheduleSsmCdkGoStack(scope constructs.Construct, id string, props *EventbridgeScheduleSsmCdkGoStackProps) awscdk.Stack {
	var sprops awscdk.StackProps
	if props != nil {
		sprops = props.StackProps
	}
	stack := awscdk.NewStack(scope, &id, &sprops)

	// Create a VPC for Security Group
	vpc := awsec2.NewVpc(stack, jsii.String("TheVPC"), &awsec2.VpcProps{
		Cidr: jsii.String("10.10.0.0/24"),
	})

	securityGroup := awsec2.NewCfnSecurityGroup(stack, jsii.String("TestingSecurityGroup"), &awsec2.CfnSecurityGroupProps{
		GroupDescription: jsii.String("Security Group for State Manager Association Demo"),
		GroupName:        jsii.String("TestingSecurityGroup"),
		SecurityGroupEgress: []interface{}{
			&awsec2.CfnSecurityGroup_EgressProperty{
				IpProtocol: jsii.String("-1"),
				CidrIp:     jsii.String("0.0.0.0/0"),
			},
		},
		SecurityGroupIngress: []interface{}{
			&awsec2.CfnSecurityGroup_IngressProperty{
				IpProtocol: jsii.String("TCP"),
				CidrIp:     jsii.String("0.0.0.0/0"),
				FromPort:   jsii.Number(22),
				ToPort:     jsii.Number(22),
			},
			&awsec2.CfnSecurityGroup_IngressProperty{
				IpProtocol: jsii.String("TCP"),
				CidrIp:     jsii.String("0.0.0.0/0"),
				FromPort:   jsii.Number(3389),
				ToPort:     jsii.Number(3389),
			},
		},
		VpcId: vpc.VpcId(),
	})

	// Create an Automation role
	automationRole := awsiam.NewRole(stack, jsii.String("automation-role"), &awsiam.RoleProps{
		AssumedBy:   awsiam.NewServicePrincipal(jsii.String("ssm.amazonaws.com"), &awsiam.ServicePrincipalOpts{}),
		Description: jsii.String("Automation role for revoking the public SSH and RDP access in security group"),
	})

	// prepare Security Group ARN
	securityGroupArn := "arn:aws:ec2:*:" + *(awscdk.Aws_ACCOUNT_ID()) + ":security-group/" + *(securityGroup.AttrGroupId())

	// Create IAM Policy for automation role
	automationPolicy := awsiam.NewPolicyStatement(&awsiam.PolicyStatementProps{
		Actions:   &[]*string{jsii.String("ec2:RevokeSecurityGroupIngress")},
		Effect:    awsiam.Effect_ALLOW,
		Resources: &[]*string{jsii.String(securityGroupArn)},
	})

	// Attach the IAM policy to the automation role
	automationRole.AddToPolicy(automationPolicy)

	// Prepare State Manager Association parameters
	associationParams := map[string][]string{
		"AutomationAssumeRole": []string{*(automationRole.RoleArn())},
		"GroupId":              []string{*(securityGroup.AttrGroupId())},
	}
	// Create a State Manager Association
	association := awsssm.NewCfnAssociation(stack, jsii.String("DemoAssociation"), &awsssm.CfnAssociationProps{
		Name:            jsii.String("AWS-DisablePublicAccessForSecurityGroup"),
		AssociationName: jsii.String("DemoAssociation"),
		Parameters:      associationParams,
	})

	// Create a scheduler role
	schedulerRole := awsiam.NewRole(stack, jsii.String("scheduler-role"), &awsiam.RoleProps{
		AssumedBy:   awsiam.NewServicePrincipal(jsii.String("scheduler.amazonaws.com"), &awsiam.ServicePrincipalOpts{}),
		Description: jsii.String("Scheduler role for starting association"),
	})

	// prepare association ARN
	associationArn := "arn:aws:ssm:*:" + *(awscdk.Aws_ACCOUNT_ID()) + ":association/" + *(association.AttrAssociationId())

	// Create IAM Policy for scheduler role
	schedulerEventPolicy := awsiam.NewPolicyStatement(&awsiam.PolicyStatementProps{
		Actions:   &[]*string{jsii.String("ssm:StartAssociationsOnce")},
		Effect:    awsiam.Effect_ALLOW,
		Resources: &[]*string{jsii.String(associationArn)},
	})

	// Attach the IAM policy to the scheduler role
	schedulerRole.AddToPolicy(schedulerEventPolicy)

	// Create an EventBridge Scheduler to start association once every 5 minutes
	awsscheduler.NewCfnSchedule(stack, jsii.String("demo-schedule"), &awsscheduler.CfnScheduleProps{
		FlexibleTimeWindow: &awsscheduler.CfnSchedule_FlexibleTimeWindowProperty{
			Mode: jsii.String("OFF"),
		},
		ScheduleExpression: jsii.String("rate(5 minute)"),
		Target: &awsscheduler.CfnSchedule_TargetProperty{
			Arn:     jsii.String("arn:aws:scheduler:::aws-sdk:ssm:startAssociationsOnce"),
			RoleArn: schedulerRole.RoleArn(),
			Input:   jsii.String("{\"AssociationIds\": [\"" + *(association.AttrAssociationId()) + "\"]}"),
		},
	})

	return stack
}

func main() {
	defer jsii.Close()

	app := awscdk.NewApp(nil)

	NewEventbridgeScheduleSsmCdkGoStack(app, "EventbridgeScheduleSsmCdkGoStack", &EventbridgeScheduleSsmCdkGoStackProps{
		awscdk.StackProps{
			Env: env(),
		},
	})

	app.Synth(nil)
}

// env determines the AWS environment (account+region) in which our stack is to
// be deployed. For more information see: https://docs.aws.amazon.com/cdk/latest/guide/environments.html
func env() *awscdk.Environment {
	// If unspecified, this stack will be "environment-agnostic".
	// Account/Region-dependent features and context lookups will not work, but a
	// single synthesized template can be deployed anywhere.
	//---------------------------------------------------------------------------
	return nil
}
