package com.myorg;

import static java.util.Collections.singletonList;
import static software.amazon.awscdk.BundlingOutput.ARCHIVED;

import java.util.Arrays;
import java.util.List;

import software.amazon.awscdk.BundlingOptions;
import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.CfnOutputProps;
import software.amazon.awscdk.DockerVolume;
import software.amazon.awscdk.Duration;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.events.EventBus;
import software.amazon.awscdk.services.events.EventPattern;
import software.amazon.awscdk.services.events.Rule;
import software.amazon.awscdk.services.events.RuleProps;
import software.amazon.awscdk.services.events.targets.SfnStateMachine;
import software.amazon.awscdk.services.events.targets.SfnStateMachineProps;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.lambda.FunctionProps;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.logs.RetentionDays;
import software.amazon.awscdk.services.s3.assets.AssetOptions;
import software.amazon.awscdk.services.sqs.Queue;
import software.amazon.awscdk.services.sqs.QueueProps;
import software.amazon.awscdk.services.stepfunctions.CatchProps;
import software.amazon.awscdk.services.stepfunctions.Choice;
import software.amazon.awscdk.services.stepfunctions.Condition;
import software.amazon.awscdk.services.stepfunctions.Fail;
import software.amazon.awscdk.services.stepfunctions.Pass;
import software.amazon.awscdk.services.stepfunctions.RetryProps;
import software.amazon.awscdk.services.stepfunctions.StateMachine;
import software.amazon.awscdk.services.stepfunctions.Succeed;
import software.amazon.awscdk.services.stepfunctions.TaskInput;
import software.amazon.awscdk.services.stepfunctions.tasks.LambdaInvoke;
import software.amazon.awscdk.services.stepfunctions.tasks.SqsSendMessage;
import software.amazon.awscdk.services.stepfunctions.tasks.SqsSendMessageProps;
import software.constructs.Construct;

public class CdkInfraStack extends Stack {

	public CdkInfraStack(final Construct scope, final String id) {
		this(scope, id, null);
	}

