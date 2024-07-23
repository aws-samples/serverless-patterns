import { Construct } from 'constructs';
import { Stack, StackProps, aws_secretsmanager as sm, CfnDynamicReference, CfnDynamicReferenceService  } from 'aws-cdk-lib'
import { SubnetType, Vpc, SecurityGroup, IpAddresses } from 'aws-cdk-lib/aws-ec2';
import { AuroraCapacityUnit, CfnDBCluster, CfnDBInstance, CfnDBSubnetGroup } from 'aws-cdk-lib/aws-rds';
import { GlobalClusterProps } from './aurora-global-cluster-stack';

export class AuroraRegionalClusterStack extends Stack {
  public readonly endpoint: string;
  public readonly port: string;
  public readonly vpc: Vpc;
  public readonly region: string;
  public readonly dbSecurityGroupId: string;
  constructor(scope: Construct, id: string, props: GlobalClusterProps) {
    super(scope, id, props);

    const cfnGlobalCluster = props.cfnGlobalCluster;
    const databasename = 'sample';

    // VPC 
    const vpc = new Vpc(this, 'Vpc', {
      ipAddresses: IpAddresses.cidr('10.0.0.0/16'),
      natGateways: 0,
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'aurora_isolated_',
          subnetType: SubnetType.PRIVATE_ISOLATED
        },
        {
          cidrMask: 24,
          name: 'public',
          subnetType: SubnetType.PUBLIC
        }
      ]
    });

    // Security group 
    const dbSecurityGroup: SecurityGroup = new SecurityGroup(this, 'db-security-group', {
      securityGroupName: 'db-security-group',
      description: 'db-security-group',
      allowAllOutbound: true,
      vpc: vpc,
    });

    // DB Subnet Group
    const subnetIds: string[] = [];
    vpc.isolatedSubnets.forEach((subnet, index) => { subnetIds.push(subnet.subnetId); });

    const dbSubnetGroup: CfnDBSubnetGroup = new CfnDBSubnetGroup(this, 'AuroraSubnetGroup', {
      dbSubnetGroupDescription: 'Subnet group to access aurora',
      dbSubnetGroupName: 'aurora-serverless-subnet-group',
      subnetIds
    });

    // Secret Manager
    const secret = new sm.CfnSecret(this, "AuroraGlobalServerlessDBSecret", {
      name: `aurora-serverless-global-db-secret`,
      generateSecretString: {
        secretStringTemplate: JSON.stringify({ username: 'postgres' }),
        excludePunctuation: true,
        includeSpace: false,
        generateStringKey: "password",
      },
    });

    // Aurora DB Cluster
    const cfndbclusterprops = {
      dbClusterIdentifier: id,
      dbSubnetGroupName: dbSubnetGroup.dbSubnetGroupName,
      engine: cfnGlobalCluster.engine,
      engineVersion: cfnGlobalCluster.engineVersion,
      globalClusterIdentifier: cfnGlobalCluster.globalClusterIdentifier,
      ...(props.isPrimary as boolean && { databaseName: databasename }),
      ...(props.isPrimary as boolean && { masterUsername: new CfnDynamicReference(CfnDynamicReferenceService.SECRETS_MANAGER, 'aurora-serverless-global-db-secret:SecretString:username').toString() }),
      ...(props.isPrimary as boolean && { masterUserPassword: new CfnDynamicReference(CfnDynamicReferenceService.SECRETS_MANAGER, 'aurora-serverless-global-db-secret:SecretString:password').toString() }),
      serverlessV2ScalingConfiguration: {
        maxCapacity: AuroraCapacityUnit.ACU_4,
        minCapacity: AuroraCapacityUnit.ACU_2,
      },
      vpcSecurityGroupIds: [dbSecurityGroup.securityGroupId]
    };

    const dbcluster = new CfnDBCluster(this, "db-cluster", cfndbclusterprops);
    dbcluster.addDependency(dbSubnetGroup);
    dbcluster.addDependency(secret);


    // Aurora Serverless DB Instance
    const cfndbinstanceprops = {
      dbClusterIdentifier: dbcluster.dbClusterIdentifier,
      dbInstanceClass: 'db.serverless',
      dbInstanceIdentifier: 'serverless-db-instance',
      engine: cfnGlobalCluster.engine,
      engineVersion: cfnGlobalCluster.engineVersion,
    };

    const dbinstance = new CfnDBInstance(this, "serverless-db-instance", cfndbinstanceprops);

    dbinstance.addDependency(dbcluster);

    this.endpoint = dbcluster.attrEndpointAddress;
    this.port = dbcluster.attrEndpointPort;
    this.vpc = vpc;
    this.region = Stack.of(this).region;
    this.dbSecurityGroupId = dbSecurityGroup.securityGroupId;
  }
}
export interface DBClusterProps extends StackProps {
  endpoint: string,
  port: string
  vpc: Vpc,
  isPrimary?: boolean,
  region: string,
  dbSecurityGroupId: string
}

