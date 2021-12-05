import { CfnOutput, Construct, RemovalPolicy, Stack, StackProps} from '@aws-cdk/core';
import { BlockPublicAccess, Bucket} from '@aws-cdk/aws-s3';
import * as sm from "@aws-cdk/aws-secretsmanager";
import { CfnDBCluster, CfnDBSubnetGroup } from '@aws-cdk/aws-rds';
import { SubnetType, Vpc } from '@aws-cdk/aws-ec2';

export class S3CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const BUCKET_NAME = 'demo-bucket-serverless-patterns'
    const service = 'demordsservice'
    const stage = 'demostage'
    const username = 'demousername'

    //VPC and Subnet Group
    const vpc = new Vpc(this, 'Vpc', {
      cidr: '10.0.0.0/16',
      natGateways: 0,
      subnetConfiguration: [   { name: 'aurora_isolated_', subnetType: SubnetType.ISOLATED } ] }); 

    const subnetIds: string[] = [];
    vpc.isolatedSubnets.forEach((subnet, index) => { subnetIds.push(subnet.subnetId); });
    const dbSubnetGroup: CfnDBSubnetGroup = new CfnDBSubnetGroup(this, 'AuroraSubnetGroup', {
     dbSubnetGroupDescription: 'Subnet group to access aurora',
     dbSubnetGroupName: 'aurora-serverless-subnet-group',
     subnetIds
  });
  //S3 Bucket
    var bucket = new Bucket(this, 'demoBucket', {
      blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
      bucketName: BUCKET_NAME,
      enforceSSL: true,
      publicReadAccess: false,
      removalPolicy: RemovalPolicy.DESTROY,
      versioned: false,
      autoDeleteObjects: true
    });
    //Secret Manager
    const secret = new sm.Secret(this, "RelationalDBStackSecret", {
      secretName: `${service}-${stage}-credentials`,
      generateSecretString: {
        secretStringTemplate: JSON.stringify({ username, }),
        excludePunctuation: true,
        includeSpace: false,
        generateStringKey: "password",
      },
    });

    //Serverless cluster
    const aurora = new CfnDBCluster(this, 'AuroraServerless', {
      databaseName: 'dbname',
      dbClusterIdentifier: 'aurora-serverless',
      engine: 'aurora',
      engineMode: 'serverless',
      enableHttpEndpoint: true,
      masterUserPassword: secret.secretValueFromJson("password").toString(),
      masterUsername: secret.secretValueFromJson("username").toString(),
      port: 3306,
      dbSubnetGroupName: dbSubnetGroup.dbSubnetGroupName,
      scalingConfiguration: {
        autoPause: true,
        maxCapacity: 2,
        minCapacity: 2,
        secondsUntilAutoPause: 3600
      }
    });
    aurora.addDependsOn(dbSubnetGroup);


    // Outputs
    new CfnOutput(this, BUCKET_NAME, {
      value: bucket.bucketName,
      description: 'The name of the s3 bucket',
    });

    new CfnOutput(this, 'VpcSubnetIds', {
      value: JSON.stringify(subnetIds)
    });
    
    new CfnOutput(this, 'VpcDefaultSecurityGroup', {
      value: vpc.vpcDefaultSecurityGroup
    });
  }
}