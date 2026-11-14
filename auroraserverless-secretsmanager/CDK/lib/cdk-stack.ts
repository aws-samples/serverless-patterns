
import { Stack, StackProps, CfnOutput  } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { aws_secretsmanager as sm } from "aws-cdk-lib";
import { CfnDBCluster, CfnDBInstance, CfnDBSubnetGroup } from 'aws-cdk-lib/aws-rds';
import { SubnetType, Vpc } from 'aws-cdk-lib/aws-ec2';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const service = 'demordsservice'
    const stage = 'demostage'
    const username = 'demousername'

    //VPC and Subnet Group
    const vpc = new Vpc(this, 'Vpc', {
      cidr: '10.0.0.0/16',
      natGateways: 0,
      subnetConfiguration: [   { name: 'aurora_isolated_', subnetType: SubnetType.PRIVATE_ISOLATED } ] }); 

    const subnetIds: string[] = [];
    vpc.isolatedSubnets.forEach((subnet, index) => { subnetIds.push(subnet.subnetId); });
    const dbSubnetGroup: CfnDBSubnetGroup = new CfnDBSubnetGroup(this, 'AuroraSubnetGroup', {
     dbSubnetGroupDescription: 'Subnet group to access aurora',
     dbSubnetGroupName: 'aurora-serverless-subnet-group',
     subnetIds
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

    //Aurora Serverless v2 cluster (the Data API needs Aurora MySQL 3.07 or higher)
    const aurora = new CfnDBCluster(this, 'AuroraServerless', {
      databaseName: 'dbname',
      dbClusterIdentifier: 'aurora-serverless',
      engine: 'aurora-mysql',
      engineVersion: '8.0.mysql_aurora.3.10.4',
      enableHttpEndpoint: true,
      storageEncrypted: true,
      masterUserPassword: secret.secretValueFromJson("password").toString(),
      masterUsername: secret.secretValueFromJson("username").toString(),
      port: 3306,
      dbSubnetGroupName: dbSubnetGroup.dbSubnetGroupName,
      serverlessV2ScalingConfiguration: {
        minCapacity: 0.5,
        maxCapacity: 2
      }
    });
    aurora.node.addDependency(dbSubnetGroup);

    //Serverless v2 writer instance
    new CfnDBInstance(this, 'AuroraServerlessWriter', {
      dbClusterIdentifier: aurora.ref,
      dbInstanceClass: 'db.serverless',
      engine: 'aurora-mysql'
    });


    // Outputs
    new CfnOutput(this, 'VpcSubnetIds', {
      value: JSON.stringify(subnetIds)
    });
    
    new CfnOutput(this, 'VpcDefaultSecurityGroup', {
      value: vpc.vpcDefaultSecurityGroup
    });
  }
}