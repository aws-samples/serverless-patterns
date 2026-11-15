import * as cdk from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { CdkStack } from '../lib/cdk-stack';

test('Validate stack resources', () => {
  const app = new cdk.App();
  const stack = new CdkStack(app, 'MyTestStack');

  Template.fromStack(stack).hasResource('AWS::SQS::Queue', {});
  Template.fromStack(stack).hasResource('AWS::SNS::Topic', {});
  Template.fromStack(stack).hasResource('AWS::KMS::Key', {});
  Template.fromStack(stack).hasResource('AWS::ECS::Cluster', {});
  Template.fromStack(stack).hasResource('AWS::ECS::TaskDefinition', {});
  Template.fromStack(stack).hasResource('AWS::ECS::Service', {});
  Template.fromStack(stack).hasResource('AWS::ElasticLoadBalancingV2::LoadBalancer', {});
});
