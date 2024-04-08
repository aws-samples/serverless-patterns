import * as path from 'path';

import { Stack, StackProps, CfnOutput, Duration, RemovalPolicy } from 'aws-cdk-lib';
import { aws_ec2 as ec2 } from 'aws-cdk-lib';
import { aws_secretsmanager as secretsmanager } from 'aws-cdk-lib';
import { aws_rds as rds } from 'aws-cdk-lib';
import { aws_lambda as lambda } from 'aws-cdk-lib';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Construct } from 'constructs';
import * as apigw from '@aws-cdk/aws-apigatewayv2-alpha';
import { HttpLambdaIntegration } from '@aws-cdk/aws-apigatewayv2-integrations-alpha';



export class RdsProxySequelizeStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "RdsProxyExampleVpc", {
      subnetConfiguration: [
        {
          name: 'Isolated',
          subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
        },
        {
          name: 'Private',
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        },
        {
          name: 'Public',
          subnetType: ec2.SubnetType.PUBLIC,
        }
      ]
    });

    const dbUsername = 'syscdk';
    const rdsSecret = new secretsmanager.Secret(this, 'RdsProxyExampleSecret', {
      secretName: id+'-rds-credentials',
      generateSecretString: {
        secretStringTemplate: JSON.stringify({ username: dbUsername }),
        generateStringKey: 'password',
        excludePunctuation: true,
        includeSpace: false,
      }
    });

    // Create a security group to be used on the lambda functions
    const lambdaSecurityGroup = new ec2.SecurityGroup(this, 'Lambda Security Group', {
      vpc
    });

    // Create a security group to be used on the RDS proxy
    const rdsProxySecurityGroup = new ec2.SecurityGroup(this, 'Only Allow Access From Lambda', {
      vpc
    });
    rdsProxySecurityGroup.addIngressRule(lambdaSecurityGroup, ec2.Port.tcp(5432), 'allow lambda connection to rds proxy');

    // Create a security group to be used on the RDS instances
    const rdsSecurityGroup = new ec2.SecurityGroup(this, 'Only Allow Access From RDS Proxy', {
      vpc
    });
    rdsSecurityGroup.addIngressRule(rdsProxySecurityGroup, ec2.Port.tcp(5432), 'allow db connections from the rds proxy');
    
    const rdsCredentials = rds.Credentials.fromSecret(rdsSecret);

    const dbName = 'nflstadiums';
    const postgreSql = new rds.DatabaseCluster(this, 'RdsProxyExampleCluster', {
      instanceProps:
      {
        vpc,
        vpcSubnets: {
          subnetType: ec2.SubnetType.PRIVATE_ISOLATED
        },
        instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
        securityGroups: [ rdsSecurityGroup ]
      },
      clusterIdentifier: 'RDSProxyExampleCluster',
      engine: rds.DatabaseClusterEngine.auroraPostgres({
        version: rds.AuroraPostgresEngineVersion.VER_15_2
      }),
      instances: 1,
      backup: { retention: Duration.days(1) },
      removalPolicy: RemovalPolicy.DESTROY,
      credentials: rdsCredentials,
      defaultDatabaseName: dbName,
    });

    const rdsProxy = postgreSql.addProxy('rdsProxyExample', {
      secrets: [ rdsSecret ],
      securityGroups: [ rdsProxySecurityGroup ],
      debugLogging: true,
      iamAuth: true,
      vpc
    });

    const rdsProxyPopulateLambda: NodejsFunction = new NodejsFunction(this, id + '-populateLambda', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, '../lambda/populate.ts'),
      vpc: vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_ISOLATED },
      securityGroups: [ lambdaSecurityGroup ],
      environment: {
        PGHOST: rdsProxy.endpoint,
        PGDATABASE: dbName,
        PGUSER: dbUsername
      },
      // Bundler removes these dependencies since they aren't imported explicitly
      // Include them so sequelize can connect to Postgres
      bundling: {
        nodeModules: [ 'pg', 'pg-hstore' ]
      }
    });

    const rdsProxyGetDataLambda: NodejsFunction = new NodejsFunction(this, id + '-getDataLambda', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, '../lambda/getData.ts'),
      vpc: vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_ISOLATED },
      securityGroups: [ lambdaSecurityGroup ],
      environment: {
        PGHOST: rdsProxy.endpoint,
        PGDATABASE: dbName,
        PGUSER: dbUsername
      },
      // Bundler removes these dependencies since they aren't imported explicitly
      // Include them so sequelize can connect to Postgres
      bundling: {
        nodeModules: [ 'pg', 'pg-hstore' ]
      }
    });

    rdsProxy.grantConnect(rdsProxyPopulateLambda, dbUsername);
    rdsProxy.grantConnect(rdsProxyGetDataLambda, dbUsername);

    const httpApi: apigw.HttpApi = new apigw.HttpApi(this, 'StadiumApi');

    const populateLambdaIntegration = new HttpLambdaIntegration('rdsProxyPopulateLambda', rdsProxyPopulateLambda );

    const getDataLambdaIntegration = new HttpLambdaIntegration('rdsProxyGetDataLambda', rdsProxyGetDataLambda);

    httpApi.addRoutes({
      path: '/populate',
      methods: [apigw.HttpMethod.POST],
      integration: populateLambdaIntegration
    });

    new CfnOutput(this, 'populateEndpointUrl', {
      value: `${httpApi.url}populate`,
      exportName: 'populateEndpointUrl'
    });

    httpApi.addRoutes({
      path: '/',
      methods: [apigw.HttpMethod.GET],
      integration: getDataLambdaIntegration
    });

    new CfnOutput(this, 'stadiumsEndpointUrl', {
      value: `${httpApi.url}`,
      exportName: 'stadiumsEndpointUrl'
    });
  };
}
