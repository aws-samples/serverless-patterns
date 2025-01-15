import { StackProps, Stack } from 'aws-cdk-lib';
import {
  IpAddresses,
  Vpc,
} from 'aws-cdk-lib/aws-ec2';
import { Construct } from 'constructs';
import { MyFargateService } from '../constructs/fargate-service';
import {
  NetworkLoadBalancer,
} from 'aws-cdk-lib/aws-elasticloadbalancingv2';
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

export interface ServiceBStackProps extends StackProps {
  cidr: string;
  iepParamId: string;
  iepParam: string;
  uriParamId: string;
  uriParam: string;
  centralApiAccount: string;
  stage: string; 
  apiDescription: string;
}

export class ServiceBStack extends Stack {
  constructor(scope: Construct, id: string, props: ServiceBStackProps) {
    super(scope, id, props);

    // Create VPC for the workload
    const vpc = new Vpc(this, 'VPC', {
      ipAddresses: IpAddresses.cidr(props.cidr),
      maxAzs: 3,
    });

    // Create Fargate for ECS service using an NLB infront of the container
    const fargateService = new MyFargateService(this, 'FargateService', {
      vpc: vpc,
      loadbalancerType: 'NLB',
    });

    // Get the API Gateway Interfsce Endpoint from Parameter Store
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

    // Create VPC link to the Fargate's NLB
    const fargateNLB = fargateService.fargateService
      .loadBalancer as NetworkLoadBalancer;

    const vpcLink = new VpcLink(this, 'VpcLink', {
      targets: [fargateNLB],
      vpcLinkName: 'ServiceBVpcLink',
    });

    // Create proxy integration
    const svcBIntegration = new Integration({
      type: IntegrationType.HTTP_PROXY,
      integrationHttpMethod: 'ANY',
      uri: `http://${fargateNLB.loadBalancerDnsName}/{proxy}`,
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
      defaultIntegration: svcBIntegration,
      defaultMethodOptions: {
        authorizationType: AuthorizationType.NONE,
        requestParameters: {
          'method.request.path.proxy': true,
        },
      },
      anyMethod: true,
    });

    // Store the API GW URL in parameter store and share it with the central api account
    // to configure the routes for the Central API
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
