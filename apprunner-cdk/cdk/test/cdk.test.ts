import * as cdk from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { CdkStack } from '../lib/cdk-stack';

test('Creates an ECS Express Mode service', () => {
  const template = Template.fromStack(new CdkStack(new cdk.App(), 'MyTestStack1'));
  template.resourceCountIs('AWS::ECS::ExpressGatewayService', 1);
  template.hasResourceProperties('AWS::ECS::ExpressGatewayService', {
    HealthCheckPath: '/',
    PrimaryContainer: { ContainerPort: 80 },
  });
});
