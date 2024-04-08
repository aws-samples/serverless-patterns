import * as cdk from 'aws-cdk-lib';
import { Template, Match } from 'aws-cdk-lib/assertions';
import * as LambdaElasticacheIntegrationpatternCdk from '../lib/lambda-elasticache-integrationpattern-cdk-stack';
import { Lambda } from 'aws-cdk-lib/aws-ses-actions';

test('Validate stack resources', () => {
  const app = new cdk.App();
  const stack = new LambdaElasticacheIntegrationpatternCdk.LambdaElasticacheIntegrationpatternCdkStack(app, 'MyTestStack');
  const template = Template.fromStack(stack);
  
  // Assert it creates the function with the correct properties
  template.hasResourceProperties("AWS::Lambda::Function", {
    Handler: "handler",
    Runtime: "nodejs18.x",
  });
});
