import * as cdk from '@aws-cdk/core';
import { Vpc } from '@aws-cdk/aws-ec2';
import { Cluster, ContainerImage } from '@aws-cdk/aws-ecs';
import { ApplicationLoadBalancedFargateService } from '@aws-cdk/aws-ecs-patterns';
import * as apig from '@aws-cdk/aws-apigatewayv2';
import path = require('path');

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new Vpc(this, 'MyVpc', {
      maxAzs: 3
    });

    const cluster = new Cluster(this, 'MyCluster', {
      vpc: vpc
    });

    const fargate = new ApplicationLoadBalancedFargateService(this, 'MyFargateService', {
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      taskImageOptions: {
        image: ContainerImage.fromAsset(path.join(__dirname, '../src/')),
      },
      assignPublicIp: false,
      memoryLimitMiB: 2048,
      publicLoadBalancer: false,
    });

    const httpVpcLink = new cdk.CfnResource(this, 'HttpVpcLink', {
      type: 'AWS::ApiGatewayV2::VpcLink',
      properties: {
        Name: 'V2 VPC Link',
        SubnetIds: vpc.privateSubnets.map(m => m.subnetId)
      }
    });

    const api = new apig.HttpApi(this, 'HttpApiGateway', {
      apiName: 'ApigwFargate',
      description: 'Integration between apigw and Application Load-Balanced Fargate Service',
    });

    const integration = new apig.CfnIntegration(this, 'HttpApiGatewayIntegration', {
      apiId: api.httpApiId,
      connectionId: httpVpcLink.ref,
      connectionType: 'VPC_LINK',
      description: 'API Integration with AWS Fargate Service',
      integrationMethod: 'GET', // for GET and POST, use ANY
      integrationType: 'HTTP_PROXY',
      integrationUri: fargate.listener.listenerArn,
      payloadFormatVersion: '1.0', // supported values for Lambda proxy integrations are 1.0 and 2.0. For all other integrations, 1.0 is the only supported value
    });

    new apig.CfnRoute(this, 'Route', {
      apiId: api.httpApiId,
      routeKey: 'GET /',  // for something more general use 'ANY /{proxy+}'
      target: `integrations/${integration.ref}`,
    })

    new cdk.CfnOutput(this, 'APIGatewayUrl', {
      description: 'API Gateway URL to access the GET endpoint',
      value: api.url!
    })
  }
}
