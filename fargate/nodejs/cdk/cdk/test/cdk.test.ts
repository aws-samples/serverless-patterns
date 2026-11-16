import { Template } from 'aws-cdk-lib/assertions';
import * as cdk from 'aws-cdk-lib';
import { CdkStack } from '../lib/cdk-stack';

test('Validate stack resources', () => {
  const app = new cdk.App();
  const stack = new CdkStack(app, 'MyTestStack');

  Template.fromStack(stack).hasResource('AWS::ECS::Cluster', {});
  Template.fromStack(stack).hasResource('AWS::ECS::TaskDefinition', {});
  Template.fromStack(stack).hasResource('AWS::ECS::Service', {});
  Template.fromStack(stack).hasResource('AWS::ElasticLoadBalancingV2::LoadBalancer', {});
});