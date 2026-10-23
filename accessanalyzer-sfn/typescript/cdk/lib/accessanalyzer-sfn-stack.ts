// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import {
  Annotations,
  CfnOutput,
  Duration,
  RemovalPolicy,
  Stack,
  StackProps,
  Token,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as kms from 'aws-cdk-lib/aws-kms';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as sqs from 'aws-cdk-lib/aws-sqs';

// IAM management events are delivered in this Region (see the README).
const IAM_EVENTS_REGION = 'us-east-1';
const RESOURCE_NAME = 'accessanalyzer-policy-guardrail';

// Access that an inline role policy must not grant. The list is explicit
// because the API documentation does not say whether wildcards are allowed in
// the actions of the access object. A FAIL means the policy might allow at
// least one of these actions on any resource in the policy.
const ACTIONS_THAT_MUST_NOT_BE_GRANTED = [
  'iam:AttachRolePolicy',
  'iam:AttachUserPolicy',
  'iam:CreateAccessKey',
  'iam:CreateLoginProfile',
  'iam:CreatePolicyVersion',
  'iam:PassRole',
  'iam:PutRolePolicy',
  'iam:PutUserPolicy',
  'iam:SetDefaultPolicyVersion',
  'iam:UpdateAssumeRolePolicy',
  'iam:UpdateLoginProfile',
];

/**
 * Amazon EventBridge -> AWS Step Functions -> IAM Access Analyzer -> Amazon SNS.
 *
 * An IAM PutRolePolicy call on a role whose name starts with a configured
 * prefix starts a workflow. The workflow passes the policy document from the
 * CloudTrail event to the Access Analyzer CheckAccessNotGranted API and
 * notifies when the result is FAIL. Removing the inline policy is an opt-in
 * (context enableRemediation=true) and is limited to the same role-name prefix.
 */
export class AccessAnalyzerSfnStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    if (!Token.isUnresolved(this.region) && this.region !== IAM_EVENTS_REGION) {
      Annotations.of(this).addWarning(
        `IAM events are delivered in ${IAM_EVENTS_REGION}. In ${this.region} the rule never matches. Deploy this stack in ${IAM_EVENTS_REGION}.`,
      );
    }

    const prefix = String(this.node.tryGetContext('roleNamePrefix') ?? 'guardrail-demo-');
    if (!/^[A-Za-z0-9_+=,.@-]{4,40}$/.test(prefix)) {
      throw new Error('roleNamePrefix must be 4 to 40 IAM role name characters and contain no wildcard');
    }
    const remediate = String(this.node.tryGetContext('enableRemediation')).toLowerCase() === 'true';

    // Amazon SNS topic, encrypted with the AWS managed key, TLS only.
    const topic = new sns.Topic(this, 'Topic', {
      displayName: 'IAM policy check results',
      masterKey: kms.Alias.fromAliasName(this, 'SnsManagedKey', 'alias/aws/sns'),
      enforceSSL: true,
    });

    // Reads the CloudTrail event that EventBridge passes in as the input.
    const eventPath = (field: string) => sfn.JsonPath.stringAt(`$.detail.${field}`);
    const notify = (stateId: string, subject: string, message: { [key: string]: unknown }) =>
      new tasks.SnsPublish(this, stateId, {
        topic,
        subject,
        message: sfn.TaskInput.fromObject({
          roleName: eventPath('requestParameters.roleName'),
          cloudTrailEventId: eventPath('eventID'),
          ...message,
        }),
      });

    // 1) The check. The policy document goes straight from the event to the API.
    const check = new tasks.CallAwsService(this, 'CheckAccessNotGranted', {
      service: 'accessanalyzer',
      action: 'checkAccessNotGranted',
      parameters: {
        PolicyDocument: eventPath('requestParameters.policyDocument'),
        PolicyType: 'IDENTITY_POLICY',
        Access: [{ Actions: ACTIONS_THAT_MUST_NOT_BE_GRANTED }],
      },
      // The IAM action prefix is access-analyzer, not the SDK service name.
      // The API takes no resource, so the statement needs Resource "*".
      iamAction: 'access-analyzer:CheckAccessNotGranted',
      iamResources: ['*'],
      resultPath: '$.check',
    });
    // Permanent errors first, with no retry. Then only transient errors.
    check.addRetry({
      errors: [
        'AccessAnalyzer.AccessDeniedException',
        'AccessAnalyzer.InvalidParameterException',
        'AccessAnalyzer.UnprocessableEntityException',
        'AccessAnalyzer.ValidationException',
      ],
      maxAttempts: 0,
    });
    check.addRetry({
      errors: ['AccessAnalyzer.InternalServerException', 'AccessAnalyzer.ThrottlingException'],
      interval: Duration.seconds(2),
      maxAttempts: 3,
      backoffRate: 2,
    });

    // 2) Policies that cannot be evaluated are reported, never silently passed.
    // MarkNotEvaluated is used by the Choice states, which have no error of
    // their own. A failed API call goes to the notification directly, so the
    // Access Analyzer error stays in $.error and reaches the message.
    const markNotEvaluated = new sfn.Pass(this, 'MarkNotEvaluated', {
      result: sfn.Result.fromObject({
        Error: 'PolicyNotEvaluated',
        Cause: 'The event has no policy document string, or the result was not PASS or FAIL.',
      }),
      resultPath: '$.error',
    });
    const notifyNotEvaluated = notify('NotifyNotEvaluated', 'IAM policy could not be checked', {
      status: 'POLICY_NOT_EVALUATED',
      error: sfn.JsonPath.objectAt('$.error'),
    });
    markNotEvaluated.next(notifyNotEvaluated).next(
      new sfn.Fail(this, 'PolicyNotEvaluated', {
        error: 'PolicyNotEvaluated',
        cause: 'The policy document could not be checked. See the Amazon SNS notification.',
      }),
    );
    check.addCatch(notifyNotEvaluated, { resultPath: '$.error' });

    // 3) FAIL: notify only, or remove the inline policy when opted in.
    const violation = {
      policyName: eventPath('requestParameters.policyName'),
      accessAnalyzerResult: sfn.JsonPath.objectAt('$.check'),
    };
    const notifyViolation = notify('NotifyViolation', 'IAM policy grants blocked access', {
      status: 'POLICY_FAILS_CHECK',
      policyRemoved: false,
      ...violation,
    });
    let onFail: sfn.IChainable = notifyViolation;
    if (remediate) {
      // A States.ALL Catch does not catch States.Runtime, so the next two
      // states only reference fields the rule pattern guarantees.
      const removePolicy = new tasks.CallAwsService(this, 'RemoveInlinePolicy', {
        service: 'iam',
        action: 'deleteRolePolicy',
        parameters: {
          RoleName: eventPath('requestParameters.roleName'),
          PolicyName: eventPath('requestParameters.policyName'),
        },
        iamAction: 'iam:DeleteRolePolicy',
        // Wildcard suffix: only roles whose name starts with the prefix.
        iamResources: [`arn:${this.partition}:iam::${this.account}:role/${prefix}*`],
        resultPath: '$.removed',
      });
      removePolicy.addRetry({ errors: ['Iam.ServiceFailureException'], interval: Duration.seconds(2), maxAttempts: 3 });
      removePolicy.addCatch(
        notify('NotifyRemovalFailed', 'IAM policy removal failed', {
          status: 'POLICY_REMOVAL_FAILED',
          error: sfn.JsonPath.objectAt('$.error'),
          ...violation,
        }).next(new sfn.Fail(this, 'RemovalFailed', { error: 'RemovalFailed', cause: 'DeleteRolePolicy failed.' })),
        { resultPath: '$.error' },
      );
      removePolicy.next(notify('NotifyRemoved', 'IAM policy removed', { status: 'POLICY_REMOVED', policyRemoved: true, ...violation }));
      onFail = new sfn.Choice(this, 'RoleInPrefixScope')
        .when(sfn.Condition.stringMatches('$.detail.requestParameters.roleName', `${prefix}*`), removePolicy)
        .otherwise(notifyViolation);
    }

    // 4) Decide. isPresent guards keep a missing field from raising States.Runtime.
    const definition = new sfn.Choice(this, 'HasPolicyDocument')
      .when(
        sfn.Condition.and(
          sfn.Condition.isPresent('$.detail.requestParameters.policyDocument'),
          sfn.Condition.isString('$.detail.requestParameters.policyDocument'),
        ),
        check.next(
          new sfn.Choice(this, 'EvaluateResult')
            .when(
              sfn.Condition.and(sfn.Condition.isPresent('$.check.Result'), sfn.Condition.stringEquals('$.check.Result', 'PASS')),
              new sfn.Succeed(this, 'PolicyCompliant'),
            )
            .when(
              sfn.Condition.and(sfn.Condition.isPresent('$.check.Result'), sfn.Condition.stringEquals('$.check.Result', 'FAIL')),
              onFail,
            )
            .otherwise(markNotEvaluated),
        ),
      )
      .otherwise(markNotEvaluated);

    const logGroup = new logs.LogGroup(this, 'StateMachineLogs', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });
    const stateMachineArn = `arn:${this.partition}:states:${this.region}:${this.account}:stateMachine:${RESOURCE_NAME}`;
    const stateMachine = new sfn.StateMachine(this, 'StateMachine', {
      stateMachineName: RESOURCE_NAME,
      stateMachineType: sfn.StateMachineType.STANDARD,
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      role: new iam.Role(this, 'StateMachineRole', {
        assumedBy: new iam.ServicePrincipal('states.amazonaws.com').withConditions({
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': stateMachineArn },
        }),
      }),
      timeout: Duration.minutes(5),
      logs: { destination: logGroup, level: sfn.LogLevel.ALL, includeExecutionData: false },
    });

    // 5) The rule: successful PutRolePolicy calls on roles with the prefix.
    const ruleArn = `arn:${this.partition}:events:${this.region}:${this.account}:rule/${RESOURCE_NAME}`;
    const invokeRole = new iam.Role(this, 'RuleInvokeRole', {
      assumedBy: new iam.ServicePrincipal('events.amazonaws.com').withConditions({
        StringEquals: { 'aws:SourceAccount': this.account },
        ArnLike: { 'aws:SourceArn': ruleArn },
      }),
    });
    const rule = new events.Rule(this, 'PutRolePolicyRule', {
      ruleName: RESOURCE_NAME,
      description: 'Successful IAM PutRolePolicy calls on roles whose name starts with the configured prefix',
      eventPattern: {
        source: ['aws.iam'],
        detailType: ['AWS API Call via CloudTrail'],
        detail: {
          eventSource: ['iam.amazonaws.com'],
          eventName: ['PutRolePolicy'],
          errorCode: events.Match.doesNotExist(),
          // IAM role names are not case sensitive, so the prefix is not either.
          requestParameters: { roleName: [{ prefix: { 'equals-ignore-case': prefix } }] },
        },
      },
    });
    rule.addTarget(
      new targets.SfnStateMachine(stateMachine, {
        role: invokeRole,
        deadLetterQueue: new sqs.Queue(this, 'RuleDeadLetterQueue', {
          retentionPeriod: Duration.days(14),
          enforceSSL: true,
          encryption: sqs.QueueEncryption.SQS_MANAGED,
        }),
      }),
    );

    new CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new CfnOutput(this, 'TopicArn', { value: topic.topicArn, description: 'Subscribe to receive results' });
    new CfnOutput(this, 'LogGroupName', { value: logGroup.logGroupName });
    new CfnOutput(this, 'RoleNamePrefix', { value: prefix });
    new CfnOutput(this, 'Mode', { value: remediate ? 'REMOVE_POLICY' : 'NOTIFY_ONLY' });
  }
}
