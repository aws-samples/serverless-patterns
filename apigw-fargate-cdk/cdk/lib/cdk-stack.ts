import { CfnOutput, CfnResource, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Vpc } from 'aws-cdk-lib/aws-ec2';
import { Cluster, ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService } from 'aws-cdk-lib/aws-ecs-patterns';
import { CfnIntegration, CfnRoute } from 'aws-cdk-lib/aws-apigatewayv2';
import { HttpApi } from '@aws-cdk/aws-apigatewayv2-alpha';
import path = require('path');

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = new Vpc(this, 'MyVpc', {
      maxAzs: 3
    });

    const cluster = new Cluster(this, 'MyCluster', {
      vpc: vpc
    });

    const fargate = new ApplicationLoadBalancedFargateService(this, 'MyFargateService', {
      assignPublicIp: false,
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      memoryLimitMiB: 2048,
      publicLoadBalancer: false,
      taskImageOptions: {
        image: ContainerImage.fromAsset(path.join(__dirname, '../src/')),
      },
    });

    const httpVpcLink = new CfnResource(this, 'HttpVpcLink', {
      type: 'AWS::ApiGatewayV2::VpcLink',
      properties: {
        Name: 'V2 VPC Link',
        SubnetIds: vpc.privateSubnets.map(m => m.subnetId)
      }
    });

    const api = new HttpApi(this, 'HttpApiGateway', {
      apiName: 'ApigwFargate',
      description: 'Integration between apigw and Application Load-Balanced Fargate Service',
    });

    const integration = new CfnIntegration(this, 'HttpApiGatewayIntegration', {
      apiId: api.httpApiId,
      connectionId: httpVpcLink.ref,
      connectionType: 'VPC_LINK',
      description: 'API Integration with AWS Fargate Service',
      integrationMethod: 'GET', // for GET and POST, use ANY
      integrationType: 'HTTP_PROXY',
      integrationUri: fargate.listener.listenerArn,
      payloadFormatVersion: '1.0', // supported values for Lambda proxy integrations are 1.0 and 2.0. For all other integrations, 1.0 is the only supported value
    });

    new CfnRoute(this, 'Route', {
      apiId: api.httpApiId,
      routeKey: 'GET /',  // for something more general use 'ANY /{proxy+}'
      target: `integrations/${integration.ref}`,
    })

    new CfnOutput(this, 'APIGatewayUrl', {
      description: 'API Gateway URL to access the GET endpoint',
      value: api.url!
    })
  }
}
