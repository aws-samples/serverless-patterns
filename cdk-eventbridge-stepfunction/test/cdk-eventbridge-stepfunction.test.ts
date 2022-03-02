import { Template } from 'aws-cdk-lib/assertions';
import * as cdk from 'aws-cdk-lib';
import * as CdkEventbridgeStepfunction from '../lib/cdk-eventbridge-stepfunction-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new CdkEventbridgeStepfunction.CdkEventbridgeStepfunctionStack(app, 'MyTestStack');
    // THEN
    Template.fromStack(stack).hasResource("AWS::Lambda::Function", {})

});
