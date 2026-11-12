#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { SfnCodebuildReleaseGateStack } from '../lib/sfn-codebuild-release-gate-stack';

const app = new cdk.App();
new SfnCodebuildReleaseGateStack(app, 'SfnCodebuildReleaseGateStack');
