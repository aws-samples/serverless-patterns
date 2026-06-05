#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { SourceTableStack } from '../lib/source-table-stack';
import { ReplicaTableStack } from '../lib/replica-table-stack';

const app = new cdk.App();

const sourceAccount = app.node.tryGetContext('sourceAccount');
const sourceRegion = app.node.tryGetContext('sourceRegion') || 'us-east-1';
const replicaAccount = app.node.tryGetContext('replicaAccount');
const replicaRegion = app.node.tryGetContext('replicaRegion') || 'us-east-1';

const sourceStack = new SourceTableStack(app, 'DynamoDbMultiAccountSourceStack', {
  env: { account: sourceAccount, region: sourceRegion },
});

new ReplicaTableStack(app, 'DynamoDbMultiAccountReplicaStack', {
  env: { account: replicaAccount, region: replicaRegion },
  sourceTable: sourceStack.table,
});
