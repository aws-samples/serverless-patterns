import { StackProps, Stack } from 'aws-cdk-lib';
import {
  IpAddresses,
  Peer,
  Port,
  SecurityGroup,
  Vpc,
} from 'aws-cdk-lib/aws-ec2';
import { Construct } from 'constructs';
import { MyFargateService } from '../constructs/fargate-service';
import {
  NetworkLoadBalancer,
  NetworkTargetGroup,
} from 'aws-cdk-lib/aws-elasticloadbalancingv2';
import { AlbArnTarget } from 'aws-cdk-lib/aws-elasticloadbalancingv2-targets';
import {
  AnyPrincipal,
  Effect,
  PolicyDocument,
  PolicyStatement,
} from 'aws-cdk-lib/aws-iam';
import {
  AuthorizationType,
  ConnectionType,
  EndpointType,
  Integration,
  IntegrationType,
  RestApi,
  VpcLink,
} from 'aws-cdk-lib/aws-apigateway';
import { ParameterTier, StringParameter } from 'aws-cdk-lib/aws-ssm';
import { CfnResourceShare } from 'aws-cdk-lib/aws-ram';

export interface ServiceAStackProps extends StackProps {
  cidr: string;
  iepParamId: string;
  iepParam: string;
  uriParamId: string;
  uriParam: string;
  centralApiAccount: string;
  stage: string
  apiDescription: string;
}

export class ServiceAStack extends Stack {
  constructor(scope: Construct, id: string, props: ServiceAStackProps) {
    super(scope, id, props);

    // Create VPC for the workload
    const vpc = new Vpc(this, 'VPC', {
      ipAddresses: IpAddresses.cidr(props.cidr),
      maxAzs: 3,
    });

    // Create Fargate for ECS service using an ALB infront of the container
    const fargateService = new MyFargateService(this, 'FargateService', {
      vpc: vpc,
      loadbalancerType: 'ALB',
    });

    // Create NLB to serve as the target for the VPC link
    // Create security group for the NLB
    const securityGroupNLB = new SecurityGroup(this, 'NLBSecurityGroup', {
      vpc: vpc,
      allowAllOutbound: true,
    });

    securityGroupNLB.addIngressRule(Peer.anyIpv4(), Port.tcp(80));

    // Create NLB
    const nlb = new NetworkLoadBalancer(this, 'NLB', {
      vpc: vpc,
      enforceSecurityGroupInboundRulesOnPrivateLinkTraffic: false,
      securityGroups: [securityGroupNLB],
      internetFacing: false,
    });

    // Add listener to NLB
    const svcAlistener = nlb.addListener('FargateALBListener', {
      port: 80,
    });

    // Add ALB as Target for NLB
    const targetGroup = new NetworkTargetGroup(this, 'ALBTarget', {
      port: 80,
      vpc: vpc,
      targets: [
        new AlbArnTarget(
          fargateService.fargateService.loadBalancer.loadBalancerArn,
          80
        ),
      ],
    });

    targetGroup.configureHealthCheck({
      path: '/Demo',
      port: '80',
    });

    svcAlistener.addTargetGroups('ALBTarget', targetGroup);

    // Add ingress rule to ALB to accept traffic from NLB
    fargateService.fargateService.loadBalancer.connections.allowFrom(
      securityGroupNLB,
      Port.tcp(80),
      'Allow inbound traffic from NLB'
    );

    // Get the API Gateway Interface Endpoint from Parameter Store
    const iepParamArn = `arn:aws:ssm:${this.region}:${props.centralApiAccount}:parameter${props.iepParam}`;
    const iepId = StringParameter.fromStringParameterArn(
      this,
      `${props.iepParamId}Share`,
      iepParamArn
    );

    // Resource policy for API Gateway to only allow traffic from a VPC Endpoint
    const apigwResourcePolicy = new PolicyDocument({
      statements: [
        new PolicyStatement({
          actions: ['execute-api:Invoke'],
          effect: Effect.ALLOW,
          principals: [new AnyPrincipal()],
          resources: ['execute-api:/*'],
        }),
        new PolicyStatement({
          actions: ['execute-api:Invoke'],
          effect: Effect.DENY,
          principals: [new AnyPrincipal()],
          resources: ['execute-api:/*'],
          conditions: {
            StringNotEquals: {
              'aws:sourceVpce': [iepId.stringValue],
            },
          },
        }),
      ],
    });

    // Create private API Gateway
    const restApi = new RestApi(this, 'PrivateRestApi', {
      description: props.apiDescription,
      endpointConfiguration: {
        types: [EndpointType.PRIVATE],
      },
      deployOptions: {
        stageName: props.stage,
        tracingEnabled: true,
      },
      policy: apigwResourcePolicy,
    });

    // Create VPC link
    const vpcLink = new VpcLink(this, 'VpcLink', {
      targets: [nlb],
      vpcLinkName: 'ServiceAVpcLink',
    });

    // Create proxy integration to fargate service's load balancer
    const svcAIntegration = new Integration({
      type: IntegrationType.HTTP_PROXY,
      integrationHttpMethod: 'ANY',
      uri: `http://${nlb.loadBalancerDnsName}/{proxy}`,
      options: {
        connectionType: ConnectionType.VPC_LINK,
        vpcLink: vpcLink,
        requestParameters: {
          'integration.request.path.proxy': 'method.request.path.proxy',
        },
      },
    });

    // Define resource
    restApi.root.addProxy({
      defaultIntegration: svcAIntegration,
      defaultMethodOptions: {
        authorizationType: AuthorizationType.NONE,
        requestParameters: {
          'method.request.path.proxy': true,
        },
      },
      anyMethod: true,
    });

    // Store the API GW URL in parameter store and share it with the central api account
    // to configure the routes in the Central API
    const uriParam = new StringParameter(this, props.uriParamId, {
      parameterName: props.uriParam,
      stringValue: restApi.url,
      tier: ParameterTier.ADVANCED,
    });

    // Share SSM Parameter
    new CfnResourceShare(this, 'URI-Share', {
      name: 'URI-Share',
      allowExternalPrincipals: true,
      principals: [props.centralApiAccount],
      resourceArns: [uriParam.parameterArn],
    });
  }
}
