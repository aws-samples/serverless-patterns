
import { Stack, StackProps, CfnOutput  } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { aws_secretsmanager as sm } from "aws-cdk-lib";
import { CfnDBCluster, CfnDBSubnetGroup } from 'aws-cdk-lib/aws-rds';
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
      subnetConfiguration: [   { name: 'aurora_isolated_', subnetType: SubnetType.ISOLATED } ] }); 

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
    new CfnOutput(this, 'VpcSubnetIds', {
      value: JSON.stringify(subnetIds)
    });
    
    new CfnOutput(this, 'VpcDefaultSecurityGroup', {
      value: vpc.vpcDefaultSecurityGroup
    });
  }
}