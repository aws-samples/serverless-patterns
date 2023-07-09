package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsec2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsecs"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsiam"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsscheduler"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type EventbridgeScheduleEcsCdkGoStackProps struct {
	awscdk.StackProps
}

func NewEventbridgeScheduleEcsCdkGoStack(scope constructs.Construct, id string, props *EventbridgeScheduleEcsCdkGoStackProps) awscdk.Stack {
	var sprops awscdk.StackProps
	if props != nil {
		sprops = props.StackProps
	}
	stack := awscdk.NewStack(scope, &id, &sprops)

	// Create a VPC for ECS Cluster
	vpc := awsec2.NewVpc(stack, jsii.String("TheVPC"), &awsec2.VpcProps{
		Cidr: jsii.String("10.10.0.0/24"),
	})

	// Create ECS Cluster
	cluster := awsecs.NewCluster(stack, jsii.String("Cluster"), &awsecs.ClusterProps{
		Vpc: vpc,
	})

	// Create a Fargate Task Definition
	taskDef := awsecs.NewFargateTaskDefinition(stack, jsii.String("TaskDef"), &awsecs.FargateTaskDefinitionProps{
		MemoryLimitMiB: jsii.Number(512),
		Cpu:            jsii.Number(256),
	})

	// Create a container definition with sample image
	taskDef.AddContainer(jsii.String("WebContainer"), &awsecs.ContainerDefinitionOptions{
		Image: awsecs.ContainerImage_FromRegistry(jsii.String("amazon/amazon-ecs-sample"), &awsecs.RepositoryImageProps{}),
	})

	// Create a scheduler role
	schedulerRole := awsiam.NewRole(stack, jsii.String("scheduler-role"), &awsiam.RoleProps{
		AssumedBy:   awsiam.NewServicePrincipal(jsii.String("scheduler.amazonaws.com"), &awsiam.ServicePrincipalOpts{}),
		Description: jsii.String("Scheduler role for running task in ECS"),
	})

	// Create IAM Policy for scheduler role
	schedulerEventPolicy := awsiam.NewPolicyStatement(&awsiam.PolicyStatementProps{
		Actions:   &[]*string{jsii.String("ecs:RunTask"), jsii.String("iam:PassRole")},
		Effect:    awsiam.Effect_ALLOW,
		Resources: &[]*string{jsii.String("*")},
	})

	// Attach the IAM policy to the scheduler role
	schedulerRole.AddToPolicy(schedulerEventPolicy)

	// Get the VPC private subnet IDs
	subnetIds := vpc.SelectSubnets(&awsec2.SubnetSelection{
		SubnetType: awsec2.SubnetType_PRIVATE_WITH_EGRESS,
	}).SubnetIds

	// Create an EventBridge Scheduler to run a task in ECS cluster and in private subnets every 15 minutes
	awsscheduler.NewCfnSchedule(stack, jsii.String("demo-schedule"), &awsscheduler.CfnScheduleProps{
		FlexibleTimeWindow: &awsscheduler.CfnSchedule_FlexibleTimeWindowProperty{
			Mode: jsii.String("OFF"),
		},
		ScheduleExpression: jsii.String("rate(15 minute)"),
		Target: &awsscheduler.CfnSchedule_TargetProperty{
			Arn:     cluster.ClusterArn(),
			RoleArn: schedulerRole.RoleArn(),
			EcsParameters: &awsscheduler.CfnSchedule_EcsParametersProperty{
				TaskDefinitionArn: taskDef.TaskDefinitionArn(),
				TaskCount:         jsii.Number(1),
				LaunchType:        jsii.String("FARGATE"),
				NetworkConfiguration: &awsscheduler.CfnSchedule_NetworkConfigurationProperty{
					AwsvpcConfiguration: &awsscheduler.CfnSchedule_AwsVpcConfigurationProperty{
						Subnets: subnetIds,
					},
				},
			},
		},
	})

	return stack
}

func main() {
	defer jsii.Close()

	app := awscdk.NewApp(nil)

	NewEventbridgeScheduleEcsCdkGoStack(app, "EventbridgeScheduleEcsCdkGoStack", &EventbridgeScheduleEcsCdkGoStackProps{
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
