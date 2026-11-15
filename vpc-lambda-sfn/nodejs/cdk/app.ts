#!/usr/bin/env node
import 'source-map-support/register';
import { App } from 'aws-cdk-lib';

import { vpcStack } from './src/stacks/vpc_stack';
import { lambdaStack } from './src/stacks/lambda_stack';
import { sfnStack } from './src/stacks/sfn_stack';

const app = new App();

const vStack = new vpcStack(app, 'vpcStack', {
    //env: { account: account, region: region }
});

const lStack = new lambdaStack(app, 'lambdaStack', {
    ivpc: vStack.iVpc,
    publicsb: vStack.publicSubNet,
    privatesb: vStack.privateSubNet,
    isg: vStack.iSecurityGroup,
    //env: { account: account, region: region }
});

new sfnStack(app, 'sfnStack', {
    ltest: lStack.testLambda,
    //env: { account: account, region: region }
});

app.synth();