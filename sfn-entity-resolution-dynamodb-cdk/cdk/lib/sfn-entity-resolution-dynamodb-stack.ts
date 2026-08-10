// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
// 2026

import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as events from 'aws-cdk-lib/aws-events';
import * as events_targets from 'aws-cdk-lib/aws-events-targets';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as glue from 'aws-cdk-lib/aws-glue';

export class SfnEntityResolutionDynamodbStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Source data bucket (upload CSV/JSON records here for matching)
    const sourceBucket = new s3.Bucket(this, 'SourceDataBucket', {
      bucketName: `entity-resolution-source-${cdk.Aws.ACCOUNT_ID}-${cdk.Aws.REGION}`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      eventBridgeEnabled: true,
    });

    // Output bucket (Entity Resolution writes matched results here)
    const outputBucket = new s3.Bucket(this, 'OutputBucket', {
      bucketName: `entity-resolution-output-${cdk.Aws.ACCOUNT_ID}-${cdk.Aws.REGION}`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
    });

    // DynamoDB table for matched entity results
    const matchResultsTable = new dynamodb.Table(this, 'MatchResultsTable', {
      tableName: 'EntityMatchResults',
      partitionKey: { name: 'matchId', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'sourceRecordId', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // AWS Glue database and table for Entity Resolution schema mapping
    const glueDatabase = new glue.CfnDatabase(this, 'GlueDatabase', {
      catalogId: cdk.Aws.ACCOUNT_ID,
      databaseInput: {
        name: 'entity_resolution_db',
        description: 'Database for AWS Entity Resolution schema mapping',
      },
    });

    const glueTable = new glue.CfnTable(this, 'GlueTable', {
      catalogId: cdk.Aws.ACCOUNT_ID,
      databaseName: 'entity_resolution_db',
      tableInput: {
        name: 'customer_records',
        description: 'Customer records for entity matching',
        storageDescriptor: {
          columns: [
            { name: 'record_id', type: 'string' },
            { name: 'full_name', type: 'string' },
            { name: 'email', type: 'string' },
            { name: 'phone', type: 'string' },
            { name: 'address', type: 'string' },
          ],
          location: `s3://${sourceBucket.bucketName}/records/`,
          inputFormat: 'org.apache.hadoop.mapred.TextInputFormat',
          outputFormat: 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
          serdeInfo: {
            serializationLibrary: 'org.openx.data.jsonserde.JsonSerDe',
          },
        },
        tableType: 'EXTERNAL_TABLE',
      },
    });
    glueTable.addDependency(glueDatabase);

    // IAM Role for Entity Resolution
    const entityResolutionRole = new iam.Role(this, 'EntityResolutionRole', {
      assumedBy: new iam.ServicePrincipal('entityresolution.amazonaws.com'),
      description: 'Role for AWS Entity Resolution to access source and output data',
    });

    sourceBucket.grantRead(entityResolutionRole);
    outputBucket.grantWrite(entityResolutionRole);

    entityResolutionRole.addToPolicy(new iam.PolicyStatement({
      actions: ['glue:GetTable', 'glue:GetDatabase'],
      resources: [
        `arn:aws:glue:${cdk.Aws.REGION}:${cdk.Aws.ACCOUNT_ID}:catalog`,
        `arn:aws:glue:${cdk.Aws.REGION}:${cdk.Aws.ACCOUNT_ID}:database/entity_resolution_db`,
        `arn:aws:glue:${cdk.Aws.REGION}:${cdk.Aws.ACCOUNT_ID}:table/entity_resolution_db/customer_records`,
      ],
    }));

    // Entity Resolution Schema Mapping
    const schemaMapping = new cdk.CfnResource(this, 'SchemaMapping', {
      type: 'AWS::EntityResolution::SchemaMapping',
      properties: {
        SchemaName: 'CustomerSchemaMapping',
        Description: 'Schema mapping for customer record matching',
        MappedInputFields: [
          { FieldName: 'record_id', Type: 'UNIQUE_ID' },
          { FieldName: 'full_name', Type: 'NAME', SubType: 'FULL' },
          { FieldName: 'email', Type: 'EMAIL_ADDRESS' },
          { FieldName: 'phone', Type: 'PHONE_NUMBER' },
          { FieldName: 'address', Type: 'ADDRESS', SubType: 'FULL' },
        ],
      },
    });

    // Entity Resolution Matching Workflow
    const matchingWorkflow = new cdk.CfnResource(this, 'MatchingWorkflow', {
      type: 'AWS::EntityResolution::MatchingWorkflow',
      properties: {
        WorkflowName: 'CustomerMatchingWorkflow',
        Description: 'Match customer records to identify duplicate entities',
        InputSourceConfig: [
          {
            InputSourceARN: `arn:aws:glue:${cdk.Aws.REGION}:${cdk.Aws.ACCOUNT_ID}:table/entity_resolution_db/customer_records`,
            SchemaArn: schemaMapping.getAtt('SchemaArn'),
          },
        ],
        OutputSourceConfig: [
          {
            OutputS3Path: `s3://${outputBucket.bucketName}/matched-results/`,
            Output: [
              { Name: 'record_id', Hashed: false },
              { Name: 'full_name', Hashed: false },
              { Name: 'email', Hashed: false },
            ],
          },
        ],
        ResolutionTechniques: {
          ResolutionType: 'ML_MATCHING',
        },
        RoleArn: entityResolutionRole.roleArn,
      },
    });
    matchingWorkflow.addDependency(glueTable);

    // Step Functions state machine
    // Step 1: Start the matching job
    const startMatchingJob = new tasks.CallAwsService(this, 'StartMatchingJob', {
      service: 'entityresolution',
      action: 'startMatchingJob',
      parameters: {
        WorkflowName: 'CustomerMatchingWorkflow',
      },
      iamResources: [`arn:aws:entityresolution:${cdk.Aws.REGION}:${cdk.Aws.ACCOUNT_ID}:matchingworkflow/CustomerMatchingWorkflow`],
      resultPath: '$.matchingJob',
    });

    // Step 2: Wait for job completion
    const waitForJob = new sfn.Wait(this, 'WaitForJobCompletion', {
      time: sfn.WaitTime.duration(cdk.Duration.seconds(30)),
    });

    // Step 3: Check job status
    const getJobStatus = new tasks.CallAwsService(this, 'GetMatchingJob', {
      service: 'entityresolution',
      action: 'getMatchingJob',
      parameters: {
        WorkflowName: 'CustomerMatchingWorkflow',
        'JobId.$': '$.matchingJob.JobId',
      },
      iamResources: [`arn:aws:entityresolution:${cdk.Aws.REGION}:${cdk.Aws.ACCOUNT_ID}:matchingworkflow/CustomerMatchingWorkflow`],
      resultPath: '$.jobStatus',
    });

    // Step 4: Store results in DynamoDB
    const storeResults = new tasks.DynamoPutItem(this, 'StoreMatchResults', {
      table: matchResultsTable,
      item: {
        matchId: tasks.DynamoAttributeValue.fromString(sfn.JsonPath.stringAt('$.matchingJob.JobId')),
        sourceRecordId: tasks.DynamoAttributeValue.fromString(sfn.JsonPath.format('job-{}', sfn.JsonPath.stringAt('$.matchingJob.JobId'))),
        status: tasks.DynamoAttributeValue.fromString(sfn.JsonPath.stringAt('$.jobStatus.Status')),
        outputPath: tasks.DynamoAttributeValue.fromString(
          sfn.JsonPath.format('s3://{}/matched-results/', outputBucket.bucketName)
        ),
        completedAt: tasks.DynamoAttributeValue.fromString(sfn.JsonPath.stringAt('$$.State.EnteredTime')),
      },
      resultPath: '$.dynamoResult',
    });

    // Job success path
    const jobSucceeded = new sfn.Succeed(this, 'MatchingJobComplete', {
      comment: 'Entity matching job completed successfully',
    });

    // Job failed path
    const jobFailed = new sfn.Fail(this, 'MatchingJobFailed', {
      error: 'MatchingJobFailed',
      cause: 'The AWS Entity Resolution matching job failed',
    });

    // Check status choice
    const isJobComplete = new sfn.Choice(this, 'IsJobComplete')
      .when(
        sfn.Condition.stringEquals('$.jobStatus.Status', 'SUCCEEDED'),
        storeResults.next(jobSucceeded)
      )
      .when(
        sfn.Condition.stringEquals('$.jobStatus.Status', 'FAILED'),
        jobFailed
      )
      .otherwise(waitForJob);

    // Wire the state machine
    const definition = startMatchingJob
      .next(waitForJob)
      .next(getJobStatus)
      .next(isJobComplete);

    const stateMachine = new sfn.StateMachine(this, 'EntityResolutionStateMachine', {
      stateMachineName: 'EntityResolutionOrchestrator',
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      timeout: cdk.Duration.hours(2),
    });

    // EventBridge rule: trigger when new data uploaded to source bucket
    const uploadRule = new events.Rule(this, 'NewDataUploadRule', {
      ruleName: 'EntityResolutionNewDataTrigger',
      description: 'Triggers entity matching when new records are uploaded to the source Amazon S3 bucket',
      eventPattern: {
        source: ['aws.s3'],
        detailType: ['Object Created'],
        detail: {
          bucket: {
            name: [sourceBucket.bucketName],
          },
          object: {
            key: [{ prefix: 'records/' }],
          },
        },
      },
    });

    uploadRule.addTarget(new events_targets.SfnStateMachine(stateMachine));

    // Outputs
    new cdk.CfnOutput(this, 'SourceBucketName', {
      value: sourceBucket.bucketName,
      description: 'Upload customer records (JSON) to the records/ prefix in this bucket',
    });

    new cdk.CfnOutput(this, 'OutputBucketName', {
      value: outputBucket.bucketName,
      description: 'Matched entity results are written here by AWS Entity Resolution',
    });

    new cdk.CfnOutput(this, 'MatchResultsTableName', {
      value: matchResultsTable.tableName,
      description: 'Amazon DynamoDB table storing match job metadata and results',
    });

    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.stateMachineArn,
      description: 'AWS Step Functions state machine orchestrating entity matching',
    });

    new cdk.CfnOutput(this, 'MatchingWorkflowName', {
      value: 'CustomerMatchingWorkflow',
      description: 'AWS Entity Resolution matching workflow name',
    });
  }
}
