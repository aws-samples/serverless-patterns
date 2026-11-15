#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { NormalizerStack } from '../lib/normalizer-stack';

const app = new cdk.App();
new NormalizerStack(app, 'NormalizerStack');
