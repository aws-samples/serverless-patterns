#!/usr/bin/env node
import 'source-map-support/register';

import { App, Stack } from 'aws-cdk-lib';
import { StepFunctionInvokeAction } from 'aws-cdk-lib/aws-codepipeline-actions';
import { PolicyStatement, Effect } from 'aws-cdk-lib/aws-iam';

import { DemoPipeline } from './src/stacks/stack_pipeline';
import { S3GlueStack } from './src/stacks/stack_s3buckets';
import { TestGlueStack } from './src/stacks/stack_glue';
import { AthenaStack } from './src/stacks/stack_athena';

const app = new App();

// make sure account and region provided here should match with one provided at file 'src/config.ts'.

const s3BucketsStack = new S3GlueStack(app, 's3GlueBucketsStack', {
    //env: { account: account, region: region }
});

const glueStack = new TestGlueStack(app, 'glueTablesStack', {
    //env: { account: account, region: region }
    s3EmpMaster: s3BucketsStack.s3EmpMaster,
});
glueStack.addDependency(s3BucketsStack);

const athenaStack = new AthenaStack(app, 'athenaStack', {
    gDB: glueStack.gDB,
    s3aQuery: s3BucketsStack.s3aQuery
})
athenaStack.addDependency(glueStack);

const demoPipeline = new DemoPipeline(app, 'demoPipeline', {
    //env: { account: account, region: region }
});

demoPipeline.addDependency(athenaStack);

const viewStep = new StepFunctionInvokeAction({
    actionName: 'UpdateViewsStage',
    stateMachine: athenaStack.sViewsMachine
});

demoPipeline.pipeline.pipeline.addStage({
    stageName: 'DeployViews',
    actions: [viewStep]
});

app.synth();
