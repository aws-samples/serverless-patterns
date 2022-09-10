import {
  aws_lambda as lambda,
  aws_lambda_nodejs as nodejs_lambda,
  aws_ec2 as ec2,
  aws_elasticloadbalancingv2 as elbv2,
  aws_elasticloadbalancingv2_targets as targets,
  CfnOutput,
  Stack,
  StackProps
} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as path from 'path';

export class AlbLambdaCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Creating vpc only with public subnets
    const myVpc = new ec2.Vpc(this, 'MyVPC', {
      subnetConfiguration: [
        {
          name: 'VpcSubnetGroup',
          subnetType: ec2.SubnetType.PUBLIC,
        }
      ]
    });

    const securityGroup = new ec2.SecurityGroup(this, 'MyLoadBalancerSG', {
      vpc: myVpc,
    });

    securityGroup.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(80),
    );

    const loadBalancer = new elbv2.ApplicationLoadBalancer(this, 'MyLoadBalancer', {
      vpc: myVpc,
      internetFacing: true,
      securityGroup: securityGroup,
    });

    const lambdaFunction = new nodejs_lambda.NodejsFunction(this, "LambdaFunction", {
      runtime: lambda.Runtime.NODEJS_14_X,
      entry: path.join(__dirname, `/../lambda/index.ts`),
      handler: "handler",
    });

    const listener = loadBalancer.addListener('MyLoadBalancerListener', { port: 80 });
    listener.addTargets('MyLoadBalancerTargets', {
      targets: [new targets.LambdaTarget(lambdaFunction)],
      healthCheck: {
        enabled: true,
      }
    });

    // Output
    new CfnOutput(this, 'ALBUrl', {
      value: `http://${loadBalancer.loadBalancerDnsName}`
    });
  }
}
