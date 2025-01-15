import { StackProps, Stack, Fn, Token, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import {
  AuthorizationType,
  ConnectionType,
  EndpointType,
  Integration,
  IntegrationType,
  RestApi,
  VpcLink,
} from 'aws-cdk-lib/aws-apigateway';
import {
  NetworkLoadBalancer,
  Protocol,
  TargetType,
} from 'aws-cdk-lib/aws-elasticloadbalancingv2';
import { Peer, Port, SecurityGroup } from 'aws-cdk-lib/aws-ec2';
import { MyVPC } from '../constructs/vpc-with-ssm';
import { MyTargetGroup } from '../constructs/target-group-cr';

export interface ServiceStackProps extends StackProps {
  svcAAccount: string;
  svcAParamName: string;
  svcAParamId: string;
  svcBAccount: string;
  svcBParamName: string;
  svcBParamId: string;
  tgwParamName: string;
  tgwParamId: string;
  tgwAccount: string;
  svcACidr: string;
  svcBCidr: string;
  centralApiCidr: string;
  stage: string;
  apiDescription: string;
}

export class CentralApiStack extends Stack {
  constructor(scope: Construct, id: string, props: ServiceStackProps) {
    super(scope, id, props);

    // Create VPC for the workload
    const myVPC = new MyVPC(this, 'MyVPC', {
      cidr: props.centralApiCidr,
      tgwParamId: props.tgwParamId,
      tgwParamName: props.tgwParamName,
      tgwAccount: props.tgwAccount,
      associatedVPCCidrs: [props.svcACidr, props.svcBCidr],
    });

    // Define security group for NLB
    const webSG = new SecurityGroup(this, 'WebSG', {
      vpc: myVPC.vpc,
    });

    webSG.addIngressRule(Peer.anyIpv4(), Port.tcp(8081));
    webSG.addIngressRule(Peer.anyIpv4(), Port.tcp(8082));

    // Create Network Load Balancer for VPC Link
    const nlb = new NetworkLoadBalancer(this, 'NLB', {
      vpc: myVPC.vpc,
      enforceSecurityGroupInboundRulesOnPrivateLinkTraffic: false,
      securityGroups: [webSG],
      internetFacing: false,
    });

    // Custom Resource to add target groups for Service A to NLB
    const nlbTargetsSvcA = new MyTargetGroup(this, 'NLBTargetsA', {
      nlbARN: nlb.loadBalancerArn,
      ssmARN: `arn:aws:ssm:${myVPC.vpc.env.region}:${props.svcAAccount}:parameter${props.svcAParamName}`,
      tgName: 'ServiceATarget',
      listenerPort: 8081,
      targetPort: 80,
      protocol: Protocol.TCP,
      targetType: TargetType.IP,
      vpcId: myVPC.vpc.vpcId,
      accountNumber: this.account,
      tags: props.tags
    });

    // Custom Resource to add target group for Service B to NLB
    const nlbTargetsSvcB = new MyTargetGroup(this, 'NLBTargetsB', {
      nlbARN: nlb.loadBalancerArn,
      ssmARN: `arn:aws:ssm:${myVPC.vpc.env.region}:${props.svcBAccount}:parameter${props.svcBParamName}`,
      tgName: 'ServiceBTarget',
      listenerPort: 8082,
      targetPort: 80,
      protocol: Protocol.TCP,
      targetType: TargetType.IP,
      vpcId: myVPC.vpc.vpcId,
      accountNumber: this.account,
      tags: props.tags
    });

    // Adding dependencies to the custom resource
    nlbTargetsSvcA.node.addDependency(nlb);
    nlbTargetsSvcB.node.addDependency(nlb);

    /* // Create listener and target group for Service A
    const svcAlistener = nlb.addListener('ServiceAListener', {
      port: 8081,
    });

    // Get NLB ENI IPs and Azs for Service A from Parameter Store
    const svcAENIParamArn = `arn:aws:ssm:${myVPC.vpc.env.region}:${props.svcAAccount}:parameter${props.svcAParamName}`;
    const scvAENIs = StringParameter.fromStringParameterArn(
      this,
      `${props.svcAParamId}Share`,
      svcAENIParamArn
    );

    // Get NLB ENI IPs and Azs for Service B from Parameter Store
    const svcBENIParamArn = `arn:aws:ssm:${myVPC.vpc.env.region}:${props.svcBAccount}:parameter${props.svcBParamName}`;
    const scvBENIs = StringParameter.fromStringParameterArn(
      this,
      `${props.svcBParamId}Share`,
      svcBENIParamArn
    );

    // Generate targets for the load balancers
    const svcATargets = this.getIPTargetLists(scvAENIs.stringValue);
    const svcBTargets = this.getIPTargetLists(scvBENIs.stringValue);

    // Add Service A Target Group
    const svcATargetGroup = new NetworkTargetGroup(this, 'ServiceATarget', {
      port: 8081,
      vpc: myVPC.vpc,
      targetType: TargetType.IP,
      targets: svcATargets,
      crossZoneEnabled: true,
    });

    svcAlistener.addTargetGroups('ALBTarget', svcATargetGroup);

    // Create listener and target group for Service B
    const svcBlistener = nlb.addListener('ServiceBListener', {
      port: 8082,
    });

    // Add Service B Target Group
    const svcBTargetGroup = new NetworkTargetGroup(this, 'ServiceBTarget', {
      port: 8082,
      vpc: myVPC.vpc,
      targets: svcBTargets,
      crossZoneEnabled: true,
    });

    svcBlistener.addTargetGroups('ALBTarget', svcBTargetGroup); */

    // Create REST API
    const restApi = new RestApi(this, 'CentralApi', {
      description: props.apiDescription,
      endpointConfiguration: {
        types: [EndpointType.REGIONAL],
      },
      deployOptions: {
        stageName: props.stage,
        tracingEnabled: true,
      },
    });

    // Create VPC link
    const vpcLink = new VpcLink(this, 'VpcLink', {
      targets: [nlb],
      vpcLinkName: 'CentralApiVpcLink',
    });

    // Create integrations
    const svcAIntegration = new Integration({
      type: IntegrationType.HTTP_PROXY,
      integrationHttpMethod: 'ANY',
      uri: `http://${nlb.loadBalancerDnsName}:8081/{proxy}`,
      options: {
        connectionType: ConnectionType.VPC_LINK,
        vpcLink: vpcLink,
        requestParameters: {
          'integration.request.path.proxy': 'method.request.path.proxy',
        },
      },
    });

    const svcBIntegration = new Integration({
      type: IntegrationType.HTTP_PROXY,
      integrationHttpMethod: 'ANY',
      uri: `http://${nlb.loadBalancerDnsName}:8082/{proxy}`,
      options: {
        connectionType: ConnectionType.VPC_LINK,
        vpcLink: vpcLink,
        requestParameters: {
          'integration.request.path.proxy': 'method.request.path.proxy',
        },
      },
    });

    // Define resource
    const svcAResource = restApi.root.addResource('svca');
    svcAResource.addProxy({
      defaultIntegration: svcAIntegration,
      defaultMethodOptions: {
        authorizationType: AuthorizationType.NONE,
        requestParameters: {
          'method.request.path.proxy': true,
        },
      },
      anyMethod: true,
    });

    const svcBResource = restApi.root.addResource('svcb');
    svcBResource.addProxy({
      defaultIntegration: svcBIntegration,
      defaultMethodOptions: {
        authorizationType: AuthorizationType.NONE,
        requestParameters: {
          'method.request.path.proxy': true,
        },
      },
      anyMethod: true,
    });

    //Outputs
    new CfnOutput(this, 'ServiceAEndpoint', {
      exportName: 'ServiceAEndpoint',
      value: `https://${restApi.restApiId}.execute-api.${this.region}.amazonaws.com/${props.stage}/svca`,
      description: 'Service A API Gateway Endpoint',
    });

    new CfnOutput(this, 'ServiceBEndpoint', {
      exportName: 'ServiceBEndpoint',
      value: `https://${restApi.restApiId}.execute-api.${this.region}.amazonaws.com/${props.stage}/svcb`,
      description: 'Service B API Gateway Endpoint',
    });
  }
}
