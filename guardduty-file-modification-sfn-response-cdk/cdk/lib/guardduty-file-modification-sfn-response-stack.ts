// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import * as cdk from 'aws-cdk-lib';
import * as guardduty from 'aws-cdk-lib/aws-guardduty';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as sfnTasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import * as path from 'path';

export class GuarddutyFileModificationSfnResponseStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const region = cdk.Stack.of(this).region;
    const account = cdk.Stack.of(this).account;

    // =========================================================
    // 1. Amazon GuardDuty Detector (use existing or create new)
    // =========================================================
    const detectorId = new cdk.CfnParameter(this, 'DetectorId', {
      type: 'String',
      description: 'Existing Amazon GuardDuty detector ID (leave empty to create new)',
      default: '',
    });

    const createDetector = new cdk.CfnCondition(this, 'ShouldCreateDetector', {
      expression: cdk.Fn.conditionEquals(detectorId.valueAsString, ''),
    });

    const detector = new guardduty.CfnDetector(this, 'GuardDutyDetector', {
      enable: true,
      findingPublishingFrequency: 'FIFTEEN_MINUTES',
    });
    detector.cfnOptions.condition = createDetector;

    const effectiveDetectorId = cdk.Fn.conditionIf(
      'ShouldCreateDetector',
      detector.ref,
      detectorId.valueAsString,
    ).toString();

    // =========================================================
    // 2. Amazon SNS Topic (incident notifications)
    // =========================================================
    const incidentTopic = new sns.Topic(this, 'IncidentTopic', {
      topicName: 'guardduty-incident-alerts',
      displayName: 'Amazon GuardDuty - Sensitive File Modification Alerts',
    });

    // =========================================================
    // 3. AWS Lambda: Instance Isolation Handler
    // =========================================================
    const isolateFn = new lambda.Function(this, 'IsolateInstanceFn', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../../lambdas/isolate-instance')),
      timeout: cdk.Duration.seconds(120),
      memorySize: 256,
      description: 'Isolates compromised Amazon EC2 instance: replaces security group, creates snapshot, tags',
    });

    // EC2 permissions for isolation actions
    isolateFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'ec2:DescribeInstances',
        'ec2:DescribeSecurityGroups',
        'ec2:CreateSecurityGroup',
        'ec2:RevokeSecurityGroupEgress',
        'ec2:ModifyInstanceAttribute',
        'ec2:CreateSnapshot',
        'ec2:CreateTags',
        'ec2:DescribeVolumes',
      ],
      resources: ['*'],
      conditions: {
        StringEquals: { 'aws:RequestedRegion': region },
      },
    }));

    // =========================================================
    // 4. AWS Step Functions: Incident Response Workflow
    // =========================================================

    // Isolate instance (HIGH severity)
    const isolateTask = new sfnTasks.LambdaInvoke(this, 'IsolateInstance', {
      lambdaFunction: isolateFn,
      outputPath: '$.Payload',
      comment: 'Replace security group, create forensic snapshot, tag instance',
    });

    // Publish HIGH severity to SNS (after isolation)
    const notifyHighTask = new sfnTasks.SnsPublish(this, 'NotifyHighSeverity', {
      topic: incidentTopic,
      subject: sfn.JsonPath.format(
        'GuardDuty CRITICAL: {} on instance {}',
        sfn.JsonPath.stringAt('$.findingType'),
        sfn.JsonPath.stringAt('$.instanceId'),
      ),
      message: sfn.TaskInput.fromJsonPathAt('$'),
      resultPath: '$.notification',
    });

    // Publish MEDIUM severity to SNS
    const notifyMediumTask = new sfnTasks.SnsPublish(this, 'NotifyMediumSeverity', {
      topic: incidentTopic,
      subject: sfn.JsonPath.format(
        'GuardDuty WARNING: {}',
        sfn.JsonPath.stringAt('$.detail.type'),
      ),
      message: sfn.TaskInput.fromJsonPathAt('$'),
      resultPath: '$.notification',
    });

    // Terminal states
    const highDone = new sfn.Pass(this, 'HighSeverityHandled', {
      result: sfn.Result.fromObject({ status: 'ISOLATED_AND_NOTIFIED' }),
    });

    const mediumDone = new sfn.Pass(this, 'MediumSeverityHandled', {
      result: sfn.Result.fromObject({ status: 'NOTIFIED' }),
    });

    const lowDone = new sfn.Pass(this, 'LowSeverityLogged', {
      result: sfn.Result.fromObject({ status: 'LOGGED' }),
    });

    // Severity routing
    const definition = new sfn.Choice(this, 'ClassifySeverity')
      .when(
        sfn.Condition.numberGreaterThanEquals('$.detail.severity', 7),
        isolateTask.next(notifyHighTask).next(highDone),
      )
      .when(
        sfn.Condition.numberGreaterThanEquals('$.detail.severity', 4),
        notifyMediumTask.next(mediumDone),
      )
      .otherwise(lowDone);

    const stateMachine = new sfn.StateMachine(this, 'IncidentResponseWorkflow', {
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      timeout: cdk.Duration.minutes(10),
      tracingEnabled: true,
      logs: {
        destination: new logs.LogGroup(this, 'SfnLogGroup', {
          logGroupName: '/aws/stepfunctions/guardduty-incident-response',
          retention: logs.RetentionDays.TWO_WEEKS,
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
        level: sfn.LogLevel.ALL,
      },
    });

    // =========================================================
    // 5. Amazon EventBridge Rule: GuardDuty findings
    //    Matches sensitive file modification findings
    // =========================================================
    new events.Rule(this, 'GuardDutyFileModRule', {
      ruleName: 'guardduty-file-modification-to-sfn',
      description: 'Routes Amazon GuardDuty sensitive file modification findings to AWS Step Functions',
      eventPattern: {
        source: ['aws.guardduty'],
        detailType: ['GuardDuty Finding'],
        detail: {
          type: [
            { prefix: 'Execution:Runtime/SensitiveFileAccess' },
            { prefix: 'Execution:Runtime/SuspiciousFileModification' },
            { prefix: 'UnauthorizedAccess:EC2' },
          ],
        },
      },
      targets: [new targets.SfnStateMachine(stateMachine)],
    });

    // =========================================================
    // Outputs
    // =========================================================
    new cdk.CfnOutput(this, 'DetectorIdOutput', {
      value: effectiveDetectorId,
      description: 'Amazon GuardDuty detector ID',
    });

    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.stateMachineArn,
      description: 'AWS Step Functions incident response workflow ARN',
    });

    new cdk.CfnOutput(this, 'IncidentTopicArn', {
      value: incidentTopic.topicArn,
      description: 'Amazon SNS incident notification topic ARN',
    });

    new cdk.CfnOutput(this, 'IsolationFunctionArn', {
      value: isolateFn.functionArn,
      description: 'AWS Lambda isolation function ARN',
    });
  }
}
