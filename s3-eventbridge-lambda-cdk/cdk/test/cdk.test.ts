import * as cdk from 'aws-cdk-lib/core';
import { CdkStack } from '../stack/s3-eventbridge-lambda-stack';

test('Creates the s3-eventbridge-lambda stack without exceptions', () => {
    expect(() => { new CdkStack(new cdk.App(), 'MyTestStack1') 
    }).not.toThrow();
});