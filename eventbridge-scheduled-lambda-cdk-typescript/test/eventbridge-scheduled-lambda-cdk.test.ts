import { Template } from 'aws-cdk-lib/assertions';
import * as cdk from 'aws-cdk-lib';
import * as EventbridgeScheduledLambdaCdk from '../lib/eventbridge-scheduled-lambda-cdk-stack';

test('Empty Stack', () => {
    const app = new cdk.App();

    // WHEN
    const stack = new EventbridgeScheduledLambdaCdk.EventbridgeScheduledLambdaCdkStack(app, 'MyTestStack');
    // THEN
    Template.fromStack(stack).hasResource("AWS::Lambda::Function", {});
});
