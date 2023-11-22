package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsiam"
	"github.com/aws/aws-cdk-go/awscdk/v2/awssqs"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsscheduler"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type EventBridgeSchedulerToSqsCdkStackProps struct {
	awscdk.StackProps
}

func NewEventBridgeSchedulerToSqsCdkStack(scope constructs.Construct, id string, props *EventBridgeSchedulerToSqsCdkStackProps) awscdk.Stack {
	var sprops awscdk.StackProps
	if props != nil {
		sprops = props.StackProps
	}
	stack := awscdk.NewStack(scope, &id, &sprops)

	// Create SQS Topic
	sqsQueue := awssqs.NewQueue(stack, jsii.String("SQSQueue"), &awssqs.QueueProps{
		QueueName: jsii.String("EventBridgeSchedulerQueue"),
	})

	// Create IAM Role
	schedulerRole := awsiam.NewRole(stack, jsii.String("EventBridgeToSQSRole"), &awsiam.RoleProps{
		AssumedBy: awsiam.NewServicePrincipal(jsii.String("scheduler.amazonaws.com"), &awsiam.ServicePrincipalOpts{}),
	})

	schedulerSqsPolicy := awsiam.NewPolicyStatement(&awsiam.PolicyStatementProps{
		Actions:   &[]*string{jsii.String("sqs:SendMessage")},
		Effect:    awsiam.Effect_ALLOW,
		Resources: &[]*string{sqsQueue.QueueArn()},
	})

	schedulerRole.AddToPolicy(schedulerSqsPolicy)

	awsscheduler.NewCfnSchedule(stack, jsii.String("PublishToSqsSchedule"), &awsscheduler.CfnScheduleProps{
		FlexibleTimeWindow: &awsscheduler.CfnSchedule_FlexibleTimeWindowProperty{
			Mode: jsii.String("OFF"),
		},
		ScheduleExpression: jsii.String("rate(5 minute)"),
		Target: &awsscheduler.CfnSchedule_TargetProperty{
			Arn:     sqsQueue.QueueArn(),
			RoleArn: schedulerRole.RoleArn(),
			Input:   jsii.String("This message was published using EventBridge Scheduler!"),
		},
	})

	return stack
}

func main() {
	defer jsii.Close()

	app := awscdk.NewApp(nil)

	NewEventBridgeSchedulerToSqsCdkStack(app, "EventBridgeSchedulerToSqsCdkStackGo", &EventBridgeSchedulerToSqsCdkStackProps{
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
