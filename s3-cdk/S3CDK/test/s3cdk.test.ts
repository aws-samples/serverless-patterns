import { S3CdkStack } from '../lib/s3cdk-stack';
import * as cdk from '@aws-cdk/core';
import { Template } from "@aws-cdk/assertions";


test('Validate stack resources', () => {
  const app = new cdk.App();
  const s3Stack = new S3CdkStack(app,'S3Stack');
  const template = Template.fromStack(s3Stack);
  template.resourceCountIs("AWS::S3::Bucket", 1);
});
