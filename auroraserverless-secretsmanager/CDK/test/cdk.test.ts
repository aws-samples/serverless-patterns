import { CdkStack } from '../lib/cdk-stack';
import * as cdk from '@aws-cdk/core';
import { Template } from "@aws-cdk/assertions";


test('Validate stack resources', () => {
  const app = new cdk.App();
  const s3Stack = new CdkStack(app,'cdkStack');
  const template = Template.fromStack(s3Stack);
  template.resourceCountIs("AWS::RDS::DBCluster", 1);
  template.resourceCountIs("AWS::EC2::VPC", 1);
});