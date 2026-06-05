import * as cdk from 'aws-cdk-lib';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import { Construct } from 'constructs';

export interface ReplicaTableStackProps extends cdk.StackProps {
  sourceTable: dynamodb.ITableV2;
}

export class ReplicaTableStack extends cdk.Stack {
  public readonly replica: dynamodb.TableV2MultiAccountReplica;

  constructor(scope: Construct, id: string, props: ReplicaTableStackProps) {
    super(scope, id, props);

    this.replica = new dynamodb.TableV2MultiAccountReplica(this, 'ReplicaTable', {
      tableName: 'MultiAccountGlobalTable',
      replicaSourceTable: props.sourceTable,
      globalTableSettingsReplicationMode: dynamodb.GlobalTableSettingsReplicationMode.ALL,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      pointInTimeRecoverySpecification: { pointInTimeRecoveryEnabled: true },
    });

    new cdk.CfnOutput(this, 'ReplicaTableName', { value: this.replica.tableName });
    new cdk.CfnOutput(this, 'ReplicaTableArn', { value: this.replica.tableArn });
  }
}
