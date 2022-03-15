import * as cdk from 'aws-cdk-lib';
import { PipelineStack } from "./app/pipeline-stack";

const app = new cdk.App();

new PipelineStack(app, "ParallelE2EPipelineCDK", {
  prefix: "ServerlessLand",
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION
  }
});
