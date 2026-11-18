#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaVerifiedPermissionsStack } from '../lib/lambda-verified-permissions-stack';
const app = new cdk.App();
new LambdaVerifiedPermissionsStack(app, 'LambdaVerifiedPermissionsStack');
