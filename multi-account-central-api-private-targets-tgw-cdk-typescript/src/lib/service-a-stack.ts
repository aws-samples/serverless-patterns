import { StackProps, Stack } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { MyVPC } from '../constructs/vpc-with-ssm';
import { MyFargateService } from '../constructs/fargate-service';
import { Peer, Port, SecurityGroup } from 'aws-cdk-lib/aws-ec2';
import { NetworkLoadBalancer, NetworkTargetGroup } from 'aws-cdk-lib/aws-elasticloadbalancingv2';
import { AlbArnTarget } from 'aws-cdk-lib/aws-elasticloadbalancingv2-targets';
import { MyELBIPAttributes } from '../constructs/get-elb-ip-and-az';
import { ParameterTier, StringParameter } from 'aws-cdk-lib/aws-ssm';
import { CfnResourceShare } from 'aws-cdk-lib/aws-ram';

export interface ServiceAStackProps extends StackProps {
  accountsForNLBShare: string[];
  svcACidr: string;
  svcBCidr: string;
  centralApiCidr: string;
  tgwParamId: string;
  tgwParamName: string;
  tgwAccount: string;
  svcANLBParamId: string;
  svcANLBParamName: string;
}

export class ServiceAStack extends Stack {
  constructor(scope: Construct, id: string, props: ServiceAStackProps) {
    super(scope, id, props);

    // Create VPC for the workload
    const myVPC = new MyVPC(this, 'MyVPC', {
      cidr: props.svcACidr,
      tgwParamId: props.tgwParamId,
      tgwParamName: props.tgwParamName,
      tgwAccount: props.tgwAccount,
      associatedVPCCidrs: [props.centralApiCidr, props.svcBCidr],
    });

    // Create Fargate for ECS
    const albFargateService = new MyFargateService(
      this,
      'ServiceA',
      {
        vpc: myVPC.vpc,
        loadbalancerType: 'ALB',
      }
    );

    // Create Network Load Balancer to route traffic from another account to the ALB
    // Create security group for the NLB
    const securityGroupNLB = new SecurityGroup(this, 'NLBSecurityGroup', {
      vpc: myVPC.vpc,
      allowAllOutbound: true,
    });

    securityGroupNLB.addIngressRule(Peer.anyIpv4(), Port.tcp(80));

    // Create Network Load Balancer for VPC Link
    const nlb = new NetworkLoadBalancer(this, 'CentralApiNlb', {
      vpc: myVPC.vpc,
      enforceSecurityGroupInboundRulesOnPrivateLinkTraffic: false,
      securityGroups: [securityGroupNLB],
      internetFacing: false,
    });

    // Add listener to NLB
    const svcAlistener = nlb.addListener('ECSALBListener', {
      port: 80,
    });

    // Add ALB as Target for NLB
    const targetGroup = new NetworkTargetGroup(this, 'ALBTarget', {
      port: 80,
      vpc: myVPC.vpc,
      targets: [new AlbArnTarget(albFargateService.fargateService.loadBalancer.loadBalancerArn, 80)]
    })

    targetGroup.configureHealthCheck({
      path: '/Demo',
      port: '80',
    })

    svcAlistener.addTargetGroups('ALBTarget',targetGroup)

    // Add ingress rule to ALB to accept traffic from NLB
    albFargateService.fargateService.loadBalancer.connections.allowFrom(
      securityGroupNLB,
      Port.tcp(80),
      'Allow inbound traffic from NLB'
    );

    // Get the NLB IP and AZs, store them in Parameter Store and share with the Central API account
    const nlbENIs = new MyELBIPAttributes(this, 'MyELBIPAttributes', {
      elbArn: nlb.loadBalancerArn,
    });

    // Store the NLB ENI information SSM Parameter Store
    const nlbParam = new StringParameter(this, props.svcANLBParamId, {
      parameterName: props.svcANLBParamName,
      tier: ParameterTier.ADVANCED,
      stringValue: nlbENIs.elbPoints,
    });

     // Share SSM Parameter
     new CfnResourceShare(this, 'SvcA-NLB-Share', {
        name: 'SvcA-NLB-Share',
        allowExternalPrincipals: true,
        principals: props.accountsForNLBShare,
        resourceArns: [nlbParam.parameterArn],
      });

  }
}
