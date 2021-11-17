import * as cdk from '@aws-cdk/core';
import * as rds from '@aws-cdk/aws-rds';
import * as ec2 from '@aws-cdk/aws-ec2';
import * as secretsmanager from '@aws-cdk/aws-secretsmanager';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 3
    });

    const databaseCredentialsSecret = new secretsmanager.Secret(this, 'DBCredentialsSecret', {
      secretName: 'aurora-user-secret',
      description: 'RDS database auto-generated user password',
      generateSecretString: {
        secretStringTemplate: JSON.stringify({ username: 'admin' }),
        generateStringKey: 'password',
        passwordLength: 30,
        excludeCharacters: "\"@/\\",
      }
    });

    const auroraServerlessCluster = new rds.ServerlessCluster(this, 'AuroraServerlessCluster', {
      enableDataApi: true,
      engine: rds.DatabaseClusterEngine.AURORA,
      credentials: rds.Credentials.fromSecret(databaseCredentialsSecret),
      vpc,
      scaling: {
        autoPause: cdk.Duration.minutes(10),
        minCapacity: rds.AuroraCapacityUnit.ACU_1,
        maxCapacity: rds.AuroraCapacityUnit.ACU_2,
      }
    });
  }
}
