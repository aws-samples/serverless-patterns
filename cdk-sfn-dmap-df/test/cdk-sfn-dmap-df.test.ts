import * as cdk from 'aws-cdk-lib/core';
import { Template } from 'aws-cdk-lib/assertions';
import { CdkSfnDmapDfStack } from '../lib/cdk-sfn-dmap-df-stack';

describe('CdkSfnDmapDfStack', () => {
  const app = new cdk.App();
  const stack = new CdkSfnDmapDfStack(app, 'TestStack');
  const template = Template.fromStack(stack);

  it('should create a durable Lambda function', () => {
    template.hasResourceProperties('AWS::Lambda::Function', {
      FunctionName: 'catalog-item-processor',
      Runtime: 'nodejs22.x',
    });
  });

  it('should create a Step Functions state machine', () => {
    template.hasResourceProperties('AWS::StepFunctions::StateMachine', {
      StateMachineName: 'catalog-update-distributed-map',
    });
  });

  it('should create an S3 bucket for catalog data', () => {
    template.hasResource('AWS::S3::Bucket', {});
  });

  it('should configure the durable function with durableConfig', () => {
    template.hasResourceProperties('AWS::Lambda::Function', {
      FunctionName: 'catalog-item-processor',
      DurableConfig: {
        ExecutionTimeout: 900,
        RetentionPeriodInDays: 1,
      },
    });
  });
});
