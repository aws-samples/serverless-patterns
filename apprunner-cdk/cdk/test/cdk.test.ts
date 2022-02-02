import { expect as expectCDK, haveResource, haveOutput } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import { CdkStack } from '../lib/cdk-stack';

test('Creates the App Runner stack without exceptions', () => {
    expect(() => { new CdkStack(new cdk.App(), 'MyTestStack1') 
    }).not.toThrow();
});
