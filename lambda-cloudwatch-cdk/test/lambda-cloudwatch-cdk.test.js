const { expect, matchTemplate, MatchStyle, haveResource } = require('@aws-cdk/assert');
const cdk = require('@aws-cdk/core');
const LambdaCloudWatchCdk = require('../lib/lambda-cloudwatch-cdk-stack');

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new LambdaCloudWatchCdk.LambdaCloudWatchCdkStack(app, 'MyTestStack');
    // THEN
    // expect(stack).to(matchTemplate({
    //   "Resources": {}
    // }, MatchStyle.EXACT))
    expect(stack).to(haveResource('AWS::IAM::Role'));
    expect(stack).to(haveResource('AWS::IAM::Policy'));
    expect(stack).to(haveResource('AWS::Lambda::Function'));
  });
