package main

import (
	"encoding/json"
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsiam"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsscheduler"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsstepfunctions"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type EventBridgeScheduleToStepFunctionStackProps struct {
	awscdk.StackProps
}

type EventInput struct {
	ExecutionId   string
	ScheduledTime string
	ScheduleArn   string
	AttemptNumber string
}

// State machine related constants
const (
	stateMachineName = "state-machine"
	passStateComment = "This is merely a placeholder comment. Replace with your own state machine tasks."
)

// Scheduler related constants
const (
	schedulerRoleName  = "SchedulerStartExecutionSfnRole"
	schedulerGroupName = "SchedulerSfnGroup"
	scheduleExpression = "cron(0 * * * ? *)"
	scheduleName       = "StartStepFunctionExecutionEveryHour"
)

func NewEventBridgeScheduleToStepFunctionStack(scope constructs.Construct, id string, props *EventBridgeScheduleToStepFunctionStackProps) awscdk.Stack {
	var sprops awscdk.StackProps
	if props != nil {
		sprops = props.StackProps
	}
	stack := awscdk.NewStack(scope, &id, &sprops)

	// State Machine
	stateMachine := awsstepfunctions.NewStateMachine(stack, jsii.String("state-machine"), &awsstepfunctions.StateMachineProps{
		Definition: awsstepfunctions.NewPass(stack, jsii.String("placeholder-state"), &awsstepfunctions.PassProps{
			Comment: jsii.String(passStateComment),
		}),
		StateMachineName: jsii.String(stateMachineName),
	})

	// Add scheduler permissions
	schedulerRole := awsiam.NewRole(stack, jsii.String("scheduler-role"), &awsiam.RoleProps{
		AssumedBy: awsiam.NewServicePrincipal(jsii.String("scheduler.amazonaws.com"), nil),
		RoleName:  jsii.String(schedulerRoleName),
	})

	policyStatement := awsiam.NewPolicyStatement(&awsiam.PolicyStatementProps{
		Actions:   jsii.Strings("states:StartExecution"),
		Effect:    awsiam.Effect_ALLOW,
		Resources: jsii.Strings(*stateMachine.StateMachineArn()),
	})

	schedulerRole.AddToPolicy(policyStatement)

	// Add schedule group
	scheduleGroup := awsscheduler.NewCfnScheduleGroup(stack, jsii.String("sfn-schedule-group"), &awsscheduler.CfnScheduleGroupProps{
		Name: jsii.String(schedulerGroupName),
	})

	// Add schedule
	eventInput, err := json.Marshal(EventInput{
		ExecutionId:   "<aws.scheduler.execution-id>",
		ScheduledTime: "<aws.scheduler.scheduled-time>",
		ScheduleArn:   "<aws.scheduler.schedule-arn>",
		AttemptNumber: "<aws.scheduler.attempt-number>",
	})

	var eventInputJsonString string

	if err != nil {
		eventInputJsonString = string(eventInput)
	} else {
		eventInputJsonString = "{\"eventId\": \"MY_SCHEDULED_EVENT\"}"
	}

	schedule := awsscheduler.NewCfnSchedule(stack, jsii.String("sfn-start-exec-schedule"), &awsscheduler.CfnScheduleProps{
		FlexibleTimeWindow: awsscheduler.CfnSchedule_FlexibleTimeWindowProperty{Mode: jsii.String("OFF")},
		ScheduleExpression: jsii.String(scheduleExpression),
		Target: awsscheduler.CfnSchedule_TargetProperty{
			Arn:     stateMachine.StateMachineArn(),
			RoleArn: schedulerRole.RoleArn(),
			Input:   jsii.String(eventInputJsonString),
		},
		GroupName: scheduleGroup.Name(),
		Name:      jsii.String(scheduleName),
	})

	// Output
	awscdk.NewCfnOutput(stack, jsii.String("SCHEDULE_NAME"), &awscdk.CfnOutputProps{Value: schedule.Name()})
	awscdk.NewCfnOutput(stack, jsii.String("STATE_MACHINE_ARN"), &awscdk.CfnOutputProps{Value: stateMachine.StateMachineArn()})

	return stack
}

func main() {
	defer jsii.Close()

	app := awscdk.NewApp(nil)

	NewEventBridgeScheduleToStepFunctionStack(app, "EventBridgeScheduleToStepFunctionStack", &EventBridgeScheduleToStepFunctionStackProps{
		awscdk.StackProps{
			Env: env(),
		},
	})

	app.Synth(nil)
}

// env determines the AWS environment (account+region) in which our stack is to
// be deployed. For more information see: https://docs.aws.amazon.com/cdk/latest/guide/environments.html
func env() *awscdk.Environment {
	return nil
}
