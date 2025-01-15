import {
  CfnRoute,
  CfnTransitGatewayAttachment,
  IpAddresses,
  IVpc,
  Vpc,
} from 'aws-cdk-lib/aws-ec2';
import { Construct } from 'constructs';
import { StringParameter } from 'aws-cdk-lib/aws-ssm';

export interface MyVPCProps {
  readonly cidr: string;
  readonly tgwAccount: string;
  readonly tgwParamId: string;
  readonly tgwParamName: string;
  readonly associatedVPCCidrs: string[];
}

export class MyVPC extends Construct {
  public readonly vpc: IVpc;

  constructor(scope: Construct, id: string, props: MyVPCProps) {
    super(scope, id);

    // Create VPC for the workload
    this.vpc = new Vpc(this, 'VPC', {
      ipAddresses: IpAddresses.cidr(props.cidr),
      maxAzs: 3,
    });

    // Get TGW ID from shared ssm parameter
    const tgwParamArn = `arn:aws:ssm:${this.vpc.env.region}:${props.tgwAccount}:parameter${props.tgwParamName}`;
    const transitGatewayId = StringParameter.fromStringParameterArn(
      this,
      `${props.tgwParamId}Share`,
      tgwParamArn
    ).stringValue;

    const privateSubnetIds = this.vpc.privateSubnets.map(
      (subnet) => subnet.subnetId
    );
    const vpcId = this.vpc.vpcId;

    // Create TGW attachment
    const tgwAttachment = new CfnTransitGatewayAttachment(
      this,
      'VPCAttachment',
      {
        subnetIds: privateSubnetIds,
        transitGatewayId: transitGatewayId,
        vpcId: vpcId,
      }
    );

    // Add routes to other VPCs via TGW to the route table
    props.associatedVPCCidrs.forEach((cidr) => {
      this.vpc.privateSubnets.forEach(
        ({ routeTable: { routeTableId } }, index) => {
          const route = new CfnRoute(this, `to-${cidr}-${index}`, {
            routeTableId,
            destinationCidrBlock: cidr,
            transitGatewayId: transitGatewayId,
          });

          route.node.addDependency(tgwAttachment);
        }
      );
    });
  }
}
