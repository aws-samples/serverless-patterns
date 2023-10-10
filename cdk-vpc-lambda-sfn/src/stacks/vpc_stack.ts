import { Stack, StackProps, Aspects, Tag } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import {
    InterfaceVpcEndpointAwsService,
    ISecurityGroup, ISubnet, SecurityGroup, SubnetType, Vpc, Peer, Port, IVpc
} from 'aws-cdk-lib/aws-ec2';


export class vpcStack extends Stack {

    public readonly iVpc: IVpc;
    public readonly publicSubNet: ISubnet[];
    public readonly privateSubNet: ISubnet[];
    public readonly iSecurityGroup: ISecurityGroup;

    constructor(scope: Construct, id: string, props?: StackProps) {
        super(scope, id, props);
        const prefix = 'test-';
        const vpc = new Vpc(this, `${prefix}VPC`, {
            cidr: '10.0.0.0/16',
            natGateways: 1,
            maxAzs: 3,
            subnetConfiguration: [
                {
                    name: `${prefix}private-subnet-1`,
                    subnetType: SubnetType.PRIVATE_WITH_NAT,
                    cidrMask: 24,
                },
                {
                    name: `${prefix}public-subnet-1`,
                    subnetType: SubnetType.PUBLIC,
                    cidrMask: 24,
                },
                {
                    name: `${prefix}isolated-subnet-1`,
                    subnetType: SubnetType.PRIVATE_ISOLATED,
                    cidrMask: 24,
                }
            ],
        });

        const vSecurityGroup = new SecurityGroup(this, 'vpcSG', {
            vpc: vpc,
            description: 'Security Group for all AWS Services within VPC',
            allowAllOutbound: true,
            securityGroupName: `${prefix}vpcSG`,
        });

        vpc.addInterfaceEndpoint(`${prefix}sfn-interface`, {
            service: InterfaceVpcEndpointAwsService.STEP_FUNCTIONS,
            subnets: {
                subnets: vpc.privateSubnets
            },
            securityGroups: [vSecurityGroup]
        });

        this.iVpc = vpc;
        this.publicSubNet = vpc.publicSubnets;
        this.privateSubNet = vpc.privateSubnets;
        this.iSecurityGroup = vSecurityGroup;

        // Update the Name tag for private subnets

        for (const subnet of vpc.publicSubnets) {
            Aspects.of(subnet).add(
                new Tag(
                    'Name',
                    `${vpc.node.id}-${subnet.node.id.replace(/Subnet[0-9]$/, '')}-${subnet.availabilityZone
                    }`,
                ),
            );
        }

        for (const subnet of vpc.privateSubnets) {
            Aspects.of(subnet).add(
                new Tag(
                    'Name',
                    `${vpc.node.id}-${subnet.node.id.replace(/Subnet[0-9]$/, '')}-${subnet.availabilityZone
                    }`,
                ),
            );
        }
    }
}

export interface vpcProps extends StackProps {
    ivpc: IVpc,
    publicsb: ISubnet[],
    privatesb: ISubnet[],
    isg: ISecurityGroup;
}