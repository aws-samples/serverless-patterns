// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import {
  Stack,
  StackProps,
  RemovalPolicy,
  Duration,
  Aws,
  CfnOutput,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cr from 'aws-cdk-lib/custom-resources';
import * as glue from 'aws-cdk-lib/aws-glue';
import * as athena from 'aws-cdk-lib/aws-athena';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as apigw from 'aws-cdk-lib/aws-apigateway';

/**
 * Amazon API Gateway (REST) -> AWS Step Functions Express Workflow (synchronous
 * StartSyncExecution) -> Amazon Athena (StartQueryExecution + GetQueryResults via
 * native Step Functions service integrations) -> results returned to the caller in
 * a single request/response. ZERO AWS Lambda functions.
 */
export class ApigwSfnExpressAthenaStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const dataPrefix = 'data/';
    const resultsPrefix = 'athena-results/';

    // ---------------------------------------------------------------------
    // Amazon S3 bucket: sample dataset (data/) + Athena query results
    // (athena-results/). Encrypted with S3-managed keys, TLS enforced,
    // public access fully blocked.
    // ---------------------------------------------------------------------
    const dataBucket = new s3.Bucket(this, 'DataBucket', {
      encryption: s3.BucketEncryption.S3_MANAGED,
      enforceSSL: true,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      // WARNING: DESTROY + autoDeleteObjects deletes the bucket and all data
      // (sample dataset AND query results) on `cdk destroy`. See README.
      removalPolicy: RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // Seed a tiny sample CSV dataset into the data/ prefix so the pattern is
    // queryable immediately after deploy with no manual data-loading step.
    // Uses an AwsCustomResource calling s3:PutObject with the CSV inline —
    // no asset bundling or bundled-CLI download (more robust than
    // BucketDeployment across build hosts).
    const seedData = new cr.AwsCustomResource(this, 'SampleDataDeployment', {
      onCreate: {
        service: 'S3',
        action: 'putObject',
        parameters: {
          Bucket: dataBucket.bucketName,
          Key: `${dataPrefix}orders.csv`,
          Body: SAMPLE_CSV,
          ContentType: 'text/csv',
        },
        physicalResourceId: cr.PhysicalResourceId.of(`${dataPrefix}orders.csv`),
      },
      onUpdate: {
        service: 'S3',
        action: 'putObject',
        parameters: {
          Bucket: dataBucket.bucketName,
          Key: `${dataPrefix}orders.csv`,
          Body: SAMPLE_CSV,
          ContentType: 'text/csv',
        },
        physicalResourceId: cr.PhysicalResourceId.of(`${dataPrefix}orders.csv`),
      },
      policy: cr.AwsCustomResourcePolicy.fromStatements([
        new iam.PolicyStatement({
          actions: ['s3:PutObject'],
          resources: [`${dataBucket.bucketArn}/${dataPrefix}*`],
        }),
      ]),
    });
    seedData.node.addDependency(dataBucket);

    // ---------------------------------------------------------------------
    // AWS Glue database + external table over the CSV data in Amazon S3.
    // The table schema is declared in CDK so Athena can query it directly.
    // ---------------------------------------------------------------------
    const glueDb = new glue.CfnDatabase(this, 'GlueDatabase', {
      catalogId: Aws.ACCOUNT_ID,
      databaseInput: {
        name: `orders_db_${Aws.ACCOUNT_ID}`,
        description: 'Sample database for the apigw-sfn-express-athena pattern',
      },
    });

    const glueTable = new glue.CfnTable(this, 'GlueTable', {
      catalogId: Aws.ACCOUNT_ID,
      databaseName: `orders_db_${Aws.ACCOUNT_ID}`,
      tableInput: {
        name: 'orders',
        description: 'Sample orders table backed by CSV in Amazon S3',
        tableType: 'EXTERNAL_TABLE',
        parameters: {
          classification: 'csv',
          'skip.header.line.count': '1',
          areColumnsQuoted: 'false',
        },
        storageDescriptor: {
          columns: [
            { name: 'order_id', type: 'string' },
            { name: 'customer', type: 'string' },
            { name: 'product', type: 'string' },
            { name: 'quantity', type: 'int' },
            { name: 'amount', type: 'double' },
            { name: 'order_date', type: 'string' },
          ],
          location: `s3://${dataBucket.bucketName}/${dataPrefix}`,
          inputFormat: 'org.apache.hadoop.mapred.TextInputFormat',
          outputFormat:
            'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
          serdeInfo: {
            serializationLibrary:
              'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
            parameters: {
              'field.delim': ',',
              'serialization.format': ',',
            },
          },
        },
      },
    });
    glueTable.addDependency(glueDb);

    // ---------------------------------------------------------------------
    // Amazon Athena workgroup with the results location pinned to the
    // athena-results/ prefix and results encrypted with SSE-S3.
    // ---------------------------------------------------------------------
    const workgroupName = `apigw-sfn-express-athena-${Aws.ACCOUNT_ID}`;
    const workgroup = new athena.CfnWorkGroup(this, 'AthenaWorkgroup', {
      name: workgroupName,
      recursiveDeleteOption: true,
      workGroupConfiguration: {
        enforceWorkGroupConfiguration: true,
        publishCloudWatchMetricsEnabled: true,
        resultConfiguration: {
          outputLocation: `s3://${dataBucket.bucketName}/${resultsPrefix}`,
          encryptionConfiguration: { encryptionOption: 'SSE_S3' },
        },
      },
    });

    // ARN helpers scoped to THIS account/region (no hardcoded account IDs).
    const workgroupArn = `arn:${Aws.PARTITION}:athena:${Aws.REGION}:${Aws.ACCOUNT_ID}:workgroup/${workgroupName}`;
    const catalogArn = `arn:${Aws.PARTITION}:glue:${Aws.REGION}:${Aws.ACCOUNT_ID}:catalog`;
    const databaseArn = `arn:${Aws.PARTITION}:glue:${Aws.REGION}:${Aws.ACCOUNT_ID}:database/orders_db_${Aws.ACCOUNT_ID}`;
    const tableArn = `arn:${Aws.PARTITION}:glue:${Aws.REGION}:${Aws.ACCOUNT_ID}:table/orders_db_${Aws.ACCOUNT_ID}/orders`;

    // ---------------------------------------------------------------------
    // Step Functions EXPRESS state machine.
    //   StartQueryExecution (REQUEST_RESPONSE) -> Wait -> GetQueryExecution
    //   -> Choice(status) -> GetQueryResults -> FormatResponse
    // Express workflows do NOT support the '.sync' (RUN_JOB) Athena
    // integration, so we start the query, then poll its status in a
    // Wait/Choice loop until it reaches SUCCEEDED before fetching results.
    // All native Step Functions service integrations -> no AWS Lambda.
    // ---------------------------------------------------------------------
    const startQuery = new tasks.AthenaStartQueryExecution(this, 'StartAthenaQuery', {
      // REQUEST_RESPONSE returns immediately with a QueryExecutionId. Express
      // state machines only support this integration pattern for Athena.
      integrationPattern: sfn.IntegrationPattern.REQUEST_RESPONSE,
      queryString: sfn.JsonPath.stringAt('$.queryString'),
      workGroup: workgroupName,
      queryExecutionContext: {
        databaseName: `orders_db_${Aws.ACCOUNT_ID}`,
      },
      resultPath: '$.queryExecution',
    });

    // Retry transient Athena throttling/service errors, then Catch any
    // remaining failure and surface a clean error payload to the caller.
    startQuery.addRetry({
      errors: ['Athena.AthenaException', 'States.TaskFailed'],
      interval: Duration.seconds(2),
      maxAttempts: 3,
      backoffRate: 2,
    });

    // Poll the query status: Wait -> GetQueryExecution -> Choice.
    const waitForQuery = new sfn.Wait(this, 'WaitForQuery', {
      time: sfn.WaitTime.duration(Duration.seconds(2)),
    });

    const getQueryExecution = new tasks.CallAwsService(this, 'GetQueryExecution', {
      service: 'athena',
      action: 'getQueryExecution',
      parameters: {
        QueryExecutionId: sfn.JsonPath.stringAt(
          '$.queryExecution.QueryExecutionId',
        ),
      },
      iamResources: [workgroupArn],
      resultPath: '$.queryStatus',
    });
    getQueryExecution.addRetry({
      errors: ['Athena.AthenaException', 'States.TaskFailed'],
      interval: Duration.seconds(2),
      maxAttempts: 3,
      backoffRate: 2,
    });

    const getResults = new tasks.AthenaGetQueryResults(this, 'GetAthenaResults', {
      queryExecutionId: sfn.JsonPath.stringAt(
        '$.queryExecution.QueryExecutionId',
      ),
      resultPath: '$.queryResults',
    });
    getResults.addRetry({
      errors: ['Athena.AthenaException', 'States.TaskFailed'],
      interval: Duration.seconds(2),
      maxAttempts: 3,
      backoffRate: 2,
    });

    const queryFailed = new sfn.Pass(this, 'QueryFailed', {
      parameters: {
        'error.$': '$.error',
        message: 'Athena query failed',
      },
    });

    // Shape the response: return only the Athena result rows to the caller.
    const formatResponse = new sfn.Pass(this, 'FormatResponse', {
      parameters: {
        'rows.$': '$.queryResults.ResultSet.Rows',
      },
    });

    // Branch on the Athena query state.
    const queryStatePath = '$.queryStatus.QueryExecution.Status.State';
    const checkQueryState = new sfn.Choice(this, 'CheckQueryState')
      .when(
        sfn.Condition.stringEquals(queryStatePath, 'SUCCEEDED'),
        getResults,
      )
      .when(
        sfn.Condition.or(
          sfn.Condition.stringEquals(queryStatePath, 'FAILED'),
          sfn.Condition.stringEquals(queryStatePath, 'CANCELLED'),
        ),
        queryFailed,
      )
      .otherwise(waitForQuery);

    startQuery.addCatch(queryFailed, { errors: ['States.ALL'], resultPath: '$.error' });
    getQueryExecution.addCatch(queryFailed, { errors: ['States.ALL'], resultPath: '$.error' });
    getResults.addCatch(queryFailed, { errors: ['States.ALL'], resultPath: '$.error' });

    // Amazon API Gateway's StepFunctionsRestApi integration wraps the request
    // body under a "body" key (input shape: {body, querystring, path}). Lift
    // the caller's queryString to the top level so the query task can read it.
    const extractInput = new sfn.Pass(this, 'ExtractInput', {
      parameters: {
        'queryString.$': '$.body.queryString',
      },
    });

    const definition = extractInput
      .next(startQuery)
      .next(waitForQuery)
      .next(getQueryExecution)
      .next(checkQueryState);
    getResults.next(formatResponse);

    const logGroup = new logs.LogGroup(this, 'StateMachineLogGroup', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const stateMachine = new sfn.StateMachine(this, 'AthenaExpressStateMachine', {
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      stateMachineType: sfn.StateMachineType.EXPRESS,
      timeout: Duration.seconds(60),
      tracingEnabled: true,
      logs: {
        destination: logGroup,
        level: sfn.LogLevel.ALL,
        includeExecutionData: true,
      },
    });

    // ---------------------------------------------------------------------
    // Least-privilege IAM for the state-machine role.
    // ---------------------------------------------------------------------
    // Athena query-execution actions, scoped to this workgroup ARN.
    stateMachine.addToRolePolicy(
      new iam.PolicyStatement({
        actions: [
          'athena:StartQueryExecution',
          'athena:GetQueryExecution',
          'athena:GetQueryResults',
          'athena:StopQueryExecution',
        ],
        resources: [workgroupArn],
      }),
    );

    // AWS Glue metadata reads Athena performs on the caller's behalf, scoped
    // to the specific catalog / database / table this pattern owns.
    stateMachine.addToRolePolicy(
      new iam.PolicyStatement({
        actions: [
          'glue:GetDatabase',
          'glue:GetTable',
          'glue:GetTables',
          'glue:GetPartition',
          'glue:GetPartitions',
        ],
        resources: [catalogArn, databaseArn, tableArn],
      }),
    );

    // Amazon S3: read the sample data, write query results, and list the
    // bucket (Athena requires ListBucket to resolve the results location).
    dataBucket.grantRead(stateMachine, `${dataPrefix}*`);
    dataBucket.grantReadWrite(stateMachine, `${resultsPrefix}*`);
    stateMachine.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ['s3:GetBucketLocation', 's3:ListBucket'],
        resources: [dataBucket.bucketArn],
      }),
    );

    // ---------------------------------------------------------------------
    // Amazon API Gateway (REST) -> StartSyncExecution on the Express state
    // machine. StepFunctionsRestApi wires the AWS service integration and
    // grants the API role sync-execution permission on THIS state machine.
    // ---------------------------------------------------------------------
    const api = new apigw.StepFunctionsRestApi(this, 'AthenaQueryApi', {
      stateMachine,
      // Express + StartSyncExecution: request/response in one HTTP call.
      useDefaultMethodResponses: true,
      deployOptions: {
        stageName: 'prod',
        tracingEnabled: true,
      },
    });

    new CfnOutput(this, 'ApiEndpoint', {
      value: api.url,
      description: 'POST here with {"queryString":"..."} to run a synchronous Athena query',
    });
    new CfnOutput(this, 'DataBucketName', { value: dataBucket.bucketName });
    new CfnOutput(this, 'AthenaWorkgroupName', { value: workgroup.name! });
    new CfnOutput(this, 'GlueDatabaseName', {
      value: `orders_db_${Aws.ACCOUNT_ID}`,
    });
  }
}

// A tiny sample dataset (6 columns, a handful of rows) seeded into S3 so the
// pattern is queryable immediately after deploy.
const SAMPLE_CSV = [
  'order_id,customer,product,quantity,amount,order_date',
  'O-1001,Acme Corp,Widget,10,199.90,2026-01-05',
  'O-1002,Globex,Gadget,3,89.97,2026-01-06',
  'O-1003,Initech,Widget,25,499.75,2026-01-07',
  'O-1004,Acme Corp,Sprocket,7,140.00,2026-01-08',
  'O-1005,Umbrella,Gadget,12,359.88,2026-01-09',
  'O-1006,Globex,Widget,5,99.95,2026-01-10',
].join('\n');
