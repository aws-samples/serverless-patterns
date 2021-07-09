
import { LambdaRestApi, EndpointType } from "@aws-cdk/aws-apigateway";
import * as lambda from "@aws-cdk/aws-lambda";
import * as cdk from "@aws-cdk/core";
import path from "path";
import config from "./config.json";
import {SecurityGroup, Vpc, Peer, Port, InterfaceVpcEndpoint, InterfaceVpcEndpointAwsService, SubnetType} from '@aws-cdk/aws-ec2';
import {PolicyStatement, ServicePrincipal, Effect, PolicyDocument, AnyPrincipal } from '@aws-cdk/aws-iam';

export class ApiStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, vpc: Vpc) {
    super(scope, id);

    //Create Security group
    const apiGatewayEndpointSG = new SecurityGroup(this, "apiGatewayEndpointSG", {
        description: "Security Group for Api Gateway Endpoint",
        vpc: vpc
    });
    apiGatewayEndpointSG.addIngressRule(Peer.ipv4('10.0.0.0/8'), Port.tcp(443));

    //Create API Gateway Interface VPC Endpoint
    const endpointAPIGateway = new InterfaceVpcEndpoint(this, "endpointAPIGateway", {
        service: InterfaceVpcEndpointAwsService.APIGATEWAY,
        vpc: vpc,
        subnets: vpc.selectSubnets({
            subnetType: SubnetType.PRIVATE
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
        subnetType: SubnetType.PRIVATE
      })
    });

    //Grant api gateway invoke permission on lambda
    handler.grantInvoke(new ServicePrincipal('apigateway.amazonaws.com'));
    
    const apiResourcePolicy = new PolicyDocument({
      statements: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          actions: ['execute-api:Invoke'],
          principals: [new AnyPrincipal()],
          resources: ['execute-api:/*/*/*'],
        })
      ]
    });
    
    const restapi  = new LambdaRestApi(this, config.prefix, {
      handler,
      description: config.description,
      endpointConfiguration: {types: [EndpointType.PRIVATE], vpcEndpoints: [endpointAPIGateway]},
      policy: apiResourcePolicy
    });

    const tags = config.tags

    tags.forEach(tag => {
      cdk.Tags.of(this).add(tag.key, tag.value)
      cdk.Tags.of(handler).add(tag.key, tag.value)
    })

    new cdk.CfnOutput(this, 'ApiUrl', {
      value: 'https://' + restapi.restApiId + '-' + endpointAPIGateway.vpcEndpointId + ".execute-api." +  this.region + ".amazonaws.com/prod",
      exportName: "ApiUrl",
      description: 'This is the api url that needs to be invoked from an ec2 instance or corporate vpn',
    });
  }
}