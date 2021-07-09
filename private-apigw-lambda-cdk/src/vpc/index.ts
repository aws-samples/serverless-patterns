
import * as cdk from "@aws-cdk/core";
import {Vpc, SubnetType} from '@aws-cdk/aws-ec2';

export class VpcStack extends cdk.Stack {
  vpc: Vpc;

  constructor(scope: cdk.App, id: string) {
    super(scope, id);

    this.vpc = new Vpc(this, 'priv-apigw-vpc', {
      cidr: '10.0.0.0/16',
      natGateways: 1,
      maxAzs: 3,
      subnetConfiguration: [
        {
          name: 'private-subnet-1',
          subnetType: SubnetType.PRIVATE,
          cidrMask: 24,
        },
        {
          name: 'public-subnet-1',
          subnetType: SubnetType.PUBLIC,
          cidrMask: 24,
        }
      ],
    });

    // Update the Name tag for the VPC
    cdk.Aspects.of(this.vpc).add(new cdk.Tag('Name', 'priv-apigw-vpc'));

    // Update the Name tag for private subnets

    for (const subnet of this.vpc.publicSubnets) {
      cdk.Aspects.of(subnet).add(
        new cdk.Tag(
          'Name',
          `${this.vpc.node.id}-${subnet.node.id.replace(/Subnet[0-9]$/, '')}-${
            subnet.availabilityZone
          }`,
        ),
      );
    }
    
    for (const subnet of this.vpc.privateSubnets) {
      cdk.Aspects.of(subnet).add(
        new cdk.Tag(
          'Name',
          `${this.vpc.node.id}-${subnet.node.id.replace(/Subnet[0-9]$/, '')}-${
            subnet.availabilityZone
          }`,
        ),
      );
    }
  }
}