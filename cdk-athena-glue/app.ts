#!/usr/bin/env node
import 'source-map-support/register';
import { App } from '@aws-cdk/core';

import { S3GlueStack } from './src/stacks/stack_s3buckets';
import { TestGlueStack } from './src/stacks/stack_glue';
import { AthenaStack } from './src/stacks/stack_athena';

const app = new App();

// make sure account and region provided here should match with one provided at file 'src/config.ts'.

const s3BucketsStack = new S3GlueStack(app, 's3GlueStack', {
    //env: { account: account, region: region }
});

const glueStack = new TestGlueStack(app, 'glueStack', {
    //env: { account: account, region: region }
    s3EmpMaster: s3BucketsStack.s3EmpMaster,
});
glueStack.addDependency(s3BucketsStack);

const athenaStack = new AthenaStack(app, 'avStack', {
    gDB: glueStack.gDB,
    s3aQuery: s3BucketsStack.s3aQuery
});
athenaStack.addDependency(glueStack);

app.synth();
