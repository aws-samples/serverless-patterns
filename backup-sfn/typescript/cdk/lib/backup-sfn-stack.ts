// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import { Stack, StackProps, RemovalPolicy, Duration, CfnOutput, Arn, ArnFormat } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as backup from 'aws-cdk-lib/aws-backup';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as sqs from 'aws-cdk-lib/aws-sqs';

// The restored table must hold at least this many items for the verdict to be SUCCESSFUL.
// The same number is used as the Scan Limit, so the check reads at most this many items.
const MIN_ITEMS = 3;
// Hours that AWS Backup keeps the restored table so the workflow can inspect it.
const VALIDATION_WINDOW_HOURS = 2;
// AWS Backup starts the restore test at a random time inside this window after the schedule fires.
const START_WINDOW_HOURS = 1;

export class BackupSfnStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Schedule of the restore test (UTC). Override with: cdk deploy -c restoreTestCron="cron(30 14 * * ? *)"
    const restoreTestCron: string = this.node.tryGetContext('restoreTestCron') ?? 'cron(0 5 ? * * *)';

    // ---- Source table, backup vault and the roles AWS Backup assumes -------------------------
    const table = new dynamodb.Table(this, 'SourceTable', {
      partitionKey: { name: 'pk', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY, // demo only
      deletionProtection: false,
    });

    // A vault that holds recovery points cannot be deleted. See Cleanup in the README.
    const vault = new backup.BackupVault(this, 'Vault', { removalPolicy: RemovalPolicy.DESTROY });

    const backupRole = new iam.Role(this, 'BackupRole', {
      assumedBy: new iam.ServicePrincipal('backup.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSBackupServiceRolePolicyForBackup'),
      ],
    });
    const restoreRole = new iam.Role(this, 'RestoreRole', {
      assumedBy: new iam.ServicePrincipal('backup.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSBackupServiceRolePolicyForRestores'),
      ],
    });

    // ---- AWS Backup restore testing (L1 only: there is no L2 construct yet) -----------------
    const plan = new backup.CfnRestoreTestingPlan(this, 'RestoreTestingPlan', {
      restoreTestingPlanName: 'sfn_validated_restore_test', // letters, digits and underscores only
      scheduleExpression: restoreTestCron,
      startWindowHours: START_WINDOW_HOURS,
      recoveryPointSelection: {
        algorithm: 'LATEST_WITHIN_WINDOW',
        recoveryPointTypes: ['SNAPSHOT'],
        includeVaults: [vault.backupVaultArn],
        selectionWindowDays: 1,
      },
    });
    const selection = new backup.CfnRestoreTestingSelection(this, 'RestoreTestingSelection', {
      restoreTestingSelectionName: 'source_table',
      restoreTestingPlanName: plan.restoreTestingPlanName,
      protectedResourceType: 'DynamoDB',
      protectedResourceArns: [table.tableArn],
      iamRoleArn: restoreRole.roleArn,
      validationWindowHours: VALIDATION_WINDOW_HOURS,
    });
    // The selection refers to the plan by its plain-string name, so CloudFormation sees no dependency by itself.
    selection.addResourceDependency(plan);

    // ---- Validation workflow -----------------------------------------------------------------
    // PutRestoreValidationResult is called exactly once per restore job: every branch ends in
    // one terminal write (SUCCESSFUL or FAILED), and a failed write never triggers another write.
    const putVerdict = (id: string, status: 'SUCCESSFUL' | 'FAILED', message: string) => {
      const task = new tasks.CallAwsService(this, id, {
        service: 'backup',
        action: 'putRestoreValidationResult',
        parameters: {
          RestoreJobId: sfn.JsonPath.stringAt('$.detail.restoreJobId'),
          ValidationStatus: status,
          ValidationStatusMessage: message,
        },
        iamAction: 'backup:PutRestoreValidationResult',
        // This action does not support resource-level permissions, so the resource must be "*".
        iamResources: ['*'],
        resultPath: sfn.JsonPath.DISCARD,
      });
      task.addRetry({ errors: ['Backup.InvalidParameterValueException', 'Backup.InvalidRequestException',
        'Backup.MissingParameterValueException', 'Backup.ResourceNotFoundException', 'States.Permissions'], maxAttempts: 0 });
      task.addRetry({ errors: ['Backup.ServiceUnavailableException'], interval: Duration.seconds(2), maxAttempts: 3 });
      task.addCatch(notRecorded, { resultPath: '$.putError' });
      return task;
    };
    const notRecorded = new sfn.Fail(this, 'ValidationNotRecorded', {
      error: 'ValidationNotRecorded',
      cause: 'AWS Backup did not accept the validation result for this restore job.',
    });
    const recorded = new sfn.Succeed(this, 'VerdictRecorded');
    const success = putVerdict('PutSuccessful', 'SUCCESSFUL',
      sfn.JsonPath.format('Restored table {} holds at least {} items.', sfn.JsonPath.stringAt('$.restored.tableName'), String(MIN_ITEMS)));
    const tooFew = putVerdict('PutFailedTooFewItems', 'FAILED',
      sfn.JsonPath.format('Restored table {} holds fewer than {} items.', sfn.JsonPath.stringAt('$.restored.tableName'), String(MIN_ITEMS)));
    const scanFailed = putVerdict('PutFailedScanError', 'FAILED',
      sfn.JsonPath.format('The restored table could not be read: {}', sfn.JsonPath.stringAt('$.error.Error')));
    const noTable = putVerdict('PutFailedNoTable', 'FAILED', 'The restore job event carries no DynamoDB table ARN.');
    [success, tooFew, scanFailed, noTable].forEach((t) => t.next(recorded));

    // The table name is the last segment of createdResourceArn (arn:...:table/<name>).
    const extractName = new sfn.Pass(this, 'ExtractTableName', {
      parameters: {
        tableName: sfn.JsonPath.arrayGetItem(
          sfn.JsonPath.stringSplit(sfn.JsonPath.stringAt('$.detail.createdResourceArn'), '/'), 1),
      },
      resultPath: '$.restored',
    });

    // Scan with Select=COUNT and Limit=MIN_ITEMS reads at most MIN_ITEMS items. DescribeTable ItemCount
    // is refreshed only about every six hours, so it cannot be used on a freshly restored table.
    const scan = new tasks.CallAwsService(this, 'CountRestoredItems', {
      service: 'dynamodb',
      action: 'scan',
      parameters: {
        TableName: sfn.JsonPath.stringAt('$.restored.tableName'),
        Select: 'COUNT',
        Limit: MIN_ITEMS,
        ConsistentRead: true,
      },
      iamAction: 'dynamodb:Scan',
      iamResources: [this.formatArn({ service: 'dynamodb', resource: 'table', resourceName: 'awsbackup-restore-test-*' })],
      resultPath: '$.scan',
    });
    scan.addRetry({ errors: ['DynamoDb.ResourceNotFoundException', 'DynamoDb.AccessDeniedException', 'States.Permissions'], maxAttempts: 0 });
    scan.addRetry({ errors: ['DynamoDb.ProvisionedThroughputExceededException', 'DynamoDb.RequestLimitExceeded',
      'DynamoDb.ThrottlingException', 'DynamoDb.InternalServerError'], interval: Duration.seconds(2), maxAttempts: 3 });
    scan.addCatch(scanFailed, { resultPath: '$.error' });

    // Guard every optional path with isPresent: a States.ALL catch does not catch States.Runtime.
    const definition = new sfn.Choice(this, 'HasRestoreJobId')
      .when(sfn.Condition.isNotPresent('$.detail.restoreJobId'), new sfn.Fail(this, 'InvalidEvent', {
        error: 'InvalidEvent', cause: 'The event has no detail.restoreJobId, so no result can be recorded.' }))
      .otherwise(new sfn.Choice(this, 'HasTableArn')
        .when(sfn.Condition.and(
          sfn.Condition.isPresent('$.detail.createdResourceArn'),
          sfn.Condition.isString('$.detail.createdResourceArn'),
          sfn.Condition.stringMatches('$.detail.createdResourceArn', 'arn:*:dynamodb:*:table/*')),
        extractName.next(scan).next(new sfn.Choice(this, 'EnoughItems')
          .when(sfn.Condition.and(sfn.Condition.isPresent('$.scan.Count'),
            sfn.Condition.numberGreaterThanEquals('$.scan.Count', MIN_ITEMS)), success)
          .otherwise(tooFew)))
        .otherwise(noTable));

    const logGroup = new logs.LogGroup(this, 'StateMachineLogs', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY, // demo only
    });
    const smRole = new iam.Role(this, 'StateMachineRole', {
      assumedBy: new iam.ServicePrincipal('states.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': Arn.format({ service: 'states', resource: 'stateMachine', resourceName: '*',
            arnFormat: ArnFormat.COLON_RESOURCE_NAME }, this) },
        },
      }),
    });
    const stateMachine = new sfn.StateMachine(this, 'ValidationStateMachine', {
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      role: smRole,
      timeout: Duration.minutes(5),
      logs: { destination: logGroup, level: sfn.LogLevel.ALL, includeExecutionData: true },
    });

    // ---- EventBridge rule: only COMPLETED restore jobs of this plan, only for DynamoDB --------
    const dlq = new sqs.Queue(this, 'RuleDlq', {
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      enforceSSL: true,
      retentionPeriod: Duration.days(14),
    });
    new events.Rule(this, 'RestoreJobCompletedRule', {
      description: 'Start the validation workflow when a restore job of the restore testing plan completes',
      eventPattern: {
        source: ['aws.backup'],
        detailType: ['Restore Job State Change'],
        detail: {
          status: ['COMPLETED'],
          // AWS Backup reports the type of a DynamoDB restore job as "DynamoDB.FullyManaged" in this event,
          // so an exact match on "DynamoDB" never matches. The prefix covers both spellings.
          resourceType: [{ prefix: 'DynamoDB' }],
          restoreTestingPlanArn: [plan.attrRestoreTestingPlanArn],
        },
      },
      targets: [new targets.SfnStateMachine(stateMachine, { deadLetterQueue: dlq, retryAttempts: 3 })],
    });

    new CfnOutput(this, 'TableName', { value: table.tableName, description: 'Seed a few items here before the backup' });
    new CfnOutput(this, 'TableArn', { value: table.tableArn });
    new CfnOutput(this, 'VaultName', { value: vault.backupVaultName });
    new CfnOutput(this, 'BackupRoleArn', { value: backupRole.roleArn, description: 'Use as --iam-role-arn for the on-demand backup' });
    new CfnOutput(this, 'RestoreTestingPlanArn', { value: plan.attrRestoreTestingPlanArn });
    new CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new CfnOutput(this, 'StateMachineLogGroup', { value: logGroup.logGroupName });
  }
}
