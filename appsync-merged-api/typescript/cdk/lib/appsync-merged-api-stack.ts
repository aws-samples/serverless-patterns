import { CfnOutput, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import * as appsync from 'aws-cdk-lib/aws-appsync';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import * as fs from 'fs';
import * as path from 'path';

interface ResolverSpec {
  typeName: string;
  fieldName: string;
  file: string;
}

export class AppsyncMergedApiStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Two source APIs, each owned by one team and backed by its own table.
    const orders = this.createSourceApi('Orders', 'orders.graphql', [
      { typeName: 'Query', fieldName: 'getOrder', file: 'getById.js' },
    ]);
    const customers = this.createSourceApi('Customers', 'customers.graphql', [
      { typeName: 'Query', fieldName: 'getCustomer', file: 'getById.js' },
      { typeName: 'Order', fieldName: 'customer', file: 'customerOfOrder.js' },
    ]);

    // Role that lets AppSync write the Merged API execution logs (AWS managed policy).
    const logsRole = this.createAppSyncRole(this, 'LogsRole');
    logsRole.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSAppSyncPushToCloudWatchLogs'),
    );

    // The Merged API. Definition.fromSourceApis creates one source API association per source API
    // and grants the merge role appsync:SourceGraphQL on that source API and appsync:StartSchemaMerge
    // on that association (AUTO_MERGE). The Merged API must offer the sources' authorization mode: IAM.
    const mergedApi = new appsync.GraphqlApi(this, 'MergedApi', {
      name: `${this.stackName}-merged`,
      definition: appsync.Definition.fromSourceApis({
        sourceApis: [orders.api, customers.api].map((sourceApi) => ({
          sourceApi,
          mergeType: appsync.MergeType.AUTO_MERGE,
        })),
        mergedApiExecutionRole: this.createAppSyncRole(this, 'MergeRole'),
      }),
      authorizationConfig: {
        defaultAuthorization: { authorizationType: appsync.AuthorizationType.IAM },
      },
      logConfig: {
        role: logsRole,
        fieldLogLevel: appsync.FieldLogLevel.ERROR,
        excludeVerboseContent: true,
        retention: logs.RetentionDays.ONE_WEEK,
      },
    });
    // Create the associations only after the source resolvers and data sources exist.
    mergedApi.node.addDependency(orders.group, customers.group);

    new CfnOutput(this, 'MergedApiUrl', { value: mergedApi.graphqlUrl });
    new CfnOutput(this, 'MergedApiId', { value: mergedApi.apiId });
    new CfnOutput(this, 'OrdersApiId', { value: orders.api.apiId });
    new CfnOutput(this, 'CustomersApiId', { value: customers.api.apiId });
    new CfnOutput(this, 'OrdersTableName', { value: orders.table.tableName });
    new CfnOutput(this, 'CustomersTableName', { value: customers.table.tableName });
    new CfnOutput(this, 'MergedApiLogGroup', { value: mergedApi.logGroup.logGroupName });
  }

  // Service role for AppSync, limited to this account and to AWS AppSync APIs in this Region.
  private createAppSyncRole(scope: Construct, id: string): iam.Role {
    return new iam.Role(scope, id, {
      assumedBy: new iam.PrincipalWithConditions(new iam.ServicePrincipal('appsync.amazonaws.com'), {
        StringEquals: { 'aws:SourceAccount': this.account },
        ArnLike: { 'aws:SourceArn': this.formatArn({ service: 'appsync', resource: 'apis', resourceName: '*' }) },
      }),
    });
  }

  private createSourceApi(name: string, schemaFile: string, resolvers: ResolverSpec[]) {
    const group = new Construct(this, name);
    const table = new dynamodb.Table(group, 'Table', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
    });
    const api = new appsync.GraphqlApi(group, `${name}Api`, {
      name: `${this.stackName}-${name.toLowerCase()}`,
      definition: appsync.Definition.fromFile(path.join(__dirname, '..', 'schema', schemaFile)),
      authorizationConfig: {
        defaultAuthorization: { authorizationType: appsync.AuthorizationType.IAM },
      },
    });

    // The L2 DynamoDB data source also grants Scan, Query and batch reads. The resolvers only call GetItem,
    // so the data source uses the L1 resource with a role limited to dynamodb:GetItem on this one table.
    const role = this.createAppSyncRole(group, 'DataSourceRole');
    table.grant(role, 'dynamodb:GetItem');
    const dataSource = new appsync.CfnDataSource(group, 'DataSource', {
      apiId: api.apiId,
      name: `${name}Table`,
      type: 'AMAZON_DYNAMODB',
      serviceRoleArn: role.roleArn,
      dynamoDbConfig: { tableName: table.tableName, awsRegion: this.region },
    });
    dataSource.node.addDependency(role);

    for (const spec of resolvers) {
      const resolver = new appsync.CfnResolver(group, `${spec.typeName}${spec.fieldName}Resolver`, {
        apiId: api.apiId,
        typeName: spec.typeName,
        fieldName: spec.fieldName,
        kind: 'UNIT',
        dataSourceName: dataSource.attrName,
        runtime: { name: 'APPSYNC_JS', runtimeVersion: '1.0.0' },
        code: fs.readFileSync(path.join(__dirname, '..', 'resolvers', spec.file), 'utf8'),
      });
      api.addSchemaDependency(resolver);
    }
    return { group, api, table };
  }
}
