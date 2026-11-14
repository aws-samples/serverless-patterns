import { Stack, StackProps} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AuroraMysqlEngineVersion, ClusterInstance, Credentials, DatabaseCluster, DatabaseClusterEngine } from 'aws-cdk-lib/aws-rds';
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

    // Aurora Serverless v2 cluster with one serverless writer instance.
    // The Data API needs Aurora MySQL 3.07 or higher on Serverless v2.
    const auroraServerlessCluster = new DatabaseCluster(this, 'AuroraServerlessCluster', {
      defaultDatabaseName: DATABASE_NAME,
      enableDataApi: true,
      engine: DatabaseClusterEngine.auroraMysql({ version: AuroraMysqlEngineVersion.VER_3_10_4 }),
      credentials: Credentials.fromSecret(databaseCredentialsSecret),
      vpc,
      writer: ClusterInstance.serverlessV2('writer'),
      serverlessV2MinCapacity: 0.5,
      serverlessV2MaxCapacity: 2,
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
