#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { ClaimCheckStack } from '../lib/claim-check-stack';

const app = new cdk.App();
new ClaimCheckStack(app, 'ClaimCheckStack');
