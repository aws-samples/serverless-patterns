#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CdkCodepipelineManualApprovalLambdaSchedulerSesStack } from '../lib/cdk-codepipeline-manual_approval-lambda-scheduler-ses-stack';

const app = new cdk.App();
new CdkCodepipelineManualApprovalLambdaSchedulerSesStack(app, 'CdkCodepipelineManualApprovalLambdaSchedulerSesStack', {});