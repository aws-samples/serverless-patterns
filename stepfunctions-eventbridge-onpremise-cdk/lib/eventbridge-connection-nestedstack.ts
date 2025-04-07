import { Construct } from "constructs";
import * as cdk from "aws-cdk-lib";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as events from 'aws-cdk-lib/aws-events';
import * as lattice from 'aws-cdk-lib/aws-vpclattice';

export interface EventBridgeConnectionNestedStackProps extends cdk.NestedStackProps {
  vpcId: string;
  onPremiseCidr: string;
  apiDomainName: string;
  apiKeySecretArn: string;
}

export class EventBridgeConnectionNestedStack extends cdk.NestedStack {

  public readonly connection: events.CfnConnection;

  constructor(scope: Construct, id: string, props: EventBridgeConnectionNestedStackProps) {
    super(scope, id, props);

    const vpc = ec2.Vpc.fromLookup(this, 'awsvpc', {vpcId: props.vpcId});

    const rgSecurityGroup = new ec2.SecurityGroup(this, "ResourceGatewaySG", {
      vpc,
      allowAllOutbound: false,
    });

    // Allow egress to on-premises VPC
    rgSecurityGroup.addEgressRule(
      ec2.Peer.ipv4(props.onPremiseCidr),
      ec2.Port.tcp(443),
      "Allow HTTPS traffic to on-premises VPC"
    );

    rgSecurityGroup.addEgressRule(
      ec2.Peer.ipv4(props.onPremiseCidr),
      ec2.Port.tcp(80),
      "Allow HTTP traffic to on-premises VPC"
    );

    const resourceGateway = new lattice.CfnResourceGateway(this, 'ResourceGateway', {
      name: 'onpremise-resource-gateway',
      ipAddressType: 'IPV4',
      vpcIdentifier: props.vpcId,
      subnetIds: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS
      }).subnetIds,
      securityGroupIds: [rgSecurityGroup.securityGroupId],
    });

    const resourceConfig = new lattice.CfnResourceConfiguration(
      this,
      'ResourceConfig',
      {
        name: 'onpremise-resource-config',
        portRanges: ['80', '443'],
        resourceGatewayId: resourceGateway.ref,
        resourceConfigurationType: 'SINGLE',
        resourceConfigurationDefinition: {
          dnsResource: {
            domainName: props.apiDomainName,
            ipAddressType: "IPV4"
          }
        }
      },
    );

    // Using level 1 construct as level 2 does not provide everything yet
    this.connection = new events.CfnConnection(this, 'Connection', {
      name: 'onpremise-connection',
      description: 'Connection to on premises API',
      authorizationType: 'API_KEY',
      authParameters: {
        apiKeyAuthParameters: {
          apiKeyName: 'x-api-key',
          apiKeyValue: cdk.SecretValue.secretsManager(props.apiKeySecretArn).unsafeUnwrap()
        }
      },
      invocationConnectivityParameters: {
        resourceParameters: {
          resourceConfigurationArn: resourceConfig.attrArn,
        }
      }
    });
  }
}
