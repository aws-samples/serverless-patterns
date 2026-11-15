#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { AppConfigFeatureFlagCdkStack } from '../lib/app-config-feature-flag-cdk-stack';

const app = new cdk.App();
new AppConfigFeatureFlagCdkStack(app, 'AppConfigFeatureFlagCdkStack');