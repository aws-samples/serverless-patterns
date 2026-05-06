import * as cdk from 'aws-cdk-lib';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class DynamodbCrossAccountReplicationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const replicaAccountId = new cdk.CfnParameter(this, 'ReplicaAccountId', {
      type: 'String',
      description: 'AWS Account ID for the replica table',
    });

    const table = new dynamodb.TableV2(this, 'SourceTable', {
      partitionKey: { name: 'PK', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'SK', type: dynamodb.AttributeType.STRING },
      billing: dynamodb.Billing.onDemand(),
      pointInTimeRecovery: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      replicas: [
        {
          region: 'us-west-2',
        },
      ],
    });

    // IAM role for cross-account access to the replica
    const crossAccountRole = new iam.Role(this, 'CrossAccountReplicaRole', {
      assumedBy: new iam.AccountPrincipal(replicaAccountId.valueAsString),
      description: 'Allows replica account to read from the global table replica',
    });

    crossAccountRole.addToPolicy(new iam.PolicyStatement({
      actions: [
        'dynamodb:GetItem',
        'dynamodb:Query',
        'dynamodb:Scan',
        'dynamodb:BatchGetItem',
      ],
      resources: [
        table.tableArn,
        `${table.tableArn}/index/*`,
      ],
    }));

    new cdk.CfnOutput(this, 'TableName', { value: table.tableName });
    new cdk.CfnOutput(this, 'TableArn', { value: table.tableArn });
    new cdk.CfnOutput(this, 'CrossAccountRoleArn', { value: crossAccountRole.roleArn });
    new cdk.CfnOutput(this, 'ReplicaRegion', { value: 'us-west-2' });
  }
}
