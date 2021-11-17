import * as cdk from '@aws-cdk/core';
import * as rds from '@aws-cdk/aws-rds';
import * as ec2 from '@aws-cdk/aws-ec2';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 3
    });

    const auroraServerlessCluster = new rds.ServerlessCluster(this, 'AuroraServerlessCluster', {
      engine: rds.DatabaseClusterEngine.AURORA,
      vpc,
      scaling: {
        autoPause: cdk.Duration.minutes(10),
        minCapacity: rds.AuroraCapacityUnit.ACU_1,
        maxCapacity: rds.AuroraCapacityUnit.ACU_2,
      }
    });
  }
}
