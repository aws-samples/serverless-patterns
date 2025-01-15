import { IVpc, Peer, Port, SecurityGroup } from 'aws-cdk-lib/aws-ec2';
import { Cluster } from 'aws-cdk-lib/aws-ecs';
import { Construct } from 'constructs';
import {
  ApplicationLoadBalancedFargateService,
  NetworkLoadBalancedFargateService,
} from 'aws-cdk-lib/aws-ecs-patterns';
import { ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { NetworkLoadBalancer } from 'aws-cdk-lib/aws-elasticloadbalancingv2';

export interface MyFargateServiceProps {
  readonly vpc: IVpc;
  readonly loadbalancerType: 'ALB' | 'NLB';
}

export class MyFargateService extends Construct {
    public readonly fargateService: ApplicationLoadBalancedFargateService | NetworkLoadBalancedFargateService;

  constructor(scope: Construct, id: string, props: MyFargateServiceProps) {
    super(scope, id);

    // Function to create Fargate with an ALB
    const createALBFargateService = (cluster: Cluster): ApplicationLoadBalancedFargateService => {
      const albFargateService = new ApplicationLoadBalancedFargateService(
        this,
        'ALBFargateService',
        {
          cluster: cluster,
          cpu: 512,
          memoryLimitMiB: 2048,
          desiredCount: 1,
          taskImageOptions: {
            image: ContainerImage.fromRegistry(
              'public.ecr.aws/bstraehle/rest-api:latest'
            ),
          },
          publicLoadBalancer: false,
        }
      );

      albFargateService.targetGroup.configureHealthCheck({
        path: '/Demo',
        port: '80',
      });

      return albFargateService;
    };

    // Function to create Fargate with an NLB
    const createNLBFargateService = (cluster: Cluster, vpc: IVpc): NetworkLoadBalancedFargateService => {
      // Create security group for the NLB
      const securityGroupNLB = new SecurityGroup(this, 'NLBSecurityGroup', {
        vpc: vpc,
        allowAllOutbound: true,
      });

      securityGroupNLB.addIngressRule(Peer.anyIpv4(), Port.tcp(80));

      // Create Network Load Balancer
      const nlb = new NetworkLoadBalancer(this, 'FargateNLB', {
        vpc: vpc,
        enforceSecurityGroupInboundRulesOnPrivateLinkTraffic: false,
        securityGroups: [securityGroupNLB],
        internetFacing: false,
      });

      const nlbFargateService = new NetworkLoadBalancedFargateService(
        this,
        'NLBFargateService',
        {
          cluster,
          cpu: 512,
          memoryLimitMiB: 2048,
          desiredCount: 1,
          taskImageOptions: {
            image: ContainerImage.fromRegistry(
              'public.ecr.aws/bstraehle/rest-api:latest'
            ),
          },
          publicLoadBalancer: false,
          loadBalancer: nlb
        }
      );

      // Adding ingress from the NLB Security Group to the Fargate Service's Security Group
      nlbFargateService.service.connections.allowFrom(
        securityGroupNLB,
        Port.tcp(80)
      );

      return nlbFargateService;
    };

    // Create Fargate for ECS
    const cluster = new Cluster(this, 'ECSCluster', {
      vpc: props.vpc,
    });

    // Create a Fargate Service with an ALB or NLB depending on the prop
    if (props.loadbalancerType === 'ALB') {
      this.fargateService = createALBFargateService(cluster);
    } else if (props.loadbalancerType === 'NLB') {
      this.fargateService = createNLBFargateService(cluster, props.vpc);
    }
  }
}
