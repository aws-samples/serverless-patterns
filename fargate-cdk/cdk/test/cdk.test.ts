import { expect as expectCDK, matchTemplate, MatchStyle, haveResource } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import { CdkStack } from '../lib/cdk-stack';

test('Validate stack resources', () => {
  const app = new cdk.App();
  const stack = new CdkStack(app, 'MyTestStack');

  expectCDK(stack).to(haveResource('AWS::ECS::Cluster'));
  expectCDK(stack).to(haveResource('AWS::ECS::TaskDefinition'));
  expectCDK(stack).to(haveResource('AWS::ECS::Service'));
  expectCDK(stack).to(haveResource('AWS::ElasticLoadBalancingV2::LoadBalancer'));
});