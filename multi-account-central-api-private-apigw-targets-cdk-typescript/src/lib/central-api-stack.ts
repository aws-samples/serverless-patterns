import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import {
  IpAddresses,
  Peer,
  Port,
  SecurityGroup,
  Vpc,
} from 'aws-cdk-lib/aws-ec2';
import {
  NetworkLoadBalancer,
  NetworkTargetGroup,
  TargetType,
} from 'aws-cdk-lib/aws-elasticloadbalancingv2';
import { Construct } from 'constructs';
import { MyENIIPAttributes } from '../constructs/get-eni-ips';
import { ParameterTier, StringParameter } from 'aws-cdk-lib/aws-ssm';
import { EndpointType, RestApi, VpcLink } from 'aws-cdk-lib/aws-apigateway';
import { CfnResourceShare } from 'aws-cdk-lib/aws-ram';

export interface CentralApiStackProps extends StackProps {
  cidr: string;
  accountsForIEPShare: string[];
  stage: string;
  apiDescription: string;
  iepParam: string;
  iepParamId: string;
}

export class CentralApiStack extends Stack {
  constructor(scope: Construct, id: string, props: CentralApiStackProps) {
    super(scope, id, props);

    // Create VPC for the Network Load Balancer and API Gateway Interface Endpoints
    const vpc = new Vpc(this, 'VPC', {
      ipAddresses: IpAddresses.cidr(props.cidr),
      maxAzs: 3,
    });

    // Create secuirty group for the APIGW Interface Endpoint
    const vpceSecurityGroup = new SecurityGroup(this, 'VpceSecurityGroup', {
      vpc: vpc,
      allowAllOutbound: true,
    });

    // Create security group for the NLB
    const securityGroupNLB = new SecurityGroup(this, 'NLBSecurityGroup', {
      vpc: vpc,
      allowAllOutbound: true,
    });

    // Allow HTTPS traffic to the NLB
    securityGroupNLB.addIngressRule(Peer.anyIpv4(), Port.tcp(443));

    // Create the Network Load Balancer used to front the APIGW Interface Endpoint network interfaces
    const nlb = new NetworkLoadBalancer(this, 'NLB', {
      vpc: vpc,
      enforceSecurityGroupInboundRulesOnPrivateLinkTraffic: false,
      securityGroups: [securityGroupNLB],
      internetFacing: false,
    });

    // All HTTPS traffic from the NLB to the Interface Endpoint network interfaces
    vpceSecurityGroup.addIngressRule(
      Peer.securityGroupId(securityGroupNLB.securityGroupId),
      Port.tcp(443)
    );

    // Create an API Gateway Interface endpoint
    const vpcEndpoint = vpc.addInterfaceEndpoint('ApiGatewayEndpoint', {
      service: {
        name: `com.amazonaws.${vpc.env.region}.execute-api`,
        port: 443,
      },
      privateDnsEnabled: true,
      open: true,
      subnets: {
        subnets: vpc.privateSubnets,
      },
      securityGroups: [vpceSecurityGroup],
    });

    // Add listener to NLB
    const vpceListener = nlb.addListener('vpceListener', {
      port: 443,
    });

    // Use a Custom Resource to get the Interface Endpoint ENI IPs needed to create the NLB target group
    const myENIIPs = new MyENIIPAttributes(this, 'MyENIIPAttributes', {
      interfaceEPId: vpcEndpoint.vpcEndpointId,
      vpc: vpc,
    });

    // Add Interface Endpoint IP Addresses as the target for the NLB
    const targetGroup = new NetworkTargetGroup(this, 'vpceTarget', {
      port: 443,
      vpc: vpc,
      targetType: TargetType.IP,
      targets: myENIIPs.ipList,
    });

    vpceListener.addTargetGroups('VPCETargetGroup', targetGroup);

    // Create the Rest API
    const restApi = new RestApi(this, 'RestApi', {
      description: props.apiDescription,
      endpointConfiguration: {
        types: [EndpointType.REGIONAL],
      },
      deployOptions: {
        stageName: props.stage,
        tracingEnabled: true,
      },
    });

    restApi.root.addMethod('ANY');

    // Create the VPC Link
    const vpcLink = new VpcLink(this, 'VpcLink', {
      targets: [nlb],
    });

    // Store the Interface endpoint ID in parameter store and share it with the service accounts so it can
    // be used in the resource policy for each private API Gateway
    const iepParam = new StringParameter(this, props.iepParamId, {
      parameterName: props.iepParam,
      stringValue: vpcEndpoint.vpcEndpointId,
      tier: ParameterTier.ADVANCED,
    });

    // Share SSM Parameter
    new CfnResourceShare(this, 'IEP-Share', {
      name: 'IEP-Share',
      allowExternalPrincipals: true,
      principals: props.accountsForIEPShare,
      resourceArns: [iepParam.parameterArn],
    });

    // Outputs
    new CfnOutput(this, 'RestApiId', {
      value: restApi.restApiId,
      description: 'Rest API Id',
      exportName: 'RestApiId',
    });

    new CfnOutput(this, `RestApiRootResourceId`, {
      value: restApi.restApiRootResourceId,
      description: 'Rest API Root Resource Id',
      exportName: 'RestApiRootResourceId',
    });

    new CfnOutput(this, 'VPCLinkId', {
      value: vpcLink.vpcLinkId,
      description: 'VPC Link Id',
      exportName: 'VPCLinkId',
    });
  }
}
