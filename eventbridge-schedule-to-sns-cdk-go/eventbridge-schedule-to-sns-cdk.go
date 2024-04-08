package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsiam"
	"github.com/aws/aws-cdk-go/awscdk/v2/awssns"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsscheduler"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type EventBridgeSchedulerToSnsCdkStackProps struct {
	awscdk.StackProps
}

func NewEventBridgeSchedulerToSnsCdkStack(scope constructs.Construct, id string, props *EventBridgeSchedulerToSnsCdkStackProps) awscdk.Stack {
	var sprops awscdk.StackProps
	if props != nil {
		sprops = props.StackProps
	}
	stack := awscdk.NewStack(scope, &id, &sprops)

	// Create SNS Topic
	snsTopic := awssns.NewTopic(stack, jsii.String("SchedulerTopic"), &awssns.TopicProps{
		DisplayName: jsii.String("EventBridgeSchedulerTopic"),
	})

	// Create IAM Role
	schedulerRole := awsiam.NewRole(stack, jsii.String("EventBridgeToSNSRole"), &awsiam.RoleProps{
		AssumedBy: awsiam.NewServicePrincipal(jsii.String("scheduler.amazonaws.com"), &awsiam.ServicePrincipalOpts{}),
	})

	schedulerSnsPolicy := awsiam.NewPolicyStatement(&awsiam.PolicyStatementProps{
		Actions:   &[]*string{jsii.String("sns:Publish")},
		Effect:    awsiam.Effect_ALLOW,
		Resources: &[]*string{snsTopic.TopicArn()},
	})

	schedulerRole.AddToPolicy(schedulerSnsPolicy)

	awsscheduler.NewCfnSchedule(stack, jsii.String("PublishToSnsSchedule"), &awsscheduler.CfnScheduleProps{
		FlexibleTimeWindow: &awsscheduler.CfnSchedule_FlexibleTimeWindowProperty{
			Mode: jsii.String("OFF"),
		},
		ScheduleExpression: jsii.String("rate(5 minute)"),
		Target: &awsscheduler.CfnSchedule_TargetProperty{
			Arn:     snsTopic.TopicArn(),
			RoleArn: schedulerRole.RoleArn(),
			Input:   jsii.String("This message was published using EventBridge Scheduler!"),
		},
	})

	return stack
}

func main() {
	defer jsii.Close()

	app := awscdk.NewApp(nil)

	NewEventBridgeSchedulerToSnsCdkStack(app, "EventBridgeSchedulerToSnsCdkStackGo", &EventBridgeSchedulerToSnsCdkStackProps{
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
