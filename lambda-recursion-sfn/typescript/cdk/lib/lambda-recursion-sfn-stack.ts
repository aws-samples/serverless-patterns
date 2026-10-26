// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as path from 'path';
import { Stack, StackProps, RemovalPolicy, Duration, CfnOutput, Arn, ArnFormat } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';

// Demo safety limits. Lambda recursive loop detection stops a chain at approximately 16 invocations.
// MAX_HOPS is a second stop inside the demo function: a single chain stops at 25 invocations.
const MAX_HOPS = 25;
// A small reserved concurrency keeps the demo bounded. The workflow later sets it to 0.
const DEMO_CONCURRENCY = 5;
// An unprocessed asynchronous event is kept at most this long (the default is 6 hours).
const MAX_EVENT_AGE = Duration.minutes(1);

export class LambdaRecursionSfnStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // ---- Demo workload: a Lambda function that invokes itself asynchronously -----------------------
    const functionLogs = new logs.LogGroup(this, 'LooperLogs', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY, // demo only
    });
    // The function invokes itself, so its policy has to name its own ARN. The ARN is built from the stack name:
    // a reference to the function would be a circular dependency between the role policy and the function.
    const functionName = `${this.stackName}-looper`;
    const looper = new lambda.Function(this, 'Looper', {
      functionName,
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: 'looper.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src')),
      timeout: Duration.seconds(5),
      environment: { MAX_HOPS: String(MAX_HOPS) },
      reservedConcurrentExecutions: DEMO_CONCURRENCY,
      logGroup: functionLogs,
      retryAttempts: 0, // a failed invocation is not repeated, so a chain is not forked by retries
      maxEventAge: MAX_EVENT_AGE,
      // recursiveLoop stays at its default (Terminate): the setting Allow lets the function be invoked recursively.
    });
    looper.addToRolePolicy(new iam.PolicyStatement({
      actions: ['lambda:InvokeFunction'],
      resources: [this.formatArn({ service: 'lambda', resource: 'function', resourceName: functionName, arnFormat: ArnFormat.COLON_RESOURCE_NAME })],
    }));

    // ---- Detection: the metric that Lambda emits when it stops a recursive invocation -----------
    const alarm = new cloudwatch.Alarm(this, 'RecursionDroppedAlarm', {
      alarmDescription: 'AWS Lambda stopped a recursive invocation of the looper function',
      metric: new cloudwatch.Metric({
        namespace: 'AWS/Lambda',
        metricName: 'RecursiveInvocationsDropped',
        dimensionsMap: { FunctionName: looper.functionName },
        statistic: 'Sum',
        period: Duration.minutes(1), // Lambda metrics have 1-minute resolution, so 1 minute is the shortest useful period
      }),
      threshold: 1,
      comparisonOperator: cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
      evaluationPeriods: 1,
      datapointsToAlarm: 1,
      treatMissingData: cloudwatch.TreatMissingData.NOT_BREACHING, // returns to OK when no loop is detected
    });

    // ---- Remediation: an AWS SDK service integration only, no Lambda function ---------------------
    const notAlarm = new sfn.Fail(this, 'InvalidEvent', {
      error: 'InvalidEvent',
      cause: 'The input is not a CloudWatch alarm state change event with detail.state.value ALARM.',
    });
    const throttleFailed = new sfn.Fail(this, 'ThrottleFailed', {
      error: 'ThrottleFailed',
      cause: 'Setting the reserved concurrency to 0 failed.',
    });

    // The call is idempotent: a second alarm event sets the same value. Only transient errors are retried.
    // Any other error is not listed in a Retry, so it goes straight to the Catch.
    // The error names are the Lambda API error names with the Step Functions prefix Lambda.
    const throttle = new tasks.CallAwsService(this, 'SetConcurrencyToZero', {
      service: 'lambda',
      action: 'putFunctionConcurrency',
      parameters: { FunctionName: looper.functionName, ReservedConcurrentExecutions: 0 },
      iamAction: 'lambda:PutFunctionConcurrency',
      iamResources: [looper.functionArn],
      taskTimeout: sfn.Timeout.duration(Duration.seconds(30)),
      resultPath: '$.throttle',
    });
    throttle.addRetry({
      errors: ['Lambda.ServiceException', 'Lambda.TooManyRequestsException', 'Lambda.ResourceConflictException', 'States.Timeout'],
      interval: Duration.seconds(2),
      maxAttempts: 3,
    });
    throttle.addCatch(throttleFailed, { resultPath: '$.throttleError' });

    // Optional paths are guarded with isPresent: a States.ALL catch does not catch States.Runtime.
    const definition = new sfn.Choice(this, 'IsAlarm')
      .when(sfn.Condition.and(
        sfn.Condition.isPresent('$.detail.state.value'),
        sfn.Condition.stringEquals('$.detail.state.value', 'ALARM')),
      throttle.next(new sfn.Succeed(this, 'LoopContained')))
      .otherwise(notAlarm);

    // The /aws/vendedlogs/states prefix keeps the log group out of the CloudWatch Logs resource policy size limit.
    const stateMachineLogs = new logs.LogGroup(this, 'StateMachineLogs', {
      logGroupName: `/aws/vendedlogs/states/${this.stackName}-workflow`,
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY, // demo only
    });
    const stateMachine = new sfn.StateMachine(this, 'ContainmentStateMachine', {
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      timeout: Duration.minutes(5),
      // The execution data holds the alarm event (alarm name, account ID, Region). Retention is one week.
      logs: { destination: stateMachineLogs, level: sfn.LogLevel.ALL, includeExecutionData: true },
    });

    // ---- Trigger: CloudWatch alarm actions cannot start a state machine, so an EventBridge rule does ----
    // The rule is on the default event bus, where CloudWatch sends alarm state changes. It matches this alarm
    // entering ALARM only, not the return to OK.
    const targetRole = new iam.Role(this, 'AlarmRuleTargetRole', {
      assumedBy: new iam.ServicePrincipal('events.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': Arn.format({ service: 'events', resource: 'rule', resourceName: '*' }, this) },
        },
      }),
    });
    new events.Rule(this, 'AlarmStateRule', {
      description: 'Start the containment workflow when the recursion alarm enters ALARM',
      eventPattern: {
        source: ['aws.cloudwatch'],
        detailType: ['CloudWatch Alarm State Change'],
        detail: { alarmName: [alarm.alarmName], state: { value: ['ALARM'] } },
      },
      targets: [new targets.SfnStateMachine(stateMachine, {
        role: targetRole,
        retryAttempts: 5,
        maxEventAge: Duration.hours(1),
      })],
    });

    new CfnOutput(this, 'FunctionName', { value: looper.functionName, description: 'Looping demo function whose concurrency the workflow sets to 0' });
    new CfnOutput(this, 'FunctionLogGroup', { value: functionLogs.logGroupName });
    new CfnOutput(this, 'AlarmName', { value: alarm.alarmName });
    new CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new CfnOutput(this, 'StateMachineLogGroup', { value: stateMachineLogs.logGroupName });
  }
}
