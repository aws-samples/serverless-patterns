import { expect as expectCDK, haveResource } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import { CdkStack } from '../lib/cdk-stack';

test('Validate stack resources', () => {
  const app = new cdk.App();
  const stack = new CdkStack(app, 'MyTestStack');

  expectCDK(stack).to(haveResource('AWS::ECS::Cluster'));
  expectCDK(stack).to(haveResource('AWS::ECS::Service'));
  expectCDK(stack).to(haveResource('AWS::ECS::TaskDefinition'));
  expectCDK(stack).to(haveResource('AWS::ElasticLoadBalancingV2::LoadBalancer'));
  expectCDK(stack).to(haveResource('AWS::ApiGatewayV2::Api'));
  expectCDK(stack).to(haveResource('AWS::ApiGatewayV2::Integration'));
  expectCDK(stack).to(haveResource('AWS::ApiGatewayV2::Route'));
  expectCDK(stack).to(haveResource('AWS::ApiGatewayV2::VpcLink'));
});
