import * as cdk from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { EventBridgeLambdaStack } from '../lib/cdk-stack';

test('Validate stack resources', () => {
  const app = new cdk.App();
  const stack = new EventBridgeLambdaStack(app, 'MyTestStack');

  Template.fromStack(stack).hasResource('AWS::Lambda::Function', {});
  Template.fromStack(stack).hasResource('AWS::Logs::LogGroup', {});
  Template.fromStack(stack).hasResource('AWS::Events::Rule', {});
});