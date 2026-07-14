// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import * as cdk from 'aws-cdk-lib';
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

export class SecurityhubFindingSfnRemediationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const region = cdk.Stack.of(this).region;
    const account = cdk.Stack.of(this).account;

    // =========================================================
    // 1. Amazon SNS Topic (security team notifications)
    // =========================================================
    const alertTopic = new sns.Topic(this, 'SecurityAlertTopic', {
      topicName: 'securityhub-remediation-alerts',
      displayName: 'AWS Security Hub - Auto-Remediation Alerts',
    });

    // =========================================================
    // 2. AWS Lambda: Remediation Handler
    // =========================================================
    const remediateFn = new lambda.Function(this, 'RemediateFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../../lambdas/remediate')),
      timeout: cdk.Duration.seconds(120),
      memorySize: 256,
      description: 'Remediates AWS Security Hub findings: closes open SGs, enables encryption, enforces MFA',
    });

    // EC2/S3/IAM permissions for remediation actions
    remediateFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'ec2:RevokeSecurityGroupIngress',
        'ec2:DescribeSecurityGroups',
        'ec2:CreateTags',
      ],
      resources: [`arn:aws:ec2:${region}:${account}:security-group/*`],
    }));

    remediateFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        's3:PutBucketPublicAccessBlock',
        's3:PutBucketEncryption',
      ],
      resources: [`arn:aws:s3:::*`],
      conditions: {
        StringEquals: { 'aws:ResourceAccount': account },
      },
    }));

    remediateFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ['securityhub:BatchUpdateFindings'],
      resources: [`arn:aws:securityhub:${region}:${account}:hub/default`],
    }));

    // =========================================================
    // 3. AWS Step Functions: Remediation Workflow
    // =========================================================

    // Remediate via Lambda
    const remediateTask = new sfnTasks.LambdaInvoke(this, 'RemediateFinding', {
      lambdaFunction: remediateFn,
      outputPath: '$.Payload',
      comment: 'Execute auto-remediation for the finding type',
    });

    // Notify security team
    const notifyTask = new sfnTasks.SnsPublish(this, 'NotifySecurityTeam', {
      topic: alertTopic,
      subject: sfn.JsonPath.format(
        'SecurityHub: {} remediated ({})',
        sfn.JsonPath.stringAt('$.remediationType'),
        sfn.JsonPath.stringAt('$.status'),
      ),
      message: sfn.TaskInput.fromJsonPathAt('$'),
      resultPath: '$.notification',
    });

    // Skip state for unsupported findings
    const skipUnsupported = new sfn.Pass(this, 'UnsupportedFinding', {
      result: sfn.Result.fromObject({ status: 'SKIPPED', reason: 'Finding type not supported for auto-remediation' }),
    });

    // Done
    const done = new sfn.Pass(this, 'RemediationComplete', {
      result: sfn.Result.fromObject({ status: 'COMPLETE' }),
    });

    // Route by finding type
    const definition = new sfn.Choice(this, 'ClassifyFinding')
      .when(
        sfn.Condition.or(
          sfn.Condition.stringMatches('$.detail.findings[0].Type', '*EC2*SecurityGroup*'),
          sfn.Condition.stringMatches('$.detail.findings[0].Type', '*Software and Configuration*'),
        ),
        remediateTask.next(notifyTask).next(done),
      )
      .when(
        sfn.Condition.stringMatches('$.detail.findings[0].Type', '*S3*PublicAccess*'),
        new sfnTasks.LambdaInvoke(this, 'RemediateS3Finding', {
          lambdaFunction: remediateFn,
          outputPath: '$.Payload',
        }).next(new sfnTasks.SnsPublish(this, 'NotifyS3Remediation', {
          topic: alertTopic,
          subject: sfn.JsonPath.format(
            'SecurityHub: {} remediated ({})',
            sfn.JsonPath.stringAt('$.remediationType'),
            sfn.JsonPath.stringAt('$.status'),
          ),
          message: sfn.TaskInput.fromJsonPathAt('$'),
          resultPath: '$.notification',
        })).next(new sfn.Pass(this, 'S3Done', {
          result: sfn.Result.fromObject({ status: 'COMPLETE' }),
        })),
      )
      .otherwise(skipUnsupported);

    const stateMachine = new sfn.StateMachine(this, 'RemediationWorkflow', {
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      timeout: cdk.Duration.minutes(10),
      tracingEnabled: true,
      logs: {
        destination: new logs.LogGroup(this, 'SfnLogGroup', {
          logGroupName: '/aws/stepfunctions/securityhub-remediation',
          retention: logs.RetentionDays.TWO_WEEKS,
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
        level: sfn.LogLevel.ALL,
      },
    });

    // =========================================================
    // 4. Amazon EventBridge Rule: Security Hub findings
    // =========================================================
    new events.Rule(this, 'SecurityHubFindingRule', {
      ruleName: 'securityhub-high-findings-to-sfn',
      description: 'Routes HIGH/CRITICAL AWS Security Hub findings to AWS Step Functions for auto-remediation',
      eventPattern: {
        source: ['aws.securityhub'],
        detailType: ['Security Hub Findings - Imported'],
        detail: {
          findings: {
            Severity: { Label: ['HIGH', 'CRITICAL'] },
            Workflow: { Status: ['NEW'] },
            RecordState: ['ACTIVE'],
          },
        },
      },
      targets: [new targets.SfnStateMachine(stateMachine)],
    });

    // =========================================================
    // Outputs
    // =========================================================
    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.stateMachineArn,
      description: 'AWS Step Functions remediation workflow ARN',
    });

    new cdk.CfnOutput(this, 'AlertTopicArn', {
      value: alertTopic.topicArn,
      description: 'Amazon SNS security alert topic ARN',
    });

    new cdk.CfnOutput(this, 'RemediateFunctionArn', {
      value: remediateFn.functionArn,
      description: 'AWS Lambda remediation function ARN',
    });
  }
}
