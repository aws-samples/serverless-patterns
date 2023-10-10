//const { expect, matchTemplate, MatchStyle, haveResource } = require('@aws-cdk/assert');

const cdk = require('aws-cdk-lib');
const { Match, Template } = require('aws-cdk-lib/assertions');
const { LambdaCloudWatchCdkStack } = require('../lib/lambda-cloudwatch-cdk-stack');

describe("Lambda Cloudwatch Stack Validation", () => {
  test('Stack Resources Created', () => {
    const stack = new cdk.Stack();
    // WHEN
    new LambdaCloudWatchCdkStack(stack, 'LambdaCloudWatchCdkStack');
    Template.fromStack(stack).findResources("AWS::Lambda::Function");
    Template.fromStack(stack).findResources("AWS::IAM::Role");
    Template.fromStack(stack).findResources("AWS::IAM::Policy");
  });
});