import { Duration, Stack, StackProps} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AuroraCapacityUnit, Credentials, DatabaseClusterEngine, ServerlessCluster } from 'aws-cdk-lib/aws-rds';
import { Vpc } from 'aws-cdk-lib/aws-ec2';
import { Secret } from 'aws-cdk-lib/aws-secretsmanager';
import { Cluster, ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService } from 'aws-cdk-lib/aws-ecs-patterns';
import path = require('path');

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const DATABASE_NAME = 'aurora_db';

    const vpc = new Vpc(this, 'Vpc', {
      maxAzs: 3
    });

    const databaseCredentialsSecret = new Secret(this, 'DBCredentialsSecret', {
      secretName: 'aurora-user-secret',
      description: 'RDS database auto-generated user password',
      generateSecretString: {
        secretStringTemplate: JSON.stringify({ username: 'admin' }),
        generateStringKey: 'password',
        passwordLength: 30,
        excludeCharacters: "\"@/\\",
      }
    });

    const auroraServerlessCluster = new ServerlessCluster(this, 'AuroraServerlessCluster', {
      defaultDatabaseName: DATABASE_NAME,
      enableDataApi: true,
      engine: DatabaseClusterEngine.AURORA,
      credentials: Credentials.fromSecret(databaseCredentialsSecret),
      vpc,
      scaling: {
        autoPause: Duration.minutes(10),
        minCapacity: AuroraCapacityUnit.ACU_1,
        maxCapacity: AuroraCapacityUnit.ACU_2,
      }
    });

    const cluster = new Cluster(this, 'Cluster', {
      vpc: vpc,
    });

    const fargate = new ApplicationLoadBalancedFargateService(this, 'FargateService', {
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      taskImageOptions: {
        image: ContainerImage.fromAsset(path.join(__dirname, '../src/')),
        environment: {
          secretArn: databaseCredentialsSecret.secretArn,
          dbClusterArn: auroraServerlessCluster.clusterArn,
          dbName: DATABASE_NAME,
        },
      },
      assignPublicIp: false,
      memoryLimitMiB: 2048,
    });

    // Grant the given identity to access to the Data API, including
    // read access to the secret attached to the cluster if present.
    auroraServerlessCluster.grantDataApiAccess(fargate.taskDefinition.taskRole);
  }
}
