import * as cdk from 'aws-cdk-lib';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class DynamodbCrossAccountReplicationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const replicaAccountId = new cdk.CfnParameter(this, 'ReplicaAccountId', {
      type: 'String',
      description: 'AWS Account ID that will assume the cross-account read role',
    });

    // Replica region must be a literal (TableV2 does not accept tokens for replica regions)
    const replicaRegion = this.node.tryGetContext('replicaRegion') || 'us-west-2';

    const table = new dynamodb.TableV2(this, 'SourceTable', {
      partitionKey: { name: 'PK', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'SK', type: dynamodb.AttributeType.STRING },
      billing: dynamodb.Billing.onDemand(),
      pointInTimeRecoverySpecification: { pointInTimeRecoveryEnabled: true },
      // DESTROY for easy cleanup in sample patterns. Use RETAIN in production.
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      replicas: [{ region: replicaRegion }],
    });

    // Cross-account read role — grants access to BOTH source and replica region ARNs
    const crossAccountRole = new iam.Role(this, 'CrossAccountReadRole', {
      assumedBy: new iam.AccountPrincipal(replicaAccountId.valueAsString),
      description: 'Allows another account to read from the DynamoDB Global Table in any region',
    });

    crossAccountRole.addToPolicy(new iam.PolicyStatement({
      actions: [
        'dynamodb:GetItem',
        'dynamodb:Query',
        'dynamodb:BatchGetItem',
      ],
      resources: [
        // Source region
        table.tableArn,
        `${table.tableArn}/index/*`,
        // Replica region (table.tableArn is source-region-scoped)
        `arn:aws:dynamodb:${replicaRegion}:${this.account}:table/${table.tableName}`,
        `arn:aws:dynamodb:${replicaRegion}:${this.account}:table/${table.tableName}/index/*`,
      ],
    }));

    new cdk.CfnOutput(this, 'TableName', { value: table.tableName });
    new cdk.CfnOutput(this, 'TableArn', { value: table.tableArn });
    new cdk.CfnOutput(this, 'CrossAccountRoleArn', { value: crossAccountRole.roleArn });
    new cdk.CfnOutput(this, 'ReplicaRegion', { value: replicaRegion });
  }
}
