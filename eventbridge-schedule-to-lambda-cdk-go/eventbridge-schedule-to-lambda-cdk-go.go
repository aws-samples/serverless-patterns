package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awslambda"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsiam"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsscheduler"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type EventbridgeScheduleToLambdaCdkGoStackProps struct {
	awscdk.StackProps
}

func NewEventbridgeScheduleToLambdaCdkGoStack(scope constructs.Construct, id string, props *EventbridgeScheduleToLambdaCdkGoStackProps) awscdk.Stack {
	var sprops awscdk.StackProps
	if props != nil {
		sprops = props.StackProps
	}
	stack := awscdk.NewStack(scope, &id, &sprops)

	// Create Go based lambda function
	goLambdaFunction := awslambda.NewFunction(stack, jsii.String("EventBridgeLambdaTarget"), &awslambda.FunctionProps{
		Runtime:      awslambda.Runtime_GO_1_X(),
		Code:         awslambda.Code_FromAsset(jsii.String("./src/main.zip"), nil),
		Handler:      jsii.String("main"),
		Timeout:      awscdk.Duration_Seconds(jsii.Number(30)),
	})

	// Create IAM Role
	schedulerRole := awsiam.NewRole(stack, jsii.String("EventBridgeSchedulerRole"), &awsiam.RoleProps{
		AssumedBy: awsiam.NewServicePrincipal(jsii.String("scheduler.amazonaws.com"), &awsiam.ServicePrincipalOpts{}),
	})

	schedulerLambdaPolicy := awsiam.NewPolicyStatement(&awsiam.PolicyStatementProps{
		Actions:   &[]*string{jsii.String("lambda:InvokeFunction")},
		Effect:    awsiam.Effect_ALLOW,
		Resources: &[]*string{goLambdaFunction.FunctionArn()},
	})

	schedulerRole.AddToPolicy(schedulerLambdaPolicy)

	// Create schedule to invoke the function every 5 minutes
	awsscheduler.NewCfnSchedule(stack, jsii.String("InvokeLambdaSchedule"), &awsscheduler.CfnScheduleProps{
		FlexibleTimeWindow: &awsscheduler.CfnSchedule_FlexibleTimeWindowProperty{
			Mode: jsii.String("OFF"),
		},
		ScheduleExpression: jsii.String("rate(5 minute)"),
		Target: &awsscheduler.CfnSchedule_TargetProperty{
			Arn:     goLambdaFunction.FunctionArn(),
			RoleArn: schedulerRole.RoleArn(),
			Input:   jsii.String("{\"input\": \"This message was sent using EventBridge Scheduler!\"}"),
		},
	})

	return stack
}

func main() {
	defer jsii.Close()

	app := awscdk.NewApp(nil)

	NewEventbridgeScheduleToLambdaCdkGoStack(app, "EventbridgeScheduleToLambdaCdkGoStack", &EventbridgeScheduleToLambdaCdkGoStackProps{
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

	// Uncomment if you know exactly what account and region you want to deploy
	// the stack to. This is the recommendation for production stacks.
	//---------------------------------------------------------------------------
	// return &awscdk.Environment{
	//  Account: jsii.String("123456789012"),
	//  Region:  jsii.String("us-east-1"),
	// }

	// Uncomment to specialize this stack for the AWS Account and Region that are
	// implied by the current CLI configuration. This is recommended for dev
	// stacks.
	//---------------------------------------------------------------------------
	// return &awscdk.Environment{
	//  Account: jsii.String(os.Getenv("CDK_DEFAULT_ACCOUNT")),
	//  Region:  jsii.String(os.Getenv("CDK_DEFAULT_REGION")),
	// }
}