	public CdkInfraStack(final Construct scope, final String id, final StackProps props) {
		super(scope, id, props);

		// The code that defines your stack goes here

		List<String> functionOnePackagingInstructions = Arrays.asList("/bin/sh", "-c",
				"cd lambda-handler " + "&& mvn clean install "
						+ "&& cp /asset-input/lambda-handler/target/lambda-handler.jar /asset-output/");

		BundlingOptions.Builder builderOptions = BundlingOptions.builder().command(functionOnePackagingInstructions)
				.image(Runtime.JAVA_11.getBundlingImage()).volumes(singletonList(
						// Mount local .m2 repo to avoid download all the dependencies again inside the
						// container
						DockerVolume.builder().hostPath(System.getProperty("user.home") + "/.m2/")
								.containerPath("/root/.m2/").build()))
				.user("root").outputType(ARCHIVED);

		Function executionLambda = new Function(this, "lambda-handler",
				FunctionProps.builder().runtime(Runtime.JAVA_11)
						.code(Code.fromAsset("../software/", AssetOptions.builder()
								.bundling(builderOptions.command(functionOnePackagingInstructions).build()).build()))
						.handler("com.myorg.App").memorySize(1024).timeout(Duration.seconds(900))
						.logRetention(RetentionDays.ONE_WEEK).build());

		// Create a Succeed state
		Succeed succeeded = Succeed.Builder.create(this, "Execution Succeed").build();
		Fail fail = Fail.Builder.create(this, "Execution Failed").build();

		// Create a Failure Queue
		Queue failureQueue = Queue.Builder.create(this, "StepFunctionFailureQueue")
				.queueName("Step-function-failure-queue").build();
		// Create an SQS SendMessage task
		SqsSendMessageProps failureQueueStepProps = SqsSendMessageProps.builder().queue(failureQueue)
				.messageBody(TaskInput.fromJsonPathAt("$")).build();
		SqsSendMessage failureQueueStep = new SqsSendMessage(this, "FailureQueue", failureQueueStepProps);
		failureQueueStep.next(fail);

		// Create a "Failure Callback" Pass state
		Pass failureCallback = Pass.Builder.create(this, "FailureCallback").build();

		// Chain the "Failure Callback" state to the failureQueueStep task
		failureCallback.next(failureQueueStep);

		// Create the LambdaInvoke task
		LambdaInvoke executionFunction = LambdaInvoke.Builder.create(this, "ExecutionJob")
				.lambdaFunction(executionLambda).retryOnServiceExceptions(true).outputPath("$.Payload").build();

		// Add retry configuration
		executionFunction
				.addRetry(RetryProps.builder().errors(Arrays.asList("Failure Exception")).maxAttempts(1).build());

		// Add catch configuration
		executionFunction.addCatch(failureCallback, CatchProps.builder().resultPath("$.message.errorMessage").build());

		// Create a Choice state
		Choice choiceState = Choice.Builder.create(this, "DoesExecutionSuccessful?").build();

		// Define transitions
		choiceState.when(Condition.stringEquals("$.processedInput.transactionStatus", "completed"), succeeded)
				.otherwise(failureCallback);

		// Set the next state of the executionFunction to the Choice state
		executionFunction.next(choiceState);

		// Create a Step Functions state machine
		StateMachine stateMachine = StateMachine.Builder.create(this, "EventBridgeCDKStateMachine")
				.stateMachineName("EventBridgeCDKStateMachine").definition(executionFunction).build();

		// Grant lambda execution roles
		executionLambda.grantInvoke(stateMachine.getRole());

		// Create an Event Bus
		EventBus customEventBus = new EventBus(this, "customEventBus");

		// Define the event rule and event pattern
		RuleProps eventRuleProps = RuleProps.builder().eventPattern(EventPattern.builder()
				.detailType(Arrays.asList("CREATE", "UPDATE", "DELETE")).source(List.of("CustomEvent")).build())
				.eventBus(customEventBus).build();

		// Create the event rule
		Rule eventRule = new Rule(this, "stepfunctionexecution-rule", eventRuleProps);

		// Create an asynchronous DLQ Queue
		Queue aysncdlqQueue = new Queue(this, "aysncdlqQueue", QueueProps.builder().queueName("aysncdlqQueue").build());

		// Add a target to the event rule with a Dead Letter Queue and retry policy
		SfnStateMachine sfnStateMachineTarget = new SfnStateMachine(stateMachine,
				SfnStateMachineProps.builder().deadLetterQueue(aysncdlqQueue)
						.maxEventAge(Duration.hours(2)).retryAttempts(3).build());

		eventRule.addTarget(sfnStateMachineTarget);
		
		// Create an output for the custom event bus
		new CfnOutput(this, "EventCustomBus", CfnOutputProps.builder()
		        .value(customEventBus.getEventBusName())
		        .description("The custom Event Bus Name")
		        .exportName("customEventBus")
		        .build());
		
		// Create an output for the Step Function state machine
		new CfnOutput(this, "StepFunction", CfnOutputProps.builder()
		        .value(stateMachine.getStateMachineName())
		        .description("The name of the stepfunction workflow")
		        .exportName("stepFunctionName")
		        .build());
		
		// Create an output for the EventBridge failure DLQ
		new CfnOutput(this, "EventBridgeFailureDLQ", CfnOutputProps.builder()
		        .value(aysncdlqQueue.getQueueName())
		        .description("EventBridge Step function Failure innovation DLQ")
		        .exportName("failureDLQName")
		        .build());

		// Create an output for the Step Function failure events queue
		new CfnOutput(this, "StepFunctionFailureEventsQueue", CfnOutputProps.builder()
		        .value(failureQueue.getQueueName())
		        .description("Step function Failure Events Queue")
		        .exportName("failureEventQueueName")
		        .build());

	}

}
