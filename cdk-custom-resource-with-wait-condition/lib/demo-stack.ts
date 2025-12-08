import { CfnWaitConditionHandle, RemovalPolicy, Stack, StackProps, CustomResource, CfnWaitCondition } from 'aws-cdk-lib';
import { Architecture, LoggingFormat, Runtime } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction, NodejsFunctionProps } from 'aws-cdk-lib/aws-lambda-nodejs';
import { LogGroup, LogGroupProps, RetentionDays } from 'aws-cdk-lib/aws-logs';
import { StateMachine, DefinitionBody } from 'aws-cdk-lib/aws-stepfunctions';
import { Construct } from 'constructs';

/**
 * Demo stack showing custom resource with wait condition pattern.
 * Uses Step Functions for long-running processes and wait conditions for synchronization.
 */
export class DemoStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Create unique wait condition handle for each deployment
    // Note: WaitCondition resources don't support updates, requiring new handles per deployment
    const resourceName: string = `WaitConditionHandle-${Date.now()}`;
    const cfnWaitConditionHandle = new CfnWaitConditionHandle(this, resourceName);

    // Common configuration for Lambda functions
    const commonLambdaProps: Partial<NodejsFunctionProps> = {
      architecture: Architecture.ARM_64,
      loggingFormat: LoggingFormat.JSON,
      runtime: Runtime.NODEJS_24_X,
      memorySize: 256,
    };

    // Common configuration for CloudWatch log groups
    const commonLogGroupProps: Partial<LogGroupProps> = {
      removalPolicy: RemovalPolicy.DESTROY,
      retention: RetentionDays.ONE_WEEK,
    };

    // Lambda function that handles custom resource lifecycle events
    // Starts Step Function execution and returns immediately
    const customResourceHandler = new NodejsFunction(this, 'CustomResourceHandler', {
      ...commonLambdaProps,
      functionName: 'CustomResourceHandler',
      entry: 'lib/lambda/custom-resource-handler.mts',
      logGroup: new LogGroup(this, 'CustomResourceHandlerLogGroup', {
        ...commonLogGroupProps,
        logGroupName: `/demo/CustomResourceHandler`,
      }),
    });

    // Lambda function that sends completion signals to wait condition handles
    const sendCompletionSignalHandler = new NodejsFunction(this, 'SendCompletionSignalHandler', {
      ...commonLambdaProps,
      functionName: 'SendCompletionSignalHandler',
      entry: 'lib/lambda/send-completion-signal.mts',
      logGroup: new LogGroup(this, 'SendCompletionSignalHandlerLogGroup', {
        ...commonLogGroupProps,
        logGroupName: `/demo/SendCompletionSignalHandler`,
      }),
    });

    // Step Function that simulates a long-running process
    // Invokes completion signal Lambda when process finishes
    const longRunningProcessStateMachine = new StateMachine(this, 'LongRunningProcessStateMachine', {
      definitionBody: DefinitionBody.fromFile('lib/sfn/long-running-process.asl.json'),
      stateMachineName: 'LongRunningProcessStateMachine',
      definitionSubstitutions: {
        SendCompletionSignalLambdaArn: sendCompletionSignalHandler.functionArn,
      },
      logs: {
        destination: new LogGroup(this, 'LongRunningProcessStateMachineLogGroup', {
          ...commonLogGroupProps,
          logGroupName: `/demo/LongRunningProcessStateMachine`,
        }),
      },
    });

    // Grant permissions for Lambda functions to interact with Step Function
    longRunningProcessStateMachine.grantStartExecution(customResourceHandler);
    sendCompletionSignalHandler.grantInvoke(longRunningProcessStateMachine);

    // Custom resource that triggers the long-running process
    const customResource = new CustomResource(this, 'CustomResource', {
      serviceToken: customResourceHandler.functionArn,
      properties: {
        WaitConditionHandle: cfnWaitConditionHandle.ref,
        StateMachineArn: longRunningProcessStateMachine.stateMachineArn,
      }
    });

    // Wait condition that blocks stack completion until process finishes
    const waitCondition = new CfnWaitCondition(this, 'WaitCondition', {
      count: 1,
      handle: cfnWaitConditionHandle.ref,
      timeout: '60', // 60 seconds timeout
    });
    
    // Ensure wait condition depends on custom resource and state machine
    waitCondition.node.addDependency(customResource);
    waitCondition.node.addDependency(longRunningProcessStateMachine);
  }
}
