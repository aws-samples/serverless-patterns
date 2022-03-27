import * as cdk from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { CdkStack } from '../lib/cdk-stack';

test('Validate stack resources', () => {
  const app = new cdk.App();
  const stack = new CdkStack(app, 'MyTestStack');

  Template.fromStack(stack).hasResource('AWS::DynamoDB::Table', {});
  Template.fromStack(stack).hasResource('AWS::Lambda::Function', {});
});