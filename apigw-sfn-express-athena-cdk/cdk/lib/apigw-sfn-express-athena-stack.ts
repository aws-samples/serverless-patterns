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
 * a single request/response. There are no AWS Lambda functions in the request
 * path. (The stack does deploy two small AWS CDK helper functions at deploy
 * time: one behind the AwsCustomResource that seeds the sample CSV and one that
 * empties the bucket on `cdk destroy`.)
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
    // Uses an AwsCustomResource calling s3:PutObject with the CSV inline -
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
    new athena.CfnWorkGroup(this, 'AthenaWorkgroup', {
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
    // All native Step Functions service integrations -> no AWS Lambda in the
    // request path.
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

    // Retry transient Athena throttling/service errors (shared by the three
    // Athena tasks). Any remaining failure is caught and routed to the
    // TaskFailed state below, which fails the execution with the caught error.
    const athenaRetry: sfn.RetryProps = {
      errors: ['Athena.AthenaException', 'States.TaskFailed'],
      interval: Duration.seconds(2),
      maxAttempts: 3,
      backoffRate: 2,
    };
    // A request that Amazon Athena rejects as invalid (for example a SQL syntax
    // error) can never succeed on retry, so it is listed first with no retries.
    // Retry entries are evaluated in order, and the catch-all entry above would
    // otherwise spend about 14 seconds of backoff on it.
    const athenaNoRetry: sfn.RetryProps = {
      errors: ['Athena.InvalidRequestException'],
      maxAttempts: 0,
    };
    startQuery.addRetry({ ...athenaNoRetry });
    startQuery.addRetry({ ...athenaRetry });

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
    getQueryExecution.addRetry({ ...athenaRetry });

    const getResults = new tasks.AthenaGetQueryResults(this, 'GetAthenaResults', {
      queryExecutionId: sfn.JsonPath.stringAt(
        '$.queryExecution.QueryExecutionId',
      ),
      resultPath: '$.queryResults',
    });
    getResults.addRetry({ ...athenaRetry });

    // Failure states. An execution that ends in a Fail state has status FAILED,
    // which the StepFunctionsRestApi response template maps to HTTP 500 with the
    // "error" and "cause" values in the body.
    //
    // From CheckQueryState when Athena reports FAILED or CANCELLED. The Athena
    // StateChangeReason is optional in the API, so it is only used as the cause
    // when it is present in the GetQueryExecution output.
    const stateChangeReasonPath =
      '$.queryStatus.QueryExecution.Status.StateChangeReason';
    const queryFailed = new sfn.Fail(this, 'QueryFailed', {
      error: 'AthenaQueryFailed',
      causePath: stateChangeReasonPath,
    });
    const queryFailedNoReason = new sfn.Fail(this, 'QueryFailedNoReason', {
      error: 'AthenaQueryFailed',
      cause: 'The Athena query failed or was cancelled without a reported reason.',
    });
    // From the addCatch handlers below, which put the caught error under $.error.
    const taskFailed = new sfn.Fail(this, 'TaskFailed', {
      errorPath: '$.error.Error',
      causePath: '$.error.Cause',
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
        sfn.Condition.and(
          sfn.Condition.or(
            sfn.Condition.stringEquals(queryStatePath, 'FAILED'),
            sfn.Condition.stringEquals(queryStatePath, 'CANCELLED'),
          ),
          sfn.Condition.isPresent(stateChangeReasonPath),
        ),
        queryFailed,
      )
      .when(
        sfn.Condition.or(
          sfn.Condition.stringEquals(queryStatePath, 'FAILED'),
          sfn.Condition.stringEquals(queryStatePath, 'CANCELLED'),
        ),
        queryFailedNoReason,
      )
      .otherwise(waitForQuery);

    startQuery.addCatch(taskFailed, { errors: ['States.ALL'], resultPath: '$.error' });
    getQueryExecution.addCatch(taskFailed, { errors: ['States.ALL'], resultPath: '$.error' });
    getResults.addCatch(taskFailed, { errors: ['States.ALL'], resultPath: '$.error' });

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
      // Note: the REST API below is edge-optimized, where the integration
      // timeout is 29 seconds and cannot be raised. A query that takes longer
      // than about 29 seconds gets a 504 at the caller while the execution keeps
      // running (up to this timeout) and the Athena query is not stopped. See
      // the README.
      timeout: Duration.seconds(60),
      tracingEnabled: true,
      logs: {
        destination: logGroup,
        level: sfn.LogLevel.ALL,
        // includeExecutionData writes the caller's SQL and the full result rows
        // to CloudWatch Logs on every request. Fine for a sample; set it to
        // false (or lower the log level) if you copy this for sensitive data.
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
    // The request body is passed to Amazon Athena as SQL, so the method requires
    // AWS IAM (SigV4) authorization and the stage caps the request rate.
    // ---------------------------------------------------------------------
    const api = new apigw.StepFunctionsRestApi(this, 'AthenaQueryApi', {
      stateMachine,
      // Express + StartSyncExecution: request/response in one HTTP call.
      useDefaultMethodResponses: true,
      defaultMethodOptions: {
        authorizationType: apigw.AuthorizationType.IAM,
      },
      deployOptions: {
        stageName: 'prod',
        tracingEnabled: true,
        // Stage-level throttling for all methods. Adjust for your workload.
        throttlingRateLimit: 5,
        throttlingBurstLimit: 10,
      },
    });

    new CfnOutput(this, 'ApiEndpoint', {
      value: api.url,
      description: 'POST here (SigV4-signed) with {"queryString":"..."} to run a synchronous Athena query',
    });
    new CfnOutput(this, 'DataBucketName', { value: dataBucket.bucketName });
    new CfnOutput(this, 'AthenaWorkgroupName', { value: workgroupName });
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
