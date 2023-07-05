import { Construct } from 'constructs';

import { Stack, StackProps, CfnOutput, aws_ec2 as ec2, aws_docdb as docdb } from 'aws-cdk-lib';

const MONGO_DB_PORT = 27017;

export interface DocumentDbStackProps extends StackProps {
  secretName: string;
}

export class DocumentDbStack extends Stack {
  public readonly clusterId: string;
  public readonly secretArn: string;
  public readonly securityGroupId: string;
  public readonly vpcId: string;

  constructor(scope: Construct, id: string, props: DocumentDbStackProps) {
    super(scope, id, props);

    const vpc = ec2.Vpc.fromLookup(this, 'default-vpc-id', {
      isDefault: true,
    });

    const docDbSg = new ec2.SecurityGroup(this, 'DocDB-SG', {
      vpc,
    });

    docDbSg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(MONGO_DB_PORT));

    const cluster = new docdb.DatabaseCluster(this, 'Database', {
      masterUser: {
        username: 'myuser', // NOTE: 'admin' is reserved by DocumentDB
        secretName: props.secretName, // optional, if you prefer to specify the secret name
      },
      dbClusterName: 'DocDbCluster',
      securityGroup: docDbSg,
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
      engineVersion: '4.0.0',
      instances: 1,
      vpc,
    });

    this.clusterId = cluster.clusterIdentifier;
    this.secretArn = cluster.secret?.secretArn!;
    this.securityGroupId = docDbSg.securityGroupId;
    this.vpcId = vpc.vpcId;

    new CfnOutput(this, 'Docdb-vpc-id', {
      value: this.vpcId,
    });
    new CfnOutput(this, 'Docdb-endpoint-port', {
      value: cluster.clusterEndpoint.port.toString(),
    });
    new CfnOutput(this, 'Docdb-cluster-identifier', {
      value: cluster.clusterIdentifier,
    });
    new CfnOutput(this, 'Docdb-security-groupId', {
      value: this.securityGroupId,
    });
    new CfnOutput(this, 'Docdb-cluster-secret-arn', {
      value: cluster.secret?.secretArn!,
    });
  }
}
