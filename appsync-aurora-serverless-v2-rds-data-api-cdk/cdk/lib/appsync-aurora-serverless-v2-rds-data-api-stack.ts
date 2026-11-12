// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as path from 'path';
import {
  Stack,
  StackProps,
  RemovalPolicy,
  CfnOutput,
  aws_appsync as appsync,
  aws_ec2 as ec2,
  aws_rds as rds,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

/**
 * AWS AppSync GraphQL API backed by an Amazon Aurora Serverless v2
 * (PostgreSQL) cluster through the RDS Data API. There are no AWS Lambda
 * functions in this pattern: AppSync talks to the database directly using an
 * RDS Data API data source and JavaScript (APPSYNC_JS) resolvers.
 *
 * Each service is load-bearing:
 *   - AWS AppSync terminates the GraphQL request and runs the resolver.
 *   - The RDS Data API data source turns a resolver into an HTTPS SQL call,
 *     which is what removes the need for an AWS Lambda function or a VPC-attached
 *     compute layer.
 *   - Amazon Aurora Serverless v2 is the relational store that scales its
 *     capacity to zero-ish when idle and holds the data the resolvers query.
 */
export class AppSyncAuroraServerlessStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const databaseName = 'appsyncdemo';

    // Minimal VPC for the Aurora cluster. The RDS Data API is reached over
    // HTTPS from AppSync, so no NAT gateway or public subnet is required.
    const vpc = new ec2.Vpc(this, 'AuroraVpc', {
      maxAzs: 2,
      natGateways: 0,
      subnetConfiguration: [
        {
          name: 'isolated',
          subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
          cidrMask: 24,
        },
      ],
    });

    // Amazon Aurora Serverless v2 PostgreSQL cluster with the RDS Data API
    // enabled. A generated admin secret in AWS Secrets Manager is what the
    // Data API uses to authenticate; storage is encrypted at rest.
    const cluster = new rds.DatabaseCluster(this, 'AuroraServerlessV2Cluster', {
      engine: rds.DatabaseClusterEngine.auroraPostgres({
        version: rds.AuroraPostgresEngineVersion.VER_16_8,
      }),
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_ISOLATED },
      writer: rds.ClusterInstance.serverlessV2('writer'),
      serverlessV2MinCapacity: 0.5,
      serverlessV2MaxCapacity: 2,
      defaultDatabaseName: databaseName,
      enableDataApi: true,
      storageEncrypted: true,
      credentials: rds.Credentials.fromGeneratedSecret('clusteradmin'),
      removalPolicy: RemovalPolicy.DESTROY,
    });

    // The generated admin secret backing the cluster. The Data API data
    // source reads this to authenticate SQL calls.
    const secret = cluster.secret!;

    // AWS AppSync GraphQL API. API key auth keeps the sample self-contained;
    // production workloads should use Amazon Cognito, OIDC, or IAM auth.
    const api = new appsync.GraphqlApi(this, 'GraphqlApi', {
      name: 'appsync-aurora-serverless-v2-rds-data-api',
      definition: appsync.Definition.fromFile(
        path.join(__dirname, '..', 'schema', 'schema.graphql'),
      ),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: appsync.AuthorizationType.API_KEY,
          apiKeyConfig: {
            description: 'Demo API key for appsync-aurora-serverless-v2-rds-data-api',
            expires: undefined,
          },
        },
      },
      xrayEnabled: true,
    });

    // RDS Data API data source for Amazon Aurora Serverless v2. This is the
    // v2 variant (addRdsDataSourceV2) that binds an IDatabaseCluster; the
    // grant of rds-data:* and the Secrets Manager read on the cluster secret
    // are scoped to those specific resource ARNs by the L2 construct.
    const dataSource = api.addRdsDataSourceV2(
      'AuroraDataSource',
      cluster,
      secret,
      databaseName,
    );

    // JavaScript (APPSYNC_JS) resolvers issue parameterised SQL through the
    // Data API. Parameters are bound, never string-concatenated, to avoid
    // SQL injection.
    dataSource.createResolver('ListTodosResolver', {
      typeName: 'Query',
      fieldName: 'listTodos',
      runtime: appsync.FunctionRuntime.JS_1_0_0,
      code: appsync.Code.fromInline(`
        import { select, createPgStatement, toJsonObject } from '@aws-appsync/utils/rds';
        import { util } from '@aws-appsync/utils';
        export function request(ctx) {
          return createPgStatement(
            select({
              table: 'todos',
              columns: ['id', 'title', 'completed'],
              orderBy: [{ column: 'id' }],
            }),
          );
        }
        export function response(ctx) {
          const { error, result } = ctx;
          if (error) {
            return util.appendError(error.message, error.type, result);
          }
          return toJsonObject(result)[0];
        }
      `),
    });

    dataSource.createResolver('CreateTodoResolver', {
      typeName: 'Mutation',
      fieldName: 'createTodo',
      runtime: appsync.FunctionRuntime.JS_1_0_0,
      code: appsync.Code.fromInline(`
        import { insert, createPgStatement, toJsonObject } from '@aws-appsync/utils/rds';
        import { util } from '@aws-appsync/utils';
        export function request(ctx) {
          const { title } = ctx.args;
          return createPgStatement(
            insert({
              table: 'todos',
              values: { title, completed: false },
              returning: ['id', 'title', 'completed'],
            }),
          );
        }
        export function response(ctx) {
          const { error, result } = ctx;
          if (error) {
            return util.appendError(error.message, error.type, result);
          }
          return toJsonObject(result)[0][0];
        }
      `),
    });

    new CfnOutput(this, 'GraphQLApiUrl', {
      value: api.graphqlUrl,
      description: 'AWS AppSync GraphQL endpoint URL',
    });

    new CfnOutput(this, 'GraphQLApiKey', {
      value: api.apiKey ?? 'n/a',
      description: 'API key for the demo GraphQL API',
    });

    new CfnOutput(this, 'GraphQLApiId', {
      value: api.apiId,
      description: 'AWS AppSync GraphQL API ID',
    });

    new CfnOutput(this, 'ClusterSecretArn', {
      value: secret.secretArn,
      description: 'Secrets Manager ARN for the Aurora cluster admin credentials',
    });

    new CfnOutput(this, 'ClusterArn', {
      value: cluster.clusterArn,
      description: 'Amazon Aurora Serverless v2 cluster ARN (used by the RDS Data API)',
    });
  }
}
