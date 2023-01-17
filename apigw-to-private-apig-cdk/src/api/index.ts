import * as apigateway from "@aws-cdk/aws-apigateway";
import * as lambda from "@aws-cdk/aws-lambda";
import * as cdk from "@aws-cdk/core";
import * as elb from '@aws-cdk/aws-elasticloadbalancingv2'
import * as elbTarget from '@aws-cdk/aws-elasticloadbalancingv2-targets'
import * as ec2 from '@aws-cdk/aws-ec2';
import * as iam from '@aws-cdk/aws-iam';
import * as customResource from '@aws-cdk/custom-resources'
import path from "path";
import config from "./config.json";

export class ApiStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, vpc: ec2.Vpc) {
    super(scope, id);

    /* Create Security group */
    const apiGatewayEndpointSG = new ec2.SecurityGroup(this, "apiGatewayEndpointSG", {
      description: "Security Group for Api Gateway Endpoint",
      vpc: vpc
    });
    apiGatewayEndpointSG.addIngressRule(ec2.Peer.ipv4('10.0.0.0/8'), ec2.Port.tcp(443));

    /* Create API Gateway Interface VPC Endpoint */
    const endpointAPIGateway = new ec2.InterfaceVpcEndpoint(this, "endpointAPIGateway", {
      service: ec2.InterfaceVpcEndpointAwsService.APIGATEWAY,
      vpc: vpc,
      subnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE
      }),
      privateDnsEnabled: true,
      securityGroups: [apiGatewayEndpointSG]
    });

    const handler = new lambda.Function(this, "handler", {
      code: new lambda.AssetCode(path.resolve(__dirname, "dist")),
      handler: `index.${config.api.handler}`,
      runtime: lambda.Runtime.NODEJS_14_X,
      vpc: vpc,
      vpcSubnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE
      })
    });

    /* Grant api gateway invoke permission on lambda */
    handler.grantInvoke(new iam.ServicePrincipal('apigateway.amazonaws.com'));

    const apiResourcePolicy = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          effect: iam.Effect.DENY,
          actions: ['execute-api:Invoke'],
          principals: [new iam.AnyPrincipal()],
          resources: ['execute-api:/*/*/*'],
          conditions: {
            StringNotEquals: {
              "aws:sourceVpce": endpointAPIGateway.vpcEndpointId
            }
          }
        }),
        new iam.PolicyStatement({
          effect: iam.Effect.ALLOW,
          actions: ['execute-api:Invoke'],
          principals: [new iam.AnyPrincipal()],
          resources: ['execute-api:/*/*/*'],
        })
      ]
    });

    const restapi = new apigateway.LambdaRestApi(this, config.prefix, {
      handler,
      description: config.description,
      endpointConfiguration: { types: [apigateway.EndpointType.PRIVATE], vpcEndpoints: [endpointAPIGateway] },
      policy: apiResourcePolicy
    });

    /* Create Load Balancer Target Group */
    const targetGroup = new elb.NetworkTargetGroup(this, 'TargetGroup', {
      port: 443,
      vpc,
      targetType: elb.TargetType.IP
    });

    for (let counter = 0; counter < vpc.availabilityZones.length; counter++) {
      const getEndpointIp = new customResource.AwsCustomResource(this, `GetEndpointIp${counter}`, {
        onUpdate: {
          service: 'EC2',
          action: 'describeNetworkInterfaces',
          outputPath: `NetworkInterfaces.${counter}.PrivateIpAddress`,
          parameters: { NetworkInterfaceIds: endpointAPIGateway.vpcEndpointNetworkInterfaceIds },
          physicalResourceId: customResource.PhysicalResourceId.of(`NetworkInterfaces.${counter}.PrivateIpAddress`)
        },
        policy: customResource.AwsCustomResourcePolicy.fromSdkCalls({ resources: customResource.AwsCustomResourcePolicy.ANY_RESOURCE })
      });
      targetGroup.addTarget(new elbTarget.IpTarget(cdk.Token.asString(getEndpointIp.getResponseField(`NetworkInterfaces.${counter}.PrivateIpAddress`)), 443));
    }
    /*  End Create Load Balancer Target Group */
    /*  Start Create Private Network Load Balancer */
    let privateAPGNLB = new elb.NetworkLoadBalancer(this, 'internalAPIGNLB', {
      vpc: vpc,
      internetFacing: false,
    });

    privateAPGNLB.addListener('listner', {
      port: 443,
      protocol: elb.Protocol.TCP,
      defaultTargetGroups: [targetGroup]
    }
    );
    /*  End Create Private Network Load Balancer */
    /*  Create VPC Link in API Gateway */
    let vpcLink = new apigateway.VpcLink(this, 'vpclink', {
      targets: [privateAPGNLB],
      vpcLinkName: 'apigconnectvpclink'
    });
    /*  End Create VPC Link in API Gateway */
    /*  Create Public API Gateway */
    const publicapi = new apigateway.RestApi(this, 'public-api');
    const integration = new apigateway.Integration({
      integrationHttpMethod: "ANY",
      type: apigateway.IntegrationType.HTTP_PROXY,
      uri: `https://${restapi.restApiId}-${endpointAPIGateway.vpcEndpointId}.execute-api.${this.region}.amazonaws.com/prod`,
      options: {
        connectionType: apigateway.ConnectionType.VPC_LINK,
        vpcLink: vpcLink,
      },
    });
    publicapi.root.addMethod('GET', integration);
    /*  End Create Public API Gateway */

    const tags = config.tags

    tags.forEach(tag => {
      cdk.Tags.of(this).add(tag.key, tag.value)
      cdk.Tags.of(handler).add(tag.key, tag.value)
    })
  }
}