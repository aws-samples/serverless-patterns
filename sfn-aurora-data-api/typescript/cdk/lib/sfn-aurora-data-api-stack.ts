import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as rds from 'aws-cdk-lib/aws-rds';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import { Construct } from 'constructs';

const DB_NAME = 'appdb';

// Idempotent schema and seed row. Each entry is one RDS Data API call, run in order.
const SCHEMA_SQL = [
  'CREATE TABLE IF NOT EXISTS inventory (sku text PRIMARY KEY, stock integer NOT NULL CHECK (stock >= 0))',
  'CREATE TABLE IF NOT EXISTS orders (id text PRIMARY KEY, sku text NOT NULL REFERENCES inventory (sku), quantity integer NOT NULL CHECK (quantity > 0))',
  'CREATE TABLE IF NOT EXISTS audit (id bigserial PRIMARY KEY, order_id text NOT NULL, event text NOT NULL)',
  "INSERT INTO inventory (sku, stock) VALUES ('SKU-100', 5) ON CONFLICT (sku) DO NOTHING",
];

export class SfnAuroraDataApiStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The cluster needs a VPC. Isolated subnets only: no NAT gateway, no internet gateway, no inbound rules.
    // The caller (AWS Step Functions) is not in the VPC: it reaches the cluster through the RDS Data API endpoint.
    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 2,
      natGateways: 0,
      subnetConfiguration: [{ name: 'isolated', subnetType: ec2.SubnetType.PRIVATE_ISOLATED, cidrMask: 24 }],
    });

    const secret = new rds.DatabaseSecret(this, 'DbSecret', { username: 'postgres' });
    secret.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);

    // Minimum capacity 0 ACUs lets the writer pause when idle (needs Aurora PostgreSQL 17.4 or later).
    const cluster = new rds.DatabaseCluster(this, 'Cluster', {
      engine: rds.DatabaseClusterEngine.auroraPostgres({ version: rds.AuroraPostgresEngineVersion.VER_17_7 }),
      writer: rds.ClusterInstance.serverlessV2('writer'),
      serverlessV2MinCapacity: 0,
      serverlessV2MaxCapacity: 2,
      serverlessV2AutoPauseDuration: cdk.Duration.minutes(5),
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_ISOLATED },
      credentials: rds.Credentials.fromSecret(secret),
      defaultDatabaseName: DB_NAME,
      enableDataApi: true,
      storageEncrypted: true,
      deletionProtection: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // One RDS Data API call. CallAwsService derives the IAM action as "rdsdata:<action>", which is not a valid
    // prefix (the IAM prefix is "rds-data"), so every call passes iamAction explicitly.
    // SDK integrations have no timeout by default, so each call gets one.
    const dataApi = (stateId: string, action: string, args: object, extra: object = {}) =>
      tasks.CallAwsService.jsonata(this, stateId, {
        service: 'rdsdata',
        action,
        iamAction: `rds-data:${action[0].toUpperCase()}${action.slice(1)}`,
        iamResources: [cluster.clusterArn],
        parameters: { ResourceArn: cluster.clusterArn, SecretArn: secret.secretArn, ...args },
        taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(60)),
        ...extra,
      });

    // Statement inside the open transaction. Values travel as named parameters, never as SQL text.
    const inTransaction = (stateId: string, sql: string, parameters: object[], extra: object = {}) =>
      dataApi(
        stateId,
        'executeStatement',
        { Database: DB_NAME, TransactionId: '{% $txId %}', Sql: sql, Parameters: parameters },
        extra,
      );

    // The first call after a pause fails with DatabaseResumingException while the writer resumes: retry only that.
    // A failed statement is a permanent error and is never retried.
    const resumeRetry = {
      errors: ['RdsData.DatabaseResumingException'],
      interval: cdk.Duration.seconds(10),
      backoffRate: 1.5,
      maxAttempts: 6,
    };

    // 1. Create the tables and the seed row outside the transaction, one statement at a time, in order.
    const runDdl = dataApi('RunDdlStatement', 'executeStatement', { Database: DB_NAME, Sql: '{% $states.input %}' });
    runDdl.addRetry(resumeRetry);
    const ensureSchema = sfn.Map.jsonata(this, 'EnsureSchema', {
      items: sfn.ProvideItems.jsonArray(SCHEMA_SQL),
      maxConcurrency: 1,
      assign: {
        orderId: '{% $states.context.Execution.Name %}',
        sku: '{% $states.input.sku %}',
        quantity: '{% $states.input.quantity %}',
      },
      outputs: '{% $states.input %}',
    }).itemProcessor(runDdl);

    // 2. Open the transaction. The id goes into a workflow variable because the Catch path needs it to roll back.
    const begin = dataApi('BeginTransaction', 'beginTransaction', { Database: DB_NAME }, {
      assign: { txId: '{% $states.result.TransactionId %}' },
    });
    begin.addRetry(resumeRetry);

    // 3. Three statements in the transaction: insert the order, take stock with a guard, write the audit row.
    const insertOrder = inTransaction(
      'InsertOrder',
      'INSERT INTO orders (id, sku, quantity) VALUES (:id, :sku, :quantity)',
      [
        { Name: 'id', Value: { StringValue: '{% $orderId %}' } },
        { Name: 'sku', Value: { StringValue: '{% $sku %}' } },
        { Name: 'quantity', Value: { LongValue: '{% $quantity %}' } },
      ],
    );
    // The WHERE guard makes "not enough stock" an update of zero rows instead of an error.
    // NumberOfRecordsUpdated is read defensively with $exists so that a response without the field counts as 0 rows.
    const decrementStock = inTransaction(
      'DecrementStock',
      'UPDATE inventory SET stock = stock - :quantity WHERE sku = :sku AND stock >= :quantity',
      [
        { Name: 'sku', Value: { StringValue: '{% $sku %}' } },
        { Name: 'quantity', Value: { LongValue: '{% $quantity %}' } },
      ],
      {
        assign: {
          rowsUpdated: '{% $exists($states.result.NumberOfRecordsUpdated) ? $states.result.NumberOfRecordsUpdated : 0 %}',
        },
      },
    );
    const insertAudit = inTransaction(
      'InsertAudit',
      "INSERT INTO audit (order_id, event) VALUES (:id, 'ORDER_PLACED')",
      [{ Name: 'id', Value: { StringValue: '{% $orderId %}' } }],
    );

    // 4. Commit, or roll back with the same transaction id.
    const commit = dataApi('CommitTransaction', 'commitTransaction', { TransactionId: '{% $txId %}' });
    const rollback = dataApi('RollbackTransaction', 'rollbackTransaction', { TransactionId: '{% $txId %}' });
    const committed = sfn.Succeed.jsonata(this, 'OrderCommitted', {
      outputs: { orderId: '{% $orderId %}', status: 'COMMITTED' },
    });
    const rejected = sfn.Fail.jsonata(this, 'OrderRolledBack', {
      error: '{% $failureError %}',
      cause: '{% $failureCause %}',
    });
    rollback.next(rejected);

    // Any failure after BeginTransaction rolls the transaction back and ends the execution in a Fail state.
    const rollBackOnError = {
      errors: [sfn.Errors.ALL],
      assign: { failureError: '{% $states.errorOutput.Error %}', failureCause: '{% $states.errorOutput.Cause %}' },
    };
    [insertOrder, decrementStock, insertAudit, commit].forEach((state) => state.addCatch(rollback, rollBackOnError));

    const stockUnavailable = sfn.Pass.jsonata(this, 'StockUnavailable', {
      assign: {
        failureError: 'InsufficientStock',
        failureCause: "{% 'No row updated: SKU ' & $sku & ' is unknown or has fewer than ' & $quantity & ' units' %}",
      },
    });
    const stockCheck = sfn.Choice.jsonata(this, 'StockReserved')
      .when(sfn.Condition.jsonata('{% $rowsUpdated = 1 %}'), insertAudit.next(commit).next(committed))
      .otherwise(stockUnavailable.next(rollback));

    const logGroup = new logs.LogGroup(this, 'StateMachineLogs', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const stateMachine = new sfn.StateMachine(this, 'OrderTransaction', {
      definitionBody: sfn.DefinitionBody.fromChainable(
        ensureSchema.next(begin).next(insertOrder).next(decrementStock).next(stockCheck),
      ),
      queryLanguage: sfn.QueryLanguage.JSONATA,
      timeout: cdk.Duration.minutes(10),
      // Execution data stays out of the logs: it contains the order values and the SQL parameters.
      logs: { destination: logGroup, level: sfn.LogLevel.ERROR, includeExecutionData: false },
    });

    // The RDS Data API reads the cluster secret with the caller's credentials, so the role needs this one secret.
    stateMachine.addToRolePolicy(
      new iam.PolicyStatement({ actions: ['secretsmanager:GetSecretValue'], resources: [secret.secretArn] }),
    );

    new cdk.CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new cdk.CfnOutput(this, 'StateMachineLogGroupName', { value: logGroup.logGroupName });
    new cdk.CfnOutput(this, 'ClusterArn', { value: cluster.clusterArn });
    new cdk.CfnOutput(this, 'SecretArn', { value: secret.secretArn });
    new cdk.CfnOutput(this, 'DatabaseName', { value: DB_NAME });
  }
}
