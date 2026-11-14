// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as snsSubscriptions from 'aws-cdk-lib/aws-sns-subscriptions';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import * as path from 'path';

export class CloudwatchLogAlarmLambdaRemediationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const region = cdk.Stack.of(this).region;
    const account = cdk.Stack.of(this).account;

    // =========================================================
    // 1. Amazon CloudWatch Log Group (monitored application logs)
    // =========================================================
    const appLogGroup = new logs.LogGroup(this, 'AppLogGroup', {
      logGroupName: '/app/monitored-service',
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // =========================================================
    // 2. Amazon SNS Topic (alarm notification fan-out)
    // =========================================================
    const alarmTopic = new sns.Topic(this, 'AlarmTopic', {
      topicName: 'log-alarm-notifications',
      displayName: 'Amazon CloudWatch Log Alarm Notifications',
    });

    // =========================================================
    // 3. AWS Lambda: Remediation Handler
    // =========================================================
    const remediationFn = new lambda.Function(this, 'RemediationFn', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../../lambdas/remediation')),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      description: 'Auto-remediation: restarts service via AWS Systems Manager when error threshold breached',
      environment: {
        ALARM_TOPIC_ARN: alarmTopic.topicArn,
      },
    });

    // SSM permissions for remediation (send commands to EC2 instances)
    remediationFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'ssm:SendCommand',
        'ssm:GetCommandInvocation',
      ],
      resources: [
        `arn:aws:ssm:${region}::document/AWS-RunShellScript`,
        `arn:aws:ec2:${region}:${account}:instance/*`,
      ],
      conditions: {
        StringEquals: {
          'aws:ResourceTag/AutoRemediate': 'true',
        },
      },
    }));

    // CloudWatch Logs permissions for context retrieval
    remediationFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'logs:GetLogEvents',
        'logs:FilterLogEvents',
      ],
      resources: [appLogGroup.logGroupArn, `${appLogGroup.logGroupArn}:*`],
    }));

    // Subscribe Lambda to SNS topic
    alarmTopic.addSubscription(
      new snsSubscriptions.LambdaSubscription(remediationFn)
    );

    // =========================================================
    // 4. IAM Role for Scheduled Query execution
    // =========================================================
    const scheduledQueryRole = new iam.Role(this, 'ScheduledQueryRole', {
      assumedBy: new iam.ServicePrincipal('logs.amazonaws.com'),
      description: 'Allows Amazon CloudWatch Logs to execute scheduled queries',
      inlinePolicies: {
        LogsQuery: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              actions: [
                'logs:StartQuery',
                'logs:GetQueryResults',
                'logs:StopQuery',
              ],
              resources: [appLogGroup.logGroupArn, `${appLogGroup.logGroupArn}:*`],
            }),
          ],
        }),
      },
    });

    // =========================================================
    // 5. AWS::CloudWatch::LogAlarm (new CFN resource type)
    //    Monitors error rate in application logs using Logs Insights
    // =========================================================
    const logAlarm = new cdk.CfnResource(this, 'ErrorRateLogAlarm', {
      type: 'AWS::CloudWatch::LogAlarm',
      properties: {
        AlarmName: 'app-error-rate-alarm',
        AlarmDescription: 'Triggers when error count exceeds threshold in application logs (monitored via Amazon CloudWatch Logs Insights query)',
        ComparisonOperator: 'GreaterThanOrEqualToThreshold',
        Threshold: 5,
        QueryResultsToAlarm: 1,
        QueryResultsToEvaluate: 1,
        TreatMissingData: 'notBreaching',
        ActionsEnabled: true,
        AlarmActions: [alarmTopic.topicArn],
        OKActions: [alarmTopic.topicArn],
        ScheduledQueryConfiguration: {
          QueryString: 'fields @timestamp, @message | filter @message like /ERROR/ | stats count(*) as error_count by bin(5m)',
          LogGroupIdentifiers: [appLogGroup.logGroupName],
          AggregationExpression: 'count(*)',
          ScheduleConfiguration: {
            ScheduleExpression: 'rate(5 minutes)',
            StartTimeOffset: 300,
          },
          ScheduledQueryRoleARN: scheduledQueryRole.roleArn,
        },
      },
    });

    // Ensure role is created before the alarm
    logAlarm.addDependency(scheduledQueryRole.node.defaultChild as cdk.CfnResource);

    // =========================================================
    // Outputs
    // =========================================================
    new cdk.CfnOutput(this, 'LogGroupName', {
      value: appLogGroup.logGroupName,
      description: 'Amazon CloudWatch Logs group being monitored',
    });

    new cdk.CfnOutput(this, 'AlarmTopicArn', {
      value: alarmTopic.topicArn,
      description: 'Amazon SNS topic for alarm notifications',
    });

    new cdk.CfnOutput(this, 'RemediationFunctionArn', {
      value: remediationFn.functionArn,
      description: 'AWS Lambda remediation function ARN',
    });

    new cdk.CfnOutput(this, 'LogAlarmName', {
      value: 'app-error-rate-alarm',
      description: 'Amazon CloudWatch Log Alarm name',
    });
  }
}
